#learn the most first thing : print 
print ("My name is salsabil, nice to meet you")
#now let's learn about variables
name = "salsabil"
age = 20
print(type(age))
#the programme will show that the age=20 is an int data type
print(type(name))
#name is a string data type
hight = 1.60
print(type(hight))
#hight is a float data type
salsabil_is_a_student = True
print(type(salsabil_is_a_student))
#salsabil is astudent is a boolean data type
#a small exercise to practice what we have learned
country="france"
population=67.39
co2_emission=4.5
print(type(country))
print(type(population))
print(type(co2_emission))
is_france_a_developed_country=True
print(type(is_france_a_developed_country))
A=15
B=7
print(A+B)
print(A-B)
print(A*B)
print(A/B)
# we have i this example 
X="25"
Y=5
print(int(X)+Y)
#we have another example for this case 
a="10"
b="20"
print(a+b)
print(int(a)+int(b))
#the first result will be 1020 because the two variables are strings and the second result will be 30 because we converted the two variables to integers
#in this example we have
x=7
y=2
print(x / y)
print(x // y)
print(x % y)
#the first result will be 3.5 because we divided 7 by 2 and the second result will be 3 because we used the floor division operator and the third result will be 1 because we used the modulus operator
#now let's learn about comparison operators
x=8
y=8
z=12
print(x==y)
print(x!=z)
print(y>z)
print(z>=12)
# new part im learning about and,or , not operators
#in this example we have
a=10
b=20
print(a<b and b==20)
print(a>b or b==20)
print(not a==10)
# lets learn about if statements
age=20
if age>=18:
    print("aadult.")
else:
    print("minor.")
#another exepmle for if 
# we have in this example 
score=6
if score>=10:
    print(" you pass the exam")
else:
    print(" you failed the exam")# here you fail study well next time 
    # thede exercises are not a guide just small steps to learn the basics of python programming language
#input
name=input("what is your name?")
print("hello ",name)
x=input("enter a number:")
print(type(x))
#input is a string data type 
a=float(input("a="))
b=float(input("b="))
print("the sum of a and b is ",a+b)
#now let's try to build a very simple calculater 
# wehave in this example
a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
print("the sum of a and b is ",a+b)
print("the difference of a and b is ",a-b)
print("the product of a and b is ",a*b)
print("the quotient of a and b is ",a/b)
#let's make the user the operation he wants to do
a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
operation=input("Enter the operation you want to do (+,-,*,/): ")
if operation=="+":
    print("the sum of a and b is ",a+b)
elif operation=="-":
    print("the difference of a and b is ",a-b)
elif operation=="*":
    print("the product of a and b is ",a*b)
elif operation=="/":
    print("the quotient of a and b is ",a/b)
else:
    print("invalid operation")
print("thank you for using our calculator")
#exercises to practice what we have learned
#first write a programme that save the name , the age , the hight ,a nd the situation of a person using variables and print them
name="assia"
age=20
hight=1.65
situation="student"
print("name",name)
print("age",age)
print("hight",hight)
print("situation",situation)
#we have a small stoor with four books the price of each book is 15 lets calculate the total price
price=15
quantity=4
totale_price=price*quantity
print("the total price is ",totale_price)
#lets write a prgramme usin if 
#we have
age1 =18
age2=20
if age1<age2:
    print("true")
else:
    print("false")
# 20--10--2026
# functions 
def say_hello(name):
    print("Hello",name)
say_hello("assia")
def add(a, b):
    print(a + b)
add(3, 4)
add(5, 6)
# the return opotion
def add(a, b):
    return a + b
add(3, 4)
print(add(3, 4))
#if with a function
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
print(check_number (5))
print(check_number (-2))
print (check_number(0))
###a very simple calculater app    #
def add (a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

print(add(3, 4))
print(subtract(10, 2))
print(multiply(3, 4))
print(divide(8, 2))
# a happy birthday function
def happy_birthday():
    print("happy birthday to you")
happy_birthday():
