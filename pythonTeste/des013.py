# FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO
# E MOSTRE SEU NOVO SALÁRIO COM 15% DE AUMENTO

sal_inicial = float(input('Digite o salário do funcionário: R$'))
sal_final = sal_inicial + sal_inicial * (15/100)

print('O novo salário do funcionário é de R${:.2f}'.format(sal_final))