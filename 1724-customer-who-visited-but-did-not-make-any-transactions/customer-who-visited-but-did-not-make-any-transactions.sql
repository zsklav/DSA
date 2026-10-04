# Write your MySQL query statement below
select c1.customer_id, count(*) as count_no_trans
from visits c1
left join transactions c2
on c1.visit_id=c2.visit_id
where c2.transaction_id IS NULL
group by c1.customer_id
order by c1.visit_id asc;