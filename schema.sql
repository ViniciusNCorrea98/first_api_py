USE ...

CREATE TABLE livros(
  id INTEGER NOT NULL auto_increment,
  nome VARCHAR(100),
  lancamento INTEGER NOT NULL,
  PRIMARY KEY (id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

INSERT INTO livros(nome, lancamento) VALUES ('Harry Potter', 2001)
INSERT INTO livros(nome, lancamento) VALUES ('Senhor dos anéis', 2000)
INSERT INTO livros(nome, lancamento) VALUES ('Little & Stich', 2003)
INSERT INTO livros(nome, lancamento) VALUES ('Gente Grande', 2009)
INSERT INTO livros(nome, lancamento) VALUES ('Click', 2006)