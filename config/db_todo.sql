USE todo_app_plus;

--
-- MODULO USUARIOS
--
CREATE TABLE empresas(
  id_empresa INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(250) NOT NULL,
  fecha_creacion DATETIME NOT NULL,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_empresa)
);

CREATE TABLE ciudades(
  id_ciudad INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(250) NOT NULL,
  fecha_creacion DATETIME NOT NULL,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_ciudad)
);

CREATE TABLE empresas_ciudades(
  id_empresa_ciudad INT NOT NULL AUTO_INCREMENT,
  id_empresa INT NOT NULL,
  id_ciudad INT NOT NULL,
  fecha_creacion DATETIME NOT NULL,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_empresa_ciudad)
);

ALTER TABLE empresas_ciudades ADD FOREIGN KEY (id_empresa) REFERENCES empresas(id_empresa);
ALTER TABLE empresas_ciudades ADD FOREIGN KEY (id_ciudad) REFERENCES ciudades(id_ciudad);

CREATE TABLE areas(
  id_area INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(250) NOT NULL,
  fecha_creacion DATETIME NOT NULL,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_area)
);

CREATE TABLE cargo(
  id_cargo INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(250) NOT NULL,
  id_area INT NOT NULL,
  fecha_creacion DATETIME NOT NULL,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_cargo)
);
ALTER TABLE cargo ADD FOREIGN KEY (id_area) REFERENCES areas(id_area);

CREATE TABLE estado_usuario(
  id_estado_usuario INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(250) NOT NULL,
  fecha_creacion DATETIME NOT NULL,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_estado_usuario)
);

CREATE TABLE equipo(
  id_equipo INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(250) NOT NULL,
  fecha_creacion DATETIME NOT NULL,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_equipo)
);

--
-- MODULO PERMISOS
--
CREATE TABLE roles(
  id_rol INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(250) NOT NULL,
  fecha_creacion DATETIME NOT NULL,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_rol)
);

CREATE TABLE permisos(
  id_permiso INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(250) NOT NULL,
  fecha_creacion DATETIME NOT NULL,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_permiso)
)

CREATE TABLE roles_permisos(
  id_rol_permiso INT NOT NULL AUTO_INCREMENT,
  id_rol INT NOT NULL,
  id_permiso INT NOT NULL,
  fecha_creacion DATETIME NOT NULL,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_rol_permiso)
);

CREATE TABLE usuarios_roles(
  id_usuario_rol INT NOT NULL AUTO_INCREMENT,
  id_usuario INT NOT NULL,
  id_rol INT NOT NULL,
  fecha_creacion DATETIME NOT NULL,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_usuario_rol)
);

CREATE TABLE usuarios_permisos(
  id_usuario_permiso INT NOT NULL AUTO_INCREMENT,
  id_usuario INT NOT NULL,
  id_permiso INT NOT NULL,
  fecha_creacion DATETIME NOT NULL,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_usuario_permiso)
);

CREATE TABLE usuarios(
  id_usuario INT NOT NULL AUTO_INCREMENT,
  dni VARCHAR(50) NOT NULL,
  nombres TEXT NOT NULL,
  apellido_paterno VARCHAR(250) NOT NULL,
  apellido_materno VARCHAR(250) NOT NULL,
  email VARCHAR(50) DEFAULT NULL,
  celular_personal INT NOT NULL,
  celular_corporativo INT DEFAULT NULL,
  id_empresa INT NOT NULL,
  id_ciudad INT NOT NULL,
  id_area INT NOT NULL,
  id_cargo INT NOT NULL,
  id_equipo INT NOT NULL,
  usuario VARCHAR(50) DEFAULT NULL,
  password TEXT DEFAULT NULL,
  token TEXT DEFAULT NULL,
  id_rol INT NOT NULL,
  id_estado_usuario INT NOT NULL,
  fecha_creacion DATETIME NOT NULL,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_usuario)
);

ALTER TABLE usuarios ADD FOREIGN KEY (id_empresa) REFERENCES empresas(id_empresa);
ALTER TABLE usuarios ADD FOREIGN KEY (id_ciudad) REFERENCES ciudades(id_ciudad);
ALTER TABLE usuarios ADD FOREIGN KEY (id_area) REFERENCES areas(id_area);
ALTER TABLE usuarios ADD FOREIGN KEY (id_cargo) REFERENCES cargo(id_cargo);
ALTER TABLE usuarios ADD FOREIGN KEY (id_estado_usuario) REFERENCES estado_usuario(id_estado_usuario);
ALTER TABLE usuarios ADD FOREIGN KEY (id_rol) REFERENCES roles(id_rol);
ALTER TABLE usuarios ADD FOREIGN KEY (id_equipo) REFERENCES equipo(id_equipo);

