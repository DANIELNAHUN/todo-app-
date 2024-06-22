import os
from datetime import datetime
from typing import Annotated, List, ParamSpecArgs
from urllib import response

from fastapi import APIRouter, Depends, HTTPException, Response
from starlette.status import HTTP_404_NOT_FOUND, HTTP_201_CREATED
from sqlalchemy.orm import Session

import models.params as models_par
import schemas.params as schemas_par
from config.db_todo import SessionLocal

params = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

"""
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄
EMPRESAS FUNCTIONS
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄

"""
@params.get("/empresas", response_model=List[schemas_par.Empresas], tags= ["Operaciones Parametros","Crud Empresas"])
async def get_empresas(db: db_dependency):
    empresas = db.query(models_par.Empresas).all()
    return empresas

@params.post("/empresas", response_model=schemas_par.Empresas, status_code = HTTP_201_CREATED, tags= ["Operaciones Parametros","Crud Empresas"])
async def create_empresa(empresa: schemas_par.Empresas, db: db_dependency):
    empresa_d = models_par.Empresas(**empresa.dict())
    empresa_d.fecha_creacion = datetime.now()
    db.add(empresa_d)
    db.commit()
    db.refresh(empresa_d)
    return Response(status_code = HTTP_201_CREATED)

@params.put("/empresas/{id_empresa}", response_model=schemas_par.Empresas, tags= ["Operaciones Parametros","Crud Empresas"])
async def update_empresa(id_empresa: int, empresa: schemas_par.Empresas, db: db_dependency):
    empresa_d = db.query(models_par.Empresas).filter(models_par.Empresas.id_empresa == id_empresa).first()
    if empresa_d is None:
        raise HTTPException(status_code=404, detail="Empresa not found")
    empresa_d.nombre = empresa.nombre
    empresa_d.fecha_modificacion = datetime.now()

    db.commit()
    db.refresh(empresa_d)
    return empresa_d

@params.delete("/empresas/{id_empresa}", response_model=schemas_par.Empresas, tags= ["Operaciones Parametros","Crud Empresas"])
async def delete_empresa(id_empresa: int, db: db_dependency):
    empresa_d = db.query(models_par.Empresas).filter(models_par.Empresas.id_empresa == id_empresa).first()
    if empresa_d is None:
        raise HTTPException(status_code=404, detail="Empresa not found")
    empresa_d.fecha_eliminacion = datetime.now()
    db.commit()
    db.refresh(empresa_d)
    return empresa_d

"""
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄
CIUDADES FUNCTIONS
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄

"""




"""
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄
EMPRESAS CIUDADES FUNCTIONS
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄

"""




"""
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄
AREAS FUNCTIONS
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄

"""




"""
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄
CARGOS FUNCTIONS
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄

"""




"""
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄
EQUIPOS FUNCTIONS
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄

"""





"""
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄
ROLES FUNCTIONS
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄

"""
@params.get("/roles", response_model=List[schemas_par.Roles], tags= ["Operaciones Parametros", "Crud Roles"])
async def get_roles(db: db_dependency):
    roles = db.query(models_par.Roles).all()
    return roles


"""
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄
TAG PERMISOS FUNCTIONS
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄

"""
@params.get("/tags_permisos", response_model=List[schemas_par.TagPermisos], tags= ["Operaciones Parametros", "Crud Tags Permisos"])
async def get_tags_permisos(db: db_dependency):
    tags_permisos = db.query(models_par.TagPermisos).all()
    return tags_permisos


"""
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄
PERMISOS FUNCTIONS
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄

"""
@params.get("/permisos", response_model=List[schemas_par.Permisos], tags= ["Operaciones Parametros", "Crud Permisos"])
async def get_permisos(db: db_dependency):
    permisos = db.query(models_par.Permisos).all()
    return permisos



"""
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄
ROLES PERMISOS FUNCTIONS
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄

"""
@params.get("/roles_permisos", response_model=List[schemas_par.RolesPermisos], tags= ["Operaciones Parametros", "Crud Roles Permisos"])
async def get_roles_permisos(db: db_dependency):
    roles_permisos = db.query(models_par.RolesPermisos).all()
    return roles_permisos


"""
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄
USUARIOS ROLES FUNCTIONS
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄

"""
@params.get("/usuarios_roles", response_model=List[schemas_par.UsuariosRoles], tags= ["Operaciones Usuarios", "Crud Usuarios Roles"])
async def get_usuarios_roles(db: db_dependency):
    usuarios_roles = db.query(models_par.UsuariosRoles).all()
    return usuarios_roles



"""
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄
USUARIOS PERMISOS FUNCTIONS
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄

"""
@params.get("/usuarios_permisos", response_model=List[schemas_par.UsuariosPermisos], tags= ["Operaciones Usuarios", "Crud Usuarios Permisos"])
async def get_usuarios_permisos(db: db_dependency):
    usuarios_permisos = db.query(models_par.UsuariosPermisos).all()
    return usuarios_permisos


"""
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄
LOGS FUNCTIONS
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄

"""