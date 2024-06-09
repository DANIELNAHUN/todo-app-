USE todo_app_plus;

--
-- MODULO PARAMETROS
--
CREATE TABLE empresas(
  id_empresa INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(250) NOT NULL,
  fecha_creacion DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_empresa)
);

CREATE TABLE ciudades(
  id_ciudad INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(250) NOT NULL,
  fecha_creacion DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_ciudad)
);

CREATE TABLE empresas_ciudades(
  id_empresa_ciudad INT NOT NULL AUTO_INCREMENT,
  id_empresa INT NOT NULL,
  id_ciudad INT NOT NULL,
  fecha_creacion DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_empresa_ciudad)
);

ALTER TABLE empresas_ciudades ADD FOREIGN KEY (id_empresa) REFERENCES empresas(id_empresa);
ALTER TABLE empresas_ciudades ADD FOREIGN KEY (id_ciudad) REFERENCES ciudades(id_ciudad);

CREATE TABLE areas(
  id_area INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(250) NOT NULL,
  fecha_creacion DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_area)
);

CREATE TABLE cargos(
  id_cargo INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(250) NOT NULL,
  id_area INT NOT NULL,
  fecha_creacion DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_cargo)
);
ALTER TABLE cargos ADD FOREIGN KEY (id_area) REFERENCES areas(id_area);

CREATE TABLE equipos(
  id_equipo INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(250) NOT NULL,
  fecha_creacion DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_equipo)
);

--
-- MODULO USUARIO / EMPLEADO
--

CREATE TABLE estados_empleados(
  id_estado_empleado INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(250) NOT NULL,
  fecha_creacion DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_estado_empleado)
);

CREATE TABLE empleados(
  id_empleado INT NOT NULL AUTO_INCREMENT,
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
  id_estado_empleado INT NOT NULL,
  fecha_creacion DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_empleado)
);

ALTER TABLE empleados ADD FOREIGN KEY (id_empresa) REFERENCES empresas(id_empresa);
ALTER TABLE empleados ADD FOREIGN KEY (id_ciudad) REFERENCES ciudades(id_ciudad);
ALTER TABLE empleados ADD FOREIGN KEY (id_area) REFERENCES areas(id_area);
ALTER TABLE empleados ADD FOREIGN KEY (id_cargo) REFERENCES cargos(id_cargo);
ALTER TABLE empleados ADD FOREIGN KEY (id_equipo) REFERENCES equipos(id_equipo);
ALTER TABLE empleados ADD FOREIGN KEY (id_estado_empleado) REFERENCES estados_empleados(id_estado_empleado);

CREATE TABLE usuarios(
  id_usuario INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(250) NOT NULL,
  userpassword TEXT NOT NULL,
  usertoken TEXT NOT NULL,
  id_empleado INT NOT NULL,
  fecha_creacion DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_usuario)
);

ALTER TABLE usuarios ADD FOREIGN KEY(id_empleado) REFERENCES empleados(id_empleado);

--
-- MODULO PERMISOS
--

CREATE TABLE roles(
  id_rol INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(250) NOT NULL,
  fecha_creacion DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_rol)
);

CREATE TABLE tag_permisos(
  id_tag INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(250) NOT NULL,
  fecha_creacion DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_tag)
);

CREATE TABLE permisos(
  id_permiso INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(250) NOT NULL,
  id_tag INT DEFAULT NULL,
  fecha_creacion DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_permiso)
);
ALTER TABLE permisos ADD FOREIGN KEY (id_tag) REFERENCES tag_permisos(id_tag);

CREATE TABLE roles_permisos(
  id_rol_permiso INT NOT NULL AUTO_INCREMENT,
  id_rol INT NOT NULL,
  id_permiso INT NOT NULL,
  fecha_creacion DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_rol_permiso)
);
ALTER TABLE roles_permisos ADD FOREIGN KEY (id_rol) REFERENCES roles(id_rol);
ALTER TABLE roles_permisos ADD FOREIGN KEY (id_permiso) REFERENCES permisos(id_permiso);

