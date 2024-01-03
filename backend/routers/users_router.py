from fastapi import APIRouter, Depends, HTTPException

from dependencies import get_db
from database import engine

import crud, models, schemas
from sqlalchemy.orm import Session
models.Base.metadata.create_all(bind=engine)
from typing import Any
import authentication as auth

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

#get all users
@router.get("/")
async def get_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: auth.User = Depends(auth.get_current_active_user)) -> list[schemas.User]:
    users = crud.get_all_users(db, skip, limit)
    return users

#get single user by id
@router.get("/{user_id}")
async def get_single_user(user_id: Any, db: Session = Depends(get_db), current_user: auth.User = Depends(auth.get_current_active_user)) -> schemas.User:
    user = crud.get_single_user_details(db = db, id = user_id) 
    return user


# create new user
@router.post("/")
async def create_new_user(user: schemas.UserCreate, db: Session = Depends(get_db)) -> schemas.User:
    return crud.create_new_user(db=db, user=user)


# update existing user
@router.put("/{user_id}")
async def update_user(user: schemas.UserBase, user_id: int, db: Session = Depends(get_db), current_user: auth.User = Depends(auth.get_current_active_user)) -> schemas.User:
    return crud.update_user_details(db=db, id=user_id, user_details=user)

# delete  user
@router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db), current_user: auth.User = Depends(auth.get_current_active_user)) -> Any:
    return crud.delete_user(db=db, id=user_id)