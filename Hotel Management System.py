#Project For Hotel Management System Using Python,File Handling and SQL Database

#Importing Required Modules

import csv
import random
import os 
import mysql.connector as c
con=c.connect(host='localhost',user='root',passwd='mysql',database='hotel')
cursor=con.cursor()
cursor.execute("use hotel")

#Defining Global Variables

hotel_database="hotel.csv"
name=phno=add=checkin=checkout=room=price=rc=p=roomno=custid=day=[]
hotel=[]
services=[]
fields=['Name','Phone No','Email','Check-In','Check-Out','Room Type','Price','Room Number',"Customer Id","Days"]
i=0
days=0
r=""

#Home Function

def Home():
    print("--------------------------------------------------")
    print("GREETINGS!\n")
    print("WELCOME TO HOTEL PARADISE")
    print("--------------------------------------------------")
    print("\t\t\t 1 Booking A Room\n")
    print("\t\t\t 2 Rooms Info\n")
    print("\t\t\t 3 Room service(Food Menu)\n")
    print("\t\t\t 4 Pay Bill\n")
    print("\t\t\t 5 Search A Record\n")
    print("\t\t\t 6 Delete Record\n")
    print("\t\t\t 7 Contact Us\n")
    print("\t\t\t 0 Exit\n")
    print("--------------------------------------------------")
    ch=int(input("What Would You Like To Do? Enter Your Choice :"))
    if ch == 1:
        print(" ")
        booking()
    elif ch == 2:
        print(" ")
        info_rooms()
    elif ch == 3:
        print(" ")
        restaurant()
    elif ch == 4:
        print(" ")
        payment()
    elif ch == 5:
        print(" ")
        search_record()
    elif ch == 6:
        print(" ")
        delete_record()
    elif ch==7:
        print(" ")
        contact()
    elif ch==0:
        print(" ")
        exit()
    else:
        print("Invalid Option")

#Defining Different Functions For The Program

#BOOKING FUNCTION

