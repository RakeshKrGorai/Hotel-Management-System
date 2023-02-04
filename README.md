# Hotel Management System

This is a basic Hotel  Management System Project which uses the concepts of MySQL and File Handling. It stores the data in sql tables and csv files.


## Steps To Run Project

- You need to have `Python` installed in your device. Can be easily downloaded from [here](https://www.python.org/downloads/) .
- You need to have `MySQL` installed in your device. Can be easily installed from [here](https://dev.mysql.com/downloads/mysql/) .
- Install `mysql-connector-python` from the command prompt : 
```
pip install mysql-connector-python
```
- In MySQL, create a database named `hotel` . Now select that database to use. 
```
create database hotel;
```
```
use hotel;
```
- Inside that database, create two tables namely `booking` and `service`. Use the syntax given below to create tables.

For table booking:
```
create table booking(
    Name Varchar(20),
    Phone_Number varchar(10),
    Email varchar(30),
    Check_In date,
    Check_Out date,
    Room_Type varchar(15),
    Price int,
    Room_Number int,
    Customer_id int,
    Payment varchar(3) default "No",
    Days int);
```
For table service:
```
create table service(
    Name varchar(20),
    Customer_id int,
    Service_Charge int default 0,
    Room_Bill int);
```
- Clone this repository (Download this repository).
- Now run "Hotel Management System.py". It should be working well.
<hr>
PS- Deleting record might give error if you try to delete data in same terminal where you booked your room. It will work if you close and re run the program and enter customer id for the customer you want to delete.

<hr>
