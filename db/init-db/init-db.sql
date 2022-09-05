CREATE TABLE IF NOT EXISTS modelo_persona
(
    id_documento BIGINT NOT NULL,
    tipo_de_documento VARCHAR(30),
    nombres VARCHAR(30),
    apellidos VARCHAR(30),
    hobbie VARCHAR(30),
    PRIMARY KEY(id_documento)
);