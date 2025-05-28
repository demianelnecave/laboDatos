#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 13 14:00:31 2025

@author: mcerdeiro
"""

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

iris = load_iris(as_frame = True)

data = iris.frame
X = iris.data
Y = iris.target

diccionario = dict(zip( [0,1,2], iris.target_names))
#%%

plt.figure(figsize=(10,10))
sns.scatterplot(data = data, x = 'sepal length (cm)' , y = 'sepal width (cm)', hue='target', palette='viridis')
plt.savefig('pairplot_iris')
#se ve que los target 1 y 2 están más correlacionados, y el sepal length y width no los separa bien
#%%
clasificador = KNeighborsClassifier(n_neighbors=16)

#entreno con los datos sabiendo sus clases
clasificador.fit(X,Y)
#veo con los mismos datos a ver cómo los clasifica
prediccion = clasificador.predict(X)

confusion_matrix = np.zeros((3,3))
for i in range(len(prediccion)):
    pred = prediccion[i]
    real = Y[i]
    #al elemento de la clase real, lo metió en la clase pred
    confusion_matrix[real,pred] += 1
del i, pred, real
#mido accuracy
acc = confusion_matrix.trace()/confusion_matrix.sum()
#%%
#solo con dos atributos
#como era de esperarse, cuando estos atributos son sobre el cépalo, el modelo pierde exactitud
X1 = X[['sepal length (cm)','sepal width (cm)']]
clasificador = KNeighborsClassifier(n_neighbors=16)

clasificador.fit(X1,Y)

prediccion = clasificador.predict(X1)
confusion_matrix = np.zeros((3,3))

for i in range(len(prediccion)):
    pred = prediccion[i]
    real = Y[i]
    confusion_matrix[real,pred] += 1
del i, pred, real
#mido accuracy
acc = confusion_matrix.trace()/confusion_matrix.sum()