"""
Edad de dos personas
"""

# La mayor de dos personas

# Solicitud de Datos
primera_persona = int(input('>>> Edad de la primera persona: '))
segunda_persona = int(input('>>> Edad de la segunda persona: '))

if primera_persona == segunda_persona:
    print('- Ambos tienen la misma edad')
elif  primera_persona > segunda_persona:
    print('- La primera persona es mayor!')
else:
    print('- La segunda persona es mayor!')
