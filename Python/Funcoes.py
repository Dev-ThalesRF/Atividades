#Funçoes 


# O que são funções e por que utilizalas ?

# Funções que já utizamos anteriormente:
# print() inprimir mensagem (int, float , str) no console (terminal, cmd)
# input() Retorna um dado informado pelo Usuario (entrada Padrão ) e pode receber str
# len() Recebe uma lista e retorna o tamanho desta lista 
# max ou min: max retorna o maior valor da lista e min o menor valor 


# Criação de Funções:

# Função Inicial:

def sudacao():
    print("Seja bem vindo!")
    print("Olá, é um prazer ter você fazendo parte desse curso!")

sudacao() 

# Função com parametro

def saudacao(nome, curso):
    print(f"Seja bem vindo, {nome}!")
    print(f"É um prazer ter você fazendo parte do curso de {curso}!")

saudacao("Thales","Python")
saudacao("Aline","Java")

# função com parametros default

def saudacao(nome, curso="Python"):
    print(f"Seja bem vindo, {nome}!")
    print(f"É um prazer ter você fazendo parte do curso de {curso}!")

saudacao("Thales" , "c++") 

# Funções com retorno:


def soma (num1,num2):
    return num1 + num2

resultado = soma(5,7)

print("O resultado da soma é:", resultado) 

def calculadora(num1 , num2, operacao="+"):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    if operacao == "*":
        return num1 * num2
    elif operacao == "/":
        return num1 / num2
resultado = calculadora (10, 20,"/")

print (resultado)


