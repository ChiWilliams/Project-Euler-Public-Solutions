# Problem 2

#First, we compute the fibonnaci numbers:
sum = 0 
limit = 4000000
fib_frame = [0,1]
index = 2

while (fib_frame[0]+fib_frame[1]) < limit:
    fib_frame =  [fib_frame[1],fib_frame[0]+fib_frame[1]]
    if index % 3 == 0:
        sum+=fib_frame[1]
    index += 1

print("The answer is",sum)

#Another way is to compute the recursion relation directly for even terms
#We have our sequence is 0, 2, 8, 34, 144
#The recursion relation is a_n = 4a_(n-1) + a_(n-2)

sum = 2
even_fib_frame = [0,2]
even_recurse = lambda a,b: a+4*b 
next_el = 8

while next_el < limit:
    even_fib_frame = [even_fib_frame[1],next_el]
    sum += next_el
    next_el = even_recurse(*even_fib_frame)

print(sum)

