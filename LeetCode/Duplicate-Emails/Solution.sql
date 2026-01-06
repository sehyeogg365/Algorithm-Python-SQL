1# Write your MySQL query statement below
2select `email` AS Email
3from `person`
4GROUP BY `email`
5HAVING count(email) > 1