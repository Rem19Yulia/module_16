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

# backend/routers/user.py
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models import User
from schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify
router = APIRouter()

