#Problem 7: find the 10001'st prime
#We use the seive of eranthosenes, which will be in O(n^2) time. There may be faster approach

prime_list = [2]
i = 3
num = 10001

while len(prime_list) < num:
    if 0 not in [i % prime for prime in prime_list]:
        prime_list.append(i)
    i += 2

print("The answer is", prime_list[num-1])