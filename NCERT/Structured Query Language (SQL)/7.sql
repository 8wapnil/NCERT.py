CREATE TABLE Product(
    PCode CHAR(5) PRIMARY KEY,
    PName VARCHAR(20),
    UPrice FLOAT,
    Manufacturer VARCHAR(20)
);

INSERT INTO Product VALUES("P01", "Washing Powder", 120, "Surf");
INSERT INTO Product VALUES("P02", "Toothpaste", 54, "Colgate");
INSERT INTO Product VALUES("P03", "Soap", 25, "Lux");
INSERT INTO Product VALUES("P04", "Toothpaste", 65, "Pepsodent");
INSERT INTO Product VALUES("P05", "Soap", 38, "Dove");
INSERT INTO Product VALUES("P06", "Shampoo", 245, "Dove");

SELECT PCode, PName, UPrice FROM Product ORDER BY PName DESC, UPrice ASC;

ALTER TABLE Product ADD Discount FLOAT;

UPDATE Product SET Discount = 0.1*UPrice WHERE UPrice > 100;
UPDATE Product SET Discount = 0 WHERE UPrice < 100;

UPDATE Product SET UPrice = 1.12*UPrice WHERE Manufacturer = "Dove";

SELECT COUNT(Manufacturer) AS Total_Products, Manufacturer FROM Product GROUP BY Manufacturer;