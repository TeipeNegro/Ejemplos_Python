print("Tienes 3 intentos para escribir los datos correctos")
contador = 0
while contador < 3:
    contraseña = input("Digite la contraseña: ")
    if contraseña == "avion1234":
        print("Contraseña correcta")
        contador = 4
    else:
        print("Contraseña incorrecta")
        contador += 1
        if contador == 3:
            print("Has alcanzado el límite permitido de intentos, por favor comuníquese con el administrador del programa")