from fastapi import FastAPI
from models import InsuranceRate
import json

app = FastAPI()

@app.get("calculate_insureance")
async def calculate_insurence(declared_value: float, cargo_type: str):
    rate = await InsuranceRate.filter(cargo_type=cargo_type).order_by("-date").first()
    if rate:
        insurance_cost = declared_value * rate.rate
        return {"insurance_cost": insurance_cost}
    else:
        return{"error": "No rate found"}
    
    
    



