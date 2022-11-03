total_eleitores = int(input("Digite o número de eleitores do município: "));
nulos = int(input("Digite o número de votos nulos do município: "));
brancos = int(input("Digite o número de votos em branco do município: "));
validos = total_eleitores - (nulos + brancos);

porcentagem_validos = validos * 100 / total_eleitores;
porcentagem_brancos = brancos * 100 / total_eleitores;
porcentagem_nulos = nulos * 100 / total_eleitores;


print("O total de votos validos foi ", porcentagem_validos,"%");
print("O total de votos em branco foi ", porcentagem_brancos, "%");
print("O total de votos nulos foi ", porcentagem_nulos, "%");