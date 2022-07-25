# CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA
# E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR
# US$1.00 = R$3.27

dinheiro = float(input('Quanto dinheiro tem na carteira: '))
dolar = dinheiro // 3.27

print('Com R${:.2f} você consegue comprar {:.2f} dólares.'.format(dinheiro, dolar))