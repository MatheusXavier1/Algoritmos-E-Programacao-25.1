v1 = eval(input())
v2 = eval(input())

pi = 0

for i in range(len(v1)):
	pi += v1[i]*v2[i]
print(pi)
