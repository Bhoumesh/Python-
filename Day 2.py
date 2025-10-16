"""IF ELSE STATEMENT"""

task = int(input("Enter your task number : "))

if(task > 10):
    print(" Do task A")
else :
    print("Do task B")    



money = int(input("Enter your money : "))

if money == 10:
    print("The ice cream will be bought")
elif money == 20:
    print("The chocolate will be bought")
elif money == 30:
    print("The cake will be bought")
else :
    print("Grocery item will be bought")



gen = input("please tell your gender as character (M or F):-")

if gen == 'M' or gen == 'm':
    print("Good morning SIR")
elif gen == "F" or gen == 'f':
    print("Good morning MAM")

else:
    print("Unidentified gender")


num = int(input("please tell your number :- "))

if num%2 == 0:
    print("even number")

else:
    print("Odd number")


name = input("Enter the name of the candidate : ")
age = int(input("Enter the age of the candidate : "))

if age >= 19:
    print(f"{name} is eligible for voting")
else:
    print(f"{name} is not eligible for voting")


year = int(input("Enter the year : "))

if year % 100 == 0 and year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


temp = int(input("Enter the temperature : "))

if temp == 0 or temp < 0:
    print("Freezing cold 🥶")
elif temp > 0 and temp <= 10:
    print("Very cold 😳")
elif temp > 10 and temp <= 20:
    print("Cold 👌")
elif temp > 20 and temp <= 30:
    print("Normal in temperature 😊")  
elif temp > 30 and temp <= 40:
    print("Hot 😎")
else :
    print("Very hot 🥵")        

""" FOR LOOP"""

a = range(1,20,1)
for i in a:
    print(i)

#####Lets print table of any number

n = int(input("Enter the number : "))

for i in range(n, (n*10)+1, n):
    print(i)


a ="Sidhgora is the best place to live"

for i in range(len(a)):
    print(a[i])

for i in range(1,21):
    if i == 56:
        print("break statement is executed")
        break
    print(i)

else:
    print("Break statement is not executed")


n = int(input("which table you want : - "))

for i in range(1,11):
    print(f"{n} * {i} = {n*i}")

n = int(input("please tell your number:- "))

sum = 0 

for i in range(1,n+1):
    sum = sum + i


print(f"your sum is {sum}")


n = int(input("please tell your number:- "))

fact = 1 

for i in range(1,n+1):
    fact = fact * i
print(f"your factorial is {fact}")    

n = int(input("tell your number :- "))
even = 0
odd = 0
for i in range(1,n+1):
    if i%2 == 0:
        even = even + i
    else:
        odd = odd + i

print(f"your even and odd sum are {even} , {odd}")


n = int(input("tell your number :- "))

sum = 0
for i in range(1, n+1):
    sum = sum + i
if sum == n:
    print("Perfect number")    
else:
    print("Not a perfect number")

n = int(input("check your number is prime or not  :-"))

count = 0

for i in range(1,n+1):
    if n%i == 0:
        count = count + 1

if count == 2:
    print("your number is prime")
else:
    print("your number is not prime")


a = "SHERYIANS"

b = ""
for i in range(len(a)-1,-1,-1):
    b = b + a[i]

print(b)

a = "NAMAN"

b = ""
for i in range(len(a)-1,-1,-1):
    b = b + a[i]


if b == a:
    print("your string is pallindrome")

else:
    print("its not a pallindrome")