-- Create database and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
    id int PRIMARY KEY AUTO_INCREMENT NOT NULL,
    state_id int,
    name VARCHAR(256)
);

ALTER TABLE cities
ADD CONSTRAINT fk_cities_states
FOREIGN KEY (state_id)
REFERENCES states(id);
