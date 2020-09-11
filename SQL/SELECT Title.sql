SELECT Title
FROM dbo.Employee


SELECT T.Title
FROM ( SELECT Title
       FROM dbo.Employee) T
GROUP BY T.Title
HAVING COUNT(*) = (SELECT MAX(NUM_VECES)
FROM (SELECT T.Title, COUNT(*) AS NUM_VECES 
FROM ( SELECT Title
       FROM dbo.Employee) T
GROUP BY T.Title
HAVING COUNT(*) > 1) T2)




SELECT MAX(NUM_VECES)
FROM (SELECT T.Title, COUNT(*) AS NUM_VECES 
FROM ( SELECT Title
       FROM dbo.Employee) T
GROUP BY T.Title
HAVING COUNT(*) > 1) T2


