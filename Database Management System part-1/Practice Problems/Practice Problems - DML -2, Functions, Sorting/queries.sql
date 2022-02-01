--Requirement 1
select substr(studentid,2) ID,studentname, gender 
    from student
    where (studentname like '%i%' or studentname like '%I%') and
        (city='Hyderabad' or city='Chennai')
    order by studentname;

--Requirement 2
select concat(courseid,concat('-',coursename)) coursedetails 
    from course
    where noofdays>3 and
        LENGTH(coursename)>12;

--Requirement 3
select studentid,
        case 
            when fee>2500 then 'A'
            when fee between 1500 and 2500 then 'B'
            when fee<1500 then 'C'
        end class
    from registration
    order by fee asc, regdate desc;

--Requirement 4
select distinct courseid 
    from registration
    where fee>=1200 and regdate like '%AUG%';

--Requirement 5
select courseid 
    from REGISTRATION
    group by courseid
    having avg(fee)<2500;

--Requirement 6
select studentid, avg(fee) avgfee
    from registration
    group by studentid
    having avg(fee)<1800 and count(*)>1;

--Requirement 7
update course set noofdays=noofdays+1 
    where coursename='Basics of Networking'
        or coursename='Cyber Security';

--Requirement 8
delete from student 
    where studentid not in (select STUDENTID from registration);

--Scenario2
select round(562.626,2) value1, ceil(562.626) value2, floor(562.626) value3
    from dual;

        