#!/usr/bin/python3


usuario = open('usuarios.csv')
for linha in usuario:
    A0, A1, A2 = linha.split(',')
    print({"Nome": A0.strip(),"Idade" :int(A1.strip()),"E-mail" :A2.strip()})
