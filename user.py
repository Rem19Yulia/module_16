from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/")
def all_users():
    pass  # Здесь будет логика для получения всех пользователей

@router.get("/{user_id}")
def user_by_id(user_id: int):
    pass  # Здесь будет логика для получения пользователя по ID

@router.post("/create")
def create_user():
    pass  # Здесь будет логика для создания пользователя

@router.put("/update")
def update_user():
    pass  # Здесь будет логика для обновления пользователя

@router.delete("/delete")
def delete_user():
    pass  # Здесь будет логика для удаления пользователя
