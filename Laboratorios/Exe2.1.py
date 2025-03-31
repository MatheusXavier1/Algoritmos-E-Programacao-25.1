# Implementar o produto interno de dois vetores.

# Ler dois vetores.  (coordenadas são inteiras)

# Imprimir o resultado do produto interno. (inteiro)

# Exemplos:

# Input: [2] [3] Output: 6

# Input: [2,3] [2,3] Output: 13

# Input: [1,1,1,1] [2,2,2,2] Output: 8
# Obs: Faça duas leituras, uma para cada vetor


v1 = eval(input())
v2 = eval(input())

pi = 0
for i in range(len(v1)):
	pi += v1[i] * v2[i]
print(v1)
