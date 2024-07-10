#Problem51

#We are looking for the first number so that a*b**c is prime 8 out of 10 times. 
#We know that we must have three (or a multiple of three asterisks) because otherwise, there will be 
#at least three multiples of three, which means its impossible

#We first find the primes below 1000000
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

#Our second function is to create the number a*b**c
#a, b, and c represent the fixed digits
#pos_1, pos_2, and pos_3 represent the position of the fixed digits
#we will index by powers of 10 by the power of 10
def num_list(a,b,c,pos_1,pos_2,pos_3):
    if pos_1 == pos_2 or pos_1 == pos_3 or pos_2 == pos_3:
        print(a,b,c,pos_1,pos_2,pos_3)
        raise ValueError("Positions must be distinct")
    #We want to find the other positions
    other_pos = list(set([0,1,2,3,4,5]) - set([pos_1,pos_2,pos_3]))
    pos = [pos_3,pos_2,pos_1]
    base = a*(10**pos[2]) + b*(10**pos[1]) + c*(10**pos[0])
    increment = 10**other_pos[0] + 10**other_pos[1] + 10**other_pos[2]
    return_list = []
    if base>=100000:
        return_list.append(base)
    for i in range(1,10):
        return_list.append(base+increment*i)
    return return_list

#We now need to increment through all possible lists, and stop when we have found the smallest value

list_of_families = []

for a in range(10):
    for b in range(10):
        for c in [1,3,7,9]:
            for pos_1 in range(2,5):
                for pos_2 in range(1,pos_1):
                    family = num_list(a,b,c,pos_1,pos_2,0)
                    if sum([1 for num in family if seive_array[num] == 1]) == 8:
                        list_of_families.append(family[0])


print("The answer is", min(list_of_families))