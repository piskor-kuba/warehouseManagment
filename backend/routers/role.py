from fastapi import APIRouter, Depends, HTTPException
from database import CRUD
from dependencies import getDB
from sqlalchemy.orm import Session
from models import schemas
from authorization.auth import get_current_active_user

router = APIRouter(prefix="/role", tags=["role"])

@router.get("/", response_model = list[schemas.Role])
def read_role(skip: int = 0, limit: int = 100, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    role = CRUD.getRole(db, skip, limit)
    if role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

@router.get("/{role_id}", response_model= schemas.Role, status_code=200)
def read_role_by_id(role_id: int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    role = CRUD.getRoleById(db=db, role_id=role_id)
    if role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return CRUD.getRoleById(db = db, role_id = role_id)

@router.post("/", response_model= schemas.RoleCreate, status_code=201)
def create_role(rol: schemas.RoleCreate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    role = CRUD.createRole(db = db, role=rol)
    if role is None:
        raise HTTPException(status_code=400, detail="Role existed")
    return role

@router.patch("/{role_id}", response_model= schemas.RoleUpdate, status_code=200)
def update_role(role_id: int, role: schemas.RoleUpdate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    rol = CRUD.getRoleById(db=db, role_id=role_id)
    if rol is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return CRUD.updateRole(db = db, role = role, role_id = role_id)


@router.delete("/{role_id}", status_code=204)
def delete_role(role_id : int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    role = CRUD.getRoleById(db,role_id)
    if role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return CRUD.delRole(db = db, role = role)
