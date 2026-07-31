from fastapi import FastAPI

from app.database import Base, engine
from app.routes import router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Employee Service"
)


app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Employee Service Running"
    }