from fastapi import FastAPI , APIRouter
import os
from dotenv import load_dotenv

load_dotenv(".env")
  
base_router=APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
)

@base_router.get("/")
async def Welcome():
    app_name=os.getenv('App_Name')
    app_version=os.getenv('App_Version')
    return{
        "app_name":app_name,
        "app_version":app_version,

    }