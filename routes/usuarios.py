import os
from datetime import datetime
from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, Response
from starlette.status import HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash

import models.usuarios as models_user
import schemas.usuarios as schemas_user
from config.db_todo import SessionLocal

usuarios = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

"""
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄
ESTADOS USUARIOS FUNCTIONS
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄

"""

@usuarios.get("/usuarios", response_model=List[schemas_user.Usuario])
async def get_usuarios(db: db_dependency):
    usuarios = db.query(models_user.Usuarios).all()
    return usuarios

@usuarios.get("/usuario/{id_usuario}", response_model=schemas_user.Usuario)
async def get_usuario(id_usuario: int, db: db_dependency):
    usuario = db.query(models_user.Usuarios).filter(models_user.Usuarios.id_usuario == id_usuario).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return usuario

@usuarios.post("/usuario", response_model=schemas_user.Usuario, status_code = HTTP_201_CREATED)
async def create_usuario(usuario: schemas_user.Usuario, db: db_dependency):
    usuario_d = models_user.Usuarios(**usuario.dict())
    usuario_d.fecha_creacion = datetime.now()
    usuario.id_estado_usuario = 1
    db.add(usuario_d)
    db.commit()
    db.refresh(usuario_d)
    return Response(status_code = HTTP_201_CREATED)

@usuarios.put("/usuario/{id_usuario}", response_model=schemas_user.Usuario)
async def update_usuario(id_usuario: int, usuario: schemas_user.Usuario, db: db_dependency):
    usuario_d = db.query(models_user.Usuarios).filter(models_user.Usuarios.id_usuario == id_usuario).first()
    if usuario_d is None:
        raise HTTPException(status_code=404, detail="Usuario not found")
    usuario_d.nombres = usuario.nombres
    usuario_d.apellido_paterno = usuario.apellido_paterno
    usuario_d.apellido_materno = usuario.apellido_materno
    usuario_d.email = usuario.email
    usuario_d.celular_personal = usuario.celular_personal
    usuario_d.celular_corporativo = usuario.celular_corporativo
    usuario_d.id_empresa = usuario.id_empresa
    usuario_d.id_ciudad = usuario.id_ciudad
    usuario_d.id_area = usuario.id_area
    usuario_d.id_cargo = usuario.id_cargo
    usuario_d.id_equipo = usuario.id_equipo
    usuario_d.usuario = usuario.usuario
    usuario_d.password = generate_password_hash(usuario.password, "pbkdf2:sha256:30", 50)
    usuario_d.id_rol = usuario.id_rol
    usuario_d.id_estado_usuario = usuario.id_estado_usuario
    usuario_d.fecha_modificacion = datetime.now()
    db.commit()
    db.refresh(usuario_d)
    return usuario_d

@usuarios.delete("/usuario/{id_usuario}", response_model=schemas_user.Usuario, status_code = HTTP_204_NO_CONTENT)
async def delete_usuario(id_usuario: int, db: db_dependency):
    usuario_d = db.query(models_user.Usuarios).filter(models_user.Usuarios.id_usuario == id_usuario).first()
    if usuario_d is None:
        raise HTTPException(status_code=404, detail="Usuario not found")
    usuario_d.fecha_eliminacion = datetime.now()
    usuario_d.id_estado_usuario = 2
    db.commit()
    db.refresh(usuario_d)
    return Response(status_code = HTTP_204_NO_CONTENT)