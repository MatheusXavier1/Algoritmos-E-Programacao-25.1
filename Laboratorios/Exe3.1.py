# Decidir se um vetor A[1 .. k] é uma subsequência de um vetor B[1 .. n]. 
# (Por exemplo, (5, 6, 4) é subsequência de (9, 5, 6, 3, 9, 6, 4, 7).).

# obs: fazer duas leituras, uma para cada vetor e retornar um booleano (True ou False).

# Ex:

# Input: [33, 9, 0] 

# [1, 3, 5, 7, 'a', 'aba']

#  Output: False



v1 = [33,9,0]
v2 = [1, 3, 5, 7, 'a', 'aba',33,'cachorro',9,'brazil lixo',0]

flag = 0
for elementos in v1:
    for i in range(len(v2)):
        if elementos == v2[i]:
            ultimo = v2[i]
            flag+=1
print(len(v1) <= flag or len(v2) <= flag)