# def square(x):  # a square function
#     return x**2

# def cube(x):  # a cube function
#     return x**3

# def absolute(x):  # an absolute value function
#     if x >= 0:
#         return x
#     else:
#         return -(x)

# def higher_order_function(type):  # a higher order function returning a function
#     if type == 'square':
#         return square
#     elif type == 'cube':
#         return cube
#     elif type == 'absolute':
#         return absolute

# result = higher_order_function('square')
# print(result(3))  # 9
# result = higher_order_function('cube')
# print(result(3))  # 27
# result = higher_order_function('absolute')
# print(result(-3))  # 3

##
# def greeting():
#     return 'Welcome to Python'

# def uppercase_decorator(function):

#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase

#     return wrapper

# g = uppercase_decorator(greeting)
# print(g())

# def greeting():
#     return 'Welcome to Python'
# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
# g = uppercase_decorator(greeting)
# print(g())

# ## Let us implement the example above with a decorator'''This decorator function is a higher order function
# # that takes a function as a parameter
# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
# @uppercase_decorator
# def greeting():
#     return 'Welcome to Python'
# print(greeting()) # WELCOME TO PYTHON

# # First Decorator
# def uppercase_decorator(function):

#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase

#     return wrapper  # Second decorator

# def split_string_decorator(function):

#     def wrapper():
#         func = function()
#         splitted_string = func.split()
#         return splitted_string

#     return wrapper  #split_string_decorator

# # @uppercase_decorator # order with decorators is important in this case - .upper() function does not work with lists
# def greeting():
#     return 'Welcome to Python'
# print(greeting())  # WELCOME TO PYTHON

numbers = [1, 2, 3, 4, 5]  # iterable


def square(x):
    return x**2


numbers_squared = map(square, numbers)
print(list(numbers_squared))  # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x: x**2, numbers)
print(list(numbers_squared))  # [1, 4, 9, 16, 25]

# numbers_str = ['1', '2', '3', '4', '5'] # iterable
# numbers_int = map(int, numbers_str)
# print(list(numbers_int)) # [1, 2, 3, 4, 5]

# names = ['Mrugendra', 'Martin', 'Chintan', 'Nikunj'] # iterabledef change_to_upper(name):
# return name.upper() names_upper_cased = map(change_to_upper, names)
#     print(list(names_upper_cased)) # ['MRUGENDRA', 'MARTIN', 'CHINTAN', 'NIKUNJ']# Let us apply it with a lambda function
#     names_upper_cased = map(lambda name: name.upper(), names)
# print(list(names_upper_cased)) # ['MRUGENDRA', 'MARTIN', 'CHINTAN', 'NIKUNJ']

# Lets filter only even nubers
# numbers = [1, 2, 3, 4, 5] # iterabledef is_even(num):
# if num % 2 == 0:
#     return True
# return Falseeven_numbers = filter(is_even, numbers)
# print(list(even_numbers)) # [2, 4]

# names = ['Mrugendra', 'Martin', 'Chintan', 'Nikunj'] # iterable
# def is_name_long(name):
# if len(name) > 7:
# return True
# return Falselong_names = filter(is_name_long, names)
# print(list(long_names)) # ['Mrugendra']

# numbers_str = ['1', '2', '3', '4', '5'] # iterable
# def add_two_nums(x, y):
# return int(x) + int(y)total = reduce(add_two_nums, numbers_str)
# print(total) # 15

# ### Exercises: Level 11. Explain the difference between map, filter, and reduce.
# 2. Explain the difference between higher order function, closure and decorator
# 3. Define a call function before map, filter or reduce, see examples.
# 4. Use for loop to print each country in the countries list.
# 5. Use for to print each name in the names list.
# 6. Use for to print each number in the numbers list.