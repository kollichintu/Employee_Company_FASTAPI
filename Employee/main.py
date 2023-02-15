from fastapi import FastAPI
from .import models
from .database import engine
from .routers import employee,company



app = FastAPI(
    title= 'Employee/Company API',
    description= 'API CRUD Operations on  Employee/Company'
)
app.include_router(employee.router)
app.include_router(company.router)

models.Base.metadata.create_all(engine)


