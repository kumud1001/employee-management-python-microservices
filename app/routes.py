from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Employee
from app.schemas import EmployeeCreate


router = APIRouter()


def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.get("/employees")
def get_employees(
    db: Session = Depends(get_db)
):
    return db.query(Employee).all()


@router.post("/employees")
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):

    emp = Employee(
        name=employee.name,
        email=employee.email,
        department=employee.department
    )

    db.add(emp)
    db.commit()
    db.refresh(emp)

    return emp