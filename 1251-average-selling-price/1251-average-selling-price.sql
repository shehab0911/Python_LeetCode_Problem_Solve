SELECT P.product_id, IFNULL(ROUND(SUM(P.price*S.units)/SUM(S.units),2),0)AS average_price
FROM PRICES P
LEFT JOIN UnitsSold S
ON P.product_id=S.product_id
AND S.purchase_date>=start_date
AND S.purchase_date<=end_date
GROUP BY P.product_id