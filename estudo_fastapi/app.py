import asyncio
import sys
from http import HTTPStatus

from fastapi import FastAPI

from estudo_fastapi.routers import auth, todos, users
from estudo_fastapi.schemas import Message

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(todos.router)

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
async def read_root():
    return {'message': 'Olá mundo!'}
