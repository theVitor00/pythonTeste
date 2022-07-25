# FAÇA UM ALGORIMO QUE LEIA O PREÇO DE UM PRODUTO
# E MOSTRE SEU NOVO PREÇO COM 5% DE DESCONTO

preco_inteiro = float(input('Digite o valor do produto: '))
preco_final = preco_inteiro - preco_inteiro * (5/100)

print('O valor do produto com desconto é de R${:.2f}'.format(preco_final))