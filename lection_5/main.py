import logging
from typing import Optional

from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.responses import HTMLResponse, JSONResponse
from starlette.templating import Jinja2Templates
from fastapi.openapi.utils import get_openapi

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(openapi_url='/api/v1/openapi.json')
templates = Jinja2Templates(directory='./lection_5/templates')


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


# @app.get('/')
# async def read_root():
#     logger.info('Отработал GET запрос.')
#     return {'Hello': 'World!'}

@app.get('/', response_class=HTMLResponse)
async def read_root():
    return '<h1>Hello World</h1>'


@app.get('/hello/{name}')
async def read_item(name: str, age: int):
    return {'Hello': name, 'Age': age}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title='Custom Title',
        version="1.0.0",
        description="Custom schema",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


@app.get('/{name}', response_class=HTMLResponse)
async def read_item(request: Request, name: str):
    print(request)
    return templates.TemplateResponse('item.html', {'request': request, 'name': name})


@app.get('/message')
async def read_message():
    message = {'message': 'Hello World!'}
    return JSONResponse(content=message, status_code=200)


@app.get('/items/{item_id}')
async def read_item(item_id: int, q: str = None):
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}


@app.get('/users/{user_id}/orders/{order_id}')
async def read_data(user_id: int, order_id: int):
    # обработка данных
    return {'user_id': user_id, 'order_id': order_id}


@app.get('/items/')
async def skip_limits(skip: int = 0, limit: int = 10):
    return {'skip': skip, 'limit': limit}


@app.post('/items/')
async def create_item(item: Item):
    logger.info('Отработал POST запрос.')
    return item


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    logger.info(f'Отработал PUT запрос для item id = {item_id}.')
    return {'item_id': item_id, 'item': item}


@app.delete('/items/{item_id}')
async def delete_item(item_id: int):
    logger.info(f'Отработал DELETE запрос для item id = {item_id}.')
    return {'item_id': item_id}