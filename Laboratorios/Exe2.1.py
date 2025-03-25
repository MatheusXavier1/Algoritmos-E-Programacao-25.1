# Implementar o produto interno de dois vetores.

# Ler dois vetores.  (coordenadas são inteiras)

# Imprimir o resultado do produto interno. (inteiro)

# Exemplos:

# Input: [2] [3] Output: 6

# Input: [2,3] [2,3] Output: 13

# Input: [1,1,1,1] [2,2,2,2] Output: 8
# Obs: Faça duas leituras, uma para cada vetor

def ProdutoInterno(vetor1, vetor2):
    somaProdutoInterno = 0
    for i in range(len(vetor1)):
        somaProdutoInterno += vetor1[i] * vetor2[i]
    return somaProdutoInterno

v1 = []
v2 = []

sizeV1 = int(input())
sizeV2 = int(input())

for i in range(sizeV1):
    v1.append(int(input()))
    
for j in range(sizeV2):
    v2.append(int(input()))

print(ProdutoInterno(v1,v2))