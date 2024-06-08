from config.db_todo import Base
from sqlalchemy import Column, ForeignKey, Text
from sqlalchemy.sql.sqltypes import Integer, String, DateTime


class EstadoUsuario(Base):
  __tablename__ = 'estado_usuario'
  id_estado_usuario = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(250))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class Usuarios(Base):
  __tablename__ = 'usuarios'
  id_usuario = Column(Integer, primary_key=True, autoincrement=True)
  dni = Column(String(50))
  nombres = Column(Text)
  apellido_paterno = Column(String(250))
  apellido_materno = Column(String(250))
  email = Column(String(250))
  celular_personal = Column(Integer)
  celular_corporativo = Column(Integer)
  id_empresa = Column(Integer, ForeignKey('empresas.id_empresa'))
  id_ciudad = Column(Integer, ForeignKey('ciudades.id_ciudad'))
  id_area = Column(Integer, ForeignKey('areas.id_area'))
  id_cargo = Column(Integer, ForeignKey('cargo.id_cargo'))
  id_equipo = Column(Integer, ForeignKey('equipo.id_equipo'))
  usuario = Column(String(50))
  password = Column(Text)
  token = Column(Text)
  id_rol = Column(Integer, ForeignKey('roles.id_rol'))
  id_estado_usuario = Column(Integer, ForeignKey('estado_usuario.id_estado_usuario'))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)