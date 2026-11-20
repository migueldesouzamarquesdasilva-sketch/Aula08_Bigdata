listas = []

while True:
    numeros = int(input('Digite um número: '))
    listas.append(numeros)

    quantidade = len(listas)

   
    resposta = input('Quer continuar [S/N]: ').upper()
    if resposta == 'N':
        break
print(f'Total de elementos: {quantidade}')
print(f'a lista é {listas}')
    









