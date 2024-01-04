from fastapi import APIRouter, Depends, HTTPException

from dependencies import get_db
from database import engine

import crud, models, schemas
import authentication as auth
from sqlalchemy.orm import Session
models.Base.metadata.create_all(bind=engine)
from typing import Any

router = APIRouter(
    prefix="/visa-details",
    tags=["Visa Details"]
)

#get all visa details
@router.get("/")
async def get_all_visa_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: auth.User = Depends(auth.get_current_active_user)) -> list[schemas.VisaDetails]:
    details = crud.get_visa_details(db=db, skip=skip, limit=limit)
    return details

#get single visa details by id
@router.get("/{id}")
async def get_single_visa_details(id: int, db: Session = Depends(get_db)) -> schemas.VisaDetails:
    details = crud.get_single_visa_details(db = db, id = id) 
    return details

#get all visa details for a user
@router.get("/{visa_id}/users/{user_id}")
async def get_member_visa_details(user_id: int, visa_id:int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: auth.User = Depends(auth.get_current_active_user)) -> list[schemas.VisaDetails]:
    details = crud.get_user_visa_details(db=db, user_id=user_id, visa_id=visa_id, skip=skip, limit=limit)
    return details


# create new visa details
@router.post("/")
async def create_new_visa_details(details: schemas.VisaDetailsCreate, db: Session = Depends(get_db), current_user: auth.User = Depends(auth.get_current_active_user)) -> schemas.VisaDetails:
    return crud.create_visa_details(db=db, visa_details=details, user=current_user)


# update existing visa information
@router.put("/{id}")
async def update_visa_details(details: schemas.VisaDetailsCreate, id:int, db: Session = Depends(get_db), current_user: auth.User = Depends(auth.get_current_active_user)) -> schemas.VisaDetails:
    return crud.update_visa_details(db=db, id=id, visa_details=details)

# # delete visa details
# @router.put("/{id}")
# async def delete_visa_details(id:int, db: Session = Depends(get_db)) -> str:
#     return crud.delete_visa_details(db=db, id=id)


# delete  visa details
@router.delete("/{id}")
async def delete_visa_details(id: int, db: Session = Depends(get_db), current_user: auth.User = Depends(auth.get_current_active_user)) -> Any:
    return crud.delete_visa_details(db=db, id=id)