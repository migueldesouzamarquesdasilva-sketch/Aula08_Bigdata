numeros = []

for i in range(12):
    numero = int(input('Informe os números: '))
    numeros.append(numero)


ordenada = sorted(numeros)

print(f'Lista Ordenada: {ordenada}')
