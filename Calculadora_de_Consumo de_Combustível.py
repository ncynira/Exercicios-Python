'''
Crie um aplicativo para calcular o consumo médio de combustível de um veículo. 
O usuário deve inserir o nome do motorista, a quantidade de quilômetros percorridos e a quantidade de combustível gasto em litros.
O programa deve calcular o consumo médio (quilômetros por litro) e classificar a eficiência do veículo conforme a tabela:

Menos de 8 km/l: Venda o carro!
Entre 8 e 12 km/l: Econômico
Mais de 12 km/l: Super econômico
Apresente o nome do motorista e a classificação de eficiência do veículo.
'''

nome = input("Nome do Motorista:\n")
quilometros = float(input(f"{nome} a quantidade de quilômetros percorridos:\n"))
combustivel = float(input(f"{nome} a quantidade de combustivel gasto, em litros:\n"))

consumo_medio = int(quilometros / combustivel)

print(f"{nome}, seu consumo médio de combustivel é de \n {consumo_medio}")

if consumo_medio <= 8:
    print(f"Venda o carro!")
elif consumo_medio > 8.1 and consumo_medio <= 12:
    print(f"Econômico")
else:
    print("Super econômico")
    