from fastapi import APIRouter

router = APIRouter(prefix="/task", tags=["task"])

@router.get("/")
def all_tasks():
    pass  # Здесь будет логика для получения всех задач

@router.get("/{task_id}")
def task_by_id(task_id: int):
    pass  # Здесь будет логика для получения задачи по ID

@router.post("/create")
def create_task():
    pass  # Здесь будет логика для создания задачи

@router.put("/update")
def update_task():
    pass  # Здесь будет логика для обновления задачи

@router.delete("/delete")
def delete_task():
    pass  # Здесь будет логика для удаления задачи
