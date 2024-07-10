#Problem 25

from math import ceil
from math import log
from math import sqrt

#Our task is to find the first term in the Fibonacci sequence to contain 1000 digits
#We could just brute force, but we can also use Binet's formula

#note that F_n = (1+sqrt5)/2^n + (1-sqrt(5))^n / 2 ~ (1+sqrt5)^n/2

#Then log_(1+sqrt5) 2*10^1000 = 1000 log_(1+sqrt5) 10 + log_(1+sqrt 5) 2
# = 1000 log(10)/log(1+sqrt 5) + log(2)/log(1+sqrt5)

def binet(n):
    return (((1+sqrt(5))/2)**n - ((1-sqrt(5))/2)**n)//sqrt(5)

print(binet(14))
print(binet(12))

phi = (1+sqrt(5))/2
print(phi)

print("The answer is", ceil(999*log(10)/log(phi) + log(sqrt(5))/log(phi)))