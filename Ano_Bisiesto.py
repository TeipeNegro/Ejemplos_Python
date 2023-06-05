ano = int(input("Porfavor, Ingrese un año: "))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("El año", ano, "es Bisiesto")
else: print("El año ", ano, "no es Bisiesto")