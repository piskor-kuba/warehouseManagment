from fastapi import FastAPI
import uvicorn
from database.database import engine
from database import models
from routers import users,product,person,employee,category,client,workplace,role
from configuration.config import Server
models.Base.metadata.create_all(bind=engine)

config = Server()
app = FastAPI()
app.include_router(users.router)
app.include_router(category.router)
app.include_router(product.router)
app.include_router(person.router)
app.include_router(employee.router)
app.include_router(client.router)
app.include_router(workplace.router)
app.include_router(role.router)

if __name__ == "__main__":
    uvicorn.run(app, host = config.host, port = config.port)
