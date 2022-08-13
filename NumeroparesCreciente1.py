print('Imprimir los numeros pares entre 0 y 200 de forma Creciente')
 
for pares in range(0,201):
    if pares == int(pares/2)*2 and pares>0:
        print(pares)