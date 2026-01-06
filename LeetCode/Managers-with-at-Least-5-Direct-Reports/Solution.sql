1# Write your MySQL query statement below
2
3SELECT e2.name
4FROM Employee e1
5JOIN Employee e2
6ON e1.managerId = e2.id
7GROUP BY e2.id, e2.name -- 추가 할 내용
8HAVING count(*) >= 5
9