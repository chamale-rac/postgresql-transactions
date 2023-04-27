-- Samuel Chamalé | 4444@schr.tech
-- 2023-04-27

-- Tables creation

CREATE TABLE product
(
    manufacturer VARCHAR(255),
    model        VARCHAR(255),
    type         VARCHAR(255),
    PRIMARY KEY (model)
);

CREATE TABLE pc
(
    model VARCHAR(255) REFERENCES product (model) ON DELETE CASCADE,
    speed FLOAT,
    ram   FLOAT,
    disk  FLOAT,
    price FLOAT,
    PRIMARY KEY (model)
);

-- Test data

INSERT INTO product (manufacturer, model, type)
VALUES ('Dell', 'XPS13', 'PC'),
       ('Lenovo', 'ThinkPad', 'PC'),
       ('Apple', 'MacBook Pro', 'PC'),
       ('HP', 'Pavilion', 'PC'),
       ('Acer', 'Aspire', 'PC'),
       ('Dell', 'XPS Tower', 'PC'),
       ('HP', 'Envy', 'PC');

INSERT INTO pc (model, speed, ram, disk, price)
VALUES ('XPS13', 2.5, 8, 256, 1200.00),
       ('ThinkPad', 2.6, 16, 512, 1500.00),
       ('MacBook Pro', 2.8, 16, 512, 1800.00),
       ('Pavilion', 2.4, 12, 512, 800.00),
       ('Aspire', 3.0, 8, 1000, 700.00),
       ('XPS Tower', 3.2, 32, 2000, 2000.00),
       ('Envy', 3.0, 16, 512, 1000.00);
