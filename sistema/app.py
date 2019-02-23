#!/usr/bin/python3  
from pymongo import MongoClient
client = MongoClient()
db = client.python
from random import randint
import re
tela = """
####################################################
#                                                  #                    
#             Sistema de Terminal 0.1              #
#                                                  #                    
####################################################

#Selecine uma opção:

1] Buscar pelo nome...
2] Cadastrar...
3] Atualizar...
4] Deletar...
5] Sair...

    Opção:_

"""
print(tela)

n = randint(10 , 99999)

opção = input('Digite uma opçao')

if opção == '1':
	print('Encontre o nome')
	nome = input('Digite o nome')
	regex = re.compile(nome, re.IGNORECASE)
	for i in db.usuarios.find({"nome":regex},{"nome":1}):
		print(i)

if opção == '2':
	print('Cadastrar')
	nome = input('Digite o nome')
	email = input('Digite o email')
	senha = input('Digite a senha')
	db.usuarios.insert({"_id" : n, "nome" : nome , "email" : email , "senha" : senha,})

if opção == '3':
	print('Atualizar')
	
	_id = input('Digite o id a atualizar')
	nome = input('Atualize o nome')
	email = input('Atualize o email')
	senha = input('Atualize a senha')

	db.usuarios.update({"_id" : int(_id)},{"nome" : nome , "email" : email , "senha" : senha,})

if opção== '4':
	print('Deletar')

if opção == '5':
	print('Sair')			











exit()





















#exit()
#from modulos.mysql import cursor, db
#nome = input('Digite o nome do usuario ' )
#email = input('Digite o email do usuario ' )
#sexo = input('Digite o sexo do usuario [0,1] ' )


#sql = "SELECT id FROM usuarios WHERE email = %s)"
#encontrado = cursor.execute(sql, [email])
#if encontrado:
#    print('Email ja existente, por favor digite outro') 

#exit()
#nome = input('Digite o nome do usuario: ')

#sql = "SELECT * FROM usuarios WHERE nome LIKE '%{0}%'".format(nome)

#cursor.execute(sql)

#for linha in cursor:
 #   print(linha)

