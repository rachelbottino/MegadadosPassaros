DROP TRIGGER IF EXISTS apaga_comentario;
DELIMITER //
CREATE TRIGGER apaga_comentario
AFTER UPDATE
   ON post FOR EACH ROW

BEGIN
	IF NEW.ativo = 0 THEN
		SET @id_post = NEW.id_post;        
        UPDATE menciona SET ativo = 0 WHERE menciona.id_post = @id_post;
        UPDATE referencia SET ativo = 0 WHERE referencia.id_post = @id_post;
	END IF;
END; //
DELIMITER ;