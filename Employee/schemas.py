from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    role: str
    experience: int
    team: str
    company_id: int
    

class Company(BaseModel):
    name: str
    location: str
    
class DisplayEmployee(BaseModel):
    name: str
    role: str
    experience: int
    team: str
    
    class Config():
        orm_mode = True


     
    
    