# Conversão de Variaveis

Idade = "26"
numero1 = "10"
numero2 = "20"

print (numero1 + numero2) # Aqui devido as variaveis estarem em str o print esta concatenando em vez de somar.
print (Idade, type(Idade)) # Aqui estamos mostrando a conteudo da variavel e o seu tipo.  

Idade_inteira = int(Idade) # Esse comando pega a variavel que estava em str e torna ela inteiro
print(Idade_inteira, type(Idade_inteira))

altura = float ( input("Informe a sua altura:"))

print(altura, type(altura))
