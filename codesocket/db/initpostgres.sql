CREATE TABLE ciudades (
  ciud_id SERIAL PRIMARY KEY,
  ciud_nombre VARCHAR(255) NOT NULL
);

CREATE TABLE personas (
  dir_person SERIAL PRIMARY KEY,
  dir_tipo_tel VARCHAR(50),
  dir_nombre VARCHAR(255) NOT NULL,
  dir_tel VARCHAR(255),
  dir_ciud_id INT,
  FOREIGN KEY (dir_ciud_id) REFERENCES ciudades (ciud_id)
);

INSERT INTO ciudades (ciud_nombre) VALUES ('Ibague');
INSERT INTO ciudades (ciud_nombre) VALUES ('Cucuta');
INSERT INTO ciudades (ciud_nombre) VALUES ('Neiva');
INSERT INTO ciudades (ciud_nombre) VALUES ('Pasto');
INSERT INTO ciudades (ciud_nombre) VALUES ('Leticia');

INSERT INTO personas (dir_tipo_tel, dir_nombre, dir_tel, dir_ciud_id) VALUES ('Movil','Camilo Cantante', '+321xxxxxxx', 5);
INSERT INTO personas (dir_tipo_tel, dir_nombre, dir_tel, dir_ciud_id) VALUES ('Movil','Bonifacio Elegante', '+322xxxxxxx', 1);
INSERT INTO personas (dir_tipo_tel, dir_nombre, dir_tel, dir_ciud_id) VALUES ('Fijo','Beneplecito Rodante', '+344xxxxxxx', 4);
INSERT INTO personas (dir_tipo_tel, dir_nombre, dir_tel, dir_ciud_id) VALUES ('Fijo','Avaro Consecuente', '+323xxxxxxx', 5);
INSERT INTO personas (dir_tipo_tel, dir_nombre, dir_tel, dir_ciud_id) VALUES ('Movil','Gloriana Avanzada', '+602xxxxxxx', 4);
