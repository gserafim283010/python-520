#!/usr/bin/python3
texto_grotesco = 'Por conseguinte, o novo modelo estrutural aqui preconizado nos obriga à análise das condições financeiras e administrativas exigidas. Ainda assim, existem dúvidas a respeito de como o surgimento do comércio virtual faz parte de um processo de gerenciamento das regras de conduta normativas. Neste sentido, a execução dos pontos do programa exige a precisão e a definição do fluxo de informações.'

nomes = ['Hector', 'Guilherme', 'Joel', 'Flávio', 'Fabiano', 'Roger', 'Cícero', 'Hugo', 'Ayron', 'Leonel', 'Pedro', 'Lucas']


if 'virtual'in texto_grotesco:
    print('Palavra "virtual" encotrada')

print(nomes[-4:])
print (len(texto_grotesco.split()))

for g in nomes :
    if g[0] in 'FH':
        print(g)







exit()
n1 = input('Digite um numero : ')
n2 = input('Digite um numero :')
resultado = int(n1)+int(n2)
if resultado > 100:
   print('Que numero grandao')
elif resultado ==50:
    print('...')
else:
    print('Que numero pequeno')
