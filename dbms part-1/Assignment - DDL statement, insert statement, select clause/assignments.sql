--Assignment 1
create table article(arcode char(5) primary key check(arcode like 'A%'),
    arname varchar2(30) not null,
    rate number(8,2),
    quantity number(4) default 0 check(quantity>=0),
    class char(1) check(class in ('A','B','C')));

--Assignment 2
insert into article values('A1001','Mouse',500,0,'C');

--Assignment 5: Mandatory
create table store(
    name varchar2(20) primary key,
    location varchar2(30) not null,
    managername varchar2(30) unique);

--Assignment 6: Mandatory
alter table store rename column name to storename;

--Assignment 7: Mandatory
create table bill(
    billno number primary key,
    storename varchar2(20) references store(storename),
    shopperid number references shopper,
    arcode char(5) references article,
    amount number,
    billdate date,
    quantity number(4) default 1 check (quantity>0));

--Assignment 8: Mandatory
create table supplier(
    supplierid varchar2(6) primary key,
    name varchar2(30),
    contactno varchar2(15) not null,
    emailid varchar2(30));

--Assignment 9: Mandatory
alter table supplier add city varchar2(10);

--Assignment 10: Mandatory
alter table supplier drop (emailid);
desc supplier;

--Assignment 11: Optional
create table city(
    city varchar2(20) unique);

--Assignment 12: Optional
drop table city;

--Assignment 13: Optional
create table address(
    houseno number,
    street varchar2(30),
    city varchar2(20) references city(city),
    zip number(6) check(zip>=0),
    state varchar2(5),
    primary key(houseno,street, city));

--Assignment 14: Optional
alter table address modify state varchar2(20);

--Assignment 17: Mandatory
insert into store values('Loyal World','Infy Campus, Mysore','Rohan Kumar');

--Assignment 18: Mandatory
insert into bill values(1001,'Loyal World',101,'A1001',1000,'20-oct-15',2);
insert into bill values(1002,'Loyal World',101,'A1002',1000,'15-nov-15',10);

--Assignment 19: Mandatory
insert into supplier values('S501','Avaya Ltd',9012345678,'Mysore');

--Assignment 3
select descr,price from hard disk;

--Assignment 25: Mandatory

--Assignment 26: Madnatory

--Assignment 27: Mandatory
select itemcode,description from item;

--Assignment 28: Mandatory

--Assignment 29: Mandatory

--Assignment 30: Mandatory

--Assignment 31: Mandatory

--Assignment 32: Mandatory

--Assignment 33: Mandatory

--Assignment 34: Mandatory
insert into city values('Mysore');

--Assignment 35: Optional
insert into address values('350','Electronics City','Mysore',570018,'Karnataka');

--Assignment 36: Optional
insert into article values('A1002','Keyboard',1000,10,'B');

--Assignment 37: Optional
