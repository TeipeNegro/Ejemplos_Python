numeroDeIntentos = 3
valida = False
for i in range(numeroDeIntentos):
    contraseña1 = input("Ingrese de favor su contraseña: ")
    if contraseña1[0].isdigit():
        contraseña2 = input("Repita su contraseña: ")
        if contraseña1 == contraseña2:
            print("Gracias, bienvenido")
            valida = True
            break
        else:
            print('Incorrecto.  %d intentos restantes' % (numeroDeIntentos-i-1))