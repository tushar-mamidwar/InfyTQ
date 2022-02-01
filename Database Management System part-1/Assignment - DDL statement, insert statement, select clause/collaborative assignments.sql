--Collaborative Assignment 1

create table shopper(
    shopperid number(4) primary key,
    shoppername varchar(20) not null,
    gender char(6) check(gender in ('Male','Female')),
    MobileNo integer not null,
    address varchar(50));

--Collaborative Assignment 2
Alter table shopper modify mobileno varchar2(15);

--Collaborative Assignment 15
insert into shopper values(101,'Mark Jane','Male',1234567890, 'Allen Street, New York');