# Write your MySQL query statement below
WITH cte AS(
SELECT customer_number,COUNT(order_number) AS numOrd
FROM Orders
GROUP BY customer_number
 )
 SELECT customer_number
 FROM cte
WHERE numOrd = (SELECT MAX(numOrd) FROM cte)
