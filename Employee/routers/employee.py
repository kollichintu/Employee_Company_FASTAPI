from fastapi import APIRouter, status, HTTPException
from ..import schemas,models
from sqlalchemy.orm import Session
from fastapi.params import Depends
from ..database import get_database
from typing import List

router = APIRouter(
    tags= ['Employee'],
    prefix="/employee"
)


#fetching all employee's  from the database
@router.get('',status_code=status.HTTP_200_OK, response_model= List[schemas.DisplayEmployee])
def get_employee(db: Session = Depends(get_database)):
    return db.query(models.Employee).all()

@router.post('')
def create_employee(request:schemas.Employee, db:Session = Depends(get_database)):
    db_employee = models.Employee(name = request.name, role = request.role, experience = request.experience,
                                  team = request.team, company_id = request.company_id)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return request


#fetching Employee by id
@router.get('/{id}', response_model=schemas.DisplayEmployee)
def get_Employee(id, db:Session = Depends(get_database)):
    if (
        Employee := db.query(models.Employee)
        .filter(models.Employee.id == id)
        .first()
    ):
        return Employee
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Employee not found with the Input Id')



#delete Employee from DB
@router.delete('/{id}')
def delete(id,db:Session = Depends(get_database)):
    delete_Employee = db.query(models.Employee).filter(models.Employee.id == id).delete(synchronize_session=False)
    db.commit()
    return {'Employee got deleted'}



#update Employee in DB
@router.put('/{id}')
def update(id, request:schemas.Employee, db:Session = Depends(get_database)):
    Employee = db.query(models.Employee).filter(models.Employee.id == id)
    if not Employee.first():
        pass
    Employee.update(request.dict())
    db.commit()
    return {'Employee got updated'}