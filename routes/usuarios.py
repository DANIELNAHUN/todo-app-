from json import load
import os
from datetime import datetime, timedelta
from typing import Annotated, List
from dotenv import load_dotenv

from fastapi import APIRouter, Depends, HTTPException, Response
from starlette.status import HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash
from jose import jwt, JWTError

import models.usuarios as models_user
import schemas.usuarios as schemas_user
from config.db_todo import SessionLocal

usuarios = APIRouter()
load_dotenv()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

"""
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄
EMPLEADOS FUNCTIONS
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄

"""

@usuarios.get("/empleados", tags= ["Operaciones Empleados"], response_model=List[schemas_user.Empleados])
async def get_empleados(db: db_dependency):
    empleados_d = db.query(models_user.Empleados).all()
    return empleados_d

@usuarios.get("/empleado/{id_empleado}", response_model=schemas_user.Empleados, tags= ["Operaciones Empleados"])
async def get_empleado(id_empleado: int, db: db_dependency):
    empleado_d = db.query(models_user.Empleados).filter(models_user.Empleados.id_empleado == id_empleado).first()
    if empleado_d is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado_d

@usuarios.post("/empleado", response_model=schemas_user.Empleados, status_code = HTTP_201_CREATED, tags= ["Operaciones Empleados"])
async def create_empleado(empleado: schemas_user.Empleados, db: db_dependency):
    empleado_d = models_user.Empleados(**empleado.dict())
    empleado_d.fecha_creacion = datetime.now()
    empleado_d.id_estado_empleado = 1
    db.add(empleado_d)
    db.commit()
    db.refresh(empleado_d)
    return Response(status_code = HTTP_201_CREATED)

@usuarios.put("/empleado/{id_empleado}", response_model=schemas_user.Empleados, tags= ["Operaciones Empleados"])
async def update_empleado(id_empleado: int, empleado: schemas_user.Empleados, db: db_dependency):
    empleado_d = db.query(models_user.Empleados).filter(models_user.Empleados.id_empleado == id_empleado).first()
    if empleado_d is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    empleado_d.nombres = empleado.nombres
    empleado_d.apellido_paterno = empleado.apellido_paterno
    empleado_d.apellido_materno = empleado.apellido_materno
    empleado_d.email = empleado.email
    empleado_d.celular_personal = empleado.celular_personal
    empleado_d.celular_corporativo = empleado.celular_corporativo
    empleado_d.id_empresa = empleado.id_empresa
    empleado_d.id_ciudad = empleado.id_ciudad
    empleado_d.id_area = empleado.id_area
    empleado_d.id_cargo = empleado.id_cargo
    empleado_d.id_equipo = empleado.id_equipo
    empleado_d.id_estado_empleado = empleado.id_estado_empleado
    empleado_d.fecha_modificacion = datetime.now()
    db.commit()
    db.refresh(empleado_d)
    return empleado_d

@usuarios.delete("/empleado/{id_empleado}", status_code = HTTP_204_NO_CONTENT, tags= ["Operaciones Empleados"])
async def delete_empleado(id_empleado: int, db: db_dependency):
    usuario_d = db.query(models_user.Empleados).filter(models_user.Empleados.id_empleado == id_empleado).first()
    if usuario_d is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    usuario_d.fecha_eliminacion = datetime.now()
    usuario_d.id_estado_empleado = 2
    db.commit()
    db.refresh(usuario_d)
    return Response(status_code = HTTP_204_NO_CONTENT)

"""
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄
USUARIOS FUNCTIONS
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄

"""
def get_user(db: db_dependency, username: str):
    usuario = db.query(models_user.Usuarios).filter(models_user.Usuarios.username == username).first()
    if usuario is None:
        return []
    return usuario

def verify_password(password: str, password_hash: str):
    return check_password_hash(password_hash, password)

def authenticate_user(db: db_dependency, username: str, password: str):
    usuario = get_user(db, username)
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuario no encontrado", headers={"WWW-Authenticate": "Bearer"})
    if not verify_password(password, usuario.userpassword):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta", headers={"WWW-Authenticate": "Bearer"})
    return usuario

def create_token(data: dict):
    data_token = data.copy()
    data_token['exp'] = datetime.utcnow() + timedelta(seconds=int(os.getenv("TK_SEC_EXP")))
    access_token = jwt.encode(data_token, key=os.getenv("SECRET_KEY"), algorithm="HS256")
    return access_token

@usuarios.post("/usuario", response_model=schemas_user.Usuarios, status_code = HTTP_201_CREATED, tags= ["Operaciones Usuarios"])
async def create_user(db: db_dependency, user: schemas_user.Usuarios):
    usuario_d = models_user.Usuarios(**user.dict())
    usuario_d.userpassword = generate_password_hash(user.userpassword, "pbkdf2:sha256:30")
    usuario_d.fecha_creacion = datetime.now()
    db.add(usuario_d)
    db.commit()
    db.refresh(usuario_d)
    return usuario_d

@usuarios.post("/login", tags= ["Operaciones Usuarios"])
async def login_user(db: db_dependency, user: schemas_user.Usuarios):
    usuario_d = authenticate_user(db, user.username, user.userpassword)
    if not usuario_d:
        raise HTTPException(status_code=401, detail="Usuario no encontrado", headers={"WWW-Authenticate": "Bearer"})
    token = create_token({"sub": usuario_d.username})
    return token