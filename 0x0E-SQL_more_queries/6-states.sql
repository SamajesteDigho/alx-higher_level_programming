-- Create database hbtn_0d_usa and table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id int AUTO INCREMENT UNIQUE NOT NULL PRIMARY,
    name VARCHAR(256) NOT NULL
);
