import os
kmtotal = 0
print('Se realizara un ejercicio A a Punto B')
etapas = int(input('Cuantas etapas va a realizar -> '))
for i in range(etapas):
    kmrecorridos = int(input('Kilometros recorridos en esta etapas -> '))
    kmtotal += kmrecorridos
print('kilometro recorridos ', kmtotal)
print('Kilometro etapas recorridas ', etapas)