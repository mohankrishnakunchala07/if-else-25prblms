'1.Check whether a number is positive, negative, or zero.'

num = int(input("enter number: "))

if num>0:
    print("positive Number")
elif num<0:
    print("Negative Number")
else:
    print("Number is Zero")

output:
enter number: 0
Number is Zero

'2.Take a number and check if it is even or odd.'

n = int(input("enter number: "))
if n % 2 ==0:
    print("Even Number")
else:
    print("Odd Number")
output:
enter number: 7
Odd Number 

'3.Check whether a person is eligible to vote (age ≥ 18).'

age = int(input("enter age:"))
if age >=18:
    print("Eligible To Vote")
else:
    print("Not Eligible")
output:
enter age:19
Eligible To Vote

'4.Take two numbers and print the greater number.'

v1=int(input("enter number:"))
v2=int(input("enter number:"))

if v1>v2:
    print(f"{v1} is Greater Number")
elif v2>v1: 
    print(f"{v2} is the greater Number")
else:
    print("Numbers Are Equal")
output:
enter number:20
enter number:30
30 is the greater Number

'5.Check whether a number is divisible by 5 or not.'

num=int(input("enter number:"))
if num%5==0:
    print(f"{num} is divisible by 5")
else:
    print(f"{num} is not divisible by 5")
#output:
enter number:45
45 is divisible by 5

'6.Take a number and check if it is a multiple of 3; otherwise print “Not multiple of 3”.'

num=int(input("enter number: "))
if num%3==0:
    print(f"{num} is multiple of 3")
else:
    print(f"{num} is not a multiple of 3")
output:
enter number: 31
31 is not a multiple of 3

'7.Check whether a character is a vowel or consonant.'

ch=input("enter character: ")
if ch in 'aeiouAEIOU':
    print("Vowel")
else:
    print("Consonant")

output:
enter character: s
Consonant

'8.Take a number and check if it is greater than 100 or not.'

num=int(input("enter number: "))

if num>100:
    print("Greater than 100")
else:
    print("Not greater than 100")

output:
enter number: 555
Greater than 100

'9.Check whether a year is a leap year or not.'

year=int(input("enter year: "))
if (year%400==0) or (year%4==0 and year%100 !=0):
    print("Leap year")
else:
    print("Not A year")
output:
enter year: 2020
Leap year

'10.Take temperature input and print “Hot” or “Cold” based on value (>30 hot).'

temperature=int(input("enter temperature: "))
if temperature>30:
    print("Climate is Hot")
else:
    print("Climate is Cold")
output:
enter temperature: 12
Climate is Cold

'11.Take marks and print grade: A (90+), B (75–89), C (50–74), Fail (<50).'

marks=int(input("enter marks: "))
if marks>=90:
    print("Grade:A")
elif marks>=75:
    print("Grade:B")
elif marks>50:
    print("Grade:C")
else:
    print("Fail")
output:
enter marks: 77
Grade:B


'12.Create a simple calculator using two numbers and an operator (+, -, *, /).'

v1=int(input("enter number: "))
v2=int(input("enter number: "))
op=input("select option (+,-,*,/):")

if op=='+':
    print("Addition two numbers:",v1+v2)
elif op=='-':
    print("Subtraction two numbers:", v1-v2)
elif op=='*':
    print("Multiplication Two numbers:",v1*v2)
