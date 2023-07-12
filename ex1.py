# append : adiciona na lista. Não funcionando em tupples
lista = [1, 3, 45, 67]

numero = int(input("Digite: "))

lista.append(numero)
print(lista)

# insert : adiciona elemento mas a diferença é que você pode escolher a posição do elemento que você quer add

lista.insert(2, numero)
# 2 é a posição  e o outro o elemento

print(lista)

# extend serve p juntar duas lista

lista2 = [10,20,50]

lista.extend(lista2)
# lista ne  e aqui junta as mana

print("Depois do extend", lista)

# pop = remover elemento da posição e se não especificar ele remove o ultimo

lista.pop(2)
#tira o elemnto naposição 2

print(lista)

# remove= remove o elemento e não o elemento na tal posição (ele só remove o primeiro elemento especificado que ele encontra)

lista.remove(20)

print(lista)

# count = conta quantas vezes o elemento aparece
print("QUantidade de 10:", lista.count(10))

# index: diz a posição do elemento pedido
lista.index(1)

print("Posição do elemento 10:",lista.index(10))

#sort = ordena a lista
lista.sort()
#crescente

lista.sort(reverse=True)
#decrescente

print(lista)

#len

print(len(lista))

#sum = soma da lista

print(sum(lista))

# max = maior valor da lista
#min = menor valor da lista

print(min(lista))
print(max(lista))
