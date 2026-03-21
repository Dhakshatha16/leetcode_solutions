SELECT name
FROM SalesPerson
WHERE sales_id NOT iN 
(SELECT o.sales_id
FROM orders o
JOIN company c
ON o.com_id=c.com_id
WHERE c.name='RED');