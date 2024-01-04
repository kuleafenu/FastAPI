from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from backend import models, schemas, authentication

# get single basic_info by id
def get_basic_info(db: Session, id: int):
    basic_info = db.query(models.BasicInfo).filter(models.BasicInfo.id == id).first()
    if basic_info is None:
        raise HTTPException(status_code=400, detail="BasicInfo not found.")
    return basic_info

# get single basic_info by Email
def get_basic_info_by_email(db: Session, email: str):
    return db.query(models.BasicInfo).filter(models.BasicInfo.email == email).first()

# get all basic info of a user
def get_user_basic_info(db: Session, user_id: int, basic_info_id:int, skip: int, limit: int):
    return db.query(models.BasicInfo).filter(models.BasicInfo.user_id == user_id and basic_info_id == models.BasicInfo.id).offset(skip).limit(limit).all()


# get all basic_information
def get_all_basic_info(db: Session, skip: int, limit: int):
    return db.query(models.BasicInfo).offset(skip).limit(limit).all()

# create new basic info
def create_basic_info(db: Session, basic_info: schemas.BasicInfoCreate, user: schemas.User):
    basic_info_exists = db.query(models.BasicInfo).filter(models.BasicInfo.email == basic_info.email).first()
    if basic_info_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="BasicInfo with email already exists.")
        
    # fake_hashed_password = basic_info.password + "notreallyhashed"
    db_basic_info = models.BasicInfo(**basic_info.model_dump())
    db_basic_info.user_id = user.id
    print("************db_basic_info.user_id", db_basic_info.user_id)
    # db_basic_info.password = fake_hashed_password
    db.add(db_basic_info)
    db.commit()
    db.refresh(db_basic_info)
    return db_basic_info


# update existing basic_info
def update_basic_info(db: Session, id: int, basic_info: schemas.BasicInfoCreate):
    existing_basic_info = db.query(models.BasicInfo).filter(models.BasicInfo.id == id).first()
    if existing_basic_info is None:
        raise HTTPException(status_code=404, detail="BasicInfo not found")
    
    existing_basic_info.contact_number = basic_info.contact_number
    existing_basic_info.date_of_birth = basic_info.date_of_birth
    existing_basic_info.email = basic_info.email
    existing_basic_info.firstname = basic_info.firstname
    existing_basic_info.lastname = basic_info.lastname
    existing_basic_info.gender = basic_info.gender
    existing_basic_info.home_address = basic_info.home_address
    existing_basic_info.nationality = basic_info.nationality
    # existing_basic_info.password = basic_info.password
    db.add(existing_basic_info)
    db.commit()
    db.refresh(existing_basic_info)
    return existing_basic_info


# delete basic_info by id
def delete_basic_info(db: Session, id: int):
    basic_info = db.query(models.BasicInfo).filter(models.BasicInfo.id == id).first()
    if basic_info is None:
        raise HTTPException(status_code=404, detail="BasicInfo not found")
    db.delete(basic_info)
    db.commit()
    return f"BasicInfo with Id {basic_info.id} is deleted!"


##########################################ACADEMIC RECORDS ###################

# Get single academic record by id
def get_single_academic_record(db: Session, id: int):
    existing_records = db.query(models.AcademicRecords).filter(models.AcademicRecords.id == id).first()
    if existing_records is None:
        raise HTTPException(status_code=404, detail="No Academic records found with the provided Id")
    return existing_records

# get all academic records
def get_academic_records(db: Session, skip: int, limit: int):
    return db.query(models.AcademicRecords).offset(skip).limit(limit).all()

# get all academic records of a user
def get_user_academic_records(db: Session, user_id: int, record_id:int, skip: int, limit: int):
    return db.query(models.AcademicRecords).filter(models.AcademicRecords.user_id == user_id and record_id == models.AcademicRecords.id).offset(skip).limit(limit).all()

# create new basic_info's Academic records
def create_academic_records(db: Session, record: schemas.AcademicRecordsCreate, user: schemas.User):        
    db_records = models.AcademicRecords(**record.model_dump())
    db_records.user_id = user.id
    db.add(db_records)
    db.commit()
    db.refresh(db_records)
    return db_records


