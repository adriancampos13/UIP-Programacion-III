#Adrian Campos
#Victor Vargas

x=0
max=0
min=9999999999999
total=0
ventas={}
a=int(input("Cuantos vendedores introducira? "))
while x<a:
    v=input("Introdusca nombre: ")
    v2=float(input("Introduzca venta mensual: "))
    ventas[v]=v2
    x=x+1

for b in  ventas:
    if ventas[b]>max:
        max=ventas[b]
    total=total+ventas[b]

for c in ventas:
    if ventas[c]<min:
        min=ventas[c]

for d in ventas:
    if ventas[d]==max:
        print("\nEl vendedor que mas vendio fue", d,"con", ventas[d])

for e in ventas:
    if ventas[e]==min:
        print("El vendedor que menos vendio fue",e,"con", ventas[e])

print("El total de ventas fue:",total)
if total>=1000000:
    print ("La meta mensual fue superada")
else:
    print("La meta mensual no fue superada")