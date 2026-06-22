-- create_database.sql
-- Creates the project database and an example users table

CREATE DATABASE IF NOT EXISTS nome_do_projeto;
USE nome_do_projeto;

CREATE TABLE IF NOT EXISTS users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
