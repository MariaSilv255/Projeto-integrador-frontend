1. O banco de dados desse projeto é feito localmente no próprio celular, utilizando o sistema de banco de dados relacional SQLite. 

2. O SQLite é um sistema de banco de dados relacional leve e open-source, que é ideal para aplicativos móveis.

3. O baco de dados possui a segunte estrutura:

CREATE TABLE usuario(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
nome_usuario VARCHAR(30) UNIQUE NOT NULL,
senha VARCHAR(30) NOT NULL);

CREATE TABLE dados_usuario(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
email VARCHAR(50) NOT NULL,
fk_IdUsuario INTEGER NOT NULL,
FOREIGN KEY (fk_IdUsuario) REFERENCES usuario (ID)
    ON DELETE CASCADE
    ON UPDATE NO ACTION);
    
CREATE TABLE broker(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
login VARCHAR(50) NOT NULL,
certificadoCliente TEXT NOT NULL,
username VARCHAR(50) NOT NULL,
chaveUsuario TEXT NOT NULL,
host VARCHAR(100) NOT NULL);

CREATE TABLE cad_irrigacao(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
descricao VARCHAR(200) NOT NULL,
fk_IdUsuario INTEGER NOT NULL,
fk_IdBroker INTEGER NOT NULL,
FOREIGN KEY (fk_IdUsuario) REFERENCES usuario (ID)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
FOREIGN KEY (fk_IdBroker) REFERENCES broker (ID)
    ON DELETE CASCADE
    ON UPDATE NO ACTION);