from datetime import date, datetime
from typing import Optional

from click import Option

from pydantic import BaseModel

class EstadoUsuario(BaseModel):
  id_estado_usuario: Optional[int]
  nombre: Optional[str] = None
  fecha_creacion: Optional[datetime] = None
  fecha_modificacion: Optional[datetime] = None
  fecha_eliminacion: Optional[datetime] = None
  class Config:
      orm_mode = True

class Usuario(BaseModel):
  id_usuario: Optional[int]
  dni: Optional[str] = None
  nombres: Optional[str] = None
  apellido_paterno: Optional[str] = None
  apellido_materno: Optional[str] = None
  email: Optional[str] = None
  celular_personal = Optional[int] = None
  celular_corporativo = Optional[int] = None
  id_empresa = Optional[int] = None
  id_ciudad = Optional[int] = None
  id_area = Optional[int] = None
  id_cargo = Optional[int] = None
  id_equipo = Optional[int] = None
  usuario = Optional[str] = None
  password = Optional[str] = None
  token = Optional[str] = None
  id_rol = Optional[int] = None
  id_estado_usuario = Optional[int] = None
  fecha_creacion: Optional[datetime] = None
  fecha_modificacion: Optional[datetime] = None
  fecha_eliminacion: Optional[datetime] = None
  class Config:
      orm_mode = True
