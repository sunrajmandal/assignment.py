age = int(input("Enter your age: "))
height = float(input("enter your height : "))
if age >= 12 and height >= 140:
    print("you can ride the roller coaster")
else:
    print("you cannot ride the roller coaster")
    
          

#Q.no.2
light = input("enter traffic light color: ")
if light == "red":
    print("stop")
elif light == "yellow":
    print("get ready")
elif light == "green":
    print("go")
else:
    print("invalid traffic light color")


#Q.no.3
number= int(input("enter a number: "))
match number:
    case 1:
        print("spring")
    case 2:
        print("summer")
    case 3:
        print("autumn")
    case 4:
        print("winter")
    case _: 
        print("invalid season number")

        
        
#Q.no.4
user_name = "admin"
password = "passs123"
input_username = input("enter username: ")
input_password = input("enter password: ")
Rename-Item "untitled-3.py" "assignment_conditions.py"


if input_username == user_name:
    
    if input_password == password:
    
     print("login successful")
    else:
        print("wrong password")
else:
    print("wrong username")

#Q.no.5
age = int(input("enter age: "))
income = int(input("enter monthly income: "))
if 21 <= age <= 60 and income >= 30000:
    print("your loan is approved" \
    "Congratulations!")
elif 21 <= age <= 60 and income <= 30000:
    print("your loan is not approved" \
    "sorry your income doesnot meet the requirements")

elif 21 > age <= 60 and income >= 30000:
    print("your loan is not approved" \
    "your age is less than 21")


elif 21 <= age < 60 and income >= 30000:
    print("your loan is not approved" \
    "your age is greater than 60")


elif 21 >= age >= 60 and income <= 30000:
    print("your loan is not approved" \
          "but income does not meet the requirements")
          


#Q.no.6
age = int(input("enter age: "))
membership_yes_or_no = input("enter yes if you have membership or no if you don't: ")
if age <= 12:
    print("ticket is free")
if 12< age < 60:
    if membership_yes_or_no == "yes":
        print("ticket price is rs150")  
    elif membership_yes_or_no == "no":
        print("ticket price is rs200")

elif age >= 60:
    print("ticket price is rs100")

else:    print("invalid input")



#Q.no.7
salary = int(input("enter salary: "))
year_of_service = int(input("enter year of service: "))
if year_of_service > 5:
    bonus = salary * 0.05
    print("your bonus is: ", bonus)           


#Q.no.8
radius = float(input("enter radius of the circle:  "))    
pi = 3.14
area = pi * radius ** 2
print("the area of the circle is: ", area)


    



#Q.no.9
age = int(input("enter age: "))
gender = input("enter gender (m or f): ")
number_of_days = int(input("enter number of days: "))

if 18 <= age < 30:
    if gender == "m":
        wages = 700 * number_of_days
        print("your wages is " , wages)
    elif gender == "f":
        wages = 750 * number_of_days

elif 30 <= age <=40 and gender == "m":
    wages = 800 * number_of_days

    print("your wages is ,wages")


          

elif gender == "f":
    wages = 850 * number_of_days
    print("your wages is , wages")
else:    print("invalid input")



#Q.no.10
number = int(input("enter number: "))  
if number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")

else:
    print("value as usual")
     








    
        



          
          