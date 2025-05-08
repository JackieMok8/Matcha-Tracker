CREATE DATABASE matcha_tracker;
USE matcha_tracker;

CREATE TABLE cafes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100),
    address VARCHAR(255),
    visiting_date DATE,
    order_taken TEXT,
    price DECIMAL,
    rating DECIMAL(3,1),
    notes TEXT
);
