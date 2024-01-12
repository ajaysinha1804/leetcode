# Write your MySQL query statement below
SELECT(
SELECT DISTINCT salary AS SecondHighestSalary
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET 1
    ) AS SecondHighestSalary
