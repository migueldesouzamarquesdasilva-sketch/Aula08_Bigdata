vendas = []

for i in range(10):
    venda = float(input('Infome as vendas: '))
    vendas.append(venda)

total_vendido = sum(vendas)

print(f'Você vendeu: {vendas}')
print(f'O total da soma foi de: R${total_vendido}') 
    