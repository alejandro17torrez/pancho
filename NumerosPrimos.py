# Solicitud de datos
limite = int(input('>>> Dame un mumero: '))
 
for numero in range(1, limite + 1):
    creo_que_es_primo = True
    for divisor in range(2,numero):
        if numero % divisor == 0:
            creo_que_es_primo = False
            break
 
    if creo_que_es_primo: