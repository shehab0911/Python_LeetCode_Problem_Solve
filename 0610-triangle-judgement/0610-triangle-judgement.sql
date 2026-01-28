# Write your MySQL query statement below
select *,if(x + y > z AND y + z > x and x + z > y,"Yes","No") as triangle
from triangle