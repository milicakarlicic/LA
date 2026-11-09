#!/usr/bin/python3

def zbir(x, y):
    return x + y

def razlika(x, y):
    return x - y

def ispis(x):
    print(x)

x = int(input('Unesite 1. broj: '))
y = int(input('Unesite 2. broj: '))

print(f'Zbir je:')
ispis(zbir(x, y))

print('Razlika je:')
ispis(razlika(x, y))
