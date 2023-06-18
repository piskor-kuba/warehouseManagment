from fastapi import APIRouter, Depends, HTTPException
from database import CRUD
from dependencies import getDB
from sqlalchemy.orm import Session
from models import schemas
from authorization.auth import get_current_active_user

router = APIRouter(prefix="/role", tags=["role"])

@router.get("/", response_model = list[schemas.Role])
def read_role(skip: int = 0, limit: int = 100, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Read roles.

    Args:
        skip (int): Number of records to skip (used for pagination).
        limit (int): Maximum number of records to return (used for pagination).
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Raises:
        HTTPException(404): If no roles are found.

    Returns:
        List[schemas.Role]: List of role objects.
    """
    role = CRUD.getRole(db, skip, limit)
    if role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

@router.get("/{role_id}", response_model= schemas.Role, status_code=200)
def read_role_by_id(role_id: int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Read role by ID.

    Args:
        role_id (int): The ID of the role.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Raises:
        HTTPException(404): If the role with the specified ID is not found.

    Returns:
        schemas.Role: The role object.
    """
    role = CRUD.getRoleById(db=db, role_id=role_id)
    if role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return CRUD.getRoleById(db = db, role_id = role_id)

@router.post("/", response_model= schemas.RoleCreate, status_code=201)
def create_role(rol: schemas.RoleCreate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Create a new role.

    Args:
        rol (schemas.RoleCreate): The role data to be created.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Raises:
        HTTPException(400): If the role already exists.

    Returns:
        schemas.RoleCreate: The created role object.
    """
    role = CRUD.createRole(db = db, role=rol)
    if role is None:
        raise HTTPException(status_code=400, detail="Role existed")
    return role

@router.patch("/{role_id}", response_model= schemas.RoleUpdate, status_code=200)
def update_role(role_id: int, role: schemas.RoleUpdate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Update an existing role.

    Args:
        role_id (int): The ID of the role to be updated.
        role (schemas.RoleUpdate): The updated role data.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Raises:
        HTTPException(404): If the role is not found.

    Returns:
        schemas.RoleUpdate: The updated role object.
    """
    rol = CRUD.getRoleById(db=db, role_id=role_id)
    if rol is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return CRUD.updateRole(db = db, role = role, role_id = role_id)


@router.delete("/{role_id}", status_code=204)
def delete_role(role_id : int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Delete a role.

    Args:
        role_id (int): The ID of the role to be deleted.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Raises:
        HTTPException(404): If the role is not found.

    Returns:
        None
    """
    role = CRUD.getRoleById(db,role_id)
    if role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return CRUD.delRole(db = db, role = role)
