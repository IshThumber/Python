# Python itertools
# itertools has 3 types of functions:
# 1. INFINITE iterator
# 2. COMBINATORIC iterator
# 3. TERMINATING iterator

# INFINITE has 3 types of functions:
# 1.count
# 2.cycle
# 3.repeat

# COMBINATORIC iterator types:
# 1.product
# 2.permutations
# 3.combinations
# 4.combinations_with_replacement

# TERMINATING iterator types:
# 1.chain
# 2.compress
# 3.dropwhile
# 4.filterfalse
# 5.islice


# use of itertools:
# fast and memory efficient

# Python program to demonstrate
# iterator module


# import operator
# import time

# L1 = [1, 2, 3]
# L2 = [2, 3, 4]

# t1 = time.time()

# a, b, c = map(operator.mul, L1, L2)

# t2 = time.time()

# print("Result:", a, b, c)
# print("Time taken by map function: %.6f" % (t2 - t1))

# t1 = time.time()

# print("Result:", end=" ")
# for i in range(3):
#     print(L1[i] * L2[i], end=" ")

# t2 = time.time()
# print("\nTime taken by for loop: %.6f" % (t2 - t1))

# ------OUTPUT--

# Result: 2 6 12
# Time taken by map function: 0.000005
# Result: 2 6 12
# Time taken by for loop: 0.000014

# -- -- -- Terminating Iterator -- -- -- #

import itertools

# CHAIN
l1 = ["a", "b", "c"]
l2 = ["c", "1", "2", "3", "4"]  # List
l3 = {"c", "d"}  # Set
l4 = (1, 2, 3)
# using chain()
result = itertools.chain(l1, l2, l3, l4)
print(list(result)) #Can join anything with anything.

# COMPRESS
names = "Blake"
value = [1, 1, 0, 1, 0]
# using compress()
result = itertools.compress(names, value)
print(list(result)) #Compress accourding to 1's or True. 

# DROPWHILE
lst = [2, 4, 5, 2, 4, 3, 4, 4]
# using dropwhile()
result = itertools.dropwhile(lambda x: x == 2, lst)
print(list(result)) #If the 1st element in the list matches with the lambda function then that element will be dropped.

# FILTERFALSE
lstt = [1, 2, 4, 5, 3, 2, 1]
# using filterfalse()
result = itertools.filterfalse(lambda x: x % 3 != 0, lstt)
print(list(result)) #if lambda is false then it will return false for the passed function.

# ISLICE
i_slice = [1, 2, 3, 4, 5, 6, 7, 8]
# using islice()
result = itertools.islice(i_slice, 0, 8, 3) # starts with 1st till 8th and skips 3 places
print(list(result))
