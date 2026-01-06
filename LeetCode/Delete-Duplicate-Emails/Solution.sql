1# Write your MySQL query statement below
2
3DELETE p
4FROM Person p
5JOIN Person e
6ON p.email = e.email
7WHERE p.id > e.id
8
9
10