--
-- MODULO NOTAS
--

CREATE TABLE estado_nota(
  id_estado_nota INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  fecha_creacion DATETIME NOT NULL,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_estado_nota)
);

CREATE TABLE prioridad(
  id_prioridad INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  fecha_creacion DATETIME NOT NULL,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_prioridad)
);
CREATE TABLE notas(
  id_nota INT NOT NULL AUTO_INCREMENT,
  titulo VARCHAR(250) NOT NULL,
  descripcion TEXT NOT NULL,
  id_usuario_create INT NOT NULL,
  id_usuario_asignado INT DEFAULT NULL,
  fecha_inicio DATETIME NOT NULL,
  fecha_limite DATETIME DEFAULT NULL,
  id_prioridad INT NOT NULL,
  id_estado_nota INT NOT NULL,
  fecha_creacion DATETIME NOT NULL,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_nota)
);
ALTER TABLE notas ADD FOREIGN KEY (id_usuario_create) REFERENCES usuarios(id_usuario);
ALTER TABLE notas ADD FOREIGN KEY (id_usuario_asignado) REFERENCES usuarios(id_usuario);
ALTER TABLE notas ADD FOREIGN KEY (id_prioridad) REFERENCES prioridad(id_prioridad);
ALTER TABLE notas ADD FOREIGN KEY (id_estado_nota) REFERENCES estado_nota(id_estado_nota);

--
-- MODULO LOGS
--

CREATE TABLE logs(
  id_log INT NOT NULL AUTO_INCREMENT,
  id_usuario INT NOT NULL,
  accion VARCHAR(250) NOT NULL, -- CREAR, MODIFICAR, ELIMINAR, CONSULTAR
  tabla VARCHAR(250) NOT NULL, -- USUARIOS, NOTAS, CIUDADES, ETC
  descripcion TEXT NOT NULL,
  fecha_creacion DATETIME NOT NULL,
  PRIMARY KEY (id_log)
);

-------------------------------------------------------------------
-------------------------------------------------------------------
-------------------- INSERCION DATOS DE PRUEBA --------------------
-------------------------------------------------------------------
-------------------------------------------------------------------

----
---- MODULO ACCESOS
----

INSERT INTO roles(nombre) VALUES ('ADMINISTRADOR'), ('SUPERVISOR'), ('COLABORADOR');
INSERT INTO permisos(nombre) VALUES
-- PERMISOS USUARIOS
('CREAR USUARIO'), ('MODIFICAR TODOS LOS USUARIOS'), ('ELIMINAR USUARIOS'), ('CONSULTAR TODOS LOS USUARIOS'), -- ACCESOS ADMIN
('MODIFICAR USUARIO PROPIO'), ('CONSULTAR USUARIO PROPIO'), -- ACCESOS GENERALES
('DAR DE BAJA USUARIO'), ('CONSULTAR USUARIOS POR EQUIPO'), -- ACCESOS ESPECIALES
-- PERMISOS NOTAS
('MODIFICAR TODAS LAS NOTAS'), ('ELIMINAR NOTAS'), ('CONSULTAR TODAS LAS NOTAS'), -- ACCESOS ADMIN
('CREAR NOTA'), ('MODIFICAR NOTA PROPIA'), ('CONSULTAR SUS NOTAS'), ('CERRAR NOTA'), -- ACCESOS GENERALES
('ASIGNAR NOTAS'), ('CONSULTAR NOTAS POR EQUIPO'), -- ACCESOS ESPECIALES
-- PARAMETROS DEL SISTEMA
('CONFIGURAR PARAMETROS'), ('CONSULTAR PARAMETROS') -- ACCESOS ADMIN
;

INSERT INTO roles_permisos(id_rol, id_permiso) VALUES
(1,1), (1,2), (1,3), (1,4), (1, 9), (1, 10), (1, 11),
(2,5), (2,6), (2,8), (2,12), (2,13), (2,14), (2,15), (2,16), (2,17),
(3,5), (3,6), (3,12), (3,13), (3,14), (3,15);

