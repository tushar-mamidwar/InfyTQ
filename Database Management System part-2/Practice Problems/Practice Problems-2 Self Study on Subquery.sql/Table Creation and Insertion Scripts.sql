DROP TABLE Country CASCADE CONSTRAINTS;
DROP TABLE CustomerDetail CASCADE CONSTRAINTS;
DROP TABLE SellerDetail CASCADE CONSTRAINTS;
DROP TABLE ProductInventory CASCADE CONSTRAINTS;
DROP TABLE BillingDetail CASCADE CONSTRAINTS;
DROP TABLE ShipDetail CASCADE CONSTRAINTS;

CREATE TABLE Country
(
 CountryId INTEGER CONSTRAINT pk_CountryId PRIMARY KEY,
 CountryName VARCHAR2(30) NOT NULL
);


CREATE TABLE CustomerDetail
(
 CustomerId INTEGER CONSTRAINT pk_CustomerId PRIMARY KEY,
 CustomerName VARCHAR2(50) NOT NULL,
 Email VARCHAR2(50) NOT NULL,
 ContactNumber VARCHAR2(20) NOT NULL,
 Address VARCHAR2(500) NOT NULL,
 CountryId INTEGER CONSTRAINT fk_CountryId_CustomerDetail REFERENCES Country(CountryId) NOT NULL
);


CREATE TABLE SellerDetail
(
 SellerId INTEGER CONSTRAINT pk_SellerId PRIMARY KEY,
 SellerName VARCHAR2(50) NOT NULL,
 SellerAddress VARCHAR2(500) NOT NULL,
 SellerZip VARCHAR2(15) NOT NULL,
 SellerContactNumber VARCHAR2(20) NOT NULL,
 SellerRating DECIMAL(3,2) CONSTRAINT chk_SellerRating CHECK (SellerRating>=0 AND SellerRating<=5),
 CountryId INTEGER CONSTRAINT fk_CountryId_SellerDetail REFERENCES Country(CountryId) NOT NULL
);


CREATE TABLE ProductInventory 
(
 ProductId INTEGER CONSTRAINT pk_ProductId PRIMARY KEY,
 ProductType VARCHAR2(50) NOT NULL,
 ProductSubType VARCHAR2(50) NOT NULL,
 ProductName VARCHAR2(50) NOT NULL,
 Make VARCHAR2(50) NOT NULL,
 Price DECIMAL(10,2) CONSTRAINT chk_Price CHECK(Price>0) NOT NULL,
 SellerId INTEGER CONSTRAINT fk_SellerId_ProductInventory REFERENCES  SellerDetail(SellerId),
 WarrantyMonths INTEGER CONSTRAINT chk_WarrantyMonths CHECK(WarrantyMonths>=0) NOT NULL,
 UnitsLeft INTEGER CONSTRAINT chk_UnitsLeft CHECK(UnitsLeft>=0) NOT NULL
);

CREATE TABLE BillingDetail
(
 BillId INTEGER,
 BillItemId INTEGER,
 CustomerId INTEGER CONSTRAINT fk_CustomerId_BillingDetail REFERENCES CustomerDetail(CustomerId) NOT NULL,
 ActualAmount DECIMAL(10,2) CONSTRAINT chk_ActualAmount_BillingDetail CHECK(ActualAmount>=0)  NOT NULL,
 CountryId INTEGER CONSTRAINT fk_CountryId_BillingDetail REFERENCES Country(CountryId) NOT NULL,
 PaymentType VARCHAR2(20) CONSTRAINT chk_PaymentType CHECK(PaymentType IN ('Cash on delivery','Net Banking','Credit/Debit  Card','Discount Coupon')) NOT NULL, 
 ItemQuantity INTEGER CONSTRAINT chk_ItemQuantity CHECK(ItemQuantity>0) NOT  NULL,
 ProductId INTEGER CONSTRAINT fk_ProductId_BillingDetail REFERENCES ProductInventory(ProductId) NOT NULL,
 PurchaseDate DATE NOT NULL,
 CONSTRAINT pk_BillIdBillItemId PRIMARY KEY(BillId,BillItemId)
);


