DROP DATABASE IF EXISTS passaros;
CREATE DATABASE passaros;
USE passaros;

CREATE TABLE cidade (
	id_cidade INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome_cidade VARCHAR(50) UNIQUE
);

CREATE TABLE usuario (
	id_usuario INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    primeiro_nome VARCHAR(20) NOT NULL,
    ultimo_nome VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    username VARCHAR(50) NOT NULL UNIQUE,
    id_cidade INT NOT NULL,
    FOREIGN KEY (id_cidade) REFERENCES cidade (id_cidade)
);

CREATE TABLE passaro (
	id_passaro INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    especie VARCHAR(100) UNIQUE
);

CREATE TABLE preferencia_passaro (
	id_usuario INT NOT NULL,
    id_passaro INT NOT NULL,
    PRIMARY KEY (id_usuario, id_passaro),
    FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario),
    FOREIGN KEY (id_passaro) REFERENCES passaro (id_passaro)
);

CREATE TABLE post (
	id_post INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    texto VARCHAR(300),
    url_foto VARCHAR(300),
    ativo BOOLEAN DEFAULT 1,
    FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario)
);

CREATE TABLE visualizou (
	id_view INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_post INT NOT NULL,
    id_usuario INT NOT NULL,
    aparelho VARCHAR(50),
    browser VARCHAR(50),
    ip VARCHAR(20) NOT NULL,
    instante DATETIME NOT NULL,
    FOREIGN KEY (id_post) REFERENCES post (id_post),
    FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario)
);

CREATE TABLE menciona (
	id_post INT NOT NULL,
    id_usuario INT NOT NULL,
    ativo BOOLEAN DEFAULT 1, 
    PRIMARY KEY (id_post, id_usuario),
    FOREIGN KEY (id_post) REFERENCES post (id_post),
    FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario)
);

CREATE TABLE referencia (
	id_post INT NOT NULL,
    id_passaro INT NOT NULL,
    ativo BOOLEAN DEFAULT 1,
    PRIMARY KEY (id_post, id_passaro),
    FOREIGN KEY (id_post) REFERENCES post (id_post),
    FOREIGN KEY (id_passaro) REFERENCES passaro (id_passaro)
);

CREATE TABLE joinha (
	id_post INT NOT NULL,
    id_usuario INT NOT NULL,
    reacao BOOLEAN,
    ativo BOOLEAN DEFAULT 1,
    PRIMARY KEY (id_post, id_passaro),
    FOREIGN KEY (id_post) REFERENCES post (id_post),
    FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario)
);

CREATE TABLE segue (
	id_usuario INT NOT NULL,
    id_usuario_seguido INT NOT NULL,
    ativo BOOLEAN DEFAULT 1,
    PRIMARY KEY (id_usuario, id_usuario_seguido),
    FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario),
    FOREIGN KEY (id_usuario_seguido) REFERENCES usuario (id_usuario)
);
    
