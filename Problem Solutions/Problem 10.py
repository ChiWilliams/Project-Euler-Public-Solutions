#Problem 10

#We update the Sieve we used to solve problem 7

prime_list = [2]
sum = 2
i = 3
num = 2e6

marked = [0] * 2000000
value = 3
s = 2
while value < 2000000:
    if marked[value] == 0:
        s += value
        i = value
        while i < 2000000:
            marked[i] = 1
            i += value
    value += 2
print(s)

"""
while i < num:
    flag = True
    j = 0
    while j<len(prime_list) and prime_list[j] < i**0.5+1:
        if i % prime_list[j] == 0:
            flag = False
        j+=1
    if flag:
        prime_list.append(i)
        sum += i
    i += 2

print("The answer is", sum)
"""