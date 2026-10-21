from http import HTTPStatus

from fastapi import FastAPI

from estudo_fastapi.routers import auth, users
from estudo_fastapi.schemas import Message

app = FastAPI()

app.include_router(auth.rauter)
app.include_router(users.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}
