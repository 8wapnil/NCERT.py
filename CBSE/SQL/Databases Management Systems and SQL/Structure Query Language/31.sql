SELECT Students.Adno, Students.Name, Students.Sex, Students.Average, Streams.Sname, Streams.Place
FROM Students JOIN Streams ON Scode;

INSERT INTO Students 
VALUES(999, "Deepak Sharma", 83, "M", 2222);

SELECT Students.*
FROM Students JOIN Streams ON Scode
WHERE Streams.Sname = "Science"