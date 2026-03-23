SELECT * FROM MOVIE;
SELECT MovieID, MovieName, (ProductionCost + BusinessCost) AS Total_Earning FROM MOVIE;
SELECT DISTINCT Category from MOVIE;
SELECT MovieID, MovieName, (BusinessCost - ProductionCost) AS NetProfit FROM MOVIE;
SELECT MovieID, MovieName, (BusinessCost - ProductionCost) AS Cost FROM MOVIE WHERE ProductionCost BETWEEN 10000 AND 100000;
SELECT * FROM MOVIE WHERE Category IN ('Action', 'Comedy');
SELECT * FROM MOVIE WHERE ReleaseDate IS NULL;