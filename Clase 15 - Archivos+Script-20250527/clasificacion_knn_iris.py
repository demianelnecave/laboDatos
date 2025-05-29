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
from matplotlib.colors import ListedColormap
iris = load_iris(as_frame = True)

data = iris.frame
X = iris.data
Y = iris.target

diccionario = dict(zip( [0,1,2], iris.target_names))
#%%

fig,ax = plt.subplots(1,1,figsize=(10,10))
ax.set_ylim(0,3.5)
plt.scatter(data = data[data['target'] == 0], x = 'petal length (cm)' , y = 'petal width (cm)', label='setosa', c='red')
plt.scatter(data = data[data['target'] == 1], x = 'petal length (cm)' , y = 'petal width (cm)', label='versicolor',c='blue')
plt.scatter(data = data[data['target'] == 2], x = 'petal length (cm)' , y = 'petal width (cm)', label='virginica', c='green')
plt.legend()
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
#graficar frontera de decisión
def plot_decision_boundary(X, y, clf):
    fig, ax = plt.subplots(figsize=(6, 6))    
    # Crear grilla
    h = 0.1
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h)) 
    # Predecir clases en cada punto de la grilla
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # Colores
    n_classes = len(np.unique(y))
    light_colors = plt.cm.Pastel1.colors[:n_classes]
    bold_colors = plt.cm.Set1.colors[:n_classes]
    cmap_light = ListedColormap(light_colors)
    cmap_bold = ListedColormap(bold_colors)
    # Graficar la frontera de decisión
    ax.contourf(xx, yy, Z, cmap=cmap_light, alpha=0.5)
    ax.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, s=40, edgecolor='k')
    ax.set_xlabel("Atributo 1")
    ax.set_ylabel("Atributo 2")
    ax.set_title("Frontera de decisión")
#creo clf
clf = KNeighborsClassifier(n_neighbors = 10)
X1 = X[['petal length (cm)', 'petal width (cm)']]
clf.fit(X1, Y)

prediccion = clf.predict(X1)

confusion_matrix = np.zeros((3,3))
for i in range(len(prediccion)):
    pred = prediccion[i]
    real = Y[i]
    #al elemento de la clase real, lo metió en la clase pred
    confusion_matrix[real,pred] += 1
del i, pred, real
#mido accuracy
acc = confusion_matrix.trace()/confusion_matrix.sum()

plot_decision_boundary(X1.values, Y, clf)
plt.show()
print(f'La accuracy es de {acc}')

clf.predict([[4.8,1.5]])
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