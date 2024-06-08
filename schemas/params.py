from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel

class Empresas(BaseModel):
  id_empresa = Optional[int] = None
  nombre = Optional[str] = None
  fecha_creacion: Optional[datetime] = None
  fecha_modificacion: Optional[datetime] = None
  fecha_eliminacion: Optional[datetime] = None
  class Config:
      orm_mode = True

class Ciudades(BaseModel):
  id_ciudad = Optional[int] = None
  nombre = Optional[str] = None
  fecha_creacion: Optional[datetime] = None
  fecha_modificacion: Optional[datetime] = None
  fecha_eliminacion: Optional[datetime] = None
  class Config:
      orm_mode = True

class EmpresasCiudades(BaseModel):
  id_empresa_ciudad = Optional[int] = None
  id_empresa = Optional[int] = None
  id_ciudad = Optional[int] = None
  fecha_creacion: Optional[datetime] = None
  fecha_modificacion: Optional[datetime] = None
  fecha_eliminacion: Optional[datetime] = None
  class Config:
      orm_mode = True

class Areas(BaseModel):
  id_area = Optional[int] = None
  nombre = Optional[str] = None
  fecha_creacion: Optional[datetime] = None
  fecha_modificacion: Optional[datetime] = None
  fecha_eliminacion: Optional[datetime] = None
  class Config:
      orm_mode = True

class Cargo(BaseModel):
  id_cargo = Optional[int] = None
  nombre = Optional[str] = None
  id_area = Optional[int] = None
  fecha_creacion: Optional[datetime] = None
  fecha_modificacion: Optional[datetime] = None
  fecha_eliminacion: Optional[datetime] = None
  class Config:
      orm_mode = True

class Equipo(BaseModel):
  id_equipo = Optional[int] = None
  nombre = Optional[str] = None
  fecha_creacion: Optional[datetime] = None
  fecha_modificacion: Optional[datetime] = None
  fecha_eliminacion: Optional[datetime] = None
  class Config:
      orm_mode = True

class Roles(BaseModel):
  id_rol = Optional[int] = None
  nombre = Optional[str] = None
  fecha_creacion: Optional[datetime] = None
  fecha_modificacion: Optional[datetime] = None
  fecha_eliminacion: Optional[datetime] = None
  class Config:
      orm_mode = True

class Permisos(BaseModel):
  id_permiso = Optional[int] = None
  nombre = Optional[str] = None
  fecha_creacion: Optional[datetime] = None
  fecha_modificacion: Optional[datetime] = None
  fecha_eliminacion: Optional[datetime] = None
  class Config:
      orm_mode = True

class RolesPermisos(BaseModel):
  id_rol_permiso = Optional[int] = None
  id_rol = Optional[int] = None
  id_permiso = Optional[int] = None
  fecha_creacion: Optional[datetime] = None
  fecha_modificacion: Optional[datetime] = None
  fecha_eliminacion: Optional[datetime] = None
  class Config:
      orm_mode = True

class UsuariosPermisos(BaseModel):
  id_usuario_permiso = Optional[int] = None
  id_usuario = Optional[int] = None
  id_permiso = Optional[int] = None
  fecha_creacion: Optional[datetime] = None
  fecha_modificacion: Optional[datetime] = None
  fecha_eliminacion: Optional[datetime] = None
  class Config:
      orm_mode = True

class Logs(BaseModel):
  id_log = Optional[int] = None
  id_usuario = Optional[int] = None
  accion = Optional[str] = None
  tabla = Optional[str] = None
  descripcion = Optional[str] = None
  fecha_creacion: Optional[datetime] = None
  class Config:
      orm_mode = True