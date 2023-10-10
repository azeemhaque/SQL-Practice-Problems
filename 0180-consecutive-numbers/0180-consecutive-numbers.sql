# Write your MySQL query statement below
SELECT DISTINCT _frist.num 
AS ConsecutiveNums 
FROM
LOGS _frist, LOGS _second, LOGS _third

WHERE _frist.num = _second.num 
AND _second.num = _third.num
AND _second.id = _frist.id + 1 
AND _third.id = _second.id + 1 
AND _third.id = _frist.id + 2