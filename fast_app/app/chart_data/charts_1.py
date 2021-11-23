from fastapi import APIRouter

charts_1 = APIRouter()

@charts_1.get("/charts/standard", tags=["charting"])
async def read_users():
    
    return [{"username": "Rick"}, {"username": "Morty"}]