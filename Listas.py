"""# Listas
#antes 
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Agora com Listas:

notas = [7.9 , 9.7 , 8.2]

# Criando Listas 

lista = [] # lista vazia
lista = list() #outra forma de criar lista 
lista = [26 , "Thales", 3.14 , false] #a lista ela pode receber todos os tipos de variaveis 
lista_de_listas = [10,[1 , 2 , 3]] """

# Listas e Slices

""" lista = [26 , "Thales", 3.14 , False]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1]) """

#Slices pegando um pedaço da lista

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3]) #vai no indice zero e pega ate o menor que tres 
print(lista[3:6]) # se no lugar do 6 você deixar vazio toda a lista sera mostrada a partir do 3 elemento
print(lista[2:6:2])

# Interações com FOR

# Utilizando os proprios elementos da lista

for elemento in lista:
    print(elemento)

print("Comprimento da lista:", len(lista))

for i in range(len(lista)):
    print(lista[i])

