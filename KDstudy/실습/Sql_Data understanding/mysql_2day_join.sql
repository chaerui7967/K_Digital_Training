# review
use classicmodels;
show tables;

# search
select * from employees;
select firstName from employees;
select firstName,lastName from employees;

# condition
select employeeNumber,firstName,lastName from employees where employees.employeeNumber >= 1300;
select city from offices where offices.officeCode=1;
select city,phone from offices where offices.officeCode=1;

# join
select orders.customerNumber as orders, customers.customerNumber as customers,
orders.orderNumber, customers.country 
from orders 
left join customers on customers.customerNumber = orders.customerNumber;

select customers.customerNumber, payments.checkNumber from customers
left join payments on customers.customerNumber = payments.customerNumber;

select orders.orderNumber, customers.country from orders
inner join customers on  orders.customerNumber = customers.customerNumber
where customers.country = 'USA';

select customers.customerName, payments.checkNumber from customers
left join payments on customers.customerNumber = payments.customerNumber
where payments.paymentDate >= '2003-06-01';

use classicmodels;
select customers.state, customers.customerName, payments.checkNumber from customers left join payments on customers.customerNumber = payments.customerNumber where payments.paymentDate >= '2004-10-06';

select count(customers.state) from customers where customers.state is not null;


# tip 데이터 활용
use tip;

select total_bill from tips where tip >= 7;

select day, avg(tip), count(*) from tips
group by day order by day desc; #(asc 기본)

SELECT smoker, total_bill, AVG(tip), count(*)
FROM tips
GROUP BY smoker, day order by smoker;