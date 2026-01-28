# Write your MySQL query statement below
select product_name ,sum(unit) as unit 
from Products 
inner join Orders 
using (product_id)
where order_date between '2020-02-01' and '2020-02-28' 
group by product_name
having unit>=100
