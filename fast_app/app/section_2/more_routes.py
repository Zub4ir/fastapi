from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.configs import settings

more_routes = APIRouter()

@more_routes.get('/section-2/test', tags=['Section 2'])
async def more_routes_test():

    return JSONResponse([
        {'message': 'Hello from Section 2'},
        {'message': 'This is still ' + settings.APP_NAME}
    ])

@more_routes.post('/section-2/test-msg/{msg}', tags=['Section 2'])
def more_routes_test_msg(msg:str):
    
    return JSONResponse([{'message': msg}])
