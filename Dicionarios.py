#Criando dicionarios
# criando um dicionario vazio
""" 
dicionario = {}
dicionario = dict()

dicionario = { "nome": "Thales", "idade": 24, "altura": 1.70}

print(dicionario)
print(dicionario["idade"]) 

 """

# Adicionando elementos em um dicionario
"""
dicionario = {}
dicionario = dict()
dicionario = { "nome": "Thales", "idade": 24, "altura": 1.70}

dicionario["programador"] = True

print(dicionario)
"""
#  Iterando sobre um dicionario
dicionario = {}
dicionario = dict()
dicionario = { "nome": "Thales", "idade": 24, "altura": 1.70}

for Chave in dicionario:
    print(Chave, dicionario[Chave])

#  Testando a existencia de uma chave:

print("peso" in dicionario) #false
print("altura" in dicionario) #True

# 
# 