1# Write your MySQL query statement below
2SELECT p.firstName, p.lastName, IFNULL(a.city, null)AS city, IFNULL(a.state, null)AS state
3FROM Person p
4LEFT JOIN Address a
5ON p.personId = a.personId 
6