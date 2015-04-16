DROP DATABASE IF EXISTS judith;
CREATE DATABASE judith;
USE judith;

GRANT ALL PRIVILEGES ON judith.*  TO 'judith'@'%' IDENTIFIED BY 'judith';

CREATE TABLE viki (
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(50),
    text VARCHAR(255),
    PRIMARY KEY(id)
)ENGINE=InnoDB;

CREATE TABLE tak (
    name VARCHAR(255) NOT NULL,
    viki_id INTEGER NOT NULL,
    PRIMARY KEY(name, viki_id),
    FOREIGN KEY(viki_id) REFERENCES viki (id)
)ENGINE=InnoDB;