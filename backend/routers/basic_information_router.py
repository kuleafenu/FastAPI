from fastapi import APIRouter, Depends, HTTPException

from backend.dependencies import get_db
from backend.database import engine

from backend import crud, models, schemas
from sqlalchemy.orm import Session
models.Base.metadata.create_all(bind=engine)
from typing import Any
from backend import authentication as auth

router = APIRouter(
    prefix="/basic_information",
    tags=["Basic Information"]
)

#get all basic information
@router.get("/")
async def get_all_basic_information(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: auth.User = Depends(auth.get_current_active_user)) -> list[schemas.BasicInfo]:
    basic_information = crud.get_all_basic_info(db, skip, limit)
    return basic_information

#get single basic information by id
@router.get("/{basic_info_id}")
async def get_single_basic_info(basic_info_id: Any, db: Session = Depends(get_db), current_user: auth.User = Depends(auth.get_current_active_user)) -> schemas.BasicInfo:
    basic_info = crud.get_basic_info(db = db, id = basic_info_id) 
    return basic_info

#get all basic for a user
@router.get("/{basic_info_id}/users/{user_id}")
async def get_user_basic_information(user_id: int, basic_info_id:int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: auth.User = Depends(auth.get_current_active_user)) -> list[schemas.BasicInfo]:
    details = crud.get_user_basic_info(db=db, user_id=user_id, basic_info_id=basic_info_id, skip=skip, limit=limit)
    return details

# create new basic information
@router.post("/")
async def create_new_basic_info(basic_info: schemas.BasicInfoCreate, db: Session = Depends(get_db), current_user: auth.User = Depends(auth.get_current_active_user)) -> schemas.BasicInfo:
    return crud.create_basic_info(db=db, basic_info=basic_info, user = current_user)


# update existing basic information
@router.put("/{basic_info_id}")
async def update_basic_info(basic_info: schemas.BasicInfoCreate, basic_info_id: int, db: Session = Depends(get_db), current_user: auth.User = Depends(auth.get_current_active_user)) -> schemas.BasicInfo:
    return crud.update_basic_info(db=db, id=basic_info_id, basic_info=basic_info)

# delete  basic information
@router.delete("/{basic_info_id}")
async def delete_basic_info(basic_info_id: int, db: Session = Depends(get_db), current_user: auth.User = Depends(auth.get_current_active_user)) -> Any:
    return crud.delete_basic_info(db=db, id=basic_info_id)