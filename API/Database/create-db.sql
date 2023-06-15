-- Active: 1686747766310@@127.0.0.1@3306
CREATE DATABASE api_file
    DEFAULT CHARACTER SET = 'utf8mb4';

USE api_file;
SELECT * FROM user;
SELECT * FROM files;
DROP TABLE user;
DROP TABLE files;
CREATE Table user(
    id_user int PRIMARY KEY AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    email varchar(100) NOT NULL UNIQUE,
    password varchar(200) NOT NULL,
    datebirth DATE not null
);
CREATE TABLE files (
    id_file INT PRIMARY KEY AUTO_INCREMENT,
    name_file VARCHAR(100) NOT NULL,
    id_user INT NOT NULL,
    FOREIGN KEY (id_user) REFERENCES api_file.user (id_user),
    status int NOT NULL
);