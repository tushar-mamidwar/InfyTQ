--Scenario 1
--Requirement 1
select distinct category,price
    from GREETINGCARD
    where price>300 or 
        category='Birthday Special';

--Requirement 2
select greetingcard.customerid
    from greetingcard inner join customer on greetingcard.CUSTOMERID=customer.customerid and 
    (length(custname)=5 or price>300);

--Requirement 3
select 'C' classification, customerid  id, custname name from customer
UNION
select 'GC' classificaton, cardid id, category name from greetingcard; 

--Scenario 2
--Requirement 1
select patient.pname, doctor.dname
    from patient inner join consultation on patient.patientid=consultation.patientid and pname like '%e%'
        INNER JOIN doctor on doctor.doctorid=consultation.doctorid and dept='Cardiology';

--Requirement 2
select dept,count(patient.patientid)
    from patient inner join consultation on patient.PATIENTID=CONSULTATION.patientid and (city='Boston' or city='Chicago')
        inner join doctor on doctor.DOCTORID=CONSULTATION.DOCTORID 
    group by dept;

--Requirement 3
select doctor.DOCTORID, dname
    from doctor inner join consultation on consultation.DOCTORID=doctor.doctorid and dept='Cardiology'
    group by doctor.doctorid,dname
    having count(PATIENTID)>1;

--Requirement 4
select doctor.doctorid 
    from doctor inner join consultation on doctor.DOCTORID=consultation.doctorid and dept='Cardiology'
union
select doctorid from consultation
    group by doctorid
    having sum(fee)>800;

--Requirement 5
select p.patientid
    from patient p inner join consultation c on p.patientid=c.patientid and city='New York'
UNION
select patientid 
    from doctor d inner join consultation c on d.doctorid = c.doctorid and dept<>'Cardiology'
    group by patientid 
    having sum(fee)<1000;
