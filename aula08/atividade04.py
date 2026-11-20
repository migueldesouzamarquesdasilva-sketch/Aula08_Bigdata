numeros = []

for i in range(15):
    numero = int(input('Informe os números: '))
    numeros.append(numero)


ordenada = sorted(numeros)

print(f'Lista Ordenada: {ordenada}')

numero = set(numeros)
numeros = list(numero)
print(len(numero))
print(numero)