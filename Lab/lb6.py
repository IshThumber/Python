# //Lambda

# x = lambda a: a + 10
# print(x(5))

# x = lambda a, b, c : a + b ** c
# print(x(5, 6, 7))

# def fun(n):
#     return lambda a: a * n

# mytripler = fun(3)
# print(mytripler(10))

# def cube(y):
#     return y*y*y
# print(cube(5))

# lambda1 = lambda y :y*y*y
# print(lambda1(5))

# table = [lambda x = x: x+10 for x in range(1,11)]

# for q in table:
#     print(table())

# tables = [lambda x=x: x * 10 for x in range(1, 11)]

# for table in tables:
#     print(table())

# Max = lambda a, b : a if a > b else b

# print(Max(1,2))

# List = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]

# sortList = lambda x: (sorted(i) for i in x)

# secondLargest = lambda x, f: [y[len(y) - 2] for y in f]
# res = secondLargest(List, sortList(List))

# print(res)

# List = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]

# # Sort each sublist
# sortList = lambda x: (sorted(i) for i in x)

# # Get the second largest element
# secondLargest = lambda x, f: [y[len(y) - 2] for y in f(x)]
# res = secondLargest(List, sortList)

# print(res)

# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# final_list = list(filter(lambda x: (x%2 != 0) , li))
# print(final_list)

# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# final_list = list(filter(lambda x: (x%2 == 0) , li))
# print(final_list)

# ages = [13, 90, 17, 59, 21, 60, 5]
# adults = list(filter(lambda age: age > 18, ages))
# print(adults)

# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# final_list = list(map(lambda x: x*2, li))
# print(final_list)

# animals = ['dog', 'cat', 'parrot', 'rabbit']
# # here we intend to change all animal names
# # to upper case and return the same
# uppered_animals = list(map(lambda animal: str.upper(animal), animals))
# print(uppered_animals)

# from functools import reduce
# li = [5, 8, 10, 20, 50, 100]
# sum = reduce((lambda x, y: x + y), li)
# print (sum)

# import functools
# # initializing list
# lis = [1,3,5,6,2,]
# # using reduce to compute maximum element from list
# print("The maximum element of the list is : ", end="")
# print(functools.reduce(lambda a, b: a if a > b else b, lis))
# Lets filter only even nubers

