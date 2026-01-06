1# Write your MySQL query statement below
2-- select `name` AS `Employee`
3-- from `Employee`
4-- where `salary` > (
5--         select `salary`
6--         from `Employee`
7--         where `managerId` = (select `id`
8--                              from `Employee`
9--                              where 
10--                             )
11        
12-- )
13SELECT e.name AS `Employee`
14FROM Employee e
15JOIN Employee m
16ON e.managerId = m.id
17WHERE e.salary > m.salary
18
19
20# 서브 쿼리 활용해보기 
21# 구조는 맞는데 비교 대상을 변경 해야 함 
22# id 와 managerId가 같은것 끼리 salary 값을 비교해야함