# Solicitud de Datos

real_madrid = float(input('Introduce las copas del real madrid: '))
barcelona = float(input('Introduce las copas del barcelona: '))
maximo = " "

if real_madrid > barcelona:
    maximo = "real madrid"
else : 
    maximo = "barcelona"
 
print(f'El equipo con mas copas es {maximo}')