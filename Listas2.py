# Metodos e Listas

lista = [1, 3, 12, 8, 2]

#append: adiciona oque for solicitado no final da lista.

print("Antes do Append: ", lista)

lista.append(3)

print("Depois do Append: ", lista)

#insert: aqui você tambem adiciona um novo elemento, mas escolhe em qual local esse elemento ficará.

lista.insert(2 , 40)

print("Depois do insert: ", lista)

#extend  ele pega os elementos da nova lista e joga no final da lista solicitada.

lista2 = [1, 2, 3]

lista.extend(lista2)

print("Depois do extend: ", lista)

#pop ele elimina o elemento do indice informado

lista.pop(0)
print("Lista apos o pop: ",lista)

#remove ele remove o primeiro elemento que e compativel com oque vc solicitou .

lista.remove(3)

print("Depois do remove: ",lista)

#count o ele conta quantas vzs o elemento que você solicitou está na lista.

print("Quantidade de 2 na lista:", lista.count(2))

# index ele diz o indice de um determinado elemento na lista

print("Indice do elemento 12: ", lista.index(12))

#sort organiza a lista

lista.sort()

print("Lista organizada de forma crescente: ",lista)

lista.sort(reverse=True)

print("Agora vamos vê de maneira decrecente: ", lista)

#Funções para a lista:

# len essa função mostra todos os elementos dentro da função

# sum soma todos os elementos daquela lista

print(sum(lista))

#max vai retornar o maior valor da lista

print("Maior elemento da lista: ", max(lista))

#min vai retornar o menot valor da lista

print("Menor elemento da lista: ", min(lista))