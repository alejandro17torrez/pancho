# Solicitud de datos
numero  = int(input('>>>Introduce el numero: '))

for potencia in range(1,11):
    resultado = numero ** potencia
    print("%d x %2d = %d" % (numero,potencia,resultado))