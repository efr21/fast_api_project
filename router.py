from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.sql.coercions import cls

from repository import TaskRepository
from schemas import TaskAdd, Task, TaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"]
)


# @router.get("")
# async def get_home():
#     return {"data": "Hello, world!"}


@router.get("")
async def get_tasks() -> list[Task]:
    tasks = await TaskRepository.find_all(cls)
    return tasks


@router.post("")
async def add_task(
        task: Annotated[TaskAdd, Depends()]

) -> TaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}
