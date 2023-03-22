from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import CRUD
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

#Dependency
def getDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "test"}\

@app.get("/category/", response_model = list[schemas.Category])
def read_category(skip: int = 0, limit: int = 100, db: Session = Depends(getDB)):
    category = CRUD.getCategory(db,skip,limit)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@app.post("/category/", response_model= schemas.Category)
def create_category(name:schemas.CategoryCreate, db: Session = Depends(getDB)):
    category = CRUD.createCategory(db,name)
    if category:
        raise HTTPException(status_code=400, detail="Category existed")
    return CRUD.createCategory(db = db, category=name)
