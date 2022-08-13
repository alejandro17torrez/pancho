"""
Radar de Velocidad
"""

# Calculo de la Velocidad del Radar

f0= 2e-10 

f1= 2.0000004e-10  

# escribir variable para obtener la respuesta de la formula
speed = (6.685 * 10**8) * (f1 - f0) / (f1 + f0)

 #Imprimir resultado en pantalla

print(f"Respuesta: {speed}")