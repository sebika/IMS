-- CREATE TABLE orders (
--     id serial PRIMARY KEY,
--     user_id INTEGER,
--     order_date TIMESTAMP,
--     FOREIGN KEY (user_id) REFERENCES auth_user (id)
-- );

-- CREATE TABLE order_items (
--     id serial PRIMARY KEY,
--     order_id INTEGER,
--     component_id INTEGER,
--     quantity INTEGER,
--     FOREIGN KEY (order_id) REFERENCES orders (id),
--     FOREIGN KEY (component_id) REFERENCES components (id)
-- );

-- CREATE TABLE memories (
--     id serial PRIMARY KEY,
--     capacity INTEGER,
--     type VARCHAR,
--     clock_speed VARCHAR,
--     FOREIGN KEY (id) REFERENCES components (id)
-- );

-- CREATE TABLE ssds (
--     id serial PRIMARY KEY,
--     capacity FLOAT,
--     FOREIGN KEY (id) REFERENCES components (id)
-- );

-- CREATE TABLE mother_boards (
--     id serial PRIMARY KEY,
--     processor_socket VARCHAR,
--     memory_type VARCHAR,
--     FOREIGN KEY (id) REFERENCES components (id)
-- );

-- INSERT INTO components (name, brand, series, price)
-- VALUES ('NVIDIA GeForce RTX 4070', 'Nvidia', 'GeForce RTX 400', 3339.99);
-- INSERT INTO gpus (memory_capacity, memory_type, clock_speed)
-- VALUES (12, 'GDDR6X', 2.48);

-- INSERT INTO components (name, brand, series, price)
-- VALUES ('Kingston FURY Beast 16GB DDR4', 'Kingston', 'FURY Beast', 199.99);
-- INSERT INTO memories (capacity, type, clock_speed)
-- VALUES (16, 'DDR4', 3.2);

-- INSERT INTO components (name, brand, series, price)
-- VALUES ('Corsair Vengeance LPX Black 32GB DDR4', 'Corsair', 'Vengeance LPX', 199.99);
-- INSERT INTO memories (capacity, type, clock_speed)
-- VALUES (32, 'DDR4', 3.2);


-- INSERT INTO public.computer_parts_store_component(
-- 	name, brand, series, price, category)
-- 	VALUES ( 'Intel Core i5 13600KF 3.5GHz', 'Intel', 'Core i5', 1559.99, 'cpu' );
-- INSERT INTO public.computer_parts_store_cpu(
-- 	architecture, cores, clock_speed, component_fk_id)
-- 	VALUES ( 'Raptor Lake', 14, 3.5, (SELECT id from public.computer_parts_store_component WHERE name='Intel Core i5 13600KF 3.5GHz') );

-- INSERT INTO public.computer_parts_store_component(
-- 	name, brand, series, price, category)
-- 	VALUES ( 'AMD Ryzen 7 7800X3D 4.2GHz', 'AMD', 'Ryzen 7', 1969.99, 'cpu' );
-- INSERT INTO public.computer_parts_store_cpu(
-- 	architecture, cores, clock_speed, component_fk_id)
-- 	VALUES ( 'Raphael', 8, 4.2, (SELECT id from public.computer_parts_store_component WHERE name='AMD Ryzen 7 7800X3D 4.2GHz') );

-- INSERT INTO public.computer_parts_store_component(
-- 	name, brand, series, price, category)
-- 	VALUES ( 'Intel Core i7 14700K 3.4GHz', 'Intel', 'Core i7', 2309.99, 'cpu' );
-- INSERT INTO public.computer_parts_store_cpu(
-- 	architecture, cores, clock_speed, component_fk_id)
-- 	VALUES ( 'Raptor Lake Refresh', 20, 3.4, (SELECT id from public.computer_parts_store_component WHERE name='Intel Core i7 14700K 3.4GHz') );

-- INSERT INTO public.computer_parts_store_component(
-- 	name, brand, series, price, category)
-- 	VALUES ( 'NVIDIA GeForce RTX 3060', 'Nvidia', 'GeForce RTX 3000', 1969.99, 'gpu' );
-- INSERT INTO public.computer_parts_store_gpu(
-- 	memory_capacity, memory_type, clock_speed, component_fk_id)
-- 	VALUES ( 12, 'GDDR6', 1.32, (SELECT id from public.computer_parts_store_component WHERE name='NVIDIA GeForce RTX 3060') );

-- INSERT INTO public.computer_parts_store_component(
-- 	name, brand, series, price, category)
-- 	VALUES ( 'NVIDIA GeForce RTX 4070', 'Nvidia', 'GeForce RTX 400', 3339.99, 'gpu' );
-- INSERT INTO public.computer_parts_store_gpu(
-- 	memory_capacity, memory_type, clock_speed, component_fk_id)
-- 	VALUES ( 12, 'GDDR6X', 2.48, (SELECT id from public.computer_parts_store_component WHERE name='NVIDIA GeForce RTX 4070') );



-- SELECT *
-- 	FROM public.computer_parts_store_component comp
-- 	JOIN public.computer_parts_store_cpu cpu ON comp.id = cpu.component_fk_id;