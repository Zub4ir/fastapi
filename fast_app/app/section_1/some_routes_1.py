from fastapi.responses import StreamingResponse
from fastapi import APIRouter
from fastapi.responses import JSONResponse, RedirectResponse
import pandas as pd
import asyncio, io, time

from app.configs import settings

# this router name a bit long, but just for illustrations
some_routes_1 = APIRouter()

@some_routes_1.get('/', tags=['Section 1'])
async def some_routes_1_index():

    # going here takes you to the docs
    
    return RedirectResponse('/docs')


@some_routes_1.get('/section-1/test-jsn', tags=['Section 1'])
async def some_routes_1_json_example():
    
    return JSONResponse([
        {'app_creator': settings.APP_CREATOR}, 
        {'message': 'protect the earth'}]
        )


@some_routes_1.get('/section-1/test-csv', tags=['Section 1'])
async def some_routes_1_csv_example():

    # sample data
    df = pd.DataFrame(data = [['Rick', 'David'], ['Dimebag', 'Darrel']], columns=['first', 'last'])

    # create bytes stream
    stream = io.StringIO()
    df.to_csv(stream, index = False)

    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=download.csv"

    return response


# Asynchronous example
# awaitable db methods here https://github.com/aio-libs/aiomysql
async def my_func_1():

    print('Func1 started..!!')
    await asyncio.sleep(5)
    print('Func1 ended..!!')

    return 'a..!!'

async def my_func_2():

    print('Func2 started..!!')
    await asyncio.sleep(5)
    print('Func2 ended..!!')

    return 'b..!!'

@some_routes_1.get("/section-1/test-async", tags=['Section 1']     )
async def some_routes_1_async_example():

    start = time.time()
    list_functions = [my_func_1(), my_func_2()]
    a,b = await asyncio.gather(*list_functions)
    end = time.time()

    print('It took {} seconds to finish execution.'.format(round(end-start)))

    return JSONResponse({
        'a': a,
        'b': b
    })