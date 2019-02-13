usuario = {'nome' : 'Belpegor', 'idade' :65000, 'username' : 'bel'}

for k in usuario:
    print('{0} -> {1}'.format(k, usuario[k]))

print(usuario.keys())
print(usuario.values())

usuario['email'] = 'bel@zebu.com'
print(usuario)

for k, v in usuario.items():
    print('{0}=>{1}.format(k,v)
