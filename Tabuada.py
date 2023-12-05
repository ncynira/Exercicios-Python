''' Crie um programa que solicite o numero de uma tabuada
após digitar o numero, mostre a tabuada completa na tela
Digite o numero: 1
1 x 19 = 1
...
1 x 10 = 10'''


nome = input("Informe seu nome: \n")
Tabuada = int(input(f"Qual numero da tabuada você precisa, {nome}: \n"))

print(f"{nome},segue a tabuada do {Tabuada}:")


for i in range(1, 11):
    resultado = Tabuada * i
    print(f"{Tabuada} x {i} = {resultado}")



