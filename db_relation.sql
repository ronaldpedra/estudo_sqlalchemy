CREATE DATABASE IF NOT EXISTS cinema;

CREATE TABLE IF NOT EXISTS filmes (
    titulo VARCHAR(50) NOT NULL,
    genero VARCHAR(50) NOT NULL,
    ano INT NOT NULL,
    PRIMARY KEY(titulo)
    );

CREATE TABLE IF NOT EXISTS atores (
    id BIGINT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    titulo_filme VARCHAR(50) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (titulo_filme) REFERENCES filmes(titulo)
    );

INSERT INTO filmes (titulo, genero, ano)
VALUES ("Forest Gump", "Drama", 1994);

INSERT INTO atores (nome, titulo_filme)
VALUES ("Tom Hanks", "Forest Gump");