def booking():
        days=0
        openfile=open(hotel_database,'a')
        fw=open('services.csv','a')
        global i
        global hotel
        print("-----------------------")
        print("BOOKING ROOMS")
        print("-----------------------")
        print(" ")
        global fields
        Booking_data=[]
        csvfile=csv.writer(openfile)
        csvfile1=csv.writer(fw)
        while True:
                n=input("Name :")
                while n=="":
                    print("Name can't be empty")
                    n=input("Name :")
                p1=input("Phone :")
                while len(p1)!=10:
                    print("Invalid Phone Number")
                    p1=input("Phone :")
                a=input("email :")
                while "@" not in a:
                    print("Invalid Email")
                    a=input("email :")
                if n!="" and p1!="" and a!="":
                    name.append(n)
                    phno.append(p1)
                    add.append(a)
                    break
        checkindate=input("Check-In Date(YYYY-MM-DD) :")
        #copy of data for file management
	
        indate=checkindate
        checkin.append(checkindate)
        checkindate=checkindate.split('-')
        ci=checkindate
        ci[0]=int(ci[0])
        ci[1]=int(ci[1])
        ci[2]=int(ci[2])
        checkoutdate=input("Check-Out Date(YYYY-MM-DD) :")
	
        #copy of date for file management
	
        outdate=checkoutdate
        checkout.append(checkoutdate)
        checkoutdate=checkoutdate.split('-')
        co=checkoutdate
        co[0]=int(co[0])
        co[1]=int(co[1])
        co[2]=int(co[2])
        if co[1]<ci[1] and co[2]<ci[2]:
                print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
                name.pop(i)
                add.pop(i)
                checkin.pop(i)
                checkout.pop(i)
                booking()
        elif co[1]==ci[1] and co[0]>=ci[0] and co[2]<=ci[2]:
                print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
                name.pop(i)
                add.pop(i)
                checkin.pop(i)
                checkout.pop(i)
                booking()
        else:
                m = {
                        1:31,
                        2:28,
                        3:31,
                        4:30,
                        5:31,
                        6:30,
                        7:31,
                        8:31,
                        9:30,
                        10:31,
                        11:30,
                        12:31
                        }
                d=0
		
                #Checking Right Credentials
		
                if (0<ci[1]<13 and 0<co[1]<13 and ci[2]<=m[ci[1]] and co[2]<=m[co[1]]):
                    #if month are same
                    if(ci[1]==co[1]):
                        days=co[2]-ci[2]
                    else:
                        for i in range(ci[1],co[1]):
                            #print(m[i])
                            days+=(m[ci[1]]-ci[2])+co[2]
                    print('Booking for ',days+1,'days')
                else:
                    print('Wrong Value')
        print("----SELECT ROOM TYPE----")
        print(" 1. Standard")
        print(" 2. Standard Plus")
        print(" 3. Suites")
        print(" 4. Cottages")
        print(("\t\tPress 0 for Room Prices"))
        ch=int(input("->"))
		
        # if-conditions to display alloted room type and it's price
        #r=""
        if ch==0:
            print(" 1. Standard- Rs. 4000")
            print(" 2. Standard Plus - Rs. 4500")
            print(" 3. Suites - Rs. 5000")
            print(" 4. Cottages- Rs. 5500")
            ch=int(input("->"))
        elif ch==1:
            room.append('Standard') 
            print("Room Type- Standard")
            r="Standard"
            price.append(4000)
            p=4000
            print("Price- 4000")
            bill=(days+1)*p
        elif ch==2:
            room.append('Standard Plus') 
            print("Room Type-Standard Plus ")
            price.append(4500)
            print("Price- 4500")
            r="Standard Plus"
            p=4500
            bill=(days+1)*p
        elif ch==3:
            room.append('Suites')
            print("Room Type- Suites")
            price.append(5000)
            print("Price- 5000")
            r='Suites'
            p=5000
            bill=(days+1)*p
        elif ch==4:
            room.append('Cottages')
            print("Room Type- Cottages")
            price.append(5500)
            print("Price- 5500")
            r="Cottages"
            p=5500
            bill=(days+1)*p
        else:
            print(" Wrong choice..!!")
        # randomly generating room no. and customer id for customer
	
        room_no = random.randrange(40)+300
        customer_id = random.randrange(60)+10
        print("")
        roomno.append(room_no)
        custid.append(customer_id)
        i=i+1
        hotel.extend([n,p1,a,indate,outdate,r,p,room_no,customer_id,days+1])
        csvfile.writerow(hotel)
        print("\t\t\t---ROOM BOOKED SUCCESSFULLY---\n")
        print("Room No. - ",room_no)
        print("Customer Id - ",customer_id)
        print("Successfully Saved into Our Database")
        data=str(hotel)
        sql="insert into booking(Name,Phone_Number,Email,Check_In,Check_Out,Room_Type,Price,Room_Number,Customer_id,Days)values('{}',{},'{}','{}','{}','{}',{},{},{},{})".format(n,str(p1),a,str(indate),str(outdate),r,p,room_no,customer_id,days+1)
        cursor.execute(sql)
        service_charge=0
        services.extend([n,customer_id,service_charge,bill])
        csvfile1.writerow(services)
	
        sql1="insert into service(Name,Customer_id,Room_Bill)values('{}',{},{})".format(n,customer_id,bill)
        cursor.execute(sql1)
        con.commit()
        hotel=[]
        openfile.close()
        n=int(input("0-BACK\n -->"))
        if n==0:
            Home() 
        else:
            exit()

#ROOM INFO FUNCTION

def standard():
        print("\t\t\tSTANDARD")
        print("---------------------------------------------------------------")
        print("Find sanctuary in our serene Standard room. A cosy double bedroom complete with an ensuite with rainfall shower and private balcony.\n")
        print("This cosy room has everything you need for R&R, including crisp 300 thread count cotton sheets, a hypoallergenic mattress, ensuite bathroom, a private balcony and, of course, superfast WiFi connection. Decorated with classic interior that complements the Algarve’s natural beauty, this room has everything you need for a relaxing stay.")
        print("\nThis room includes\n")
        print("1.Air Conditioning")
        print("2.High Speed WiFi")
        print("3.Multi-Line Telephone")
        print("4.Flat Screen TV with International Channels")
        print("5.Daily Maid Service")
        print("")

