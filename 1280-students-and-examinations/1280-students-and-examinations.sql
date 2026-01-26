# Write your MySQL query statement below
select s.student_id,s.student_name, sb.subject_name,count(e.subject_name) as attended_exams
from students s
cross join Subjects sb
left join Examinations e
on s.student_id=e.student_id and sb.Subject_name=e.Subject_name
group by s.student_id,s.student_name,sb.subject_name
order by s.student_id, sb.subject_name