elif op=='/':
    if v2!=0:
        print("Division Two Numbers", v1/v2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid number")
output:
enter number: 90
enter number: 45
select option (+,-,*,/):/
Division Two Numbers 2.0

'13.Take a number and print: “FizzBuzz” (divisible by 3 & 5), “Fizz” (only 3), “Buzz” (only 5), otherwise print number'.

num=int(input("enter number:"))
if num%5==0 and num%3==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
else:
    print(num)
output:
enter number:99
Fizz

'14.Check whether a character is uppercase, lowercase, digit, or special character.'

ch=input("enter character:")
if ch>='a' and ch<='z':
    print("lower case")
elif ch>='A' and ch<='Z':
    print("Upper case")
elif ch>'0' and ch<='9':
    print("Digit")
else:
    print("special character")
output:
enter character:!
special character


'15.Take salary and assign tax percentage: No tax (<2.5L), 5% (2.5L–5L), 20% (5L–10L), 30% (>10L).'

salary=int(input("enter salary: "))
if salary<=250000:
    tax=0
elif salary<=500000:
    tax=(salary-250000) * 5/100
    print(f'Tax for {salary}:',tax)
elif salary <=1000000:
    tax=(salary-250000) * 20/100
    print(f'Tax for {salary}:',tax)
elif salary>1000000:
    tax=(salary-250000) * 30/100
    print(f'Tax for {salary}:',tax)
output:
enter salary: 700000
Tax for 700000: 90000.0

'16.Find the largest of three numbers using nested if.'

n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
n3=int(input("enter third number:"))

if n1>n2:
    if n1>n3:
        print(n1, "is the largest")
    else:
        print(n3, "is the largest number")
else:
    if n2>n3:
        print(n2, "is the largest")
    else:
        print(n3, " is the largest")
output:
enter first number:60
enter second number:50
enter third number:40
60 is the largest

'17.Take three angles and check if they form a valid triangle.'

a=int(input("enter angle:"))
b=int(input("enter angle:"))
c=int(input("enter angle:"))
if (a+b+c==180):
    print("Valid Triangle")
else:
    print("Not A valid Triangle")
output:
enter angle:80
enter angle:40
enter angle:60
Valid Triangle

'18.Find the second largest among three numbers.'

a=int(input("enter number:"))
b=int(input("enter number:"))
c=int(input("enter number:"))

if (a>b and a<c) or (a<b and a>c):
    print("Second largest=",a)
elif (b>a and b<c) or (b>c and b<a):
    print("Second Largest=",b)
else:
    print("Second Largest=",c)
output:
enter number:40
enter number:60
enter number:80
Second Largest= 60

'19.Check whether a character is an alphabet or not (without using built-in functions).'

ch =input("enter character:")
if (ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
    print("alphabet")
else:
    print("Not A alphabet")
output:
enter character:m
alphabet


'20.Calculate electricity bill based on units: First 100 free, next 100 ₹5/unit, above 200 ₹10/unit.'

units=int(input("enter units:"))
if units<=100:
    bill=0
elif units <=200:
    bill=(units-100) * 5
else:
    bill=(100*5) + (units-200) * 10 
print("Electricity Bill = ", bill) 
output:
enter units:250
Electricity Bill =  1000

'21.Movie ticket pricing based on age: Child (<12), Adult, Senior (>60).'

age=int(input("enter age: "))

if age<12:
    print("Child")
elif age>60:
    print("Senior Citizen")
else:
    print("Adult")
output:
enter age: 54
Adult


'22.Implement login system with maximum 3 attempts (use nested if).'

username="mohan"
password="1234" 

u= input("enter username:")

if u == username:
    p=int(input("enter password:"))

    if p == password:
        print("Login Successful")
    else:
        print("wrong password")
        p = int(input("enter password again:"))

        if p == password:
            print("Login Successful")
        else:
            print("Wrong password")
            p = int(input("enter password again:"))

            if p == password:
                print("Login Successful")
            else:
                print("Max Attempts Reached")
else:
    print("Invalid Username")
output:
enter username:mohan
enter password:1256
wrong password
enter password again:6543
Wrong password
enter password again:9870
Max Attempts Reached


'23.Check whether a number is a palindrome (use conditions).'

num=input("enter number:")

rev=num[::-1]

if num==rev:
    print("palindrome")
else:
    print("Not A palindrome")
output:
enter number:121
palindrome

'24.Apply discount based on shopping amount: 5000 → 20%, >2000 → 10%, otherwise no discount.'

amount=int(input("enter amount: "))

if amount<2000:
    discount=0
elif amount<5000:
    discount=amount*10/100
    print(discount)
else:
    discount=amount*20/100
    
print("Discount =", discount)
print("Final amount =", amount - discount)
output:
enter amount: 9900
Discount = 1980.0
Final amount = 7920.0

'25.Traffic signal system: Red, Yellow, Green actions.'

signal=input("enter Signal Colour:")

if signal == "Red":
    print("Stop")
elif signal == "Yellow":
    print("Get Ready")
elif signal == "Green":
    print("Go")

else:
    print("Invalid Signal")
output:
enter Signal Colour:Red
Stop

