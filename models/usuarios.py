from sqlalchemy import Column, ForeignKey, Text
from sqlalchemy.sql.sqltypes import DateTime, Integer, String

from config.db_todo import Base


class EstadosEmpleados(Base):
  __tablename__ = 'estados_empleados'
  id_estado_empleado = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(250))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class Empleados(Base):
  __tablename__ = 'empleados'
  id_empleado = Column(Integer, primary_key=True, autoincrement=True)
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
  id_cargo = Column(Integer, ForeignKey('cargos.id_cargo'))
  id_equipo = Column(Integer, ForeignKey('equipos.id_equipo'))
  id_estado_empleado = Column(Integer, ForeignKey('estados_empleados.id_estado_empleado'))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

# AGREGAR TABLA USUARIOS
class Usuarios(Base):
  __tablename__ = 'usuarios'
  id_usuario = Column(Integer, primary_key=True, autoincrement=True)
  username = Column(String(250))
  userpassword = Column(Text)
  usertoken = Column(Text)
  id_empleado = Column(Integer, ForeignKey('empleados.id_empleado'))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)