from datetime import date, datetime
from typing import Optional
from unittest.mock import Base

from click import Option

from pydantic import BaseModel

class EstadosEmpleados(BaseModel):
  id_estado_empleado: Optional[int] = None
  nombre: Optional[str] = None
  fecha_creacion: Optional[datetime] = None
  fecha_modificacion: Optional[datetime] = None
  fecha_eliminacion: Optional[datetime] = None
  class Config:
      orm_mode = True

class Empleados(BaseModel):
  id_empleado: Optional[int] = None
  dni: Optional[str] = None
  nombres: Optional[str] = None
  apellido_paterno: Optional[str] = None
  apellido_materno: Optional[str] = None
  email: Optional[str] = None
  celular_personal : Optional[int] = None
  celular_corporativo : Optional[int] = None
  id_empresa : Optional[int] = None
  id_ciudad : Optional[int] = None
  id_area : Optional[int] = None
  id_cargo : Optional[int] = None
  id_equipo : Optional[int] = None
  id_estado_empleado : Optional[int] = None
  fecha_creacion: Optional[datetime] = None
  fecha_modificacion: Optional[datetime] = None
  fecha_eliminacion: Optional[datetime] = None
  class Config:
      orm_mode = True

# ARREGLAR TABLA USUARIO
class Usuarios(BaseModel):
  id_usuario: Optional[int] = None
  username: Optional[str] = None
  userpassword: Optional[str] = None
  usertoken: Optional[str] = None
  id_empleado: Optional[int] = None
  fecha_creacion: Optional[datetime] = None
  fecha_modificacion: Optional[datetime] = None
  fecha_eliminacion: Optional[datetime] = None
  class Config:
      orm_mode = True