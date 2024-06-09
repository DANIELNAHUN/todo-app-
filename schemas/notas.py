from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class EstadosNotas(BaseModel):
  id_estado_nota: Optional[int] = None
  nombre: Optional[str] = None
  fecha_creacion: Optional[datetime] = None
  fecha_modificacion: Optional[datetime] = None
  fecha_eliminacion: Optional[datetime] = None
  class Config:
      orm_mode = True

class Prioridades(BaseModel):
  id_prioridad: Optional[int] = None
  nombre: Optional[str] = None
  fecha_creacion: Optional[datetime] = None
  fecha_modificacion: Optional[datetime] = None
  fecha_eliminacion: Optional[datetime] = None
  class Config:
      orm_mode = True

class Notas(BaseModel):
  id_nota: Optional[int] = None
  titulo: Optional[str] = None
  descripcion: Optional[str] = None
  id_usuario_create: Optional[int] = None
  id_usuario_asignado: Optional[int] = None
  fecha_inicio: Optional[datetime] = None
  fecha_limite: Optional[datetime] = None
  id_prioridad: Optional[int] = None
  id_estado_nota: Optional[int] = None
  fecha_creacion: Optional[datetime] = None
  fecha_modificacion: Optional[datetime] = None
  fecha_eliminacion: Optional[datetime] = None
  class Config:
      orm_mode = True