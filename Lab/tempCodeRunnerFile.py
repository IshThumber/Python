
# DROPWHILE
lst = [2, 4, 5, 2, 4, 3, 4, 4]
# using dropwhile()
result = itertools.dropwhile(lambda x: x == 2, lst)
print(list(result)) #
