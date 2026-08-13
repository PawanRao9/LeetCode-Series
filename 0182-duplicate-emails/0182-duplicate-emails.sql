# Write your MySQL query statement belo
SELECT email as Email 
fROM Person 
group by email 
having count(email) > 1;