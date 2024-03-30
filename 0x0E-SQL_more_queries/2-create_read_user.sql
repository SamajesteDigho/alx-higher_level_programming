-- Read User
-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user
CREATE USER user_0d_2@localhost IDENTIFIED BY "user_0d_2_pwd";

-- Grant privilege
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
