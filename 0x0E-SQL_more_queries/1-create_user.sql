-- Create server user
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';

-- Grant privileges
GRANT ALL TO user_0d_1@localhost;
