CREATE DATABASE Proyecto_A;
USE Proyecto_A;

CREATE TABLE Perfil(
    pk_id_perfil INT AUTO_INCREMENT PRIMARY KEY,
    nombre_perfil VARCHAR(30) NOT NULL UNIQUE
);

CREATE TABLE Usuarios(
    pk_id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(100) NOT NULL UNIQUE,
    fk_id_perfil INTEGER NOT NULL
);

CREATE TABLE Terminal(
    pk_id_terminal INT AUTO_INCREMENT PRIMARY KEY,
    nombre_terminal VARCHAR(100) NOT NULL UNIQUE,
    fk_id_usuario INTEGER NOT NULL
);

CREATE TABLE Ruta(
    pk_id_ruta INT AUTO_INCREMENT PRIMARY KEY,
    nombre_ruta VARCHAR(100) NOT NULL UNIQUE,
    fk_id_usuario INTEGER NOT NULL,
    cantidad_pasajeros INTEGER NOT NULL,
    camino VARCHAR(100) NOT NULL
);

CREATE TABLE Camino(
    pk_id_camino INT AUTO_INCREMENT PRIMARY KEY,
    posicion INTEGER NOT NULL,
    fk_id_ruta INTEGER NOT NULL,
    fk_id_terminal INTEGER NOT NULL
);

CREATE TABLE Venta(
    pk_id_venta INT AUTO_INCREMENT PRIMARY KEY,
    fk_id_usuario INTEGER NOT NULL,
    fk_id_terminal_1 INTEGER NOT NULL,
    fk_id_terminal_2 INTEGER NOT NULL,
    fk_id_ruta INTEGER NOT NULL,
    cantidad_pasajeros INTEGER NOT NULL
);

CREATE TABLE Boleto(
    pk_id_boleto INT AUTO_INCREMENT PRIMARY KEY,
    fk_id_venta INTEGER NOT NULL,
    idemtificacion_boleto VARCHAR(100) NOT NULL UNIQUE
);

ALTER TABLE Usuarios
ADD FOREIGN KEY (fk_id_perfil) REFERENCES Perfil(pk_id_perfil);

ALTER TABLE Terminal
ADD FOREIGN KEY (fk_id_usuario) REFERENCES Usuarios(pk_id_usuario);

ALTER TABLE Ruta
ADD FOREIGN KEY (fk_id_usuario) REFERENCES Usuarios(pk_id_usuario);

ALTER TABLE Camino
ADD FOREIGN KEY (fk_id_ruta) REFERENCES Ruta(pk_id_ruta);

ALTER TABLE Camino
ADD FOREIGN KEY (fk_id_terminal) REFERENCES Terminal(pk_id_terminal);

ALTER TABLE Venta
ADD FOREIGN KEY (fk_id_usuario) REFERENCES Usuarios(pk_id_usuario);

ALTER TABLE Venta
ADD FOREIGN KEY (fk_id_terminal_1) REFERENCES Terminal(pk_id_terminal);

ALTER TABLE Venta
ADD FOREIGN KEY (fk_id_terminal_2) REFERENCES Terminal(pk_id_terminal);

ALTER TABLE Venta
ADD FOREIGN KEY (fk_id_ruta) REFERENCES Ruta(pk_id_ruta);

ALTER TABLE Boleto
ADD FOREIGN KEY (fk_id_venta) REFERENCES Venta(pk_id_venta);

INSERT INTO Perfil (nombre_perfil) VALUES ("Administrador");
INSERT INTO Perfil (nombre_perfil) VALUES ("Vendedor");
