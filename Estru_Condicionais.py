#Estruturas Condicionais 
idade = int(input("Qual a sua idade ?"))

if idade >= 18:
    print ("Você e maior de Idade!")
else:  
    print ("Você e menor de Idade Trouxa!!")


media = float(input("Informe a media do Estudante"))

if media >= 7:
    print("Você foi Aprovado!")
elif media >= 5:
    print("Você ira frequentar a recurperação")
else:
    print("Você foi Reprovadao!!")


media = int(input("Qual foi sua media este bimestre?"))

presenca = int(input("Qual foi sua media de presença este ano ?"))

if media >= 7 and presenca >= 70:
    print ("Aprovado!")
else:
    print("Reprovado!")