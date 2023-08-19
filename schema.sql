CREATE DATABASE workout_db;

-- DROP TABLES 
DROP TABLE IF EXISTS routine;
DROP TABLE IF EXISTS exercise;
DROP TABLE IF EXISTS "user" CASCADE;

-- CREATE TABLES

CREATE TABLE routine (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    user_id INTEGER REFERENCES "user"(id)
);

CREATE TABLE exercise (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    sets INTEGER,
    reps INTEGER,
    weight INTEGER,
    time INTEGER,
    speed INTEGER,
    distance INTEGER,
    routine_id INTEGER REFERENCES routine(id)
);

CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL
);