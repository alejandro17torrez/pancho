# Declaración de variables

a = 0
b = 0
x = 0

# Recolección de datos

a = float(input("a: "))
b = float(input("b: "))

x = -b/a
print(f"Solución x: {x}")
if b != 0:
    print("La ecuación no tiene solución")
else:
    print("La ecuación tiene infinitas soluciones")
