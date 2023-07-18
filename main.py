from tortoise import Tortoise
from app.main import app
from app.rate_loader import load_rates_from_json
from decouple import config
import uvicorn


DB_USER  = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_NAME = config("DB_NAME")

DATABASE_URL = f"postgres://{DB_USER}:{DB_PASSWORD}@localhost:5432/{DB_NAME}"

async def init_db():
    await Tortoise.init(
        db_url=DATABASE_URL,
        modules={"models": ["app.models"]},
    )
    
    await Tortoise.generate_schemas()
    


if __name__ == "__main__":
    
    load_rates_from_json("rates.json")
    app.include_router(app.router)
    uvicorn.run("main:app", host = "0.0.0.0", port=8000, reload=True)