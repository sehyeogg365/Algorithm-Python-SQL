1# Write your MySQL query statement below
2SELECT DISTINCT num AS ConsecutiveNums
3FROM (
4    SELECT 
5        num,
6        LEAD(num, 1) OVER (ORDER BY id) AS next_1,
7        LEAD(num, 2) OVER (ORDER BY id) AS next_2
8    FROM Logs
9) AS temp
10WHERE num = next_1 AND next_1 = next_2;