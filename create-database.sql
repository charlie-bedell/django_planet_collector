CREATE DATABASE planetcollector;

CREATE USER planet_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE planetcollector TO planet_admin;
