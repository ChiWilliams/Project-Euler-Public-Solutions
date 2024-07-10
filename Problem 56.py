#Problem 56
#Maximum digit sum for a^b for pairs a and b

#We try a naive method: try each of the 10000 pairs, calculate their sum, and return the maximum

answer = 1
for a in range(1,100):
    for b in range(1,100):
        dig_sum = sum(int(x) for x in str(a**b))
        if dig_sum > answer:
            answer = dig_sum

print("The answer is", answer)