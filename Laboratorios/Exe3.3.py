# Faça duas funções: uma codificar uma mensagem e outra para descodificar uma mensagem.
# Deve receber uma mensagem (string), essa mensagem só tem as letras padrões e espaço (não tem acento, símbolo, maiúscula e número). A ordem deste alfabeto começa com "a" e termina com espaço, ou seja espaço fica depois da letra "z".
# Além da mensagem, receba um número que é a senha para codificar ou descodificar a mensagem.
# Para codificar, cada letra deve ser movida pelo alfabeto o número de letras. Exemplo: letra "a" e senha 1 retorna "b";  letra "a" e senha 3 retorna "d"; letra "b" e senha 2 retorna "d".
# Exemplo de codificação: "abc", senha 1, retorna "bcd".
# Para descodificar o processo é inverso. A mensagem recebida já está codificada e a senha serve para reconstruir a mensagem original. Exemplo: "bcd", senha 1, retorna "abc".
# Se a operação de shift passa o final do alfabeto, deve retorna para o início do alfabeto. Exemplo: codificar "xyz", senha 5, retorna "bcd". descodificar "a" senha 5 retorna "w".
# Leia uma tupla (x, m, s):
# x: booleano (True, False) - True se é para codificar a mensagem m e False para descodificar a mensagem m.
# m: String - mensagem
# s: inteiro - senha usada para codificar ou descodificar.
# Input: (True, "abc", 1)

# Output: "bcd"

# Input: (False, "bcd", 1)

# Output: "abc"

# Input: (True, "xyz", 5)

# Output: "bcd"

# Input: (False, "bcd", 5)

# Output: "xyz"

alfa = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ')

# def codec(operation,pssw,num):

pssw = "abc"
num = 3
psswList = list(pssw)
size = len(pssw)
for i in range(size):
    psswList[i] = psswList[i+num]

output = str(psswList)
print(output)