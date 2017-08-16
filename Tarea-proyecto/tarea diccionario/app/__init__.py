# Haga un programa que lea las ventas mensuales de todos los vendedores de la compañia ABC,
# Muestre las Ventas totales,
# El vendedor que mas vendio y el que menos vendio.
# Finalmente si ABC, paso la meta mensual, que es 1,000,000

def imprimir_diccionario(w):
    print("\nVENTAS")
    for art, cant in w.items():
        print("Venta: " + str(art)) #+ "(cantidad: " + str(cant) + ")")

if __name__ == '__main__':
    diccionario = {}

    while True:
        print('Compañia ABC')

        print('VENTAS')
        print('1. agregar venta')
        print('2. Suma de ventas')
        print('3. ver lista de ventas')
        print('4. salir')
        try:
            opc = int(input("OPCION:"))
        except ValueError:
            opc = 0

        if  opc == 1:
            print("\nIngresar venta")
            artInsertar = int(input("Venta"))

            if artInsertar not in diccionario:

                 diccionario[artInsertar] = 1
            else:
                 diccionario[artInsertar] += 1

        elif opc == 2:
            menor = 99999999999999999999
            mayor = 0
            print("\nSuma de ventas")
            s = sum(diccionario.keys())
            print(s)

            if s > 1000:

                print("La compañia paso la meta mensual")
            else:

                print("\nLa compañia no paso la menta")

        elif opc == 3:

            imprimir_diccionario(diccionario)

        elif opc == 4:

           break
        else:
            print("ERROR::Opcion no valida")
    print("Hasta luego")
    if __name__ == "__main__":
        app.run()