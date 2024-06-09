from config.db_todo import Base
from sqlalchemy import Column, ForeignKey, Text
from sqlalchemy.sql.sqltypes import Integer, String, DateTime


class EstadosNotas(Base):
  __tablename__ = 'estados_notas'
  id_estado_nota = Column(Integer, primary_key=True)
  nombre = Column(String(50))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class Prioridades(Base):
  __tablename__ = 'prioridades'
  id_prioridad = Column(Integer, primary_key=True)
  nombre = Column(String(50))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class Notas(Base):
  __tablename__ = 'notas'
  id_nota = Column(Integer, primary_key=True, autoincrement=True)
  titulo = Column(String(250))
  descripcion = Column(Text)
  id_usuario_create = Column(Integer, ForeignKey('usuarios.id_usuario'))
  id_usuario_asignado = Column(Integer, ForeignKey('usuarios.id_usuario'))
  fecha_inicio = Column(DateTime)
  fecha_limite = Column(DateTime)
  id_prioridad = Column(Integer, ForeignKey('prioridades.id_prioridad'))
  id_estado_nota = Column(Integer, ForeignKey('estados_notas.id_estado_nota'))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)