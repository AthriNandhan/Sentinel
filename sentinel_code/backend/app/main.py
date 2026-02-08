from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Sentinel-Code backend")

app.include_router(router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Sentinel-Code Backend is running"}
