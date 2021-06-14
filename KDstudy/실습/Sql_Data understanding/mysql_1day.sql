select sum(amount), count(checkNumber) from classicmodels.payments;
select * from classicmodels.customers;
select productName, productLine from products;
use sakila;
select * from actor;
select count(*) from classicmodels.customers where country ='USA';
use classicmodels;
select * from orders where orderDate between '2003-01-06' and '2003-01-18';
select * from orders where year(orderDate) = 2003;

select customerNumber from customers where country in ('USA', 'UK');
select count(customerNumber) from customers where country is null;

select * from employees where jobTitle = 'Sales Rep';
select distinct officeCode from employees;

select distinct productLine from products;
select productName from products where buyPrice between 50 and 100;

select customerNumber from customers where country in ('USA');