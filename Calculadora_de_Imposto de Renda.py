'''
Crie um programa que calcule o Imposto de Renda devido por um contribuinte. O usuário deve inserir o nome 
do contribuinte e o salário mensal. O programa deve calcular o imposto com base nas seguintes faixas:

Até R$ 1.903,98: isento
De R$ 1.903,99 até R$ 2.826,65: 7.5%
De R$ 2.826,66 até R$ 3.751,05: 15%
De R$ 3.751,06 até R$ 4.664,68: 22.5%
Acima de R$ 4.664,68: 27.5%
Apresente o nome do contribuinte e o valor do imposto a pagar.
'''
nome = input("Digite o nome do contribuente:\n")
salário = float(input(f"Digite o salário mensal do {nome}:\n"))
Contribuição = float(input(f"Digite a contribuição previdenciaria mensal de {nome}:\n"))

Liquido = (salário - Contribuição)

print(f"Salario liquido: {Liquido}")

if Liquido <= 1903.98:
    print(f"{nome} isento")
elif Liquido >= 2826.66 and Liquido < 3751.05:
    print(f"{nome} terá que pagar 7.5%")
elif Liquido >= 3751.06 and Liquido < 4664.67:
    print(f"{nome} terá que pagar 15%")
else:
    Liquido <= 4664.68
    print(f"O {nome} terá que pagar 27.5%")

