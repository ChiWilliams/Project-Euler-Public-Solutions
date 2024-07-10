#Problem 6

#This is quite straightforward:

def sum_square(n):
    return n**2 * (n+1)**2 / 4 #Use formula for arithmetic sequence and square it
def squared_sum(n):
    return (2*n+1)*(n+1)*(n) / 6 #Use formula for sum of squares

print("The answer is", sum_square(100) - squared_sum (100))