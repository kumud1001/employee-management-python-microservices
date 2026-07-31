from fastapi import APIRouter, HTTPException
import httpx


router = APIRouter()

EMPLOYEE_SERVICE_URL = "http://localhost:8001"


@router.get("/employees")
async def get_employees():

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{EMPLOYEE_SERVICE_URL}/employees"
        )

    return response.json()


@router.get("/employees/{employee_id}")
async def get_employee(employee_id: int):

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{EMPLOYEE_SERVICE_URL}/employees/{employee_id}"
        )

    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return response.json()


@router.post("/employees")
async def create_employee(employee: dict):

    async with httpx.AsyncClient() as client:

        response = await client.post(
            f"{EMPLOYEE_SERVICE_URL}/employees",
            json=employee
        )

    return response.json()


@router.put("/employees/{employee_id}")
async def update_employee(
    employee_id: int,
    employee: dict
):

    async with httpx.AsyncClient() as client:

        response = await client.put(
            f"{EMPLOYEE_SERVICE_URL}/employees/{employee_id}",
            json=employee
        )

    return response.json()


@router.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int):

    async with httpx.AsyncClient() as client:

        response = await client.delete(
            f"{EMPLOYEE_SERVICE_URL}/employees/{employee_id}"
        )

    return {
        "message": "Employee deleted successfully"
    }