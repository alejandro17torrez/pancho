"""
Calculadora Freelancer
"""

# Solicitud de Datos
DOLARES_POR_HORA = 20

# Obtener el calculo de pagos por hora

horas_semanal = float(input("Semanal: "))

horas_mensual = float(input("Mensual: "))

# escribir variable para obtener la respuesta de la formula
pago_semanal =  DOLARES_POR_HORA * horas_semanal
pago_mensuales =  DOLARES_POR_HORA * horas_mensual

# Imprimir resultado en pantalla

print(f"""
        pagos semanales : {pago_semanal}
        pagos mensuales : {pago_mensuales}
    """)