CREATE TABLE users (
    id serial PRIMARY KEY,
    email VARCHAR,
    first_name VARCHAR,
    last_name VARCHAR,
    password VARCHAR
);

CREATE TABLE components (
    id serial PRIMARY KEY,
    name VARCHAR,
    brand VARCHAR,
    series VARCHAR,
    price FLOAT
);

CREATE TABLE orders (
    id serial PRIMARY KEY,
    user_id INTEGER,
    order_date TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE order_items (
    id serial PRIMARY KEY,
    order_id INTEGER,
    component_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (order_id) REFERENCES orders (id),
    FOREIGN KEY (component_id) REFERENCES components (id)
);

CREATE TABLE cpus (
    id serial PRIMARY KEY,
    architecture VARCHAR,
    cores INTEGER,
    clock_speed FLOAT,
    FOREIGN KEY (id) REFERENCES components (id)
);

CREATE TABLE gpus (
    id serial PRIMARY KEY,
    memory_capacity INTEGER,
    memory_type VARCHAR,
    clock_speed FLOAT,
    FOREIGN KEY (id) REFERENCES components (id)
);

CREATE TABLE memories (
    id serial PRIMARY KEY,
    capacity INTEGER,
    type VARCHAR,
    clock_speed VARCHAR,
    FOREIGN KEY (id) REFERENCES components (id)
);

CREATE TABLE ssds (
    id serial PRIMARY KEY,
    capacity FLOAT,
    FOREIGN KEY (id) REFERENCES components (id)
);

CREATE TABLE mother_boards (
    id serial PRIMARY KEY,
    processor_socket VARCHAR,
    memory_type VARCHAR,
    FOREIGN KEY (id) REFERENCES components (id)
);

INSERT INTO users (email, first_name, last_name, password)
VALUES ('user1@example.com', 'John', 'Doe', 'password1');

INSERT INTO users (email, first_name, last_name, password)
VALUES ('user2@example.com', 'Jane', 'Smith', 'password2');

INSERT INTO components (name, brand, series, price)
VALUES ('Intel Core i5 13600KF 3.5GHz', 'Intel', 'Core i5', 1559.99);
INSERT INTO cpus (architecture, cores, clock_speed)
VALUES ('Raptor Lake', 14, 3.5);

INSERT INTO components (name, brand, series, price)
VALUES ('AMD Ryzen 7 7800X3D 4.2GHz', 'AMD', 'Ryzen 7', 1969.99);
INSERT INTO cpus (architecture, cores, clock_speed)
VALUES ('Raphael', 8, 4.2);

INSERT INTO components (name, brand, series, price)
VALUES ('Intel Core i7 14700K 3.4GHz', 'Intel', 'Core i7', 2309.99);
INSERT INTO cpus (architecture, cores, clock_speed)
VALUES ('Raptor Lake Refresh', 20, 3.4);

INSERT INTO components (name, brand, series, price)
VALUES ('NVIDIA GeForce RTX 3060', 'Nvidia', 'GeForce RTX 3000', 1969.99);
INSERT INTO gpus (memory_capacity, memory_type, clock_speed)
VALUES (12, 'GDDR6', 1.32);

INSERT INTO components (name, brand, series, price)
VALUES ('NVIDIA GeForce RTX 4070', 'Nvidia', 'GeForce RTX 400', 3339.99);
INSERT INTO gpus (memory_capacity, memory_type, clock_speed)
VALUES (12, 'GDDR6X', 2.48);

INSERT INTO components (name, brand, series, price)
VALUES ('Kingston FURY Beast 16GB DDR4', 'Kingston', 'FURY Beast', 199.99);
INSERT INTO memories (capacity, type, clock_speed)
VALUES (16, 'DDR4', 3.2);

INSERT INTO components (name, brand, series, price)
VALUES ('Corsair Vengeance LPX Black 32GB DDR4', 'Corsair', 'Vengeance LPX', 199.99);
INSERT INTO memories (capacity, type, clock_speed)
VALUES (32, 'DDR4', 3.2);
