A = float(input("Digite o preço do litro de álcool: "));
RendimentoA = float(input("Digite os quilometro por litro de álcool: "));

G = float(input("Digite o preço do litro da gasolina: "));
RendimentoG = float(input("Digite os quilometros por litro de gasolina:"));
precoA= G * 0.7

if (A <= precoA):
  print('ALCOOL')
else:
  print('GASOLINA')
