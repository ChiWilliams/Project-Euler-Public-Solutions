#Problem 50 -- Consecutive prime sum

#This is a dumb brute force: we will just find all the primes and then check

import time
start_time = time.time()

#This is the upper limit for testing
up_lim = 1000000

#We first find all of the primes under up_lim
seive_array = [0]*up_lim
i = 2 #minimum prime

#This is a sieve
while i<up_lim:
    s = i
    while s<up_lim:
        seive_array[s] += 1
        s += i
    i+=1

prime_list = []
for i in range(up_lim):
    if seive_array[i] ==1: #i.e. it's only factor is itself
        prime_list.append(i)


max_prime = 1
max_length = 1
for i in range(min(5000,len(prime_list)-1)):
    i_length = 0
    cur_sum = prime_list[i]
    i_prime = cur_sum
    length = 1
    while cur_sum<up_lim:
        if seive_array[cur_sum] ==1:
            i_length = length
            i_prime = cur_sum
        try:
            cur_sum += prime_list[i+length]
        except:
            raise Exception("List index out of range, i=",i,"length=",length)
        length += 1 
    if i_length > max_length:
        max_length = i_length
        max_prime = i_prime
        
print("The answer is", max_prime,"with",max_length,"divisors.")

"""
max_length = 1
max_prime = 1
while i < 1000:
    cur_sum = i
    length = 1
    while cur_sum<i:
        if seive_array[cur_sum] == 1 and length>max_length:
            max_length = length
            max_prime = cur_sum
        s += 1
        length += 1
        cur_sum += 1
"""

        

print("Done!")
print("--- %s seconds ---" % (time.time() - start_time))