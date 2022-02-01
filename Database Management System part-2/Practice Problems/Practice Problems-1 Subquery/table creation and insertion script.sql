/* Practice Problem 1 */

drop table customer CASCADE CONSTRAINTS;
drop table flight CASCADE CONSTRAINTS;
drop table booking CASCADE CONSTRAINTS;

create table customer(
custid varchar2(5) primary key check(custid like 'C%'),
custname varchar2(10));

create table flight(
flightid varchar2(5) primary key check (flightid like 'F%'),
flightname varchar2(15),
flighttype varchar2(20) check (flighttype in ('Domestic','International')),
source varchar2(15),
destination varchar2(15)
);

Alter table flight modify flightname varchar2(20);

create table booking(
bookingid number primary key,
flightid varchar2(5) references flight(flightid),
custid varchar2(5) references customer(custid),
travelclass varchar2(30) check(travelclass in('Business','Economy')),
flightcharge number,
bookingdate date
);

insert into customer values('C301','John');
insert into customer values('C302','Sam');
insert into customer values('C303','Robert');
insert into customer values('C304','Albert');
insert into customer values('C305','Jack');

insert into flight values('F101','Spice Jet Airlines','Domestic','Mumbai','Kolkata');
insert into flight values('F102','Indian Airlines','International','Delhi','Germany');
insert into flight values('F103','Deccan Airlines','Domestic','Chennai','Bengaluru');
insert into flight values('F104','British Airways','International','London','Italy');
insert into flight values('F105','Swiss Airlines','International','Zurich','Spain');


insert into booking values(201,'F101','C301','Business',12000,'22-Mar-18');
insert into booking values(202,'F105','C303','Business',30000,'17-May-18');
insert into booking values(203,'F103','C302','Economy',3000,'23-Jun-18');
insert into booking values(204,'F101','C302','Economy',10000,'12-Oct-18');
insert into booking values(205,'F104','C303','Business',25000,'16-Jan-19');
insert into booking values(206,'F105','C301','Business',30000,'22-Jan-19');
insert into booking values(207,'F104','C304','Economy',22000,'16-Feb-19');
insert into booking values(208,'F101','C304','Business',12000,'18-Sep-19');


select * from customer;
select * from flight;
select * from booking;


