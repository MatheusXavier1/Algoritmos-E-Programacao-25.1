Idades = []

for i in range(3):
    idade = int(input())
    while idade < 5 or idade > 100:
        idade = int(input("Entre um valor 5<=N<=100!\n"))
    Idades.append(idade)

Idades.sort()

print("="*10)
print(Idades[1])