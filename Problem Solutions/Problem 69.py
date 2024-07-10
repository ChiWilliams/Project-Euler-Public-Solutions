#Problem 69
#Find the Totient Maximum

#Note that if p divides n, then phi(p*n) = p*phi(n), so the ratio remains the same
#Hence, our greatest value will be 2*3*5*7*... until it is less than 1000000

#To be lazy, we will find the first 100 primes, and multiply them together until they reach 1e6

prime_list = [2]
i = 3
num = 100

while len(prime_list) < num:
    if 0 not in [i % prime for prime in prime_list]:
        prime_list.append(i)
    i += 2

product = 1
answer = 1
i = 0
while product<1e6:
    answer = product
    product *= prime_list[i]
    i+=1

print("The answer is", answer)
