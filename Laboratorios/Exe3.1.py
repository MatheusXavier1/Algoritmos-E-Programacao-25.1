# Decidir se um vetor A[1 .. k] é uma subsequência de um vetor B[1 .. n]. 
# (Por exemplo, (5, 6, 4) é subsequência de (9, 5, 6, 3, 9, 6, 4, 7).).

# obs: fazer duas leituras, uma para cada vetor e retornar um booleano (True ou False).

# Ex:

# Input: [33, 9, 0] 

# [1, 3, 5, 7, 'a', 'aba']

#  Output: False

def SubSequencia(v1, v2):
    flag = 0
    for i in range(len(v1)):
        for j in range(len(v2)):
            if v1[i] == v2[j]:
                flag+=1
    return flag == len(v1)

v1 = [5,6,4]
v2 = [9,5,6,3,9,6,4,7]

print(SubSequencia(v1,v2))