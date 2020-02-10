import math
import random

pi = math.pi
print("Value of pi is",pi)

i = random.randint(0, 100)

if i<50 or i>50:
    print(i,"\n")

picked_fruit = random.choice(['orange', 'strawberry', 'banana'])

for n in range(1,3):
    print(picked_fruit,"\n")

def multiply(a,b):
    c=a*b
    return c

print("12 x 96 =",multiply(12,96))
print("48 x 17 =",multiply(48,17))
print("196523 x 87323 =",multiply(196523,87323))
