from pydantic import BaseModel, Field
from datetime import date


#################### BASE SCHEMAS #######################
class BasicInfoBase(BaseModel):
    firstname: str
    lastname: str
    date_of_birth: date
    gender: str
    nationality: str
    contact_number: str | None = None
    email: str

class AcademicRecordsBase(BaseModel):
    degree: str
    major: str | None
    university: str
    gpa: str | None = None
    graduation_date: date

class VisaDetailsBase(BaseModel):
    visa_type: str
    issue_date: date
    expiry_date: date


class UserBase(BaseModel):
    email: str
    firstname: str
    lastname: str
    user_type: str


#################### CREATE SCHEMAS #######################

class BasicInfoCreate(BasicInfoBase):
    home_address: str = Field(default=None, description="Your current residential address of the country of study")

class AcademicRecordsCreate(AcademicRecordsBase):
    pass

class VisaDetailsCreate(VisaDetailsBase):
    pass 

class UserCreate(UserBase):
    password: str

#################### LIST SCHEMAS #######################
class AcademicRecords(AcademicRecordsBase):
    id: int

    class Config:
        from_attributes = True


class VisaDetails(VisaDetailsBase):
    id: int

    class Config:
        from_attributes = True

class BasicInfo(BasicInfoBase):
    id: int
    home_address: str | None

    class Config:
        from_attributes = True


class User(UserBase):
    id: int
    disabled: bool 
    basic_info: list[BasicInfo]
    academic_records: list[AcademicRecords]
    visa_details: list[VisaDetails]


    class Config:
        from_attributes = True

