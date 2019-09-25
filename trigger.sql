DELIMITER //
CREATE TRIGGER apaga_comentario
AFTER UPDATE
   ON post FOR EACH ROW

BEGIN
	IF NEW.ativa = False THEN
		#update na tabela de menções de usuarios
		UPDATE menciona
		SET ativa = False 
		WHERE id_post = post.id_post;
		
		#update na tabela de referências de pássaros
		UPDATE referencia
		SET ativa = False
		WHERE id_post = post.id_post;
	END IF;

END; //
DELIMITER ;