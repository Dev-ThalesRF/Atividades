"""for variavel in range(81): # para a variavel dentro do faixa 10
    print(variavel)

for variavel in range (1,11):# assim ele vai começar no 1 e vai contar ate 10
    print(variavel)

for variavel in range (0,22,2): #agora o terceiro parametro vai contar de 2 em 2.
    print(variavel)"""

"""
nota 1 = float(input("Informe sua nota 1"))
nota 1 = float(input("Informe sua nota 2"))
nota 1 = float(input("Informe sua nota 3"))
"""
soma = 0

for i in range(1,4):
    nota = float(input(f"Infome a sua nota{i}:"))

    soma = soma + nota

print(soma / 3)
