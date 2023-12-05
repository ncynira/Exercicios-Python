'''
Desenvolva um programa que classifique um hotel baseado na avaliação dos hóspedes. 
O usuário deve digitar o nome do hotel e três notas referentes aos critérios de conforto, limpeza e localização. 
O programa deve calcular a média das notas e emitir uma classificação:

Média menor que 4: Hotel de 1 estrela
Média de 4 a 6: Hotel de 3 estrelas
Média de 6 a 8: Hotel de 4 estrelas
Média 9 ou superior: Hotel de 5 estrelas
No final, o programa deve exibir o nome do hotel e sua classificação em estrelas.
'''

nome = input("Digite o nome do hotel:\n")

nota1 = float(input(f"Qual nota você atribui ao conforto do hotel {nome}:\n"))
nota2 = float(input(f"Digite a nota que você atribui para a lipesa do hotel {nome}:\n"))
nota3 = float(input(f"Digite a nota que você atribui a localização do hotel {nome}:\n"))

media = (nota1 + nota2 + nota3) / 3

if media <3.9:
    print(f"O {nome} foi classificado como 1 estrela")
elif media >= 4 and media <= 5.9:
    print(f"O {nome} foi classificado como 3 estrelas")
elif media >= 6 and media <= 8:
    print(f"O {nome} foi classificado como 4 estrelas")
else:
    print(f"O {nome} foi classificado como 5 estrelas")


