'''
Elabore um programa que calcule a bonificação anual de um funcionário. 
Peça o nome do funcionário, o salário e o tempo de serviço em anos na empresa. A bonificação é dada da seguinte forma:

Menos de 1 ano de serviço: sem bonificação
De 1 a 3 anos de serviço: 10% do salário
De 4 a 6 anos de serviço: 15% do salário
De 7 a 10 anos de serviço: 20% do salário
Mais de 10 anos de serviço: 25% do salário
O programa deve mostrar o nome do funcionário e o valor da bonificação que ele receberá.
'''
nome = input("Informe seu nome:\n")
tempo = float(input("Qual seu tempo de serviço?\n"))


if tempo < 1:
    print(f"{nome}, não será bonificado")

elif tempo >= 1 and tempo <= 3:
    print(f"{nome}, sua bonificação será de 10% do salário")

elif tempo >= 4 and tempo <= 6:
    print(f"{nome}, sua bonificação será de 15% do salário")
elif tempo >= 7 and tempo <= 10:
    print(f"{nome}, sua bonificação será de 20% do salário")

else:
    print(f"{nome}, sua bonificação será de 25% do salário")

