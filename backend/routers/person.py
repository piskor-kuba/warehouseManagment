from fastapi import APIRouter, Depends, HTTPException
from database import CRUD
from dependencies import getDB
from sqlalchemy.orm import Session
from models import schemas
from authorization.auth import get_current_active_user

router = APIRouter(prefix="/person", tags=["person"])

@router.get("/", response_model = list[schemas.Persons])
def read_persons(skip: int = 0, limit: int = 100, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    persons = CRUD.getPersons(db, skip, limit)
    if persons is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return persons


@router.post("/", response_model= schemas.PersonsCreate, status_code=201)
def create_person(name: schemas.PersonsCreate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    person = read_persons(db = db)
    if name in person:
        raise HTTPException(status_code=400, detail="Person existed")
    return CRUD.createPerson(db = db, person = name)

@router.patch("/{person_id}", response_model= schemas.PersonsUpdate, status_code=200)
def update_employee(person_id: int, person: schemas.PersonsUpdate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    return CRUD.updatePerson(db = db, person = person, person_id = person_id)


@router.delete("/{person_id}", status_code=204)
def delete_product(person_id : int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    person = CRUD.getPersonById(db,person_id)
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return CRUD.delPerson(db = db, person = person)
