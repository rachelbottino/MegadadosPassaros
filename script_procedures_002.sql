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
CREATE PROCEDURE adiciona_usuario(IN primeiro_nome VARCHAR(20), IN ultimo_nome VARCHAR(20), IN email VARCHAR(50), IN username varchar(100), IN id_cidade INT)
BEGIN
	INSERT INTO usuario (primeiro_nome, ultimo_nome, email, username, id_cidade) VALUES (primeiro_nome, ultimo_nome, email, username, id_cidade);
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

DROP PROCEDURE IF EXISTS adiciona_mencao;
DELIMITER //
CREATE PROCEDURE adiciona_mencao(IN id_post INT, IN id_usuario INT)
BEGIN
	INSERT INTO menciona (id_post, id_usuario) VALUES (id_post, id_usuario);
END//
DELIMITER ;

DROP PROCEDURE IF EXISTS adiciona_referencia;
DELIMITER //
CREATE PROCEDURE adiciona_referencia(IN id_post INT, IN id_passaro INT)
BEGIN
	INSERT INTO referencia (id_post, id_passaro) VALUES (id_post, id_passaro);
END//
DELIMITER ;

DROP PROCEDURE IF EXISTS adiciona_joinha;
DELIMITER //
CREATE PROCEDURE adiciona_joinha(IN id_post INT, IN id_usuario INT, IN reacao BOOLEAN)
BEGIN
	INSERT INTO joinha(id_post, id_usuario, reacao) VALUES (id_post, id_usuario, reacao);
END//
DELIMITER ;

DROP PROCEDURE IF EXISTS adiciona_segue;
DELIMITER //
CREATE PROCEDURE adiciona_segue(IN id_usuario INT, IN id_usuario_seguido INT)
BEGIN
	INSERT INTO segue (id_usuario, id_usuario_seguido) VALUES (id_usuario, id_usuario_seguido);
END//
DELIMITER ;

DROP PROCEDURE IF EXISTS adiciona_visualizacao;
DELIMITER //
CREATE PROCEDURE adiciona_visualizacao(IN id_post INT, IN id_usuario INT, IN aparelho VARCHAR(50), IN browser varchar(50), IN ip VARCHAR(20), IN instante datetime)
BEGIN
	INSERT INTO visualizou (id_post, id_usuario, aparelho, browser, ip, instante) VALUES (id_post, id_usuario, aparelho, browser, ip, instante);
END//
DELIMITER ;
