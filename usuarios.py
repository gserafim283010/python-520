#!/usr/bin/python
def fui(l):
    return l['nome']

def fprint(i, user):
    print('{0:.>4} {1:.<20} {2:.<40}'.format(i,user['nome'], user['email']))

def hprint():
    return ('{0:.4} {1:.<20} {2:.<40}'.format('ID','NOME', 'EMAIL')) 

usuario = [] 
for linha in open('usuarios.csv'):
    A0, A1, A2 = linha.split(',')
    usuario.append({"nome": A0.strip(),"idade" :int(A1.strip()),"email" :A2.strip()})
print(hprint())

for l,u in enumerate(sorted(usuario, key=fui), start=-1):
    fprint(l,u)









exit()
nomes = []

for linha in usuario:
    nomes.append(linha['Nome'])

for n in sorted(nomes):    
    print (n)
