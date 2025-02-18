import math
from math import sqrt, floor
import random
import emoji
num2 = random.choice("samuel","bruno","diegp")
num2 = random.shuffle("samuel","bruno","diegp")
print(num2)


num = float(input("digite um numero"))
raiz = math.trunc(num)
print("a raiz de {} é igual a {}".format(num,math.ceil(raiz)))

num3 = int(input("digite um numero"))
raiz = sqrt(num)
print("a raiz de {} é igual a {}".format(num3,floor(raiz)))

