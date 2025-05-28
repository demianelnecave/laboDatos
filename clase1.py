# -*- coding: utf-8 -*-
"""
comentario prueba

"""
import random

import math 

import csv

import numpy as np

import pandas as pd


a = 6

b = []

b.append(a)

#%% le sumo 5 
a += 5

b.append(a)
#%%


#%% diccionarios

d = dict(zip([1,2],[3,4]))

a = zip([1,2],[3,4])
#%%

#%%

prueba = random.random()

# semilla para reproducir experimento

#si no se especifica la seed se crea por timestamp


random.seed(5)

prueba = random.random()
print(prueba)

random.seed(5)
prueba = random.random()
print(prueba)


random.seed(5)
prueba = random.random()
print(prueba)

#%%

#%%
x = 5 
print(math.sqrt(2))

math.exp(math.log(x))


#%%

#%% manejo de archivos

filename = 'datame.txt'

with open(filename, 'rt') as file:
    data = file.read()


linea_inicio = "Este 2025 retomamos con nuestras ya clásicas charlas Dátame"

linea_fin = "Sin presupuesto no hay universidad"

data = linea_inicio + "\n" + data + "\n" + linea_fin


new_name = open("datame_2025.txt","w")

new_name.write(data)

new_name.close()



#%% archivos csv

with open('cronograma_sugerido.csvloc', 'rt') as file:
    lista_materias = []
    
    next(file)  #avanza el iterador

    for line in file:
        datos_linea = line.split(',')
        print(datos_linea[1])
        lista_materias.append(datos_linea[1])
        
        
    
    print(lista_materias)
    
    
#otra forma con modulo csv (respeta mejor comas interiores)

with open('cronograma_sugerido.csv','rt') as file:
    lista2_materias = []
    filas = csv.reader(file)
    encabezado = next(file)
    
    for fila in filas:
        lista2_materias.append(fila[1])
        print(fila[1])
        print("\nLa correlatividad de esta materia es: " + fila[2] +"\n")
        
    print(lista2_materias)
#%%


#%% Ejerciciosloc

def generala_tirar():
    dados = []
    for i in range(5):
        num = random.randint(1, 6)
        dados.append(num)
    if es_escalera(dados):
        print("ESCALERA")
    elif es_full(dados):
        print("FULL")
    elif es_poker(dados):
        print("POKER")
    elif es_generala(dados):
        print("GENERALA")
    return dados
def es_escalera(lista):
    l = lista.sort()
    i = 0
    if lista.len() == 0:
        return True
    if l[i] == l[i+1]-1:
        es_escalera(lista[1:])
    else:
        return False
def es_full(lista):
    if lista.len() == 2:
        return False
    if lista.count(i) == 3:
        return True
    else:
        return es_full(lista[1:])
def es_poker(lista):
    if lista.len() == 3:
        return False
    if lista.count(i) == 4:
        return True
    else:
        return es_poker(lista[1:])
def es_generala(lista):
    if lista.count(i) == 5:
        return True
    else:
        return False                


generala_tirar()


def lector_lineas_datame():
    filename = 'datame.txt'

    with open(filename, 'rt') as file:
        for line in file:
            if 'estudiante' in line:
                print(line)
            
lector_lineas_datame()   
#%%

#%% NUMPY
a = np.array([[1,2,3],[4,2,6], [2,8,2]])

print(a[1,2])

np.zeros(2)

np.ones((2,3))

#c = np.arrange(2,9,2)  #de 2 hasta 9 de a dos pasos

d = np.linspace(0,10, num=5) #5 nums equidistantes del cero al diez

a.ndim

a.shape

a.reshape((3,-1)) #tres por lo que corresponda

def pisar_elemento(M,e):
    elems_por_dim = M.shape
    print(elems_por_dim)
    for i in range(elems_por_dim[0]):
        for j in range(elems_por_dim[1]):
            if M[i,j]== e:
                M[i,j] = -1
    return M
pisar_elemento(a, 2)
#%%

#%% PANDAS 



#%%



