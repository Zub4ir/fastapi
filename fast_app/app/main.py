from logging import debug
from fastapi import FastAPI

from app.chart_data.charts_1 import charts_1

application = FastAPI(title="PRIME Fast API")

application.include_router(charts_1)

@application.get("/")
async def root():
    
    return {"message": "This is Fast API"}

@application.get("/fapi/ts-numeric/{entity}")
def numeric(entity: int): # note not async
    
    return [{"date": "1", "entity": entity, "value": 50}, {"date": "2", "entity": entity, "value": 100}]

