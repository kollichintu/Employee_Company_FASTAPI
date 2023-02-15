
from sqlalchemy import Integer,Column,String,ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Employee(Base):
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    role = Column(String)
    experience = Column(Integer)
    team = Column(String)
    company_id = Column(Integer,ForeignKey('company.id'))
    company = relationship("Company",back_populates= 'employees')
    

class Company(Base):
    __tablename__ = 'company'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    employees = relationship("Employee", back_populates= 'company')
    