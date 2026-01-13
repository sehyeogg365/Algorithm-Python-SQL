1# Write your MySQL query statement below
2# 서브쿼리 
3SELECT MAX(salary) AS SecondHighestSalary
4FROM (SELECT  salary, DENSE_RANK() OVER(ORDER BY SALARY DESC) AS `rank`
5      FROM Employee
6    ) a
7WHERE a.rank = 2
8