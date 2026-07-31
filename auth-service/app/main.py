from fastapi import FastAPI

from .database import Base, engine
from . import models


Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="Authentication Service",
    version="1.0"
)


@app.get("/")
def home():

    return {
        "service": "Authentication Service",
        "status": "Running"
    }