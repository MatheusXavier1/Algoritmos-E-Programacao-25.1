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

<<<<<<< Updated upstream:Laboratorios/lab3/Exe3.1.py
for elemento in v1:
	while j<len(v2):
		#print(f"v1:{elemento}, v2:{v2[j]}")
		if elemento == v2[j]:
			flag+=1
			break
		j+=1
print(flag == len(v1))
=======
v1 = eval(input())
v2 = eval(input())  
flag = 0

j = 0

for i in v1:
    while j<len(v2):
        print(j)
        if i != v2[j]:
            # print(f"i: {i}, v2: {v2[j]}")
            # print(f"flag: {flag}")
            j+=1
        if i == v2[j]:
            # print(f"i: {i}, v2: {v2[j]}")
            flag+=1
            j+=1
            # print(f"flag: {flag}")
            break
print(flag == len(v1))


# for elementos in v1:
#     for i in range(len(v2)):
#         if elementos == v2[i]:
#             ultimo = v2[i]
#             flag+=1
# print(len(v1) <= flag or len(v2) <= flag)clear
>>>>>>> Stashed changes:Laboratorios/Exe3.1.py
