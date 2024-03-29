CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 3663655b752a

CREATE TABLE `NYC` (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    year INTEGER NOT NULL, 
    leading_cause VARCHAR(100) NOT NULL, 
    sex VARCHAR(10) NOT NULL, 
    race_ethnicity VARCHAR(50), 
    deaths INTEGER NOT NULL, 
    death_rate INTEGER NOT NULL, 
    age_adjusted_death_rate INTEGER NOT NULL, 
    PRIMARY KEY (id)
);

DROP TABLE nyc;

INSERT INTO alembic_version (version_num) VALUES ('3663655b752a');

