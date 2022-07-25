# FAÇA UM PROGRAMA QUE LEIA A LARGURA E ALTURA DE UMA PAREDE EM METROS
# CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA
# SABENDO QUE CADA LITRO DE TINTA PINTA UMA ÁREA DE 2M²

l = float(input('Digite a Largura da parede: '))
a = float(input('Digite a Altura da parede: '))
area = l * a
t = area // 2

print('A área da parede é de {:.2f} metros quadrados. Serão necessários {} litros de tinta para pintá-la.'.format(area, t))
