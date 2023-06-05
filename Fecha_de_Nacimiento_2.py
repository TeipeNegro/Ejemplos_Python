#No Funciona

from datetime import date

def calcular_edad_anos(fecha_nacimiento):
    fecha_actual = date.today()
    resultado = fecha_actual.year - fecha_nacimiento.year
    resultado -= ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return resultado

fecha_nacimiento_usuario = date()
date = input("Porfavor, Ingrese su fecha de Nacimiento (año, mes, dia): ")
edad = calcular_edad_anos(fecha_nacimiento_usuario)

print(f"Su Edad es de {edad} años")