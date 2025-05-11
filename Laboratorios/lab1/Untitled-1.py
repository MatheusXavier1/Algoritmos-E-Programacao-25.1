def retorna_divisores(n):
    return {i for i in range(1, n + 1) if n % i == 0}

def retorna_intersecao(numeros):
    # Pega o conjunto de divisores do primeiro número
    intersecao = retorna_divisores(numeros[0])
    
    # Faz a interseção com os demais
    for num in numeros[1:]:
        intersecao &= retorna_divisores(num)
    
    return intersecao

# Exemplo de uso:
entrada = eval(input("Digite uma tupla de números inteiros positivos: "))
print(retorna_intersecao(entrada))
