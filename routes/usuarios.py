import os
from datetime import datetime, timedelta
from json import load
from typing import Annotated, List

from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, Response
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from starlette.status import (HTTP_201_CREATED, HTTP_204_NO_CONTENT,
                              HTTP_404_NOT_FOUND)
from werkzeug.security import check_password_hash, generate_password_hash

import models.params as models_params
import models.usuarios as models_user
import schemas.usuarios as schemas_user
from config.db_todo import SessionLocal
from . import functions as func

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
async def get_empleados(db: db_dependency, token: str):
    # user = get_user_by_usertoken(db=db, token=token)
    # if user is None:
    #     raise HTTPException(status_code=404, detail="Usuario no encontrado")
    # list_permisos = get_permisos_by_user(db=db, id_usuario=user.id_usuario)
    list_permisos = func.get_permisos(db=db, token=token)
    if 8 in list_permisos:
        empleados_d = db.query(models_user.Empleados).all()
        return empleados_d
    else:
        raise HTTPException(status_code=403, detail="Acceso denegado")

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
def get_user_by_username(db: db_dependency, username: str):
    usuario = db.query(models_user.Usuarios).filter(models_user.Usuarios.username == username).first()
    if usuario is None:
        return []
    return usuario

def get_permisos(db: db_dependency, token: str):
    user = get_user_by_usertoken(db=db, token=token)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    list_permisos = get_permisos_by_user(db=db, id_usuario=user.id_usuario)
    return list_permisos

def get_user_by_usertoken(db: db_dependency, token: str):
    usuario = db.query(models_user.Usuarios).filter(models_user.Usuarios.usertoken == token).first()
    if usuario is None:
        return []
    return usuario

def get_permisos_by_user(db: db_dependency, id_usuario: int):
    permisos_user = []
    roles = db.query(models_params.UsuariosRoles).filter(models_params.UsuariosRoles.id_usuario == id_usuario).all()
    roles_permisos = db.query(models_params.RolesPermisos).filter(models_params.RolesPermisos.id_rol.in_([role.id_rol for role in roles])).all()
    permisos = db.query(models_params.UsuariosPermisos).filter(models_params.UsuariosPermisos.id_usuario == id_usuario).all()
    permisos_by_user = [permiso.id_permiso for permiso in permisos]
    permisos_by_rol = [permiso.id_permiso for permiso in roles_permisos]
    if len(permisos_by_rol) > 0:
        permisos_user.extend(permisos_by_rol)
    if len(permisos_by_user) > 0:
        permisos_user.extend(permisos_by_user)
    if len(permisos_user) == 0:
        return []
    return permisos_user


def verify_password(password: str, password_hash: str):
    return check_password_hash(password_hash, password)

def authenticate_user(db: db_dependency, username: str, password: str):
    usuario = get_user_by_username(db, username)
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
    if not usuario_d.usertoken:
        token = create_token({"sub": usuario_d.username})
        usuario_d.usertoken = token
    else:
        token = usuario_d.usertoken
    db.commit()
    db.refresh(usuario_d)
    return usuario_d

@usuarios.post("/logout", tags= ["Operaciones Usuarios"])
async def logout_user(db: db_dependency, user: schemas_user.Usuarios):
    usuario_d = get_user_by_username(db, user.username)
    if not usuario_d:
        raise HTTPException(status_code=401, detail="Usuario no encontrado", headers={"WWW-Authenticate": "Bearer"})
    usuario_d.usertoken = None
    db.commit()
    db.refresh(usuario_d)
    return usuario_d

