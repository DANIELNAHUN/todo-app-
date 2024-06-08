from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.notas import notas
from routes.params import params
from routes.usuarios import usuarios

load_dotenv()

app = FastAPI(
    title="API App Todo ++",
    version="1.0",
    description="Aplicacion Todo para practicar Gestion de Usuario con Token, Roles, Permisos y Logs",
    contact={
        "name": "Daniel Calcina",
        "email": "danielnahuncalcinafuentes@gmail.com"
    }
)

origins = [
    "https://172.16.0.6",
    "https://172.16.0.6:8081",
]

app.add_middleware(
  CORSMiddleware,
  allow_origins = ["*"],
  allow_credentials = True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(notas, prefix='/api/todo/notas')
app.include_router(params, prefix='/api/todo/parametros')
app.include_router(usuarios, prefix='/api/todo/usuarios')