CREATE TABLE usuarios_roles(
  id_usuario_rol INT NOT NULL AUTO_INCREMENT,
  id_usuario INT NOT NULL,
  id_rol INT NOT NULL,
  fecha_creacion DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_usuario_rol)
);
ALTER TABLE usuarios_roles ADD FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario);
ALTER TABLE usuarios_roles ADD FOREIGN KEY (id_rol) REFERENCES roles(id_rol);

CREATE TABLE usuarios_permisos(
  id_usuario_permiso INT NOT NULL AUTO_INCREMENT,
  id_usuario INT NOT NULL,
  id_permiso INT NOT NULL,
  fecha_creacion DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_usuario_permiso)
);
ALTER TABLE usuarios_permisos ADD FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario);
ALTER TABLE usuarios_permisos ADD FOREIGN KEY (id_permiso) REFERENCES permisos(id_permiso);

--
-- MODULO NOTAS
--

CREATE TABLE estados_notas(
  id_estado_nota INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  fecha_creacion DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_estado_nota)
);

CREATE TABLE prioridades(
  id_prioridad INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  fecha_creacion DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
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
  fecha_creacion DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  fecha_modificacion DATETIME DEFAULT NULL,
  fecha_eliminacion DATETIME DEFAULT NULL,
  PRIMARY KEY (id_nota)
);
ALTER TABLE notas ADD FOREIGN KEY (id_usuario_create) REFERENCES usuarios(id_usuario);
ALTER TABLE notas ADD FOREIGN KEY (id_usuario_asignado) REFERENCES usuarios(id_usuario);
ALTER TABLE notas ADD FOREIGN KEY (id_prioridad) REFERENCES prioridades(id_prioridad);
ALTER TABLE notas ADD FOREIGN KEY (id_estado_nota) REFERENCES estados_notas(id_estado_nota);

--
-- MODULO LOGS
--

CREATE TABLE logs(
  id_log INT NOT NULL AUTO_INCREMENT,
  id_usuario INT NOT NULL,
  accion VARCHAR(250) NOT NULL, -- CREAR, MODIFICAR, ELIMINAR, CONSULTAR
  tabla VARCHAR(250) NOT NULL, -- USUARIOS, NOTAS, CIUDADES, ETC
  campo VARCHAR(250) DEFAULT NULL,
  valor_anterior TEXT DEFAULT NULL,
  valor_nuevo TEXT DEFAULT NULL,
  descripcion TEXT NOT NULL,
  fecha_creacion DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id_log)
);

ALTER TABLE logs ADD FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario);

-- -----------------------------------------------------------------
-- -----------------------------------------------------------------
-- ------------------ INSERCION DATOS DE PRUEBA --------------------
-- -----------------------------------------------------------------
-- -----------------------------------------------------------------

-- --
-- -- MODULO ACCESOS
-- --

INSERT INTO roles(nombre) VALUES ('ADMINISTRADOR'), ('SUPERVISOR'), ('COLABORADOR'), ('RRHH');
INSERT INTO tag_permisos(nombre) VALUES ('PARAMETROS SISTEMA'), ('EMPLEADOS'), ('USUARIOS'), ('NOTAS');
INSERT INTO permisos(nombre, id_tag) VALUES
-- PARAMETROS DEL SISTEMA
('CONFIGURAR PARAMETROS', 1), ('CONSULTAR PARAMETROS', 1), -- ACCESOS ADMIN
-- PERMISOS EMPLEADOS
('ELIMINAR EMPLEADOS', 2), -- ACCESOS ADMIN
('MODIFICAR DATOS PERSONALES', 2), ('CONSULTAR DATOS EMPLEADO PROPIO', 2), -- ACCESOS GENERALES
('CREAR EMPLEADO', 2), ('DAR DE BAJA EMPLEADO', 2), ('CONSULTAR TODOS LOS EMPLEADOS', 2), ('MODIFICAR TODOS LOS EMPLEADOS', 2), -- ACCESOS RRHH
-- PERMISOS USUARIOS
('CREAR USUARIO', 3), ('MODIFICAR TODOS LOS USUARIOS', 3), ('ELIMINAR USUARIOS', 3), ('CONSULTAR TODOS LOS USUARIOS', 3), -- ACCESOS ADMIN
('CAMBIAR CONTRASEÑA', 3), ('CONSULTAR USUARIO PROPIO', 3), -- ACCESOS GENERALES
-- PERMISOS NOTAS
('MODIFICAR TODAS LAS NOTAS', 4), ('ELIMINAR NOTAS', 4), ('CONSULTAR TODAS LAS NOTAS', 4), -- ACCESOS ADMIN
('CREAR NOTA', 4), ('MODIFICAR NOTA PROPIA', 4), ('CONSULTAR SUS NOTAS', 4), ('CERRAR NOTA', 4), -- ACCESOS GENERALES
('ASIGNAR NOTAS', 4), ('CONSULTAR NOTAS POR EQUIPO', 4) -- ACCESOS ESPECIALES
;

