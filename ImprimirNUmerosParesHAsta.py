# Solicitud de Datos
numero = int(input('>>> Introduce un numero: '))
 
for item in range(0,numero + 1):
    if item == int(item/2)*2 and item>0:
        print(item)    