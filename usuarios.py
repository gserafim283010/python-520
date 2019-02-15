#!/usr/bin/python3
def fui(l):
    return l['Nome']

usuario = [] 
for linha in open('usuarios.csv'):
    A0, A1, A2 = linha.split(',')
    usuario.append({"Nome": A0.strip(),"Idade" :int(A1.strip()),"E-mail" :A2.strip()})
for linha in sorted(usuario, key=fui):
    print(linha['Nome'])

exit()
nomes = []

for linha in usuario:
    nomes.append(linha['Nome'])

for n in sorted(nomes):    
    print (n)