INSERT INTO roles_permisos(id_rol, id_permiso) VALUES
-- ROL ADMIN
-- -- MODULO PARAMETROS
(1,1), (1,2),
-- -- MODULO EMPLEADOS
(1,3), (1,6), (1,7), (1,8), (1, 9),
-- -- MODULO USUARIOS
(1, 10), (1, 11), (1, 12), (1, 13), (1, 14),
-- -- MODULO NOTAS
(1, 16), (1, 17), (1, 18), (1, 19), (1, 22), (1, 23),
-- ROL SUPERVISOR
-- -- MODULO EMPLEADOS
(2,5),
-- -- MODULO USUARIOS
(2, 14), (2, 15),
-- -- MODULO NOTAS
(2, 19), (2, 20), (2, 21), (2, 22), (2, 23), (2, 24),
-- ROL COLABORADOR
-- MODULO EMPLEADOS
(3, 5),
-- -- MODULO USUARIOS
(3, 14), (3, 15),
-- -- MODULO NOTAS
(3, 19), (3, 20), (3, 21), (3, 22),
-- ROL RRHH
-- -- MODULO EMPLEADOS
(4, 4), (4, 5), (4, 6), (4, 7), (4, 8),
-- -- MODULO USUARIOS
(4, 14), (4, 15),
-- -- MODULO NOTAS
(4, 19), (4, 20), (4, 21), (4, 22), (4, 23), (4, 24)
;

-- --
-- -- MODULO USUARIOS
-- --
INSERT INTO empresas(nombre) VALUES ('CABAPICE'), ('CABLEFAST'), ('MAFERANA'), ('EFICIENT'), ('WORKPLANNER');
INSERT INTO ciudades(nombre) VALUES ('ILO'), ('MOQUEGUA'), ('TACNA'), ('AREQUIPA'), ('MOLLENDO');
INSERT INTO areas(nombre) VALUES ('CONTABILIDAD'), ('LOGISTICA'), ('MARKETING'), ('TI');
INSERT INTO cargos(nombre, id_area) VALUES ('JEFATURA CONTABILIDAD', 1), ('ANALISTA MARKETING', 3), ('ASISTENTE LOGISTICO', 2), ('ENCARGADO TI', 4), ('ASISTENTE TI', 4), ('SUPERVISOR TI', 4);
INSERT INTO equipos(nombre) VALUES ('TI'), ('DISEÑO'), ('LOGISTICA'), ('CALL CENTER'), ('CONTABILIDAD');
INSERT INTO estados_empleados(nombre) VALUES ('ACTIVO'), ('INACTIVO'), ('SUSPENDIDO');
INSERT INTO empleados
(dni, nombres, apellido_paterno, apellido_materno, celular_personal, id_empresa, id_ciudad, id_area, id_cargo, id_equipo, id_estado_empleado, fecha_creacion)
VALUES
('74621395', 'DANIEL', 'CALCINA', 'FUENTES', '922996705', 2, 4, 4, 4, 1, 1, CURRENT_TIMESTAMP),
('75362422', 'MILTON', 'HACHA', 'VASQUEZ', '930255996', 5, 1, 4, 6, 1, 1, CURRENT_TIMESTAMP),
('72757524', 'BRAYAN', 'VALDEZ', 'QUISPE', '995000427', 5, 1, 4, 5, 1, 1, CURRENT_TIMESTAMP);

