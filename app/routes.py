from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import SessionLocal
from .models import Employee
from .schemas import EmployeeCreate


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



@router.get("/employees/{employee_id}")
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()


    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee



@router.post("/employees")
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):

    new_employee = Employee(
        name=employee.name,
        email=employee.email,
        department=employee.department
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee



@router.put("/employees/{employee_id}")
def update_employee(
    employee_id: int,
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):

    existing = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()


    if not existing:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )


    existing.name = employee.name
    existing.email = employee.email
    existing.department = employee.department


    db.commit()
    db.refresh(existing)

    return existing



@router.delete("/employees/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()


    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )


    db.delete(employee)
    db.commit()


    return {
        "message": "Deleted successfully"
    }