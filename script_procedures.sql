USE passaros;

DROP PROCEDURE IF EXISTS adiciona_cidade;
DELIMITER //
CREATE PROCEDURE adiciona_cidade(IN nova_cidade VARCHAR(50))
BEGIN
    INSERT INTO cidade (nome_cidade) VALUES (nova_cidade);
END//
DELIMITER ;

DROP PROCEDURE IF EXISTS adiciona_usuario;
DELIMITER //
CREATE PROCEDURE adiciona_usuario(IN primeiro_nome VARCHAR(20), ultimo_nome VARCHAR(20), email VARCHAR(50), id_cidade INT)
BEGIN
	INSERT INTO usuario (primeiro_nome, ultimo_nome, email, id_cidade) VALUES (primeiro_nome, ultimo_nome, email, id_cidade);
END//
DELIMITER ;

DROP PROCEDURE IF EXISTS adiciona_passaro;
DELIMITER //
CREATE PROCEDURE adiciona_passaro(IN novo_passaro VARCHAR(20))
BEGIN
	INSERT INTO passaro (especie) VALUES (novo_passaro);
END//
DELIMITER ;

DROP PROCEDURE IF EXISTS adiciona_preferencia;
DELIMITER //
CREATE PROCEDURE adiciona_preferencia(IN id_usuario INT, IN id_passaro INT)
BEGIN
	INSERT INTO preferencia_passaro (id_usuario, id_passaro) VALUES (id_usuario, id_passaro);
END//
DELIMITER ;

DROP PROCEDURE IF EXISTS adiciona_post;
DELIMITER //
CREATE PROCEDURE adiciona_post(IN id_usuario INT, IN titulo VARCHAR(100),IN texto VARCHAR(300),IN url_foto VARCHAR(300))
BEGIN
	INSERT INTO post (id_usuario, titulo, texto, url_foto) VALUES (id_usuario, titulo, texto, url_foto);
END//
DELIMITER ;
