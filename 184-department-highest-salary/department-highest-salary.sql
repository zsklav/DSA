# Write your MySQL query statement below
# can not use row number for tie , but can use dense_rank or rank
select d.name AS Department , 
    e.name AS Employee,
    e.salary AS Salary 
    from(
        select *,
            rank() over(
                partition by departmentID
                order by salary desc
            ) as rnk
        from employee 
    ) e
    join department d on
    e.departmentId=d.id
WHERE e.rnk=1;
