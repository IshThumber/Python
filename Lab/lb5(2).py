import math
import string
import random
from time import time
# def random_user_id():
#     return random.randint(1, 1000000)

# print(random_user_id())

Length = int(input("Enter your length id: "))
times = int(input("Enter number times: "))

# def user_id_gen_by_user():
#     return random.randint(10**(Length - 1), 10**(Length))


def user_id_gen_by_user():
    res = ''.join(
        random.choices(string.ascii_uppercase + string.digits, k=Length))
    return res


for f in range(times):
    print(user_id_gen_by_user())


def list_of_rgb_color_gen():
    return [random.randint(0, 255) for _ in range(3)]

print()
print(tuple(list_of_rgb_color_gen()))