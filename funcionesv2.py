print("mas sobre funciones")
def suma_ab(a,b):
    s=a+b 
    return s 
def resta(a,b):
    r=a-b 
    return r
def div(a,b):
    su=a/b 
    return su
def multi(a,b):
    ressu=a*b
    return ressu

print("calculando suma...")
n1=int(input("ingresa el primer numero"))
n2=int(input("ingresa el segundo numero"))
suma=suma_ab(n1,n2)
print(f"la suma de {n1} y {n2} es {suma}")

print("calculando resta...")
n3=int(input("ingresa el primer numero"))
n4=int(input("ingresa el segundo numero"))
rest=resta(n3,n4)
print(f"la resta de {n3} y {n4} es {rest}")

print("calculando división...")
n5=int(input("ingresa el primer numero"))
n6=int(input("ingresa el segundo numero"))
divs=div(n5,n6)
print(f"la división de {n5} y {n6} es {divs}")

print("calculando multiplicación...")
n7=int(input("ingresa el primer numero"))
n8=int(input("ingresa el segundo numero"))
mut=multi(n7,n8)
print(f"la división de {n7} y {n8} es {mut}")


