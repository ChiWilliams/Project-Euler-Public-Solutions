#Problem 74
from math import factorial

# Our factorial sum-er
def fact_dig_sum(number):
    acc = 0
    for char in str(number):
        acc+= factorial(int(char))
    return acc

#naive solution:
"""
answer = 0
for num in range(1000000):
    chain = [num]
    next = fact_dig_sum(num)
    while next not in chain:
        chain.append(next)
        next = fact_dig_sum(next)
    if len(chain) == 60:
        answer+=1

print("The answer is", answer)
"""

#slightly faster:

max = 1000000
array = [0] * max # we initialize the first million numbers and how long their chain is
acc = 0


for num in range(max):
    if array[num] == 0: #checking that we haven't seen this number before
        chain = [num]
        next = fact_dig_sum(num)
        flag = True
        while flag:
            if next < max and array[next] != 0:
                l = len(chain)
                for i in range(l):
                    if chain[i] < max:
                        array[chain[i]] = array[next] + l - i
                break
            elif next in chain:
                ind = chain.index(next)
                l = len(chain) 
                loop_length = l-ind 
                for i in range(l):
                    if i < ind and chain[i]<max:
                        array[chain[i]] = loop_length + ind - i
                    elif chain[i] < max:
                        array[chain[i]] = loop_length
                break
                       
            chain.append(next)
            next = fact_dig_sum(next)
        if array[chain[0]] == 60:
            acc += 1

print("The answer is", acc)
