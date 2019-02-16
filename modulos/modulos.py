import time
import random
import datetime
from subprocess import run, PIPE
from sentidos.som import FREQUENCIA, doppler


print(FREQUENCIA)
doppler()



exit()
r = run(['apt-get','install', '-y', 'sl'], stdout=PIPE, stderr=PIPE)
#print(r.stdout.decode('utf-8'))
if r.returncode != 0:
    print('Deu merda..')


letras = ['A', 'B', 'C', 'D']

print(random.randint(100, 999))

time.sleep(1)

print(random.choice(letras))

print(datetime.datetime.now())

hoje = datetime.datetime.now()
print(hoje.strftime('%d/%m/%Y'))
