CREATE TABLE Product(
    PCode CHAR(3) PRIMARY KEY,
    PName VARCHAR(20),
    UPrice FLOAT,
    Manufacturer VARCHAR(20)
);

INSERT INTO Product VALUES(P01, "Washing Powder", 120, "Surf");
INSERT INTO Product VALUES(P02, "Toothpaste", 54, "Colgate");
INSERT INTO Product VALUES(P03, "Soap", 25, "Lux");
INSERT INTO Product VALUES(P04, "Toothpaste", 65, "Pepsodent");
INSERT INTO Product VALUES(P05, "Soap", 38, "Dove");
INSERT INTO Product VALUES(P06, "Shampoo", 245, "Dove");

SELECT PCode, PName, UPrice FROM Product ORDER BY PName DESC, UPrice ASC;

ALTER TABLE Product ADD Discount FLOAT;

