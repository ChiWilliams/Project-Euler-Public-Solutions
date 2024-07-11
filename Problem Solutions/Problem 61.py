#Problem 61

#The goal is to find the sum of six cyclic figurate numbers

#We first calculate all of the triangular, square, etc. numbers and add them to a list of all the nums
#with the same first two digits


def shape(i,s):
    #first, calculate the i-th "s"-gonal number:
    # s = num sides, i = num of dots
    return i*((s-2)*i-(s-4)) //2


shapes = [[] for _ in range(6)]
shape_dict = {}
s = 3
for s in range(3,9):
    i = 1
    while True:
        num = shape(i,s)
        if num>= 10000:
            break
        if num>= 1000:
            shapes[s-3].append(num)
            key = (num//100,s)
            if key not in shape_dict:
                shape_dict[key] = []
            shape_dict[key].append(num)
        i+=1

def dfs(shape_dict, num, start,s,array,is_cyclic,s_candidates):
    #Depth first search to find cyclic figurate numbers.
    if s==3 and is_cyclic:
        if num == start:
            print("The answer is", sum(array))
            return
    else:
        array.append(num)

        
        if not s_candidates:
            next_s = 3
            key = (num%100,next_s)
            if key in shape_dict:
                for next_num in shape_dict.get(key):
                    dfs(shape_dict,next_num,start,next_s,array[:],True,[])
        else:
            for next_s in s_candidates:
                s_cands_next = s_candidates[:]
                s_cands_next.remove(next_s)
                key = (num % 100, next_s)
                if key in shape_dict:
                    for next_num in shape_dict[key]:
                        dfs(shape_dict,next_num,start,next_s,array[:],True,s_cands_next)

#DFS_recurse(shape_dict,8128,8128,3,[],False,[i for i in range(4,6)])

for i in shapes[0]:
    dfs(shape_dict,i,i,3,[],False,[i for i in range(4,9)])



    