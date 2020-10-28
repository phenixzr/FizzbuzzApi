CREATE DATABASE fizzbuzz;
CREATE TABLE fizzbuzz ( id SERIAL PRIMARY KEY, int1 integer, int2 integer, mlimit integer, str1 varchar, str2 varchar );

GRANT INSERT ON fizzbuzz TO fzapiuser ;
GRANT SELECT ON fizzbuzz TO fzapiuser ;
GRANT UPDATE ON fizzbuzz_id_seq TO fzapiuser ;