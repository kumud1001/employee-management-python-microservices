from fastapi import FastAPI
from .routes import router


app = FastAPI(
    title="Employee API Gateway"
)


app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "API Gateway Running"
    }