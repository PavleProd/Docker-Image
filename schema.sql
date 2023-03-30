DROP DATABASE IF EXISTS `wgdb`;
CREATE DATABASE `wgdb`;
USE `wgdb`;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
    `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `surname` VARCHAR(255) NOT NULL,
    `nationality` VARCHAR(255) NOT NULL
);

INSERT INTO `users` (name, surname, nationality)
VALUES ('Pavle', 'Prodanovic', 'Serbia'), ('Lev', 'Tolstoy', 'Russia'), ('Anastasija', 'Kotlaja', 'Montenegro');
