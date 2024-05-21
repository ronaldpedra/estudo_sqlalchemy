CREATE DATABASE IF NOT EXISTS cinema;

USE cinema;

CREATE TABLE IF NOT EXISTS filmes (
    titulo VARCHAR(50) NOT NULL,
    genero VARCHAR(50) NOT NULL,
    ano INT NOT NULL,
    PRIMARY KEY(titulo)
    );

INSERT INTO filmes (titulo, genero, ano)
VALUES ("Forest Gump", "Drama", 1994);