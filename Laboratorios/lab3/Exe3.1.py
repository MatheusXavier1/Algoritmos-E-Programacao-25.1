# Decidir se um vetor A[1 .. k] é uma subsequência de um vetor B[1 .. n]. 
# (Por exemplo, (5, 6, 4) é subsequência de (9, 5, 6, 3, 9, 6, 4, 7).).

# obs: fazer duas leituras, uma para cada vetor e retornar um booleano (True ou False).

# Ex:

# Input: [33, 9, 0] 

# [1, 3, 5, 7, 'a', 'aba']

#  Output: False

v1 = eval(input())
v2 = eval(input())

j,flag  = 0,0

for elemento in v1:
	while j<len(v2):
		#print(f"v1:{elemento}, v2:{v2[j]}")
		if elemento == v2[j]:
			flag+=1
			break
		j+=1
print(flag == len(v1))
