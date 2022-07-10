DROP DATABASE `roomchat`;

CREATE DATABASE `roomchat`;

DROP TABLE IF EXISTS `roomchat`.`user`;

CREATE TABLE `roomchat`.`user` (
  `username` VARCHAR(50) NOT NULL,
  `password` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`username`))
COLLATE='utf8mb4_unicode_ci'
ENGINE=InnoDB;

INSERT INTO `roomchat`.`user` (`username`,`password`)
VALUES 
    ('admin','admin');

DROP TABLE IF EXISTS `roomchat`.`message`;

CREATE TABLE `roomchat`.`message` (
  `message_id` INT(11) NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(50) NOT NULL,
  `time` DATETIME NOT NULL,
  `content` VARCHAR(1000) NULL COLLATE 'utf8mb4_unicode_ci',
  PRIMARY KEY (`message_id`))
COLLATE='utf8mb4_unicode_ci'
ENGINE=InnoDB;

INSERT INTO `roomchat`.`message` (`username`,`time`,`content`)
VALUES 
    ('admin','2022-7-11 05:22:00','Hello world');