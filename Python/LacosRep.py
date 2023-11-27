# "while" = enquanto 

numero_sorteado = 20

numero_escolhido = int(input("Informe um numero entre 1 e 20:"))

while numero_escolhido != numero_sorteado:
    print("Você errou o numero, tente novamente...")

    numero_escolhido = int(input("Informe um numero entre 1 e 20:"))
print("Parabens! Você acertou!") 

contador = 0

while contador <= 10:
    print(contador)

    contador = contador + 1