def standard_plus():
	print("\t\t\tSTANDARD PLUS")
	print("---------------------------------------------------------------")
	print("Enjoy all the comfort and style of the Standard but in our larger room. With a size of 26m², the Standard Plus is ideal for longer stays.")
	print("\nWith a private entrance and ground floor access, our Standard Plus rooms have all the comfort and style of the Standard but with added space. With a size of 26m², and a private balcony perfect for sipping a cocktail at sunset, the Standard Plus is ideal for longer stays at The Paradise Hotel. Complete with a divinely comfortable twin or double bed, crisp 300 thread count cotton sheets and modern en suite bathroom fitted with all amenities, oversized 600 tog bath towels, hairdryer, vanity sink and magnifying make-up mirror.")
	print("\nThis room includes\n")
	print("1.Air Conditioning")
	print("2.High Speed WiFi")
	print("3.Multi-Line Telephone")
	print("4.Flat Screen TV with International Channels")
	print("5.Daily Maid Service")
	print("")
        
def suites():
        print("\t\t\tSUITES")
        print("---------------------------------------------------------------")
        print("Our stylish suites are complete with a double bedroom, living space with cosy couches, ensuite and private balcony. Dreamy.")
        print("\nBright and airy, our stylish suites feature separate living areas with cosy couches to lounge on, as well as a divine double bedroom for the ultimate R&R. In the bathroom, a glorious shower awaits, with a vanity sink and mirror equipped with hairdryer, magnifying make-up mirror, and signature Paradise slides.")
        print("\nThis room includes\n")
        print("1.Air Conditioning")
        print("2.High Speed WiFi")
        print("3.Multi-Line Telephone")
        print("4.Flat Screen TV with International Channels")
        print("5.Daily Maid Service")
        print("")

def cottages():
        print("\t\t\tCOTTAGES")
        print("---------------------------------------------------------------")
        print("Our charming two-bedroom cottages each have their own living room, kitchenette, bathroom and patio. Great for couples and families looking for a blissful getaway.")
        print("\nThe perfect retreat. Situated among the pine trees, our two-bedroom cottages each have their own living room, kitchenette, bathroom and patio. Great for couples and families, with modern and luxurious style and all The Paradise Hotel action on the doorstep, it’s ideal for a dreamy getaway.")
        print("\nThis room includes\n")
        print("1.Air Conditioning")
        print("2.High Speed WiFi")
        print("3.Multi-Line Telephone")
        print("4.Flat Screen TV with International Channels")
        print("5.Daily Maid Service")
        print("")

def info_rooms(): 
        print()
        print("		 ------ HOTEL ROOMS INFO ------")
        print("")
        standard()
        standard_plus()
        suites()
        cottages()
        n=int(input("0-BACK\n ->"))
        if n==0:
        	Home()
        else:
        	exit()

# RESTAURANT FUNCTION 

