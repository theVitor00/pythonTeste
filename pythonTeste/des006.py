# CRIE UM ALGORITMO QUE LEIA UM NÚMERO E MOSTRE
# O SEU DOBRO, O SEU TRIPLO E A SUA RAIZ QUADRADA


num = int(input('Digite um número inteiro: '))
dobro = num * 2
triplo = num * 3
rquad  = num**0.5   #pow(n, (1/2))

print('O dobro de {} é {}, seu triplo é {} e sua raiz quadrada é igual a {:.0f}'.format(num, dobro, triplo, rquad))
