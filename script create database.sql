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
    ('admin','admin'),
    ('user','user'),
    ('hien','1');

DROP TABLE IF EXISTS `roomchat`.`message`;

CREATE TABLE `roomchat`.`message` (
  `message_id` INT(11) NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(50) NOT NULL,
  `time` DATETIME NOT NULL,
  `content` VARCHAR(1000) NULL COLLATE 'utf8mb4_unicode_ci',
  PRIMARY KEY (`message_id`),
  FOREIGN KEY (`username`) REFERENCES `user` (`username`))
COLLATE='utf8mb4_unicode_ci'
ENGINE=InnoDB;

INSERT INTO `roomchat`.`message` (`username`,`time`,`content`)
VALUES 
    ('admin', '2022-07-11 05:22:00', 'Hello world'),
    ('hien', '2022-07-11 06:42:42', 'hello mọi ngừi'),
    ('user', '2022-07-11 06:43:12', 'helu cả nhà '),
    ('user', '2022-07-11 06:43:19', 'có ai ở đây không?'),
    ('admin', '2022-07-11 06:44:09', 'có t nhé'),
    ('user', '2022-07-11 06:44:27', 'bye mọi người');