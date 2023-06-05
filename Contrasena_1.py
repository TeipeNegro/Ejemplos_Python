contrasena="casa"
 
for i in range(3):
    entrada=input("Indica la contraseña para acceder: ")
    if entrada==contrasena:
        break
 
if entrada==contrasena:
    print("Bienvenido al Curso de Informática I")
else:
    print("Lo sentimos, no acertaste.")