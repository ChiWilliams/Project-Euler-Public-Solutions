#Problem 40 -- Chaperowne

#I ended up calculating this on paper, but I don't have a clean solution to share
#Essentially the main idea is that you can break things up and calculate by paper

answer = 1*1*5*3*7*2*1
print("The answer is",answer)

#Alternatively (from another poster)
s = ""
l = len(s)
x,next,prev,sum = 1,1,0,1
while l < 1000000:
	s = str(x);
	l += len( str(x) )
	if l >= next:
		sum *= int( s[next - prev - 1 ])
		next = next*10
	prev = l	
	x += 1
print(sum)