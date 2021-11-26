from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.configs import settings

some_routes_2 = APIRouter()

@some_routes_2.get('/section-1/another-api', tags=['Section 1'])
async def some_routes_2_another_api():
    
    return JSONResponse([
        {'message': 'Hello from the same section but a different router'}
        ])