#Write a program to check whether the given number is in between 1 and 100 or not
num = int(input("Enter a number: "))
if num >= 1 and num <= 100:
    print("The number is in between 1 and 100.")
else:   
     print("The number is not in between 1 and 100.")


#Check whether the user input number is even or odd and display it to user.
num = int(input("enter a number: "))
if num % 2 == 0:
     print("num is a even number")
else:
     print("num is a odd number")
     

#ques. no.3
     

months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
month_number = int(input("Enter a month number (1-12): "))
if month_number in months:
    print(months[month_number])

#ques. no.4
marks = int(input("Enter your marks: "))
if marks >= 80:
    print("Grade: A")
elif 60<marks<80:
    print("Grade: B")
elif 50<marks<60:
    print("Grade: C")
elif 40<marks<50:
    print("Grade: D")
elif 30<marks<40:
    print("Grade: E")
else:
    print("Grade: F")


#Q.no.5
num1 = int(input("Enter first number: "))
if num1 % 7 == 0:
    print("The number is divisible by 7.")
else:  
    print("The number is not divisible by 7.")


#Q.no.6
num1 = int(input("enter first number: "))
num2 = int(input("enter secomd number: "))
enter_operator = input("enter operator: ")
if enter_operator == "+":
    print(num1 + num2)
elif enter_operator == "-":
    print(num1 - num2)
elif enter_operator == "*":
    print(num1 * num2)
elif enter_operator == "/":
   
   print(num1 / num2)
else:    
    print("invalid operator")



#Q.no.7
salary = int(input("Enter your salary: "))
credit_score = int(input("Enter your credit score: "))
if salary >= 50000 and credit_score >= 700:
    print("eligible")
else:
    print("not eligible")




#Q.no.8
integers = int(input("Enter an integer: "))
if integers % 2 == 0 and integers % 5 == 0:
    print("fizzbuzz")
elif integers % 5 == 0:
    print("buzz")
elif integers % 2 == 0:
    print("fizz")


else:
    print(integers)

#Q.no.9
enter_character = str(input("Enter a character: "))
if enter_character in {'a', 'e', 'i', 'o', 'u'}:
    print("vowel")
else:
    print("consonant")


#q.no.10
enter_marks = int(input("Enter your marks: "))
if enter_marks >= 90:
    print("Grade: A")
elif 80 <= enter_marks <=89:
    print("Grade: B")
elif 70 <= enter_marks <=79:
    print("Grade: C")

   
#Q.no.11
enter_age = int(input("Enter age: "))
if enter_age < 13:

    print("child")
elif 13 <=enter_age <= 19:
    print("teenager")
elif enter_age > 19:
    print("adult")


#Q.no.12
character = input("Enter a character: ")
if character.isupper():
    print("uppercase")
elif character.islower():
    print("lowercase")
elif character.isdigit():
    print("digit")

#Q.no.13
color = input("Enter a color: ")
if color == "red":
    print("stop")
elif color == "yellow":
    print("get ready")
elif color == "green":
    print("go")


#Q.no.14
age = int(input("Enter your age: "))
experience = int(input("enter your evperience:"))
if age < 18 and experience >= 2:

    print("You are  eligible to job.")
else:
    print("You are not eligible to job.")


#Q.no.15    
temperature = int(input("enter current temperature: "))
if temperature > 30:
    print("It's hot, stay hydrated!")
elif 15<temperature<30:
    print("enjoy the wheather!")
elif temperature < 15:
    print("It's cold, wear warm clothes!")

#Q.no.16
menu = input("enter your order: ")
if menu == "pizza":
    print("pizza: $10")
elif menu == "burger":
    print("burger: $7")
elif menu == "pasta":
    print("pasta: $8")


#Q.no.17
height = int(input("enter height in feet:"))
if height >= 6 :
    print("selected")

             
elif height < 6:
    print("not selected")

#Q.no.18
age = int(input("enter age:"))
if age < 18:
    print("not eligible to watch the movie")
elif age >= 18:
    print("eligible to watch the movie")


#Q.no.19
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "password123":
    print("Access granted.")
else:
    print("Access denied.")


#Q.no.20
month = int(input("Enter month number (1-12): "))
if month == 12 or month == 1 or month == 2:
    print("Winter")
elif month == 3 or month == 4 or month == 5:
    
    print("Spring")
elif month == 6 or month == 7 or month == 8:
    print("Summer")
elif month == 9 or month == 10 or month == 11:
    print("Autumn")


