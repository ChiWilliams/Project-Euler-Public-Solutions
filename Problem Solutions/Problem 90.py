#Problem 90

squares = [(0,1),(0,4),(0,9),(1,6),(2,5),(3,6),(4,9),(6,4),(8,1)]

#This function checks whether a given square number can be made by two cubes
def makeable_num(set1, set2, square):
    num1, num2 = square[0], square[1] #split the square into digit
    return (num1 in set1 and num2 in set2) or (num2 in set1 and num1 in set2)

#This function checks through the entire set of squares whether a number works
def valid_cube_pair(set1,set2,squares): 
    six_nine = set([6,9]) 
    if set1.intersection(six_nine): #we check if set1 has a 6 or a 9
        set1 = set1.union(six_nine) # if it has one, we make sure it has both
    if set2.intersection(six_nine): #ditto for set2
        set2 = set2.union(six_nine)
    result = True
    for square in squares:
        if not makeable_num(set1,set2,square):
            result = False
            break
    return result

#we now need to iterate over all combinations
#We use a recursive way to list out all ordered combinations of length 6
digits = list(range(10))


def list_ordered_subets(digits):
    def recur_helper(active,pool,results):
        if len(active) == 6:
            results.append(active)
            return
        if len(pool) ==0:
            return
        next = pool[-1]
        recur_helper(active[:], pool[:-1], results)
        recur_helper(active + [next], pool[:-1], results)

    results = []
    recur_helper([], digits, results)
    return results

cube_combos = list_ordered_subets(digits)
length = len(cube_combos)

acc = 0
for i in range(length):
    for j in range(i, length):
        acc += int(valid_cube_pair(set(cube_combos[i]),set(cube_combos[j]),squares))

print("The answer is", acc)