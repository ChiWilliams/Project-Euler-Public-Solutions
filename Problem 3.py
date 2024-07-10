#Problem 3

#Basic approach: just keep dividing out small primes until you reach a prime
#That will be the largest prime divisor


#This function finds the smallest non-1 number that divides the number
#Thus, it will return a prime number
#If the number in question is prime, it will return that number
def find_smallest_divisor(num):
    i = 2
    flag = True
    while i<=num**0.5+1: #we give a fudge in case of floating errors
        if num % i == 0:
            return i
        i += 1
    return num

#We recursively divide out by the smallest prime divisor remaining
#When we reach a prime number, we know that this will be the largest prime divisor
def find_largest_prime(num):
    divisor = find_smallest_divisor(num)
    if divisor == num:
        return num
    else:
        print(divisor)
        return find_largest_prime(num/divisor)

num = 600851475143
#num = 2**64
#print(sqrt(2**25))
# num = 2*3*7*11*101
# num = 5*7*13*29


print("The largest prime divisor is",find_largest_prime(num))