def restaurant():
    id=int(input("Customer Id: "))
    k=0
    counter=0
    fw=open('services.csv','a')
    csvfile=csv.writer(fw)
    global i
    with open('hotel.csv','r') as csvfiler:
        csvr=csv.reader(csvfiler)
        for row in csvr:
                #print(len(row))
                for i in range(0,len(row)):
                    #print(i)
                    if row[8]==str(id):
                        k=k+1
                        x=row[8]
                        name=row[0]
                        customerid=row[8]
                        print(' ')
                        print('Welcome',row[0],".What would you like to have today?")
                        print("----------------------------------------------------------------")
                        print("----------------------------------------------------------------") 
                        print("\t\tHotel Paradise Menu Card")
                        print("----------------------------------------------------------------")
                        print("----------------------------------------------------------------")
                        print("\n BREADS			       		THALI MEAL DEALS")
                        print("----------------------------------	 -----------------------------------") 
                        print(" 1 Toast X2................ 25.00	 36.Chana and Puri..............50.00 ") 
                        print(" 2 French Toasts........... 30.00        37.Halwa and Puri..............40.00") 
                        print("--------------------------               38.Chana Halwa Puri............65.00") 
                        print(" ROTIS AND PARATHAS	                 -----------------------------------") 
                        print(" -------------------------	 	 CHINESE")
                        print(" 3.Plain Roti X1............... 10.00	 -----------------------------------")
                        print(" 4.Butter Roti X1.............. 20.00	 39.Veg Chowmein..................80.00")
                        print(" 5.Butter Nan.................. 25.00	 40.Butter Chowmein..............100.00") 
                        print(" 6.Aaloo Paratha X1.............25.00    41.Noodles.......................40.00") 
                        print(" 7.Aaloo and Onion Paratha X1...30.00	 42.Ramen.........................60.00")
                        print(" 8.Paneer Paratha X1............45.00    43.Veg Spring Rolls.............100.00")
                        print(" ------------------------------------	 44.Mixed Spring Rolls...........150.00")
                        print(" SABJI	 				-----------------------------------") 
                        print(" ------------------------------------	DALS") 
                        print(" 9.Aaloo Gobi..................90.00	------------------------------------") 
                        print(" 10.Bhindi Fry................ 90.00     45.Dal Tadka.....................80.00")
                        print(" 11.Mix Veg....................90.00	 46.Dal Fry.......................80.00")
                        print(" 12.Mushroom Masala...........120.00	 47.Dal Makhni...................100.00")
                        print(" 13.Aaloo Matar...............100.00     48.Rajma........................100.00")
                        print(" 14.Matar Paneer..............120.00     49.Chhole.......................100.00")
                        print(" 15.Kadai Paneer..............120.00     -----------------------------------")
                        print(" 16.Shahi Paneer..............120.00	 RICE")
                        print(" -----------------------------------	 -----------------------------------")
                        print(" SOUPS                   		 50.Plain Rice....................90.00")
                        print("------------------------------------	 51.Jeera Rice....................90.00")
                        print(" 17.Tomato Soup................50.00	 52.Fried Rice...................120.00")
                        print(" 18.Manchow Soup...............55.00	 53.Paneer Fried Rice............165.00")
                        print(" 19.Hot Sour Soup..............55.00	 54.Veg Pulao....................130.00") 
                        print(" 20.Palak Soup.................55.00	 55.Matar Pulao..................140.00")
                        print("------------------------------------	 -----------------------------------")
                        print(" SOUTH INDIAN DISHES                     SANDWICHES")
                        print("------------------------------------	 -----------------------------------")
                        print(" 21.Plain Dosa.................70.00	 56.Veg Sandwich..................45.00")
                        print(" 22.Masala Dosa................80.00	 57.Cheese Sandwich...............65.00")
                        print(" 23.Paneer Masala Dosa........100.00	 58.Grilled Sandwich.............120.00")
                        print(" 24.Dahi Vada..................55.00	 59.Club Sandwich................120.00")
                        print(" 25.Idli Sambhar...............30.00	 60.Veg Cheese Grilled Sandwich..140.00")
                        print(" 26.Idli Fried.................40.00	 61.Veg Toasted Sandwich..........70.00")
                        print("------------------------------------	 -----------------------------------")
                        print(" PIZZA 					  ICE CREAMS")
                        print("------------------------------------	 -----------------------------------")
                        print(" 27.Cheese Pizza..............140.00	 62.Vanilla Ice cream.............60.00")
                        print(" 28.Mushroom Pizza............160.00	 63.Strawberry Ice cream..........60.00")
                        print(" 29.Margherita................130.00	 64.Chocolate Ice cream...........60.00")
                        print(" 30.Paneer Pizza..............160.00	 65.Pineapple Ice cream...........60.00")
                        print(" 31.Tomato Pasta Pizza........150.00	 66.Butterscotch Ice cream........60.00")
                        print("------------------------------------	 -----------------------------------")
                        print(" BEVERAGES				  DESSERTS")
                        print("------------------------------------	 -----------------------------------")
                        print(" 32.Pepsi(500 ml)..............60.00	 67.Choco Lava Cake..............100.00")
                        print(" 33.Slice(350 ml)..............50.00	 68.Butterscotch Mousse Cake.....100.00")
                        print(" 34.7Up(500 ml)................60.00	 69.Red Velvet Lava Cake.........130.00")
                        print(" 35.Mirinda(500 ml)............60.00	 70.Blueberry Cheese Lava Cake...130.00")
                        print("------------------------------------	 -----------------------------------")
                        print("Press 0 -to end ")
                        ch=1
                                
                        while(ch!=0):
                            ch=int(input(" -> ")) 
                                                
                            # if-elif-conditions to assign item 
                            # prices listed in menu card 
                                                
                            if ch==1 or ch==5 or ch==6:
                                cost=25
                                counter=counter+cost
                            elif ch==2 or ch==7 or ch==25:
                                cost=30
                                counter=counter+cost
                            elif ch==3:
                                cost=10
                                counter=counter+cost
                            elif ch==4:
                                cost=20
                                counter=counter+cost
                            elif ch==8 or ch==56:
                                cost=45
                                counter=counter+cost
                            elif (ch<=11 and ch>=9) or ch==50 or ch==51:
                                cost=90
                                counter=counter+cost
                            elif (ch<=16 and ch>=14) or ch==12 or ch==52 or ch==58 or ch==59:
                                cost=120
                                counter=counter+cost
                            elif (ch<=20 and ch>=18) or ch==24:
                                cost=55
                                counter=counter+cost
                            elif ch==21 or ch==61:
                                cost=70
                                counter=counter+cost
                            elif ch==17 or ch==33 or ch==36:
                                cost=50
                                counter=counter+cost
                            elif ch==22 or ch==39 or ch==45 or ch==46:
                                cost=80
                                counter=counter+cost
                            elif ch==26 or ch==37 or ch==41:
                                cost=40
                                counter=counter+cost
                            elif ch==27 or ch==55 or ch==60:
                                cost=140
                                counter=counter+cost
                            elif ch==28 or ch==30:
                                cost=160
                                counter=counter+cost
                            elif ch==31 or ch==44:
                                cost=150
                                counter=counter+cost
                            elif ch==32 or ch==34 or ch==35 or ch==42 or(ch>=62 and ch<=66):
                                cost=60
                                counter=counter+cost
                            elif ch==38 or ch==57:
                                cost=65
                                counter=counter+cost
                            elif ch==53:
                                cost=165
                                counter=counter+cost
                            elif ch==13 or ch==23 or ch==40 or ch==43 or (ch>=47 and ch<=49) or ch==68 or ch==67:
                                cost=100
                                counter=counter+cost
                            elif ch==29 or ch==54 or ch==70 or ch==69:
                                cost=130
                                counter=counter+cost
                            elif ch==0:
                                pass
                            else:
                                print("Wrong Choice..!!")
                                    
                        if counter!=0:
                                print("Total Bill: ",counter)
                                service=[]
                                bill=str(counter)
                                service.extend([name,customerid,bill])
                                csvfile.writerow(service)
                                service=[]
                                print('Order Placed.Coming Right Up')
                                sql="update service set Service_Charge ={} where Customer_id={};".format(counter,x)
                                cursor.execute(sql)
                                con.commit()
                                z='NO'
                                sql1="update booking set Payment='{}' where Customer_id={}".format(z,x)
                                cursor.execute(sql1)
                                con.commit()
                                break
                                    
                        else:
                                print("Order Not Placed")
                                break
                    else:
                        pass
        if k==0:
            print("User with the given Customer id is not registered.")

        n=int(input("0-BACK\n ->"))
        if n==0:
                Home()
        else:
                exit()

