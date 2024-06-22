from typing import Annotated

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

import models.params as models_params
import models.usuarios as models_user
from config.db_todo import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


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