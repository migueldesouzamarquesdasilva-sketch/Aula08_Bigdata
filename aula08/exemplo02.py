produtos = []

for i in range(3):
    produto = input('\nInforme o nome do produto: ')
    produtos.append(produto) # Adiciona na lista produtos

print(produtos)

# Acesso ao elemento
n = int(input('\nDigite a posição do elemento a acessar: '))
print(produtos[n-1]) # 1

# Alterando uma lista "nome de um elemento"
produtos[n-1] = input(f'\nInforme o novo nome do produto {n}: ') # 2
print(produtos)

# Remover da lista
produto_a_remover = input('\nDigite o nome do produto a remover: ')

if produto_a_remover in produtos:
    produtos.remove(produto_a_remover)
print(produtos)

#Pesquisar métodos insert["inserir"], pop(2)["apaga"], clear["apaga toda a lista"]


