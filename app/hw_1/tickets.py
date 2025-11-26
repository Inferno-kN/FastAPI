#
# Данные: заявки с приоритетом и статусом.
#
# TICKETS = [
#  {
#   "id": int,
#   "title": str,
#   "description": str,
#   "priority": str,
#   "status": str
#  }
# ]
# Ограничения:
# все поля - обязательные
# допустимые значения для поля "priority": "low", "medium", "high"
# допустимые значения для поля "status": "open", "in_progress", "closed"
#
#
# 1. Реализовать CRUD для тикетов.
# 2. Добавить фильтрацию:
# - GET /tickets?status=open
# - GET /tickets?priority=high
# 3. Добавить PUT /tickets/{id}/close — переводит статус в closed.

from typing import Literal
from pydantic import BaseModel
from fastapi import HTTPException
from fastapi import FastAPI
from starlette.status import HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT, HTTP_201_CREATED

app = FastAPI()

class TicketCreate(BaseModel):
    title: str
    description: str
    priority: Literal['low', 'medium', 'high']
    status: Literal['open', 'in_progress', 'closed']


class TicketUpdate(BaseModel):
    title: str
    description: str
    priority: Literal['low', 'medium', 'high']
    status: Literal['open', 'in_progress', 'closed']


class TicketDelete(BaseModel):
    title: str
    description: str
    priority: Literal['low', 'medium', 'high']
    status: Literal['open', 'in_progress', 'closed']


TICKETS = [
 {
  "id": 1,
  "title": 'не знаю че добавить',
  "description": 'это называется недостаток чтения книг или вообще его отсутствие',
  "priority": "medium",
    "status": "open"
 }
]

Next_id = 2


@app.get("/tickets", summary='Получение всех билетов')
async def get_tickets():
    return {"tickets": TICKETS}


@app.get("/tickets/status/{status}", summary="Фильтрация по статусу")
async def get_ticket_status(status: Literal['open', 'in_progress', 'closed']):
    if status:
        return [ticket for ticket in TICKETS if ticket.get('status') == status]


@app.get("/tickets/priority/{priority}", summary='Фильтрация по приоритету')
async def filter_priority(priority: Literal['low', 'medium', 'high']):
    if priority:
        return [ticket for ticket in TICKETS if ticket.get('priority') == priority]


@app.put("/tickets/{ticket_id}/close", summary="Переводит статус в closed")
async def change_status_closed(ticket_id: int):
    for ticket in TICKETS:
        if ticket.get('id') == ticket_id:
            ticket['status'] = 'closed'
            return ticket
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Билет не найден")


@app.get("/tickets/{ticket_id}", summary='Получение билета по его id')
async def get_ticket(ticket_id: int, title: str, description: str, priority: Literal['low', 'medium', 'high'], status: Literal['open', 'in_progress', 'closed']):
    for ticket in TICKETS:
        if ticket.get('id') == ticket_id:
            return ticket
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Билет не найден")


@app.post("/tickets", status_code=HTTP_201_CREATED, summary="Создание билета")
async def create_ticket(ticket: TicketCreate):
    global Next_id

    new_ticket = {
        "id": Next_id,
        "title": ticket.title,
        "description": ticket.description,
        "priority": ticket.priority,
        "status": ticket.status
    }
    TICKETS.append(new_ticket)
    Next_id += 1
    return new_ticket


@app.put("/tickets/{ticket_id}", summary="Обновление пользователя")
async def update_ticket(ticket_id: int, ticket: TicketUpdate):
    for t in TICKETS:
        if t.get('id') == ticket_id:
            t['title'] = ticket.title
            t['description'] = ticket.description
            t['priority'] = ticket.priority
            t['status'] = ticket.status
            return t
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Билет не найден")


@app.delete("/tickets/{ticket_id}", status_code=HTTP_204_NO_CONTENT, summary="Удаление билета")
async def delete_ticket(ticket_id: int, ticket: TicketDelete):
    for t in TICKETS:
        if t.get('id') == ticket_id:
            TICKETS.remove(t)
    raise HTTPException(status_code=HTTP_404_NOT_FOUND)