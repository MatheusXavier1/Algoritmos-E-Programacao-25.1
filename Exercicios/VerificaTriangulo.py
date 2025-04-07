def VerificaTriangulo(tamanhoDosLados):
    ladosUnicos = len(set(tamanhoDosLados))

    if ladosUnicos == 1:
        return "equilatero"
    elif ladosUnicos == 2:
        return "isosceles"
    else:
        return "escaleno"
    
a = eval(input())
b = eval(input())
c = eval(input())

print(VerificaTriangulo(a))
print(VerificaTriangulo(b))
print(VerificaTriangulo(c))
