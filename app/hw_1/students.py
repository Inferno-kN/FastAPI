from fastapi import HTTPException, FastAPI
from typing import Dict
from starlette.status import HTTP_404_NOT_FOUND, HTTP_409_CONFLICT, HTTP_204_NO_CONTENT, HTTP_201_CREATED

# Данные: простая база студентов.
# Ограничения:
# поле "value" внутри "grades" может содержать значение только от 1 до 5
# "name" и "group" - обязательные поля для студентов
# STUDENTS = [
#  {
#   "id": int,
#   "name": str,
#   "group": str,
#   "grades": [
#    {
#     "subject": str,
#     "value": int
#    }
#   ]
#  }
# ]
#
# 1. Реализовать CRUD для студентов.
# 2. Добавить маршрут GET /students/{id}/avg-grade — вернуть средний балл.
# 3. Добавить фильтрацию GET /students?group=IVT-101 — фильтрация по группе

STUDENTS = [
 {
  "id": 1,
  "name": "Lesha",
  "group": "223",
  "grades": [
   {
    "subject": "good",
    "value": 4
   }
  ]
 }
]
next_id = 2


app = FastAPI()


@app.get("/students/{student_id}/avg-grade", summary='Получение среднего балла конкретного студента')
async def get_avg_grade_student(student_id: int):
    save_list_grades = []
    for student in STUDENTS:
        grades_list = student['grades']
        if student.get('id') == student_id:
            for elem in grades_list:
                save_list_grades.append(elem.get('value'))
            avg_grade = sum(save_list_grades) / len(save_list_grades)
            return avg_grade

    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail='Студент не найден')


@app.get("/students", summary="Фильтрация по группе")
async def filter_group(group: str | None = None):
    result = []
    for student in STUDENTS:
        if student.get('group') == group:
            result.append(student)
    if not result:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail='Студенты не найдены')
    return result


@app.get("/students", summary="Получение всех студентов")
async def get_students() -> dict:
    return {"students": STUDENTS}


@app.get("/students/{student_id}", summary="Получение студента по уникальному идентификатору")
async def get_student(student_id: int):
    student = next((student for student in STUDENTS if student.get('id') == student_id), None)
    if student is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail='Студент не найден')
    return student


@app.post("/students", status_code=HTTP_201_CREATED, summary="Создаем студента")
async def create_student(data: Dict[str, str | str | int]):
    global next_id
    name = data.get('name')
    group = data.get('group')
    grades_subject = data.get('subject')
    grades_value = data.get('value')

    new_student = {
        "id" : next_id,
        "name": name,
        "group": group,
        "grades": [
            {
                "subject": grades_subject,
                "value": grades_value
            }]
}
    STUDENTS.append(new_student)
    next_id += 1
    return new_student


@app.put("/students/{student_id}", summary="Обновление студента")
async def update_student(student_id: int, data: Dict[str, str | str | int]):
    for student in STUDENTS:
        if student.get('id') == student_id:
            student['name'] = data.get('name')
            student['group'] = data.get('group')
            student['subject'] = data.get('subject')
            student['value'] = data.get('value')
            return student
    raise HTTPException(status_code=HTTP_404_NOT_FOUND)


@app.delete("/students/{student_id}", status_code=HTTP_204_NO_CONTENT, summary="Удаление студента")
async def delete_student(student_id: int):
    for student in STUDENTS:
        if student.get('id') == student_id:
            STUDENTS.remove(student)

    raise HTTPException(status_code=HTTP_404_NOT_FOUND)