CREATE TABLE ShipDetail
(
 ShipId INTEGER CONSTRAINT pk_ShipId PRIMARY KEY,
 ShipAddress VARCHAR2(500) NOT NULL,
 ShipZip VARCHAR2(15) NOT NULL, 
 ShipCost DECIMAL(10,2) CONSTRAINT chk_ShipCost CHECK(ShipCost>=0) NOT NULL ,
 SellerId INTEGER CONSTRAINT fk_SellerId_ShipDetail REFERENCES SellerDetail(SellerId) NOT NULL,
 CustomerId INTEGER CONSTRAINT fk_CustomerId_ShipDetail REFERENCES CustomerDetail(CustomerId) NOT NULL,
 ShipStatus VARCHAR2(25) CONSTRAINT chk_ShipStatus CHECK(ShipStatus IN ('Delivered','Consignee not available','Returned back to   seller','Dispatched','Yet to be dispatched')) NOT NULL,
 ShipDate DATE NOT NULL,
 DeliveryDate DATE,
 CountryId INTEGER CONSTRAINT fk_CountryId_ShipDetail REFERENCES Country(CountryId) NOT NULL,
 CONSTRAINT chk_ShipDateDeliveryDate CHECK(DeliveryDate>=ShipDate)
);



DELETE FROM BillingDetail;
DELETE FROM ShipDetail;
DELETE FROM ProductInventory;
DELETE FROM SellerDetail;
DELETE FROM CustomerDetail;
DELETE FROM Country;

INSERT INTO Country(CountryId,CountryName) VALUES(1,'India');
INSERT INTO Country(CountryId,CountryName) VALUES(2,'USA');
INSERT INTO Country(CountryId,CountryName) VALUES(3,'Brazil');
INSERT INTO Country(CountryId,CountryName) VALUES(4,'England');
INSERT INTO Country(CountryId,CountryName) VALUES(5,'Australia');
INSERT INTO Country(CountryId,CountryName) VALUES(6,'South Africa');

INSERT INTO CustomerDetail(CustomerId,CustomerName,Email,ContactNumber,Address,CountryId) 
VALUES (1,'Albert','Albert@gmail.com','+91-8888888888','Mumbai, India',1);
INSERT INTO CustomerDetail(CustomerId,CustomerName,Email,ContactNumber,Address,CountryId) 
VALUES(2,'Anabela','Anabela@gmail.com','+1-206-999-2222','Washinton DC, USA',2);
INSERT INTO CustomerDetail(CustomerId,CustomerName,Email,ContactNumber,Address,CountryId) 
VALUES(3,'Angeles','Angie@gmail.com','+91-8888888888','Mumbai, India',1);
INSERT INTO CustomerDetail(CustomerId,CustomerName,Email,ContactNumber,Address,CountryId) 
VALUES(4,'Carlos','Carlos@gmail.com','+55-21-4444-5555','Rio De Janeiro, Brazil',3);
INSERT INTO CustomerDetail(CustomerId,CustomerName,Email,ContactNumber,Address,CountryId) 
VALUES(5,'Daniel','Daniel@gmail.com','+1-212-999-2222','New York, USA',2);
INSERT INTO CustomerDetail(CustomerId,CustomerName,Email,ContactNumber,Address,CountryId) 
VALUES(6,'Davis','Davis@gmail.com','+55-21-4444-5555','Rio De Janeiro, Brazil',3);
INSERT INTO CustomerDetail(CustomerId,CustomerName,Email,ContactNumber,Address,CountryId) 
VALUES(7,'Helen','Helen@gmail.com','+44-20-7777-3333','London, England',4);
INSERT INTO CustomerDetail(CustomerId,CustomerName,Email,ContactNumber,Address,CountryId) 
VALUES(8,'Karin','Karin@gmail.com','+61-2-5555-2222','Canberra, Australia',5);
INSERT INTO CustomerDetail(CustomerId,CustomerName,Email,ContactNumber,Address,CountryId) 
VALUES(9,'Janine','Janine@gmail.com','+27-41-888-7777','Pretoria, South Africa',6);


