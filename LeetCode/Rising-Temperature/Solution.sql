1# Write your MySQL query statement below
2-- 2015년 1월 2일의 기온은 전날보다 높았습니다(10 -> 25). 
3-- 2015년 1월 4일의 기온은 전날보다 높았습니다(20 -> 30).
4SELECT w1.id
5FROM Weather w1
6JOIN Weather w2 ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
7WHERE w1.temperature > w2.temperature;