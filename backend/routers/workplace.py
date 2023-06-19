from fastapi import APIRouter, Depends, HTTPException
from database import CRUD
from dependencies import getDB
from sqlalchemy.orm import Session
from models import schemas
from authorization.auth import get_current_active_user

router = APIRouter(prefix="/workplace", tags=["workplace"])

@router.get("/", response_model = list[schemas.Workplace])
def read_workplace(skip: int = 0, limit: int = 100, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Retrieve a list of workplaces.

    Args:
        skip (int): Number of records to skip.
        limit (int): Maximum number of records to retrieve.
        current_user (schemas.LoginData): Current user data.
        db (Session): Database session.

    Returns:
        List[schemas.Workplace]: List of workplaces.

    """
    workplace = CRUD.getWorkplace(db, skip, limit)
    if workplace is None:
        raise HTTPException(status_code=404, detail="Workplace not found")
    return workplace

@router.get("/{workplace_id}", response_model= schemas.Workplace, status_code=200)
def read_workplace_by_id(workplace_id: int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Retrieve a workplace by its ID.

    Args:
        workplace_id (int): ID of the workplace.
        current_user (schemas.LoginData): Current user data.
        db (Session): Database session.

    Returns:
        schemas.Workplace: Workplace information.

    """
    workplace = CRUD.getWorkplaceById(db=db, workplace_id=workplace_id)
    if workplace is None:
        raise HTTPException(status_code=404, detail="Workplace not found")
    return CRUD.getWorkplaceById(db = db, workplace_id = workplace_id)

@router.post("/", response_model= schemas.WorkplaceCreate, status_code=201)
def create_workplace(work: schemas.WorkplaceCreate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Create a new workplace.

    Args:
        work (schemas.WorkplaceCreate): Workplace data.
        current_user (schemas.LoginData): Current user data.
        db (Session): Database session.

    Returns:
        schemas.WorkplaceCreate: Created workplace information.

    """
    workplace = CRUD.createWorkplace(db = db, workplace=work)
    if workplace is None:
        raise HTTPException(status_code=400, detail="Workplace existed")
    return workplace

@router.patch("/{workplace_id}", response_model= schemas.WorkplaceUpdate, status_code=200)
def update_workplace(workplace_id: int, workplace: schemas.WorkplaceUpdate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Update an existing workplace.

    Args:
        workplace_id (int): ID of the workplace to update.
        workplace (schemas.WorkplaceUpdate): Updated workplace data.
        current_user (schemas.LoginData): Current user data.
        db (Session): Database session.

    Returns:
        schemas.WorkplaceUpdate: Updated workplace information.

    """
    wor = CRUD.getWorkplaceById(db=db, workplace_id=workplace_id)
    if wor is None:
        raise HTTPException(status_code=404, detail="Workplace not found")
    return CRUD.updateWorkplace(db = db, workplace = workplace, workplace_id = workplace_id)

@router.delete("/{workplace_id}", status_code=204)
def delete_workplace(workplace_id : int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Delete a workplace.

    Args:
        workplace_id (int): ID of the workplace to delete.
        current_user (schemas.LoginData): Current user data.
        db (Session): Database session.

    Returns:
        None

    Raises:
        HTTPException: If the workplace is not found.

    """
    workplace = CRUD.getWorkplaceById(db,workplace_id)
    if workplace is None:
        raise HTTPException(status_code=404, detail="Workplace not found")
    return CRUD.delWorkplace(db = db, workplace = workplace)
