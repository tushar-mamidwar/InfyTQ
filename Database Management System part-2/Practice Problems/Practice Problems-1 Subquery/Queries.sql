--Requirement 1
select c.custid, custname
    from customer c inner join booking b on c.custid=b.custid
    where FLIGHTCHARGE=(select max(flightcharge)
                            from booking bi
                            where bi.travelclass='Economy');
--Requirement 2
select f.flightid,f.flightname 
    from flight f inner join booking b on b.flightid=f.flightid 
    where flighttype='International'
    group by f.flightid,f.flightname
    having count(f.flightid) = (select max(count(fi.flightid))
                            from flight fi inner join booking b on fi.flightid=b.flightid
                            where fi.flighttype='International'
                            group by fi.flightid);

--Requirement 3
select c.custid,custname
    from customer c inner join booking b on c.custid=b.custid
    group by c.custid,custname
    having sum(FLIGHTCHARGE)<= (select avg(FLIGHTCHARGE)
                        from customer ci inner join booking bi on ci.custid=bi.custid
                        where TRAVELCLASS='Business');

--Requirement 4
select b.bookingid, f.flightid, c.custid
    from booking b inner join flight f on f.flightid=b.flightid
        inner join customer c on c.custid=b.custid
    where f.flighttype<>'Domestic' and 
        b.travelclass='Business' and 
        custname like '%e%';

--Requirement 5
select b.bookingid, source, destination,bookingdate
    from booking b inner join flight f on f.flightid=b.flightid
    where flightcharge<(select avg(flightcharge)
                            from booking bi inner join flight fi on fi.flightid=bi.flightid
                            where fi.flighttype=f.flighttype);

--Requirement 6
--Identify the customer(s) who have paid flight charge more than the average flight charge of all 
--other customers, who have booked the flight tickets for the same travel class. Write a SQL query to 
--display id and name of the identified customers.
select c.custid,custname
    from customer c inner join booking b on b.custid=c.custid
    where flightcharge >= all(select FLIGHTCHARGE
                                from booking bi
                                where bi.travelclass=b.travelclass);

--Requirement 7
--Identify the customer(s) who have booked tickets for both international and domestic flights. 
--Write a SQL query to display the name of the identified customers.
select custname
    from customer c inner join booking b on b.custid=c.custid
        inner join flight f  on f.flightid=b.flightid
    where flighttype='Domestic' and
        c.custid in (select custid 
                        from booking b inner join flight f on f.flightid=b.flightid
                        where f.flighttype='International');

--Requirement 8
-- Display flight’s id of the booked flight tickets, which fulfills EITHER of these requirements:

--Flight’s id of the booked flight tickets that are booked for the maximum number of times for the 
--travel class ‘Business’

--The total flight charge of a flight id of booked flight tickets is more than the average flight charge of
 --all bookings done for the same flight for travel class ‘Economy’.

select flightid
    from booking
    where travelclass='Business'
    group by flightid
    having count(flightid)=(select max(count(*))
                                from booking
                                where travelclass='Business'
                                group by flightid)
union
select flightid
    from booking
    where travelclass='Economy'
    group by flightid 
    having sum(flightcharge)>(select avg(FLIGHTCHARGE)
                        from booking
                        where TRAVELCLASS='Economy');
    