SELECT TOP (1) Title, LEN(Title)
  FROM Chinook.dbo.Album
  ORDER BY LEN(Title), Title
SELECT TOP (1) Title, LEN(Title)
  FROM Chinook.dbo.Album
  ORDER BY LEN(Title) DESC,Title;


/*SELECT TOP 1 CITY, LEN(CITY) 
FROM STATION 
ORDER BY LEN(CITY),CITY; 
SELECT TOP 1 CITY, LEN(CITY) 
FROM STATION 
ORDER BY LEN(CITY) DESC,CITY;*/

-- CASE

SELECT 
CASE
WHEN (MARKS <= 70) THEN 'NULL'
WHEN (MARKS > 70) THEN Name
END Name,
CASE  
WHEN (Marks >= 0 AND Marks <= 9)  THEN 1
WHEN Marks >= 10 AND Marks <= 19  THEN 2
WHEN Marks >= 20 AND Marks <= 29  THEN 3
WHEN Marks >= 30 AND Marks <= 39  THEN 4
WHEN Marks >= 40 AND Marks <= 49  THEN 5
WHEN Marks >= 50 AND Marks <= 59  THEN 6
WHEN Marks >= 60 AND Marks <= 69  THEN 7
WHEN Marks >= 70 AND Marks <= 79  THEN 8
WHEN Marks >= 80 AND Marks <= 89  THEN 9
WHEN Marks >= 90 AND Marks <= 100  THEN 10
END Grades, 
Marks
FROM Students;


--Top Competitors

SELECT t2.hacker_id, t2.name
    FROM (SELECT t1.name, t1.hacker_id, t1.challenge_id, t1.score, cha.difficulty_level
        FROM (SELECT hac.name, sub.hacker_id, sub.challenge_id, sub.score
                FROM Submissions sub
                JOIN Hackers hac on sub.hacker_id = hac.hacker_id) t1
        JOIN Challenges cha on cha.challenge_id = t1.challenge_id) t2
    JOIN Difficulty dif on dif.difficulty_level = t2.difficulty_level
WHERE t2.score = dif.score
GROUP BY t2.hacker_id, t2.name
HAVING COUNT(t2.hacker_id) > 1
ORDER BY COUNT(t2.hacker_id) DESC, t2.hacker_id ASC


SELECT h.hacker_id, h.name
FROM submissions s
JOIN challenges c ON s.challenge_id = c.challenge_id
JOIN difficulty d ON c.difficulty_level = d.difficulty_level 
JOIN hackers h ON s.hacker_id = h.hacker_id
WHERE s.score = d.score 
GROUP BY h.hacker_id, h.name
HAVING COUNT(s.hacker_id) > 1
ORDER BY COUNT(s.hacker_id) DESC, s.hacker_id ASC

SELECT
    H.hacker_id, H.name
FROM
    Hackers H
    INNER JOIN Submissions S ON S.hacker_id = H.hacker_id
    INNER JOIN Challenges C ON C.challenge_id = S.challenge_id
    INNER JOIN Difficulty D ON D.difficulty_level = C.difficulty_level AND D.score = S.score
GROUP BY H.hacker_id, H.name
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC, H.hacker_id

-------------------------------------------------------------------------------------------------------------

SELECT NUMPRE, COUNT(*) AS NUM_VECES 
FROM ( SELE... repetidos )
GROUP BY NUMPRE
HAVING COUNT(*) > 1
ORDER BY NUM_VECES DESC;


SELECT cus.customer_name, NVL(pro.product_name,'N/A'), NVL(invo.quantity,0)
FROM customer cus
LEFT JOIN invoice inv on inv.customer_id = cus.id
LEFT JOIN invoice_item invo on invo.invoice_id = inv.id
LEFT JOIN product pro on pro.id = invo.product_id
ORDER BY cus.id, pro.id, inv.id asc;


(SELECT LOCT
FROM (SELECT COUNT(N1) AS CONTEO, N1 AS LOCT
FROM (SELECT LO.NAME AS N1, CO.NAME AS N2 
    FROM LOCATIONS LO
    JOIN COMPANIES CO ON CO.LOCATION_ID = LO.ID
    JOIN PEOPLE PO ON PO.COMPANY_ID = CO.ID) T1
GROUP BY N1) T2
WHERE CONTEO = 31)

SELECT LO.NAME AS N1, CO.NAME AS N2
    FROM LOCATIONS LO
    JOIN COMPANIES CO ON CO.LOCATION_ID = LO.ID
    JOIN PEOPLE PO ON PO.COMPANY_ID = CO.ID)
WHERE  LO.NAME = (SELECT LOCT
                FROM (SELECT COUNT(N1) AS CONTEO, N1 AS LOCT
                FROM (SELECT LO.NAME AS N1, CO.NAME AS N2 
                 FROM LOCATIONS LO
                 JOIN COMPANIES CO ON CO.LOCATION_ID = LO.ID
                JOIN PEOPLE PO ON PO.COMPANY_ID = CO.ID) T1
                GROUP BY N1) T2
                WHERE CONTEO = 31)