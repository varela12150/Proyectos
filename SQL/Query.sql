SELECT con.contest_id, con.hacker_id,  con.name, 
       sum(sub.total_submissions), sum(sub.total_accepted_submissions), 
       sum(vs.total_views), sum(vs.total_unique_views)
FROM contests con 
JOIN colleges col on con.contest_id = col.contest_id 
JOIN challenges cha on  col.college_id = cha.college_id 
LEFT JOIN (SELECT challenge_id, sum(total_submissions) as total_submissions,       
           sum(total_accepted_submissions) as total_accepted_submissions 
           FROM submission_stats 
           GROUP BY challenge_id) sub on cha.challenge_id = sub.challenge_id
LEFT JOIN (SELECT challenge_id, sum(total_views) as total_views, 
           sum(total_unique_views) as total_unique_views
           FROM view_stats 
           GROUP BY challenge_id) vs on cha.challenge_id = vs.challenge_id
GROUP BY con.contest_id, con.hacker_id,  con.name
HAVING sum(sub.total_submissions)!=0 AND 
       sum(sub.total_accepted_submissions)!=0 AND
       sum(vs.total_views)!=0 AND
       sum(vs.total_unique_views)!=0
ORDER BY contest_id;


----------------------------------------------------------------------------------------------------------------

with a as (select ch.college_id, sum(vs.total_views) as tv,sum(vs.total_unique_views) as tuv
            from challenges ch
            join view_stats vs on (vs.challenge_id = ch.challenge_id)
            group by ch.college_id),
b as (select ch.college_id, sum(ss.total_submissions) as ts, sum(ss.total_accepted_submissions) as tas
        from challenges ch join submission_stats ss on (ss.challenge_id = ch.challenge_id)
        group by ch.college_id)
select
con.contest_id,
con.hacker_id,
con.name,
sum(b.ts),
sum(b.tas),
sum(a.tv),
sum(a.tuv)
from
contests con
join colleges col on (con.contest_id = col.contest_id)
join a on (a.college_id = col.college_id)
join b on (b.college_id = col.college_id)
group by
con.contest_id,
con.hacker_id,
con.name
order by
con.contest_id
;
--------------------------------------------------------------------------------------------------------


SELECT Name || '(' || SUBSTR(Occupation, 1, 1) || ')'
FROM OCCUPATIONS
ORDER BY Name;

SELECT 'There are a total of ' || Count(Name) || ' ' || LOWER(Occupation) || 's.'
FROM Occupations
GROUP BY Occupation
ORDER BY Count(Name), Occupation;

SELECT CONCAT(name,'(',LEFT(occupation,1),')')
FROM OCCUPATIONS 
ORDER BY name;

SELECT  CONCAT('There are a total of ',COUNT(occupation), CASE
              WHEN occupation = 'Doctor' THEN ' doctors'
              WHEN occupation = 'Singer' THEN ' singers'
              WHEN occupation = 'Actor' THEN ' actors'
              WHEN occupation = 'Professor' THEN ' professors'
              END)
FROM OCCUPATIONS 
GROUP BY occupation
ORDER BY Count(Name), Occupation;

--------------------------------------------------------------------------------------

SELECT co.company_code, co.founder, 
    COUNT(distinct le.lead_manager_code), COUNT(distinct se.senior_manager_code), 
    COUNT(distinct ma.manager_code),COUNT(distinct em.employee_code)
FROM Company co, Lead_Manager le, Senior_Manager se, Manager ma, Employee em 
where co.company_code = le.company_code 
    and le.lead_manager_code = se.lead_manager_code 
    and se.senior_manager_code = ma.senior_manager_code 
    and ma.manager_code = em.manager_code 
GROUP BY co.company_code 
ORDER BY co.company_code;