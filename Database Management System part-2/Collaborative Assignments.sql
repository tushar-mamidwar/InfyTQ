--Collaborative Assignment 93

select itemcode, itemtype, descr, category
    from item i
    where exists(select 1 
                    from purchasebill p 
                    where p.itemcode=i.itemcode);

--Collaborative Assignment 94
select itemcode, itemtype, descr, category
    from item
    where itemcode in (select itemcode 
                        from quotation
                        where qstatus='Rejected' and 
                            quotedprice=(select min(quotedprice)
                                            from quotation
                                            where qstatus='Rejected'));

--Collaborative Assignment 95
select i.itemcode, descr
    from item i inner join quotation q on i.itemcode = q.itemcode
    where quotedprice in (select max(quotedprice)
                            from quotation
                            where qstatus='Closed' or 
                                qstatus='Rejected')
        and (qstatus='Closed' or
        qstatus='Rejected');

--Collaborative Assignment 96
select itemcode,descr,price
    from item
    where price=(select max(price)
                    from item
                    where price<>(select max(price) 
                    from item));
                
--Collaborative Assignment 97
select empid, empname, designation
    from empdetails
    where empid in (select managerid from empdetails);

--Assignment 98 : Mandatory
select ename, job
    from emp
    where empno in (select empno from empvehicle);

--Assignment 99 : Mandatory
select ename 
    from emp
    where sal in (select max(sal) 
                    from emp);
--Assignment 100 : Mandatory
select empno,ename
    from emp
    where empno in (select empno 
                        from empvehicle
                        where vehicleid=(select v.vehicleid
                            from vehicle v inner join empvehicle ev on v.vehicleid=ev.vehicleid
                            group by v.vehicleid
                            having count(empno)=(select max(count(empno))
                                from empvehicle
                                group by vehicleid)));

--Assignment 101 : Mandatory
select e.empno,e.ename,e.deptno
    from emp e inner join emp e2 on e2.ename='Smith' and e.deptno=e2.deptno
    where e.ename<>'Smith';

--Assignment 102 : Mandatory
select i.itemcode,descr,qdate
    from quotation q inner join item i on i.itemcode=q.itemcode
    where quotedprice<(select max(quotedprice) 
                            from quotation qi
                            where q.qdate=qi.qdate);

--Assignment 103 : Mandatory
select billid, itemcode
    from purchasebill b
    where billamount<=(select avg(billamount)
                            from purchasebill bi 
                            where b.roid=bi.roid);

--Assignment 104 : Mandatory
select distinct q.sname, q.itemcode, descr
    from quotation q inner join item i on i.itemcode=q.itemcode
    where quotedprice<(select max(quotedprice)
                        from quotation qi
                        where q.itemcode=qi.itemcode
                        and qi.sname<>q.sname);

--Assignment 105 : Mandatory
select empid,empname,designation, salary
    from empdetails e
    where salary=(select max(salary)
                    from empdetails ei
                    where ei.designation=e.designation);

--Assignment 106 : Mandatory
select custid,custname
    from customer c
    where not exists(select 1 
                        from purchasebill p
                        where p.custid=c.custid);

--Assignment 107 : Optional
select billid, itemcode, custid, billamount, billdate, quantity
    from purchase bill b
    where exist (select 1 
                    from customer c 
                    where custtype='Privilaged' AND
                        c.custid=b.custid) and
            exist (select 1 
                        from item i
                        where itemtype='FMCG' and b.itemcode=i.itemcode);

--Assignment 108 : Optional
select custid, custname
    from customer c 
    where custid in (select custid from purchasebill);

--Assignment 109 : Optional
select empno, ename
    from emp e
    where sal> ( select avg(sal)
                    from emp ei
                    where e.deptno=ei.deptno);

--Assignment 110 : Optional
delete from empvehicle
    where empno in (select empno
                        from emp e
                        where sal=(select max(sal)
                                        from emp ei
                                        where ei.deptno=e.deptno));

--Assignment 111 : Optional
update emp e set sal=(select avg(sal)
                        from emp ei
                        where ei.deptno=e.deptno);

--Assignment 100 : Mandatory