INSERT INTO usuarios(username, userpassword, usertoken, id_empleado, fecha_creacion)
VALUES
('daniel', 'daniel', 'daniel', 1, CURRENT_TIMESTAMP),
('milton', 'milton', 'milton', 2, CURRENT_TIMESTAMP),
('brayan', 'brayan', 'brayan', 3, CURRENT_TIMESTAMP);

-- --
-- -- MODULO ROLES POR USUARIOS
-- --
INSERT INTO usuarios_roles(id_usuario, id_rol) VALUES (1, 1), (2, 2), (3, 3);

-- --
-- -- MODULO NOTAS
-- --
INSERT INTO prioridades(nombre) VALUES ('ALTA'), ('MEDIA'), ('BAJA');
INSERT INTO estados_notas(nombre) VALUES ('NUEVA'), ('PENDIENTE'), ('EN PROCESO'), ('FINALIZADO');
INSERT INTO notas(titulo, descripcion, id_usuario_create, id_usuario_asignado, fecha_inicio, id_prioridad, id_estado_nota, fecha_creacion)
VALUES
('Nota de prueba', 'Esta es una nota de prueba', 1, 1, '2022-01-01', 1, 2, CURRENT_TIMESTAMP);

-- -----------------------------------------------------------------
-- -----------------------------------------------------------------
-- --------------------------- VISTAS ------------------------------
-- -----------------------------------------------------------------
-- -----------------------------------------------------------------

-- Vista para obtener los permisos por cada rol del sistema
CREATE VIEW vista_permisos_rol AS
SELECT r.nombre AS rol, p.nombre AS permiso, tp.nombre AS tag_permiso
FROM roles r
INNER JOIN roles_permisos rp ON r.id_rol = rp.id_rol
INNER JOIN permisos p ON rp.id_permiso = p.id_permiso
INNER JOIN tag_permisos tp ON p.id_tag = tp.id_tag ORDER BY r.id_rol, tp.id_tag;

-- Vista para obtener los usuarios por cada rol del sistema
CREATE VIEW vista_usuarios_rol AS
SELECT CONCAT(e.nombres,' ',e.apellido_paterno) AS empleado, u.username, r.nombre AS rol
FROM usuarios u
INNER JOIN usuarios_roles ur ON u.id_usuario = ur.id_usuario
INNER JOIN roles r ON ur.id_rol = r.id_rol
INNER JOIN empleados e ON u.id_empleado = e.id_empleado;

-- Vista para obtener los permisos de un usuario
CREATE VIEW vista_permisos_usuario AS
SELECT CONCAT(e.nombres,' ',e.apellido_paterno) AS empleado, p.nombre AS permiso, tp.nombre AS tag_permiso
FROM empleados e
INNER JOIN usuarios u ON e.id_empleado = u.id_empleado
INNER JOIN usuarios_roles ur ON u.id_usuario = ur.id_usuario
INNER JOIN roles r ON ur.id_rol = r.id_rol
INNER JOIN roles_permisos rp ON r.id_rol = rp.id_rol
INNER JOIN permisos p ON rp.id_permiso = p.id_permiso
INNER JOIN tag_permisos tp ON p.id_tag = tp.id_tag
UNION
SELECT CONCAT(e.nombres,' ',e.apellido_paterno) AS empleado, p.nombre AS permiso, tp.nombre AS tag_permiso
FROM empleados e
INNER JOIN usuarios u ON e.id_empleado = u.id_empleado
INNER JOIN usuarios_permisos up ON u.id_usuario = up.id_usuario
INNER JOIN permisos p ON up.id_permiso = p.id_permiso
INNER JOIN tag_permisos tp ON p.id_tag = tp.id_tag;