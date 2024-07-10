#Problem 30
#Find sum of all numbers where sum of fifth powers is the root

from functools import reduce

sum = 0
i = 2

def digit_power_sum(n):
    return reduce(lambda a,b:int(a)+int(b)**5,"0"+str(n))

print(digit_power_sum(1634))
print(digit_power_sum(8208))

while i<1000000:
    if i == digit_power_sum(i):
        sum+=i
        print(i)
    i+=1

print("The answer is", sum)
