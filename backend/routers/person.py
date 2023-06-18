from fastapi import APIRouter, Depends, HTTPException
from database import CRUD
from dependencies import getDB
from sqlalchemy.orm import Session
from models import schemas
from authorization.auth import get_current_active_user

router = APIRouter(prefix="/person", tags=["person"])

@router.get("/", response_model = list[schemas.Persons])
def read_persons(skip: int = 0, limit: int = 100, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Retrieve a list of persons.

    Args:
        skip (int): The number of persons to skip (for pagination).
        limit (int): The maximum number of persons to retrieve (for pagination).
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Raises:
        HTTPException(404): If no persons are found.

    Returns:
        list[schemas.Persons]: A list of person objects.
    """
    persons = CRUD.getPersons(db, skip, limit)
    if persons is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return persons

@router.get("/{person_id}", response_model= schemas.Persons, status_code=200)
def read_person_by_id(person_id: int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Retrieve a person by their ID.

    Args:
        person_id (int): The ID of the person to retrieve.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Raises:
        HTTPException(404): If the person is not found.

    Returns:
        schemas.Persons: The person object.
    """
    person = CRUD.getPersonById(db=db, person_id=person_id)
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return person


@router.post("/", response_model= schemas.PersonsCreate, status_code=201)
def create_person(name: schemas.PersonsCreate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Create a new person.

    Args:
        name (schemas.PersonsCreate): The data for creating the person.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Raises:
        HTTPException(400): If the person already exists.

    Returns:
        schemas.PersonsCreate: The created person object.
    """
    person = CRUD.createPerson(db = db, person = name)
    if person is None:
        raise HTTPException(status_code=400, detail="Person existed")
    return person

@router.patch("/{person_id}", response_model= schemas.PersonsUpdate, status_code=200)
def update_person(person_id: int, person: schemas.PersonsUpdate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Update a person.

    Args:
        person_id (int): The ID of the person to update.
        person (schemas.PersonsUpdate): The updated data for the person.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Raises:
        HTTPException(404): If the person is not found.

    Returns:
        schemas.PersonsUpdate: The updated person object.
    """
    per = CRUD.getPersonById(db=db, person_id=person_id)
    if per is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return CRUD.updatePerson(db = db, person = person, person_id = person_id)


@router.delete("/{person_id}", status_code=204)
def delete_person(person_id : int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Delete a person.

    Args:
        person_id (int): The ID of the person to delete.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Raises:
        HTTPException(404): If the person is not found.

    Returns:
        None
    """
    person = CRUD.getPersonById(db,person_id)
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return CRUD.delPerson(db = db, person = person)
