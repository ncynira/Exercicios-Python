'''
Desenvolva um programa que determine se uma pessoa está apta a votar. O usuário deve informar o nome e a idade. 
As regras para determinar a elegibilidade são:

Menos de 16 anos: não pode votar
De 16 a 17 anos: voto facultativo
De 18 a 70 anos: voto obrigatório
Mais de 70 anos: voto facultativo
O programa deve informar o nome da pessoa e se ela deve votar, não pode votar ou se o voto é facultativo.
'''

nome = input("Digite seu nome:\n")
idade = float(input("Qual sua idade?\n"))

if idade < 16:
    print(f"Obrigada por seu interesse, mas você ainda não vota. A partir dos 16 anos.")
elif idade >= 16 and idade <= 17:
    print(f"Você pode votar, mas não tem a obrigatoriedade")
elif idade >= 18 and idade <= 70:
    print(f"Para você, o voto é obrigatório.")
else:
    print(f"Você pode votar, mas não tem a obrigatoriedade")
