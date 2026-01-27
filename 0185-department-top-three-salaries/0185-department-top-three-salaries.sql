# Write your MySQL query statement below
SELECT D.name AS Department,E.name AS Employee,E.Salary
FROM Employee E
LEFT JOIN Department D
ON E.departmentId=D.ID
WHERE 3>(SELECT COUNT(DISTINCT(E2.SALARY))
        FROM EMPLOYEE E2
        WHERE E2.SALARY>E.SALARY AND
        E2.departmentId=E.departmentId


)