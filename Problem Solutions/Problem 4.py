#Problem 4

#We start with a dumb approach
from math import floor
from math import log10

def num_digits(n):
    if n<1:
        raise ValueError("N must be an integer")
    return floor(log10(n))+1

def is_palindrome(n):
    dig = num_digits(n)
    dig_array = [floor(n/(10**i))-floor(n/(10**(i+1)))*10 for i in range(dig)]
    return dig_array == dig_array[::-1]

#We start with a max value we know:
max_value = 12321

for i in range(100,1000):
    for j in range(i,1000):
        if is_palindrome(i*j) and i*j > max_value:
            max_value = i*j

print("The answer is",max_value)

#ALTERNATE BRUTE FORCE:
def is_str_palindrome(n):
    n_str = str(n)
    return n_str == reversed(n_str)

max_value = 12321
max_i = 1
max_j = 1

for i in range(1000,10000):
    for j in range(i,10000):
        if is_palindrome(i*j) and i*j > max_value:
            max_value = i*j
            max_i = i
            max_j = j

print("The answer is", max_i, "times", max_j, "=", max_value)