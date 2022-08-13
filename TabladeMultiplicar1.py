# Solicitud de datos
numero  = int(input('>>>Introduce el numero: '))

for multiplicador in range(1,11):
    resultado = numero * multiplicador
    print("%d x %2d = %d" % (numero,multiplicador,resultado))