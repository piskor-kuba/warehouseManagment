from fastapi import FastAPI
import uvicorn
from database.database import engine
from database import models
from routers import items, users

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)


@app.get("/")
def read_root():
    return {"Hello": "test"}


if __name__ == "__main__":
    uvicorn.run(app, host = "localhost", port = 8000)
