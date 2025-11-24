# 2. Пользователи и их профили
#
# Данные: список пользователей.
#
#     username: str
#     email: str
#     full_name: str | None = None
#     is_active: bool = True
#
# Добавить проверку, чтобы username был уникален (если уже есть — вернуть 400).
# Добавить маршрут GET /users/by-username/{username}.

from typing import Dict
from fastapi import HTTPException
from fastapi import FastAPI
from starlette.status import HTTP_422_UNPROCESSABLE_CONTENT, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT, HTTP_409_CONFLICT, HTTP_201_CREATED

app = FastAPI()

Users = [
    {
        "id": 1,
        "username": "Pashkevich",
        "email": "zukzuk@bk.ru",
        "full_name": 'Pashkevich Pashkevich',
        "in_active": True
    }
]
NEXT_ID = 2
Users_set = set()

@app.get("/", summary='Стартовая ветка')
async def route():
    return {"messgae": "Hello, world!"}


@app.get("/users")
async def get_users() -> dict:
    return {"users": Users}


@app.get("/users/by-username/{username}", summary="Получение пользователя по его нику")
async def get_user_by_username(username: str):
    for user in Users:
        if user.get('username') == username:
            return user

    raise HTTPException(status_code=404, detail="Пользователь не найден")


@app.get("/user/{user_id}", summary="Получение юзера по уникальному идентификатору")
async def get_user(user_id: int):
    user = next((user for user in Users if user.get('id') == user_id), None)
    if user is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Юзер не найден")
    return user


@app.post("/users", status_code=HTTP_201_CREATED, summary="Создаем пользователя")
async def create_user(data: Dict[str, str | str | bool]):
    global NEXT_ID, Users_set
    username = data.get('username')
    email = data.get('email')
    full_name = data.get('full_name')
    is_active = data.get('is_active')
    if username in Users_set:
        raise HTTPException(status_code=HTTP_409_CONFLICT, detail="Имя пользователя занято!")

    new_user = {
        'id': NEXT_ID,
        'username': username,
        'email': email,
        'full_name': full_name,
        'is_active': is_active
    }

    Users.append(new_user)
    Users_set.add(username)
    NEXT_ID += 1
    return new_user


@app.put("/users/{user_id}", summary="Обновление пользователя")
async def update_user(user_id: int, data: Dict[str, str | str | bool]):
    for user in Users:
        if user.get('id') == user_id:
            user['username'] = data.get('username')
            user['email'] = data.get('email')
            user['full_name'] = data.get('full_name')
            user['is_active'] = data.get('is_active')
            return user

    raise HTTPException(status_code=HTTP_404_NOT_FOUND)


@app.delete('/users/{user_id}', status_code=HTTP_204_NO_CONTENT, summary="Удаление пользователя")
async def delete_user(user_id: int):
    for user in Users:
        if user.get('id') == user_id:
            deleted_user = user
            Users.remove(user)
            return deleted_user

    raise HTTPException(status_code=HTTP_404_NOT_FOUND)