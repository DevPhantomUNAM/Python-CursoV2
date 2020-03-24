# Excepciones en flujo de ejecución de un programa Python.

try:
    numero = int(input('Escriba un número entero: '))

    print('Contenido de la variable `numero`:', numero)
    print('El tipo de dato de la variable `numero` es:', type(numero))
except ValueError as e:
    print('ERROR: ', e)

print()
print('El programa ha terminado')