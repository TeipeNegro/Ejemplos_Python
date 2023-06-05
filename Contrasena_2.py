contraseña="sulca"
 
for i in range(3):
    usuario= input("Dame tu nombre de usuario: ")
    contraseña=input("Indica la contraseña para acceder: ")
    if usuario== "diego" and contraseña == "sulca":
        break
 
if usuario== "diego" and contraseña == "sulca":
    print("Felcidades es la contraseña correcta")
else:
    print("Lo sentimos, no acertaste.")