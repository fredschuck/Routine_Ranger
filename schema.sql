-- CREATE DATABASE
CREATE DATABASE routineranger_db;

-- DROP TABLES 
DROP TABLE IF EXISTS routine;
DROP TABLE IF EXISTS exercise;
DROP TABLE IF EXISTS "user" CASCADE;
DROP TABLE IF EXISTS exercise_attributes;
DROP TABLE IF EXISTS logged_exercises;
DROP TABLE IF EXISTS routine_exercise;
DROP TABLE IF EXISTS bodyweight;


-- CREATE TABLES
CREATE TABLE routine (
    routine_id SERIAL PRIMARY KEY,
    routine_name VARCHAR (80) NOT NULL
);

CREATE TABLE exercise (
    exercise_id SERIAL PRIMARY KEY,
    exercise_name VARCHAR(50) NOT NULL
);

CREATE TABLE exercise_attributes (
    exercise_attributes_id SERIAL PRIMARY KEY,
    exercise_id INTEGER REFERENCES exercise ON DELETE CASCADE,
    sets BOOLEAN NOT NULL,
    reps BOOLEAN NOT NULL,
    weight BOOLEAN NOT NULL,
    height BOOLEAN NOT NULL,
    speed BOOLEAN NOT NULL,
    distance BOOLEAN NOT NULL,
    time BOOLEAN NOT NULL
)

CREATE TABLE logged_exercises (
    log_id SERIAL PRIMARY KEY,
    exercise_id INTEGER REFERENCES exercise ON DELETE CASCADE,
    log_date DATE DEFAULT CURRENT_DATE,
    log_time TIME DEFAULT CURRENT_TIME,
    sets INTEGER,
    reps INTEGER,
    weight INTEGER,
    height INTEGER,
    speed INTEGER,
    distance INTEGER,
    time INTEGER
);

CREATE TABLE routine_exercise (
    routine_exercise_id SERIAL PRIMARY KEY,
    routine_id INTEGER REFERENCES routine ON DELETE CASCADE,
    exercise_id INTEGER REFERENCES exercise ON DELETE CASCADE
);

CREATE TABLE bodyweight (
    id SERIAL PRIMARY KEY,
    weight INTEGER,
    date DATE DEFAULT CURRENT_DATE
);

-- CREATE TABLE "user" (
--     id SERIAL PRIMARY KEY,
--     username VARCHAR (80) UNIQUE NOT NULL,
--     password VARCHAR (100) NOT NULL,
--     email VARCHAR (100) UNIQUE NOT NULL,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );