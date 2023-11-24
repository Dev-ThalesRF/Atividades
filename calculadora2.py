num1 = float(input("Qual o 1° numero?"))
num2 = float(input("Qual o 2° numero?"))

print("Escolha um operação:")
print("Sendo 1 Adição")
print("Sendo 2 subtração")
print("Sendo 3 divisão")
print("Sendo 4 multiplicação")

op = int(input("Qual o peração escolhida:"))

if op == 1:
    print("Resultado: ", num1 + num2)
elif op == 2:
    print("Resultado: ", num1 - num2)
elif op ==3:
    print("Resultado: ", num1 / num2)
elif op == 4:
    print("Resultado: ", num1 * num2 )