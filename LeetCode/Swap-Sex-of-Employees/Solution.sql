1# Write your MySQL query statement below
2
3# Salary id name sex salary
4
5-- UPDATE 테이블명
6-- SET 컬럼명 = CASE 
7--                 WHEN 조건1 THEN 결과1
8--                 WHEN 조건2 THEN 결과2
9--                 ELSE 기존컬럼명 -- 혹은 다른 처리
10--              END;
11
12
13UPDATE Salary
14SET sex = CASE 
15                WHEN sex = 'f' THEN 'm'
16                WHEN sex = 'm' THEN 'f'
17                ELSE ' ' -- 혹은 다른 처리
18             END;
19