INSERT INTO SellerDetail(SellerId, SellerName, SellerAddress, SellerZip, SellerContactNumber, SellerRating, CountryId) 
VALUES(1,'WRetail','New Delhi, India', '100001','+91-9999999999',4.7,1);
INSERT INTO SellerDetail(SellerId, SellerName, SellerAddress, SellerZip,SellerContactNumber, SellerRating, CountryId) 
VALUES(2,'DSMart','Washington, USA', '20009','+1-206-777-3333',4.2,2);
INSERT INTO SellerDetail(SellerId, SellerName, SellerAddress, SellerZip, SellerContactNumber, SellerRating, CountryId) 
VALUES(3,'Vida','Rio De Janeiro, Brazil', '28640-000','+55-21-5555',3.8,3);
INSERT INTO SellerDetail(SellerId, SellerName, SellerAddress, SellerZip,SellerContactNumber, SellerRating, CountryId) 
VALUES(4,'GBRRetail','London, England', 'WC2N','+44-20-7777-4444',3.3,4);
INSERT INTO SellerDetail(SellerId, SellerName, SellerAddress, SellerZip,SellerContactNumber, SellerRating, CountryId) 
VALUES(5,'FoxRetail','Canberra, Australia', '2600','+61-2-5555-1111',2.9,5);
INSERT INTO SellerDetail(SellerId, SellerName, SellerAddress, SellerZip, SellerContactNumber, SellerRating, CountryId) 
VALUES(6,'Makhaya Brothers','Pretoria, South Africa', '0001','+27-12-999-5555',2.5,6);
INSERT INTO SellerDetail(SellerId, SellerName, SellerAddress, SellerZip, SellerContactNumber, SellerRating, CountryId) 
VALUES(7,'BangaloreRetail','Bangalore, India', '560063','+91-9999999998',4.3,1);
INSERT INTO SellerDetail(SellerId, SellerName, SellerAddress, SellerZip, SellerContactNumber, SellerRating, CountryId) 
VALUES(8,'NYNew','New York, USA', '00501','+1-212-555-6666',3.8,2);
INSERT INTO SellerDetail(SellerId, SellerName, SellerAddress, SellerZip, SellerContactNumber, SellerRating, CountryId) 
VALUES(9,'GarrinchaRetail','Brasilia, Brazil', '70000','+55-61-4444-3333',4.2,3);
INSERT INTO SellerDetail(SellerId, SellerName, SellerAddress, SellerZip, SellerContactNumber, SellerRating, CountryId) 
VALUES(10,'ABRetail','Port Elizabeth, South Africa', '6001','+27-41-888-6666',4.5,6);


INSERT INTO ProductInventory VALUES(1,'Automobiles','Four wheeler','Lamborghini Gallardo Spyder','Lamborghini',18000000,1,60,2);
INSERT INTO ProductInventory VALUES(2,'Clothing and Accessory','Belt','Kenneth Cole Black and White Leather Belt','Kenneth Cole',2500,2,0,200);
INSERT INTO ProductInventory VALUES(3,'Automobiles','Two wheeler','Honda CBR 250R','Honda',193000,1,60,11);
INSERT INTO ProductInventory VALUES(4,'Electronics','Mobile','Apple IPhone 7 16GB','Apple',60000,1,24,20);
INSERT INTO ProductInventory VALUES(5,'Electronics','Mobile','Lumia 1320','Microsoft',42199,2,24,20);
INSERT INTO ProductInventory VALUES(6,'Home','Furniture','Wooden photo frame','AllWood',3,2,0,200);
INSERT INTO ProductInventory VALUES(7,'Jewellery','Women Jewellery','Kundan jewellery set','Kundan',2000,1,0,20);
INSERT INTO ProductInventory VALUES(8,'Shoes','Sports','Adidas Shoes','Adidas',700,3,0,10);
INSERT INTO ProductInventory VALUES(9,'Sports','Lawn Tennis','Tennis racket','LT',200,4,0,150);
INSERT INTO ProductInventory VALUES(10,'Health','Gym','Door gym','GD',700,5,0,20);
INSERT INTO ProductInventory VALUES(11,'Automobiles','Four wheeler','BMW Z4','BMW',6890000,6,0,20);


