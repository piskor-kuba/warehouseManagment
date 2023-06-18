from fastapi import APIRouter, Depends, HTTPException
from database import CRUD
from dependencies import getDB
from sqlalchemy.orm import Session
from models import schemas
from authorization.auth import get_current_active_user

router = APIRouter(prefix="/employee", tags=["employee"])

@router.get("/", response_model = list[dict])
def read_employees(skip: int = 0, limit: int = 100, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Retrieve a list of employees.

    Args:
        skip (int): Number of records to skip (for pagination).
        limit (int): Maximum number of records to retrieve (for pagination).
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Returns:
        List[dict]: List of employee records.

    Raises:
        HTTPException(404): If no employees are found.
    """
    employee = CRUD.getEmployees(db, skip, limit)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employees not found")
    return employee

@router.get("/{employee_id}", response_model= dict, status_code=200)
def read_employee_by_id(employee_id: int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Retrieve an employee by ID.

    Args:
        employee_id (int): The ID of the employee to retrieve.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Returns:
        dict: Employee record.

    Raises:
        HTTPException(404): If the employee is not found.
    """
    employee = CRUD.getEmployeeById(db=db, employee_id=employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.post("/", response_model= schemas.EmployeesCreate, status_code=201)
def create_employee(emp: schemas.EmployeesCreate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Create a new employee.

    Args:
        emp (schemas.EmployeesCreate): The employee data to create.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Returns:
        schemas.EmployeesCreate: The created employee.

    Raises:
        HTTPException(400): If the employee already exists.
    """
    employee = CRUD.createEmployee(db = db, employee=emp)
    if employee is None:
        raise HTTPException(status_code=400, detail="Employee existed")
    return employee

@router.patch("/{employee_id}", response_model= schemas.EmployeesUpdate, status_code=200)
def update_employee(employee_id: int, employee: schemas.EmployeesUpdate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Update an existing employee.

    Args:
        employee_id (int): The ID of the employee to update.
        employee (schemas.EmployeesUpdate): The updated employee data.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Returns:
        schemas.EmployeesUpdate: The updated employee.

    Raises:
        HTTPException(404): If the employee is not found.
    """
    emp = CRUD.getEmployeeById(db=db, employee_id=employee_id)
    if emp is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return CRUD.updateEmployee(db = db, employee = employee, employee_id = employee_id)


@router.delete("/{employee_id}", status_code=204)
def delete_product(employee_id : int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Delete an employee.

    Args:
        employee_id (int): The ID of the employee to delete.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Raises:
        HTTPException(404): If the employee is not found.
    """
    employee = CRUD.getEmployeeById(db,employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail=" Employee not found")
    return CRUD.delEmployee(db = db, employee = employee)