#PAYMENT FUNCTION

def payment():
        id=int(input('Enter customer id-->'))
        k=0
        with open('hotel.csv','r') as csvfiler:
            csvr=csv.reader(csvfiler)
            for row in csvr:
                for i in range(0,len(row)):
                    if row[8]==str(id):
                        k=k+1
                        print("Yo")
                        print("Welcome",row[0],". Here is your bill:")
                        sql='select * from service where Customer_id={}'.format(id)
                        cursor.execute(sql)
                        rows=cursor.fetchall()
                        for x in rows:
                            hotel_service=x[2]
                            room_chrg=x[3]
                            print('Hotel Service',hotel_service)
                            print('Room Charge',room_chrg)
                        sql1='select Payment from booking where Customer_id={}'.format(id)
                        cursor.execute(sql1)
                        row1=cursor.fetchall()
                        print("Your Total bill is:",hotel_service+room_chrg)
                        if row1==[('NO',)]:
                            ch=input("Do you wish to make your payment now? y-yes,or any other character to exit-->")
                            if ch=='y' or ch=='Y':
                                print("Enter mode of payment")
                                print(" 1- Credit/Debit Card")
                                print(" 2- Paytm/PhonePe")
                                print(" 3- Using UPI")
                                print(" 4- Cash")
                                x=int(input("-> "))
                                if 1<=x<=4:
                                    print("\n\n --------------------------------")
                                    print("		 Hotel Paradise")
                                    print(" --------------------------------")
                                    print("			 Bill")
                                    print(" --------------------------------")
                                    print(" Name: ",row[0],"\t\n")
                                    print("\n\t\n Room Charges:",room_chrg)
                                    print(" Restaurant Charges: \t",hotel_service)
                                    print(" --------------------------------")
                                    print("\n Total Amount: ",(hotel_service+room_chrg))
                                    print(" --------------------------------")
                                    print("		 Thank You")
                                    print("		 Visit Again :)")
                                    print(" --------------------------------\n")
                                    z="YES"
                                    sql2="update booking set payment='{}' where Customer_id={};".format(z,id)
                                    cursor.execute(sql2)
                                    con.commit()
                                else:
                                    print("Wrong Choice,please retry")
                        else:
                            print("\n\nYour Payment is already done")
                        n = int(input("0-BACK\n ->"))
                        if n==0:
                            Home()
                            break
                        else:
                            exit()


