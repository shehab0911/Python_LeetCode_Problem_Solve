# Write your MySQL query statement below
select  customer_id
from Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_keY)= (select COUNT(product_key)
                            from Product
                            )
