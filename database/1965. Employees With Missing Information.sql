select employee_id
from Employees e
where employee_id NOT IN (select employee_id from Salaries)
UNION
select employee_id
from Salaries
where employee_id NOT IN (select employee_id from Employees)
order by employee_id asc;
