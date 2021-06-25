DROP DATABASE templatedatabase;
CREATE DATABASE templatedatabase;
USE templatedatabase;
CREATE TABLE test_table (
    id INT NOT NULL AUTO_INCREMENT,
    test_int INT,
    CONSTRAINT id_pk PRIMARY KEY (id)
); 