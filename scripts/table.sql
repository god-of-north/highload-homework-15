CREATE TABLE IF NOT EXISTS users (
    user_id BIGINT AUTO_INCREMENT PRIMARY KEY,

    birth_day DATE,

    registration_date DATE,
    user_login VARCHAR(255) NOT NULL,
    user_email VARCHAR(255) NOT NULL,
    firstname VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    patronymic VARCHAR(255) NOT NULL,
    sex VARCHAR(32),
    job_position VARCHAR(255) NOT NULL,
    description TEXT

)  ENGINE=InnoDB;

CREATE INDEX btree_index USING BTREE ON users (birth_day);
CREATE INDEX hash_index USING HASH ON users (birth_day);

OPTIMIZE TABLE users;
