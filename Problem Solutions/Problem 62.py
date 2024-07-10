#Problem 62

#We are seeking to find the smallest cube so that exactly five of its permutations are cube
#We will go increasing by cubes, breaking down each digit

dict = {}

i = 1
flag = True
curr_cube_len = 1
candidates = []
answer = 0
num_permutations = 5

while flag:
    cube = str(i**3)

    #first, check if we have completed all cubes up to a certain digit length
    if len(cube) > curr_cube_len:
        if candidates:
            answer = min(candidates)
            flag = False
        curr_cube_len += 1
    #we create an array recording how often each digit shows up
    digit_array = [0]*10
    for char in cube:
        digit_array[int(char)] += 1
    digits = tuple(digit_array) #convert to tuple for the hash

    #We now keep track how much each digit combination shows up
    if digits in dict:
        dict[digits][0] += 1
        if dict[digits][0] == num_permutations:
            candidates.append(dict[digits][1]**3)
        if dict[digits][0] == num_permutations+1:
            candidates.remove(dict[digits][1]**3)
    else:
        dict[digits] = [1,i]

    #increment the while loop
    i+=1

print("The answer is", answer)
