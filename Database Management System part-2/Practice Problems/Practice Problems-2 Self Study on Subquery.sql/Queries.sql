-- Problem Statement 1
select customerid, customername, email, ContactNumber
    from customerdetail
    where customerid in (select customerid 
                            from BillingDetail
                            group by customerid
                            having sum(actualamount) = (select max(sum(actualamount))
                                                                from BillingDetail
                                                                group by customerid));

-- Problem Statement 2
select COUNTRYNAME,c.customerid,(select max(sum(ACTUALAMOUNT))
                                    from BILLINGDETAIL b
                                    where b.countryid=c.countryid
                                    group by customerid) totalamount
    from CUSTOMERDETAIL c inner join country co on c.countryid=co.countryid
    where customerid in (select customerid
                            from billingDetail bi
                            where bi.countryid=c.countryid
                            group by customerid
                            having sum(actualamount)=(select max(sum(actualamount))
                                                                from BillingDetail bi2
                                                                where bi2.countryid=c.countryid
                                                                group by customerid))
    order by countryname;


-- Problem Statement 4
select shipid,SHIPADDRESS,shipzip,shipstatus,customername
    from customerdetail c inner join shipdetail s on c.customerid=s.customerid
    where EXISTS (select 1 from SELLERDETAIL sd
                    where SELLERRATING>4 and
                    sd.sellerid=s.sellerid) AND
        customername like '%a%';