# update existing existing academic records
def update_academic_records(db: Session, id: int, record: schemas.AcademicRecordsCreate):
    existing_records = db.query(models.AcademicRecords).filter(models.AcademicRecords.id == id).first()
    if existing_records is None:
        raise HTTPException(status_code=404, detail="Academic records with provied Id not found")
    
    existing_records.degree = record.degree
    existing_records.gpa = record.gpa
    existing_records.graduation_date = record.graduation_date
    existing_records.major = record.major
    existing_records.university = record.university
    db.add(existing_records)
    db.commit()
    db.refresh(existing_records)
    return existing_records

# delete academic records by id
def delete_academic_records(db: Session, id: int):
    record = db.query(models.AcademicRecords).filter(models.AcademicRecords.id == id).first()
    print("*****record id", record)
    if record is None:
        raise HTTPException(status_code=404, detail="Academic record not found")
    db.delete(record)
    db.commit()
    return f"Academic records with Id {record.id} is deleted!"




##########################################Visa Details ###################

# Get single visa details by id
def get_single_visa_details(db: Session, id: int):
    details = db.query(models.VisaDetails).filter(models.VisaDetails.id == id).first()
    if details is None:
        raise HTTPException(status_code=404, detail="No Visa details found with the provided Id")
    return details

# get all visa details
def get_visa_details(db: Session, skip: int, limit: int):
    return db.query(models.VisaDetails).offset(skip).limit(limit).all()

# get all visa details of a user
def get_user_visa_details(db: Session, user_id: int, visa_id:int, skip: int, limit: int):
    return db.query(models.VisaDetails).filter(models.VisaDetails.user_id == user_id and models.VisaDetails.id == visa_id).offset(skip).limit(limit).all()

# create new user's Visa Details
def create_visa_details(db: Session, visa_details: schemas.VisaDetailsCreate, user: schemas.User):        
    db_visa_details = models.VisaDetails(**visa_details.model_dump())
    db_visa_details.user_id = user.id
    db.add(db_visa_details)
    db.commit()
    db.refresh(db_visa_details)
    return db_visa_details


# update existing visa details
def update_visa_details(db: Session, id: int, visa_details: schemas.VisaDetailsCreate):
    existing_visa_details = db.query(models.VisaDetails).filter(models.VisaDetails.id == id).first()
    if existing_visa_details is None:
        raise HTTPException(status_code=404, detail="Visa Details with provied Id not found")
    
    existing_visa_details.expiry_date = visa_details.expiry_date
    existing_visa_details.issue_date = visa_details.issue_date
    existing_visa_details.visa_type = visa_details.visa_type

    db.add(existing_visa_details)
    db.commit()
    db.refresh(existing_visa_details)
    return existing_visa_details

# delete visa details by id
def delete_visa_details(db: Session, id: int):
    details = db.query(models.VisaDetails).filter(models.VisaDetails.id == id).first()
    if details is None:
        raise HTTPException(status_code=404, detail="Visa details not found")
    db.delete(details)
    db.commit()
    return details.id








##########################################User Details ###################

# Get single User details by id
def get_single_user_details(db: Session, id: int):
    details = db.query(models.User).filter(models.User.id == id).first()
    if details is None:
        raise HTTPException(status_code=404, detail="User not found")
    return details

# get all Users 
def get_all_users(db: Session, skip: int, limit: int):
    return db.query(models.User).offset(skip).limit(limit).all()

# User signup
def create_new_user(db: Session, user: schemas.UserCreate):   
    existing_user_details = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user_details:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")

    user.password = authentication.get_password_hash(user.password)
    user_details = models.User(**user.model_dump())
    db.add(user_details)
    db.commit()
    db.refresh(user_details)
    return user_details


# update existing user details
def update_user_details(db: Session, id: int, user_details: schemas.UserBase):
    existing_user_details = db.query(models.User).filter(models.User.id == id).first()
    if existing_user_details is None:
        raise HTTPException(status_code=404, detail="User with provied Id not found.")
    
    existing_user_details.firstname = user_details.firstname
    existing_user_details.lastname = user_details.lastname
    existing_user_details.email = user_details.email

    db.add(existing_user_details)
    db.commit()
    db.refresh(existing_user_details)
    return existing_user_details

# delete User by id
def delete_user(db: Session, id: int):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return user.id