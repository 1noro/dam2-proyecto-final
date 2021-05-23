DELIMITER $$
  DROP PROCEDURE IF EXISTS insert_post;$$
  CREATE PROCEDURE insert_post(
    IN new_author VARCHAR(50),
    IN new_comment VARCHAR(512),
    IN new_fileurl VARCHAR(512),
    IN new_thread BIGINT
  ) BEGIN
    SET @last_id = 0;
    SELECT id INTO @last_id FROM POST
      ORDER BY id DESC LIMIT 1;
    IF (@last_id IS NULL) THEN
      SET @last_id = 0;
    END IF;
    INSERT
      INTO POST (id, author, comment, fileurl, thread)
      VALUES (@last_id + 1, new_author, new_comment, new_fileurl, new_thread);
  END;$$
DELIMITER ;
