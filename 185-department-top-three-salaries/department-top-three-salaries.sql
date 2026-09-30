# Write your MySQL query statement below
select d.name AS Department , 
    e.name AS Employee,
    e.salary AS Salary 
    from(
        select *,
            DENSE_RANK() over(
                partition by departmentID
                order by salary desc
            ) as rnk
        from employee 
    ) e
    join department d on
    e.departmentId=d.id
WHERE e.rnk<=3;