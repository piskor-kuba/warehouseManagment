from fastapi import APIRouter, Depends, HTTPException
from database import CRUD
from dependencies import getDB
from sqlalchemy.orm import Session
from models import schemas
from authorization.auth import get_current_active_user

router = APIRouter(prefix="/employee", tags=["employee"])

@router.get("/", response_model = list[schemas.Employees])
def read_employees(skip: int = 0, limit: int = 100, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    employee = CRUD.getEmployees(db, skip, limit)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employees not found")
    return employee


@router.post("/", response_model= schemas.EmployeesCreate, status_code=201)
def create_employee(emp: schemas.EmployeesCreate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    employee = read_employees(db = db)
    if emp in employee:
        raise HTTPException(status_code=400, detail="Employee existed")
    return CRUD.createEmployee(db = db, employee=emp)

@router.patch("/{employee_id}", response_model= schemas.EmployeesUpdate, status_code=200)
def update_employee(employee_id: int, employee: schemas.EmployeesUpdate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    return CRUD.updateEmployee(db = db, employee = employee, employee_id = employee_id)


@router.delete("/{employee_id}", status_code=204)
def delete_product(employee_id : int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    employee = CRUD.getProductById(db,employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail=" Employee not found")
    return CRUD.delEmployee(db = db, employee = employee)
