valor = { 'nome': 'gio', 'idade': 17, 'altura': 1.65 }

print(valor)
print(valor['idade'])

#adicionar elemento em dicionarios

valor['altura'] = input("Digite sua altura: ")
# sobreescreve o outro elemento

print(valor)

#imprimindo a chave e o valor com for

for i in valor:
    print(i, valor[i])

#saber se o elemento existe no dicionario

print('peso' in valor)

# retorna falso pois ele não existe no dicionario