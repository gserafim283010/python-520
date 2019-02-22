#!/usr/bin/python3  

from modulos.mysql import cursor, db
nome = input('Digite o nome do usuario ' )
email = input('Digite o email do usuario ' )
sexo = input('Digite o sexo do usuario [0,1] ' )


sql = "SELECT id FROM usuarios WHERE email = %s)"
encontrado = cursor.execute(sql, [email])
if encontrado:
    print('Email ja existente, por favor digite outro') 










exit()
nome = input('Digite o nome do usuario: ')

sql = "SELECT * FROM usuarios WHERE nome LIKE '%{0}%'".format(nome)

cursor.execute(sql)

for linha in cursor:
    print(linha)

