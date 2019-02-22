#!/usr/bin/python3
from pymongo import MongoClient

client = MongoClient()
db = client.python

id = int(input('Digite um id qualquer'))
nome = input('Digite seu nome')
email = input('Digite seu email')
senha = input('Digite a senha')


db.usuarios.insert({"_id": id , "nome" : nome , "email" : email , "senha" : senha })



exit()
for i in db.usuarios.find():
    if 'filhos' in i:
        for f in i ['filhos']:
            if f['nome'] == 'Heitor':
                print(f['nome'])
