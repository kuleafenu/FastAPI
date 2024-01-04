from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from datetime import date
from sqlalchemy.orm import relationship

from backend.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key= True, index= True)
    email = Column(String, unique=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    password = Column(String)
    disabled = Column(Boolean, default=False)
    user_type = Column(String)
    basic_info = relationship("BasicInfo", back_populates="user", passive_deletes='all')
    academic_records = relationship("AcademicRecords", back_populates="user", passive_deletes='all')
    visa_details = relationship("VisaDetails", back_populates="user", passive_deletes='all')


class BasicInfo(Base):
    __tablename__ = "basic_information"
    id = Column(Integer, primary_key= True, index= True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    firstname = Column(String)
    lastname = Column(String)
    date_of_birth = Column(String)
    gender = Column(String)
    nationality = Column(String)
    contact_number = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    home_address = Column(String)
    user = relationship("User", back_populates="basic_info", passive_deletes='all')
 



class AcademicRecords(Base):
    __tablename__ = "academic_records"
    id = Column(Integer, primary_key= True, index= True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates = "academic_records", passive_deletes='all')
    degree = Column(String)
    major = Column(String)
    university = Column(String)
    gpa = Column(String)
    graduation_date = Column(String)


    
class VisaDetails(Base):
    __tablename__ = "visa_details"
    id = Column(Integer, primary_key= True, index= True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates = "visa_details", passive_deletes='all')
    visa_type = Column(String)
    issue_date = Column(String)
    expiry_date = Column(String)


    