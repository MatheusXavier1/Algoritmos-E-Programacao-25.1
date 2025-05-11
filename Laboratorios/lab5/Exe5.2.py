# Faça uma função que retorna um conjunto (set) com todos os divisores de um número inteiro positivo.

# Faça uma segunda função que recebe os dois ou mais números inteiros positivos.
# Chame a primeira função para um dos números obtendo os conjuntos de seus divisores.
# Calcule e retorne a interseção desses conjuntos, ou seja, os divisores comum desses números.
# Entrada uma tupla com os números.
# Saída um conjunto com os divisores comuns.

def RetornaDivisores(input):
    output = set()
    for i in range(input+1):
        if i != 0:
            if input % i == 0: 
                output.add(i)
    return output

def RetornaIntersecao(input):
    output = RetornaDivisores(input[0])

    for num in input[1:]:
        output &= RetornaDivisores(num)
    return output

input = eval(input())

print(RetornaIntersecao(input)) 
