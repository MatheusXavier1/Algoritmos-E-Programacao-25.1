# Faça um algoritmo que receba dois vetores A[1 .. n] e B[1 .. m] e decida se existe um índice i tal que A[i] = B[i].
# obs: fazer duas leituras, uma para cada vetor e retornar um booleano (True ou False).

# Ex:

# Input: [1, 3, 5, 7, 'a', 'aba']

# [33, 9, 0]

#  Output: False

a = eval(input())
b = eval(input())

flag = 0

for i in range(len(a)):
    if a[i] == b[i]:
        print(True)
    else:
        print(False)