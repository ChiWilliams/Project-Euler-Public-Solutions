#Problem 14

#Here we will use mostly a brute force solution, but will pay attention to if it works

collatz_dict = {1:1}

#We collatz calculate without keeping anything in our 

def collatz_chain_calculator(n,dict):
    if n in dict:
        pass
    else:
        if n % 2 == 0:
            dict[n] = collatz_chain_calculator(n//2,dict) + 1
        else:
            dict[n] = collatz_chain_calculator((3*n+1)//2,dict) + 2 #We do two collatz steps at once to save time
    return dict[n]

collatz_array = [0] * int(1e6+1)
max_val = 0
max_i = 1
for i in range(1,int(1e6+1)):
    collatz_array[i] = collatz_chain_calculator(i,collatz_dict)
    if collatz_array[i] > max_val:
        max_i = i
        max_val = collatz_array[i]

print("The maximum starting value is", max_i)







# print("The max starting number is", max_index,"with a chain of length",max_length)