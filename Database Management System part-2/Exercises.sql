--Exercise 63: Correlated subquery
select prodid,category,pdesc,price 
    from product p
    where price=(select max(price) from product pi
                    where pi.category=p.category);

--Exercise 64: Correlated Subquery
select sname
    from salesman s
    where not exists (select sid from sale si where si.sid=s.sid);

--Exercise 65: Correlated Subquery
select sname 
    from salesman s
    where exists(select sid 
                    from sale si
                    where si.sid=s.sid and
                    sldate between '1-jun-15' and '30-jun-15');

--Exercise 66: Correlated Subquery
select s.sid,sname,location 
    from salesman s inner join sale sl on s.sid=sl.sid
        inner join saledetail sd on sd.saleid=sl.saleid
        inner join product pd on sd.prodid=pd.prodid
    group by s.sid,sname, location
    having sum((price-discount)*quantity)>
            (select avg(sum((price-discount)*quantity)) 
                from salesman si inner join sale sl on si.sid=sl.sid
                    inner join saledetail sd on sd.saleid=sl.saleid
                    inner join product pd on sd.prodid=pd.prodid
                where s.location=si.location
                group by si.sid);

