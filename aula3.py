#!/usr/bin/python3
for i. linha in enumerate(arquivo):
    if i%2 == 0:
        print(linha.strip())


exit()
arquivo = open('zen.txt')
for linha in arquivo:
    if linha !='-\n':
        print(linha)

exit()
arquivo = open('zen.txt')
for linha in arquivo:
     print(linha, end='')



#print(arquivo)