INSERT INTO ShipDetail(ShipId,ShipAddress,ShipZip,ShipCost,SellerId,CustomerId,ShipStatus,ShipDate,DeliveryDate,CountryId) 
VALUES(1,'Mumbai, India','200002',200,1,1,'Delivered','15-Nov-2016','18-Nov-2016',1);
INSERT INTO ShipDetail(ShipId,ShipAddress,ShipZip,ShipCost,SellerId,CustomerId,ShipStatus,ShipDate,DeliveryDate,CountryId) 
VALUES(2,'Washington DC, USA','20009',5,2,2,'Dispatched','18-Nov-2016',NULL,2);
INSERT INTO ShipDetail(ShipId,ShipAddress,ShipZip,ShipCost,SellerId,CustomerId,ShipStatus,ShipDate,DeliveryDate,CountryId) 
VALUES(3,'Delhi, India','100002',200,1,3,'Dispatched','21-Nov-2016',NULL,1);
INSERT INTO ShipDetail(ShipId,ShipAddress,ShipZip,ShipCost,SellerId,CustomerId,ShipStatus,ShipDate,DeliveryDate,CountryId) 
VALUES(4,'Rio De Janeiro, Brazil','28640-000',50,3,4,'Delivered','19-Nov-2016','22-Nov-2016',3);
INSERT INTO ShipDetail(ShipId,ShipAddress,ShipZip,ShipCost,SellerId,CustomerId,ShipStatus,ShipDate,DeliveryDate,CountryId) 
VALUES(5,'Washington DC, USA','00501',5,2,5,'Delivered','18-Nov-2016','21-Nov-2016',2);
INSERT INTO ShipDetail(ShipId,ShipAddress,ShipZip,ShipCost,SellerId,CustomerId,ShipStatus,ShipDate,DeliveryDate,CountryId) 
VALUES(6,'London, England','WC2N',2,4,7,'Dispatched','18-Nov-2016',NULL,4);


INSERT INTO BillingDetail(BillId,BillItemId,CustomerId,ActualAmount,CountryId,PaymentType,ItemQuantity,ProductId,PurchaseDate) VALUES(1,1,1,193000,1,'Net Banking',1,3,'15-Nov-16');
INSERT INTO BillingDetail(BillId,BillItemId,CustomerId,ActualAmount,CountryId,PaymentType,ItemQuantity,ProductId,PurchaseDate) VALUES(2,1,2,42199,2,'Net Banking',1,5,'18-Nov-16');
INSERT INTO BillingDetail(BillId,BillItemId,CustomerId,ActualAmount,CountryId,PaymentType,ItemQuantity,ProductId,PurchaseDate) VALUES(3,1,3,60000,1,'Net Banking',1,4,'21-Nov-16');
INSERT INTO BillingDetail(BillId,BillItemId,CustomerId,ActualAmount,CountryId,PaymentType,ItemQuantity,ProductId,PurchaseDate) VALUES(4,1,4,700,3,'Net Banking',1,8,'19-Nov-16');
INSERT INTO BillingDetail(BillId,BillItemId,CustomerId,ActualAmount,CountryId,PaymentType,ItemQuantity,ProductId,PurchaseDate) VALUES(5,1,5,2500,2,'Net Banking',1,2,'18-Nov-16');
INSERT INTO BillingDetail(BillId,BillItemId,CustomerId,ActualAmount,CountryId,PaymentType,ItemQuantity,ProductId,PurchaseDate) VALUES(6,1,7,200,4,'Net Banking',1,9,'18-Nov-16');