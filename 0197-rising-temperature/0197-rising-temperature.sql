WITH cte AS
(SELECT *,DATE_ADD(recordDate,INTERVAL-1 DAY) AS yesterdays_day
, LAG(recordDate) OVER(ORDER BY recordDate) AS prev_recordDate,LAG(temperature) OVER(ORDER BY recordDate) AS prev_temp
FROM Weather)
SELECT id
FROM cte
WHERE prev_recordDate = yesterdays_day AND temperature > prev_temp