# RECORD FUNCTION

def search_record():
        id=int(input('Enter customer id-->'))
        k=0
        with open('hotel.csv','r') as csvfiler:
            csvr=csv.reader(csvfiler)
            for row in csvr:
                for i in range(0,len(row)):
                    if row[8]==str(id):
                        k=k+1
                        print("----------------------------------------------------------------------------------------------------------------------")
                        print('Name:',row[0])
                        print('\nPhone Number:',row[1])
                        print("\nEmail:",row[2])
                        print("\nCheck-In Date:",row[3])
                        print("\nCheck-Out Date",row[4])
                        print("\nRoom Type:",row[5])
                        print("\nPrice:",row[6])
                        print("\nRoom Number:",row[7])
                        print('\nCustomer Id:',row[8])
                        print('\nBooked for:',row[9],'days')
                        print("----------------------------------------------------------------------------------------------------------------------")
                        break
                    else:
                        pass
            if k==0:
                    print("Record with the given customer id is not registered.Please retry!!")
            csvfiler.close()
            n = int(input("0-BACK\n ->"))
            if n == 0:
                Home()
            else:
                exit()

#DELETE RECORD FUNCTION

def delete_record():
    csvfilew1=open("new.csv","w")
    csvw=csv.writer(csvfilew1)
    cid=int(input("Enter Your Customer Id :"))
    k=0
    l=[]
    with open(hotel_database,'r')as csvfiler:
        csvr=csv.reader(csvfiler)
        #print(csvr)
        for row in csvr:
            for i in range(0,len(row)):
                if str(cid)==row[8]:
                    k=k+1
                    print("Record Found,Deleting It.......")
                    print("............")
                    print(".........")
                    print(".....")
                    print("Record Deleted!!")
                    break
                elif str(cid)!=row[8]:
                    csvw.writerow(row)
                    break
        if k==0:
                print("Record with the given customer id is not registered.Please retry!!")
    
                
    csvfilew1.close()
    csvfiler.close()
    os.remove("hotel.csv")
    os.rename("new.csv","hotel.csv")
    st="delete from booking where Customer_id={}".format(cid)
    cursor.execute(st)
    con.commit()
    n = int(input("0-BACK\n ->"))		
    if n == 0:
        Home()
    else:
        exit()
	

#CONTACT FUNCTION

def contact():
	print("------------------------------------------")
	print("\t\tHotel Paradise")
	print("------------------------------------------")
	print("\nHere's how you can contact us")
	print("\nTELEPHONE:")
	print("\n\t+91 612 2203040")
	print("\nFAX:")
	print("\n\t+91 612 2203060")
	print("\nADDRESS:")
	print("\n\tHotel Paradise, South Gandhi Maidan, Mumbai , Maharashtra - 400029, India")
	print('\nGENERAL ENQUIRIES:')
	print('\n\t+91 612 2203040')
	print('\n\takm@paradise.com')	
	n = int(input("0-BACK\n ->"))		
	if n == 0:
		Home()
	else:
		exit()

def exit():
	print("\nThank You for using our services")
	
Home()
con.close()
