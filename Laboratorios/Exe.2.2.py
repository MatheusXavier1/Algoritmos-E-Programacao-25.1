# Faça um algoritmo que receba dois vetores A[1 .. n] e B[1 .. m] e decida se existe um índice i tal que A[i] = B[i].
# obs: fazer duas leituras, uma para cada vetor e retornar um booleano (True ou False).

# Ex:

# Input: [1, 3, 5, 7, 'a', 'aba']

# [33, 9, 0]

#  Output: False

def TemIguais(lista1, lista2):
    flagTemIgual = 0
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                flagTemIgual += 1
    if flagTemIgual > 0:
        return True
    else:
        return False
    
l1 = [1, 3, " ", 7, 'a', 'aba1']
l2 = [33, 9, 0, "oi "] 

print(TemIguais(l1, l2))