----
---- MODULO USUARIOS
----
INSERT INTO empresas(nombre) VALUES ('CABAPICE'), ('CABLEFAST'), ('MAFERANA'), ('EFICIENT'), ('WORKPLANNER');
INSERT INTO ciudades(nombre) VALUES ('ILO'), ('MOQUEGUA'), ('TACNA'), ('AREQUIPA'), ('MOLLENDO');
INSERT INTO areas(nombre) VALUES ('CONTABILIDAD'), ('LOGISTICA'), ('MARKETING'), ('TI');
INSERT INTO cargo(nombre, id_area) VALUES ('JEFATURA CONTABILIDAD', 1), ('ANALISTA MARKETING', 3), ('ASISTENTE LOGISTICO', 2), ('ENCARGADO TI', 4), ('ASISTENTE TI', 4), ('SUPERVISOR TI', 4);
INSERT INTO equipo(nombre) VALUES ('TI'), ('DISEÑO'), ('LOGISTICA'), ('CALL CENTER'), ('CONTABILIDAD');
INSERT INTO estado_usuario(nombre) VALUES ('ACTIVO'), ('INACTIVO'), ('SUSPENDIDO');
INSERT INTO usuarios
(dni, nombres, apellido_paterno, apellido_materno, celular_personal, id_empresa, id_ciudad, id_area, id_cargo, id_equipo, id_rol, id_estado_usuario, fecha_creacion)
VALUES
('74621395', 'DANIEL', 'CALCINA', 'FUENTES', '922996705', 2, 4, 4, 4, 1, 1, 1, CURRENT_TIMESTAMP),
('75362422', 'MILTON', 'HACHA', 'VASQUEZ', '930255996', 5, 1, 4, 6, 1, 2, 1, CURRENT_TIMESTAMP),
('72757524', 'BRAYAN', 'VALDEZ', 'QUISPE', '995000427', 5, 1, 4, 5, 1, 3, 1, CURRENT_TIMESTAMP);

----
---- MODULO ROLES POR USUARIOS
----
INSERT INTO usuarios_roles(id_usuario, id_rol) VALUES (1, 1), (2, 2), (3, 3);

----
---- MODULO NOTAS
----
INSERT INTO prioridad(nombre) VALUES ('ALTA'), ('MEDIA'), ('BAJA');
INSERT INTO estado_nota(nombre) VALUES ('NUEVA'), ('PENDIENTE'), ('EN PROCESO'), ('FINALIZADO');
INSERT INTO notas(titulo, descripcion, id_usuario_create, id_usuario_asignado, fecha_inicio, id_prioridad, id_estado_nota, fecha_creacion)
VALUES
('Nota de prueba', 'Esta es una nota de prueba', 1, 1, '2022-01-01', 1, 2, CURRENT_TIMESTAMP);

-------------------------------------------------------------------
-------------------------------------------------------------------
----------------------------- VISTAS ------------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------

-- Vista para obtener los permisos por cada rol del sistema
CREATE VIEW vista_permisos_rol AS
SELECT r.id_rol, r.nombre as nombre_rol, p.id_permiso, p.nombre as nombre_permiso
FROM roles r
INNER JOIN roles_permisos rp ON r.id_rol = rp.id_rol
INNER JOIN permisos p ON rp.id_permiso = p.id_permiso;

-- Vista para obtener los usuarios por cada rol del sistema
CREATE VIEW vista_usuarios_rol AS
SELECT u.id_usuario, u.nombres as nombre_usuario, u.apellido_paterno, r.id_rol, r.nombre as nombre_rol
FROM usuarios u
INNER JOIN usuarios_roles ur ON u.id_usuario = ur.id_usuario
INNER JOIN roles r ON ur.id_rol = r.id_rol;

-- Vista para obtener los permisos de un usuario
CREATE VIEW vista_permisos_usuario AS
SELECT p.nombre AS permiso, u.nombres
FROM usuarios u
JOIN usuarios_roles ur ON u.id_usuario = ur.id_usuario
JOIN roles r ON ur.id_rol = r.id_rol
JOIN roles_permisos rp ON r.id_rol = rp.id_rol
JOIN permisos p ON rp.id_permiso = p.id_permiso
UNION
SELECT p.nombre AS permiso, u.nombres
FROM usuarios u
JOIN usuarios_permisos up ON u.id_usuario = up.id_usuario
JOIN permisos p ON up.id_permiso = p.id_permiso