# Declaracion de Variables
Letra = ''

#Solicitud de Datos

Letra = input('>>>Introduce Una Letra : ')

if Letra <= "z" and Letra >= 'a' : # a-z (97-122)
    print ('La Letra es minuscula')

elif letra <= 'Z' and letra >= 'A':  # A-Z (65-90)
    print('La letra es Mayuscula.')
else:
    print('El valor introducido no es una letra.')
