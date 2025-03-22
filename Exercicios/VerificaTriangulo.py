def VerificaTriangulo(tamanhoDosLados):
    ladosUnicos = len(set(tamanhoDosLados))

    if ladosUnicos == 1:
        return "equilatero"
    elif ladosUnicos == 2:
        return "isosceles"
    else:
        return "escaleno"
    
a = [10,20,10]
b = [10,10,20]
c = [10,20,30]


print(VerificaTriangulo(a))
print(VerificaTriangulo(b))
print(VerificaTriangulo(c))