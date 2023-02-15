from fastapi import APIRouter, status, HTTPException
from ..import schemas,models
from fastapi.params import Depends
from sqlalchemy.orm import Session
from ..database import get_database

router = APIRouter(
    tags= ['Company'],
    prefix="/company"
)

#fetching all companies  from the database
@router.get('',status_code=status.HTTP_200_OK)
def get_company(db: Session = Depends(get_database)):
    return db.query(models.Company).all()


@router.post('')
def create_company(request:schemas.Company, db:Session = Depends(get_database)):
    db_company = models.Company(name=request.name, location=request.location)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return request


#fetching Company by id
@router.get('/{id}')
def get_Company(id, db:Session = Depends(get_database)):
    if (
        Company := db.query(models.Company)
        .filter(models.Company.id == id)
        .first()
    ):
        return Company
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Company not found with the Input Id')



#delete Company from DB
@router.delete('/{id}')
def delete(id,db:Session = Depends(get_database)):
    delete_Company = db.query(models.Company).filter(models.Company.id == id).delete(synchronize_session=False)
    db.commit()
    return {'Company got deleted'}



#update Company in DB
@router.put('/{id}')
def update(id, request:schemas.Company, db:Session = Depends(get_database)):
    Company = db.query(models.Company).filter(models.Company.id == id)
    if not Company.first():
        pass
    Company.update(request.dict())
    db.commit()
    return {'Company got updated'}
