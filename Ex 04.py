valor1 = int(input('Digite um valor: '));
valor2 = int(input('Digite outro valor: '));
valor3 = int(input('Digite outro valor: '));

if (valor1 > valor2 and valor2 > valor3):
  print("A soma dos valores maiores é: ", valor1 + valor2)
elif (valor3 > valor2 and valor1 > valor2):
  print("A soma dos valores maiores é: ", valor1 + valor3)
else:
  print("A soma dos valores maiores é: ", valor2 + valor3)