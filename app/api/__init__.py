from fastapi import APIRouter 
from api.stocks import router as api_routes

base_router = APIRouter()
base_router.include_router(api_routes, prefix="/api/v1", tags=["stocks"])

@base_router.get("/")
async def index():
    return { 
        "response_status": 200, 
        "message": "Welcome to Pheno!",
    }