/* Practice Problem 1 */
drop table course cascade constraints;
drop table student cascade constraints;
drop table registration cascade constraints;

create table student(studentid varchar2(6) primary key,studentname varchar2(40),gender char(1),city varchar2(20));
create table course(courseid number primary key,coursename varchar2(40),noofdays number);
create table registration(registerid number,studentid varchar2(6) references student(studentid),courseid references course(courseid),fee number,regdate date);

insert into student values('S101','Xavier','M','Chennai');
insert into student values('S102','Nancy','F','Hyderabad');
insert into student values('S103','John','M','Pune');
insert into student values('S104','Isabelle','F','Hyderabad');
insert into student values('S105','Rahim','M','Pune');
insert into student values('S106','Kevin','M','Chennai');

insert into course values(906,'Advanced Python',6);
insert into course values(905,'Software Engineering',2);
insert into course values(904,'Basics of Networking',4);
insert into course values(903,'DBMS Basics',3);
insert into course values(902,'Cyber Security',5);
insert into course values(901,'Introduction to Data Science',5);

insert into registration values(801,'S102',906,1200,'11-AUG-17');
insert into registration values(802,'S103',901,2500,'14-AUG-17');
insert into registration values(803,'S101',902,3000,'18-JUN-17');
insert into registration values(804,'S102',901,2500,'21-AUG-17');
insert into registration values(805,'S103',903,1000,'04-JUN-17');
insert into registration values(806,'S104',905,1000,'16-AUG-17');

select * from student;
select * from course;
select * from registration;
