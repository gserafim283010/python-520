#!/usr/bin/python3

def fui(l):
    return l.upper()


letras = ['a','Z','b','c' ,'A']
ordenadas = sorted(letras, key=lambda i : i.upper())

for g in ordenadas:
    print(g)
