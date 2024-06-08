from config.db_todo import Base
from sqlalchemy import Column, ForeignKey, Text
from sqlalchemy.sql.sqltypes import Integer, String, DateTime


class Empresas(Base):
  __tablename__ = 'empresas'
  id_empresa = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(250))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class Ciudades(Base):
  __tablename__ = 'ciudades'
  id_ciudad = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(250))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class EmpresasCiudades(Base):
  __tablename__ = 'empresas_ciudades'
  id_empresa_ciudad = Column(Integer, primary_key=True, autoincrement=True)
  id_empresa = Column(Integer, ForeignKey('empresas.id_empresa'))
  id_ciudad = Column(Integer, ForeignKey('ciudades.id_ciudad'))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class Areas(Base):
  __tablename__ = 'areas'
  id_area = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(250))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class Cargo(Base):
  __tablename__ = 'cargo'
  id_cargo = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(250))
  id_area = Column(Integer, ForeignKey('areas.id_area'))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class Equipo(Base):
  __tablename__ = 'equipo'
  id_equipo = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(250))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class Roles(Base):
  __tablename__ = 'roles'
  id_rol = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(250))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class Permisos(Base):
  __tablename__ = 'permisos'
  id_permiso = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(250))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class RolesPermisos(Base):
  __tablename__ = 'roles_permisos'
  id_rol_permiso = Column(Integer, primary_key=True, autoincrement=True)
  id_rol = Column(Integer, ForeignKey('roles.id_rol'))
  id_permiso = Column(Integer, ForeignKey('permisos.id_permiso'))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class UsuariosPermisos(Base):
  __tablename__ = 'usuarios_permisos'
  id_usuario_permiso = Column(Integer, primary_key=True, autoincrement=True)
  id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
  id_permiso = Column(Integer, ForeignKey('permisos.id_permiso'))
  fecha_creacion = Column(DateTime)
  fecha_modificacion = Column(DateTime)
  fecha_eliminacion = Column(DateTime)

class Logs(Base):
  __tablename__ = 'logs'
  id_log = Column(Integer, primary_key=True, autoincrement=True)
  id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
  accion = Column(String(250))
  tabla = Column(String(250))
  descripcion = Column(Text)
  fecha_creacion = Column(DateTime)