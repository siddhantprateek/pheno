from fastapi import APIRouter
import json
import os
from modules import converter
router = APIRouter()


# @route: /api/v1
@router.get("/")
async def root():
    return {"status": 200, "message": "Welcome root of to Pheno!"}

# @route: /api/v1/stocks
@router.get("/stocks")
async def stocks():
    current_directory = os.getcwd()
    
    converter.csv_to_json()

    json_data_path = f'{current_directory}/data/output.json'

    with open(json_data_path, 'r') as json_file:
        data = json.load(json_file)
    return data