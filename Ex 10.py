salario_fixo = int(input("Digite o salário fixo do funcionário: "))
carros_vendidos = int(input("Digite o total de carros vendidos pelo funcionário: "));
comissao_carro = int(input("Digite a comissão fixa do funcionário: ")) 
valor_carros_vendido = int(input("Digite o valor das vendas: "));

total_vendas = valor_carros_vendido * 0.05;
salario_final = salario_fixo + total_vendas + (comissao_carro * carros_vendidos);
print("O salário final do funcionário é: ", salario_final)
