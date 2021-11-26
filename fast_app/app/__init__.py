from logging import debug
from fastapi import FastAPI

# fast api docs settings
fast_description = """
## Hello

This is FastAPI. FastAPI documentation [here](https://fastapi.tiangolo.com).

I've coded the index url "/" to redirect to this docs page [/docs](/docs). Docs are also available on [/redoc](/redoc).

"""

fast_tags_metadata = [
        {
            "name": "Section 1",
            "description": "This is Section 1 description",
        },
        {
            "name": "Section 2",
            "description": "Section 2 description",
        },
    ]

# create fast api application
application = FastAPI(
        title='My FastAPI', 
        description=fast_description,
        contact={
            "name": "Zubair Patel",
            "url": "https://www.zubair-patel.co.za",
            "email": "email@domain.co.za",
        },
        openapi_tags=fast_tags_metadata
)

# import routers
from app.section_1.some_routes_1 import some_routes_1
application.include_router(some_routes_1)

from app.section_1.some_routes_2 import some_routes_2
application.include_router(some_routes_2)

from app.section_2.more_routes import more_routes
application.include_router(more_routes)