/*
Rex, a librarian wants to automate the book transactions(borrowing and returning) in his library. Here is the structure and rules for the book table that has been designed.

-Unique book id which consists of six alphanumeric characters and starts with B

-The book Title does not exceed 50 characters

-The name of the author does not exceed 20 characters

-Genre belongs to one of Mystery or Thriller

-Year of publication of the book

A table has to be created to store the details. Can you help with the creation of the table as per Rex’s requirement?
*/

create table book(
    book_id char(6) check(book_id like 'B%'),
    title varchar2(50),
    author varchar2(20),
    genre char(8) check(genre in ('Mystery','Thriller')),
    year_of_publication number(4));




/*
Mathew, a retail store owner wants to automate the purchase transactions(customer purchase items from the retailoutlet) in his retail store. Create a table item according to the structure, constraints and description as given below:



After the creation of the table given above, perform the following changes to existing table item:

Add a new column discount with data type NUMBER.

Modify the data type for description column to VARCHAR2(45) and category column to  VARCHAR2(5).

Change the column name description to itemdescription with same data type.

Remove the column itemtype and primary key constraint for the above table.
*/
drop table item;
create table item(
    itemcode varchar2(6) constraint ic_primary_key primary key,
    itemtype varchar2(30),
    description varchar2(50) not null,
    price number(5,2),
    category char(1)
);

alter table item add discount number;

alter table item modify (description varchar(45), category varchar2(5));

alter table item rename column description to itemdescription;

alter table item drop constraint ic_primary_key;
alter table item drop (itemtype);
desc item;

/*
Consider a University that offers various courses to its students on its campus. A student can register/signup for a 
specific course of their interest. Below are the table structures and sample data for tables course and courseregistration maintained 
by the University.

Requirement 1:
A new course ‘Software Engineering’ is introduced in the University with courseid C208, which will be handled for 3 
days of duration and the fee charged for this course is INR 1200. Can you help with the SQL command to add the required 
new course information to the course table?

Requirement 2:
A course with id C204 is registered by a student with id S306. R507 is the registrationid given for this registration. 
An insert statement is written to add courseid, studentid and registrationid to courseregistration table as a new record. 
Upon execution of the INSERT statement, an error message was expected since only the data of courseid, registrationid and 
studentid were provided in the SQL statement. There was a default value as SYSDATE set for registration date at the time of 
table creation. Identify the insert statement that can be used for the above scenario for successful execution.
*/

insert into course values('C208','Software Engineering',3,1200);

insert into COURSEREGISTRATION (registrationid,studentid,courseid) values('R507','S306','C204');


/*
“CareForYou” is a well-known hospital for its care and service. There are various types of employees such as 
doctors, attendants, admins, etc., Employees draw salary as per their nature of work. The information about 
employees is stored in employee table. The details of a doctor such as their qualification, specialization 
and fee are stored in doctor table. In patientfee and out patientfee is as per the hospital norms.

Here is the structure for tables employee and doctor with sample data:


Requirement 1:
Identify the Cardiologists and Nephrologists whose outpatientfee is in the range of 400 and 600(both inclusive) 
and inpatientfee more than 650. Write a SQL query to display id and qualification of the identified doctor(s).

Requirement 2:
Identify the doctor(s) having outpatientfee less than 500. Write a SQL query to display specialization and 
outpatientfee of the identified doctor(s).

Requirement 3:

Identify the female employees whose name contains either character ‘i’ anywhere or ‘a’ as second character 
and drawing salary less than or equal to 90000. Write a SQL query to display empno, empname and emptype of 
the identified employee(s).

Requirement 4:
Identify the employees who have registered their mailid and joined in the month of November 2016. Write 
a SQL query to display name and gender of the identified employee(s).

*/

select doctorid, qualification
    from doctor
    where outpatientfee between 400 and 600 and
        inpatientfee > 650 and
        specialization in ('Cardiology', 'Nephrology');

select specialization, outpatientfee
    from doctor
    where outpatientfee<500;

select empno, empname, emptype
     from employee
     where empname like '%i%' or
        empname like '_a%' and
        salary<=90000 and 
        gender='F';

select empname, gender
    from employee
    where emailid is not null and 
        DATEOFJOINING between '1-Nov-16' and '30-Nov-16';
