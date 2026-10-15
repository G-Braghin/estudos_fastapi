from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from estudo_fastapi.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}


@app.get(
    '/exercio-aula02', status_code=HTTPStatus.OK, response_class=HTMLResponse
)
def exercio_aula02():
    message = """
    <html>
      <head>
        <title>Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""

    return message
