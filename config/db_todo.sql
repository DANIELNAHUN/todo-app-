USE todo_app_plus;

--
-- MODULO USUARIOS
--
CREATE TABLE empresas(
  id_empresa INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  PRIMARY KEY (id_empresa)
);

CREATE TABLE ciudades(
  id_ciudad INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  PRIMARY KEY (id_ciudad)
);

CREATE TABLE empresas_ciudades(
  id_empresa_ciudad INT NOT NULL AUTO_INCREMENT,
  id_empresa INT NOT NULL,
  id_ciudad INT NOT NULL,
  PRIMARY KEY (id_empresa_ciudad)
);

ALTER TABLE empresas_ciudades ADD FOREIGN KEY (id_empresa) REFERENCES empresas(id_empresa);
ALTER TABLE empresas_ciudades ADD FOREIGN KEY (id_ciudad) REFERENCES ciudades(id_ciudad);

CREATE TABLE areas(
  id_area INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  PRIMARY KEY (id_area)
);

CREATE TABLE cargo(
  id_cargo INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  PRIMARY KEY (id_cargo)
);

CREATE TABLE estado_usuario(
  id_estado_usuario INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  PRIMARY KEY (id_estado_usuario)
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
  usuario VARCHAR(50) DEFAULT NULL,
  password TEXT DEFAULT NULL,
  token TEXT DEFAULT NULL,
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

--
-- MODULO NOTAS
--

CREATE TABLE estado_nota(
  id_estado_nota INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  PRIMARY KEY (id_estado_nota)
);

CREATE TABLE prioridad(
  id_prioridad INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  PRIMARY KEY (id_prioridad)
);
CREATE TABLE notas(
  id_nota INT NOT NULL AUTO_INCREMENT,
  titulo VARCHAR(50) NOT NULL,
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

--
-- DATOS DE PRUEBA
--

INSERT INTO empresas(nombre) VALUES ('CABAPICE'), ('CABLEFAST'), ('MAFERANA'), ('EFICIENT'), ('WORKPLANNER');
INSERT INTO ciudades(nombre) VALUES ('ILO'), ('MOQUEGUA'), ('TACNA'), ('AREQUIPA'), ('MOLLENDO');
INSERT INTO areas(nombre) VALUES ('CONTABILIDAD'), ('LOGISTICA'), ('MARKETING'), ('TI');
INSERT INTO cargo(nombre) VALUES ('JEFATURA CONTABILIDAD'), ('ANALISTA MARKETING'), ('ASISTENTE LOGISTICO'), ('ENCARGADO TI'), ('ASISTENTE TI');
INSERT INTO estado_usuario(nombre) VALUES ('ACTIVO'), ('INACTIVO'), ('SUSPENDIDO');
INSERT INTO prioridad(nombre) VALUES ('ALTA'), ('MEDIA'), ('BAJA');
INSERT INTO estado_nota(nombre) VALUES ('NUEVA'), ('PENDIENTE'), ('EN PROCESO'), ('FINALIZADO');
INSERT INTO usuarios
(dni, nombres, apellido_paterno, apellido_materno, celular_personal, id_empresa, id_ciudad, id_area, id_cargo, id_estado_usuario, fecha_creacion)
VALUES
('74621395', 'DANIEL', 'CALCINA', 'FUENTES', '922996705', 2, 4, 4, 4, 1, CURRENT_TIMESTAMP),
('75233654', 'MILTON', 'HACHA', 'VASQUEZ', '922996706', 2, 4, 4, 5, 1, CURRENT_TIMESTAMP);