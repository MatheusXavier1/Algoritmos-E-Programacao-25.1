def f_lazy_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Entrada de n
n = int(input())

# Loop para imprimir os primeiros n números da sequência de Fibonacci
for i, x in enumerate(f_lazy_fibonacci()):
    if i >= n:
        break
    print(x, end=' ')
