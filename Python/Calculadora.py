print("Escolha uma operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = int(input("Digite o número da operação desejada: "))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if op == 1:
    print("Resultado: ", num1 + num2)
elif op == 2:
    print("Resultado: ", num1 - num2)
elif op == 3:
    print("Resultado: ", num1 * num2)
elif op == 4:
    print("Resultado: ", num1 / num2)
else:
    print("Operação inválida!")