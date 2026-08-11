# Write your MySQL query statement below
-- SELECT id ,salary
-- FROM (
--     SELECT e.id,e.salary
--            DENSE_RANK() OVER (ORDER BY e.salary DESC) AS dk
--     FROM Employee e
-- ) as ranked
-- WHERE dk = 2;
select max(salary) as SecondHighestSalary from employee where salary <(select max(salary) from employee);
-- select distinct salary as SecondHighestSalary from employee order by salary desc limit 1 OFFSET 1;
