A = int(input('Digite o valor de um lado do triângulo: '))
B = int(input('Digite o valor do outro lado: '))
C = int(input('Digite o valor do outro lado: '))

soma1 = A + B
soma2 = B + C
soma3 = C + A

if (soma1 < C or soma1 < B or soma1 < A):
  print('Não é um triângulo')
elif (soma2 < A or soma2 < B or soma2 < C):
  print('Não é um triângulo')
elif (soma3 < B or soma3 < A or soma3 < C):
  print('Não é um triângulo')
else:
  print('É um triângulo ! ')

#para formar um triângulo, o valor de cada lado deve ser menor que a soma dos outros 2 lados