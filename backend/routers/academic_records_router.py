from fastapi import APIRouter, Depends, HTTPException

from dependencies import get_db
from database import engine

import crud, models, schemas
from sqlalchemy.orm import Session
import authentication as auth
models.Base.metadata.create_all(bind=engine)
from typing import Any

router = APIRouter(
    prefix="/academic-records",
    tags=["Academic Records"]
)

#get all academic records
@router.get("/")
async def get_all_academic_records(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: auth.User = Depends(auth.get_current_active_user)) -> list[schemas.AcademicRecords]:
    academic_records = crud.get_academic_records(db=db, skip=skip, limit=limit)
    return academic_records


#get all academic records for a user
@router.get("/{record_id}/user/{user_id}")
async def get_user_academic_records(user_id: int, record_id:int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: auth.User = Depends(auth.get_current_active_user)) -> list[schemas.AcademicRecords]:
    academic_records = crud.get_user_academic_records(db=db, user_id=user_id, record_id=record_id, skip=skip, limit=limit)
    return academic_records

#get single academic record by id
@router.get("/{record_id}")
async def get_single_academic_record(record_id: int, db: Session = Depends(get_db), current_user: auth.User = Depends(auth.get_current_active_user)) -> schemas.AcademicRecords:
    user = crud.get_single_academic_record(db = db, id = record_id) 
    return user


# create new academic records
@router.post("/")
async def create_new_academic_record(record: schemas.AcademicRecordsCreate, db: Session = Depends(get_db), current_user: auth.User = Depends(auth.get_current_active_user)) -> schemas.AcademicRecords:
    return crud.create_academic_records(db=db, record=record, user= current_user)


# update existing academic record
@router.put("/{record_id}")
async def update_academic_records(record: schemas.AcademicRecordsCreate, record_id:int, db: Session = Depends(get_db), current_user: auth.User = Depends(auth.get_current_active_user)) -> schemas.AcademicRecords:
    return crud.update_academic_records(db=db, id=record_id, record=record)

# # delete academic records
# @router.put("/{record_id}")
# async def delete_academic_records(record_id:int, db: Session = Depends(get_db)) -> str:
#     return crud.delete_academic_records(db=db, id=record_id)

# delete  academic record
@router.delete("/{id}")
async def delete_academic_record(id: int, db: Session = Depends(get_db), current_user: auth.User = Depends(auth.get_current_active_user)) -> Any:
    return crud.delete_academic_records(db=db, id=id)