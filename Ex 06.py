fruta = input("Digite a fruta que deseja: ");
peso = int(input('Digite o peso da fruta: '));

if fruta == 'Morango':
    if peso <= 5: 
        preco = peso * 8.5;
        print('O Total da sua compra é: ', preco);
    else :
        preco = peso * 7.9;
        print('O Total da sua compra é: ', preco);
elif fruta == 'Maca':
    if peso <= 5: 
        preco = peso * 7.8;
        print('O Total da sua compra é: ', preco);
    else :
        preco = peso * 7.2;
        print('O Total da sua compra é: ', preco);
else : 
    print('Não temos essa fruta disponível :( ');