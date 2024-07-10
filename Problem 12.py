#Problem 12

#We need to find the first triangle number with at least 500 divisors
#We note that we can do this by finding number of divisors of n/2 and n-1 and then multiplying them 
#together. We note that to get at least fifty divisors, we only needed to get to 5000.
#Thus, we can try multiplying up to 10000 to see if anything works

#We will use a sieve to develop

upperlim = 100000
array = [0]*upperlim
divisor = 1

while divisor<upperlim:
    increment = divisor
    while increment<upperlim:
        array[increment] += 1
        increment += divisor
    divisor += 1

print("done")

num_divisors = 1
i = 1
answer = 0
for i in range(upperlim//2):
    if array[i]*array[(2*i-1)] > 500:
        answer = (i*(2*i-1))
        break
    if array[i]*array[2*i+1]>500:
        answer = (i*(2*i+1))
        break

print("The answer is", answer)


    
