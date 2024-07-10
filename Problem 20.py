#Problem 20

from math import factorial
from functools import reduce

fact_str = str(factorial(100)) #We compute the number and then convert it into a string

sum = reduce(lambda a,b:int(a)+int(b),fact_str) #We take the sum of the int

print("The answer is", sum)