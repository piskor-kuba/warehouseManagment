from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn
from database.database import engine
from database import models
from routers import users,product,person,employee,category,client,workplace,role

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = [
    "http://localhost/",
    "http://localhost:8000/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=[""],
)

app.include_router(users.router)
app.include_router(category.router)
app.include_router(product.router)
app.include_router(person.router)
app.include_router(employee.router)
app.include_router(client.router)
app.include_router(workplace.router)
app.include_router(role.router)


if __name__ == "__main__":
    uvicorn.run(app, host = "localhost", port = 8000)
