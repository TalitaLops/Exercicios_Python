fabrica = int(input("Digite o custo de Fábrica do carro: "));

distribuidor = fabrica * 0.28;
impostos = fabrica * 0.45;

custo_final= fabrica + distribuidor + impostos;
print("O custo final pro consumidor é: ",custo_final);