# a=3
# if a>0:
#     print("a IS +VE")

## ---- ##

# a = int (input("Enter a number: "))
# if (a % 2) == 0:
#     print("Even number")
# else:
#     print("Odd number")

## ---- ##

# age = int(input("Enter your age: "))
# if (age >= 18):
#     print("You are old enough to drive")
# else:
#     print("You need {} years to learn driveing".format(18-age))

## ---- ##

# my_age = int(input("Enter your age: "))
# age = 30

# if (my_age > age):
#     if (my_age - age) <= 1:
#         print("You are {} year older than me".format(my_age - age))
#     else:
#         print("I am older then you by {} years".format(my_age - age))
# elif (my_age < age):
#     if (age - my_age) >= 1:
#         print("You are {} year younger than me".format(age - my_age))
#     else:
#         print("I am younger then you by {} years".format(age - my_age))
# else:
#     print("You are the same age as me")

## ---- ##

# a = int(input("Enter number 1 : "))
# b = int(input("Enter number 2 : "))

# if (a>b):
#     print("{} is greater then {}".format(a,b))
# elif (a<b):
#     print("{} is greater then {}".format(b,a))
# else:
#     ("{} is equal to {}".format(a,b))

## ---- ##

# cnt = 0
# while cnt <= 5:
#     if cnt == 2:
#         continue
#     print(cnt)
#     cnt = cnt + 1

## ---- ##

# person = {
#     'fname': 'abc',
#     'lname': 'bcd',
#     'age': '23',
#     'city': 'bangalore',
#     'skills': ['python', 'java', 'c++', 'JavaScript'],
#     'address': {
#         'street': 'space street',
#         'city': 'bangalore',
#         'zip': '560068'
#     }
# }

# for key in person:
#     print(key)

# for key, value in person.items():
#     print(key, value)

## ---- ##

# list = list(range(11))
# print(list)

# st = set (range(2,11))
# print(st)

# li = list(range(0,11,2))
# print(li)
# st1 = set(range(0,11,2))
# print(st1)

## ---- ##

# person = {
#     'fname': 'abc',
#     'lname': 'bcd',
#     'age': '23',
#     'city': 'bangalore',
#     'skills': ['python', 'java', 'c++', 'JavaScript'],
#     'address': {
#         'street': 'space street',
#         'city': 'bangalore',
#         'zip': '560068'
#     }
# }

# for key in person:
#     if key == 'skills':
#         for skill in person['skills']:
#             print(skill)

## ---- ##

# for x in range(10,-1,-1):
#     print(x)

# x=10
# while (x>=0):
#     print(x)
#     x = x - 1

# for i in range(1,9):
#     for j in range (1,9):
#         if j<=i:
#             print("#",end=" ")
#         else:
#             print("#",end=" ")
#     print()

# py = ['Python', 'Numpy','Pandas','Django', 'Flask']
# for a in py:
#     print(a)

# x=0
# while (x<=100):
#     if(x%2!=0):
#         print(x)
#     x = x + 1

## ---- ##

# def num():
#     num1=3
#     num2=5
#     total = num1 + num2
#     print(total)

# num()

## ---- ##

# def sq(x):
#     return x*x
# print(sq(5))

# def name(fname,lname):
#     return fname + " " + lname

# print("full name:", name("abc","bcd"))

# cnt = 0
# while cnt <= 5:
#     print(cnt)
#     cnt = cnt + 1
# else:
#     print(cnt)