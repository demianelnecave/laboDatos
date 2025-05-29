'''
Guía clasificación con árboles de decisión
'''
import numpy as np 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier,plot_tree
import matplotlib.pyplot as plt 
import duckdb as db
#%%
df = pd.read_csv('arboles.csv')
#%%
#Investigo el df y grafico cosillas

res_query = db.query('''
                     SELECT COUNT(*) as cant_individuos,
                            nombre_com
                     FROM df
                     GROUP BY nombre_com
                     ORDER BY cant_individuos DESC
         ''').to_df()
res_query = db.query('''
                     SELECT AVG(altura_tot) as prom_alt, 
                            AVG(diametro) as prom_dim,
                            nombre_com
                     FROM df
                     GROUP BY nombre_com
                     ORDER BY prom_alt DESC
         ''').to_df()
         
fig,ax = plt.subplots()
ax.bar(data=res_query, height = 'prom_alt', x = 'nombre_com')
ax.set_title('Altura total promedio según especie de árbol')
plt.show()
#%%
res_query = db.query('''
                     SELECT altura_tot, 
                             diametro,
                            nombre_com
                     FROM df
         ''').to_df()      
fig,ax = plt.subplots()
ax.scatter(data=res_query[res_query['nombre_com']== 'Eucalipto'], x = 'diametro', y = 'altura_tot', label = 'Eucalipto', c='green')
ax.scatter(data=res_query[res_query['nombre_com']== 'Jacarandá'], x = 'diametro', y = 'altura_tot', label = 'Jacarandá', c='violet')
ax.scatter(data=res_query[res_query['nombre_com']== 'Pindó'], x = 'diametro', y = 'altura_tot', label = 'Pindó', c='brown')
ax.scatter(data=res_query[res_query['nombre_com']== 'Ceibo'], x = 'diametro', y = 'altura_tot', label = 'Ceibo', c='orange')
ax.set_title('Altura total promedio según especie de árbol')
ax.set_xlabel('Diámetro tronco (cm)')
ax.set_ylabel('Altura (m)')
ax.legend()
plt.show()
#%%
res_query = db.query('''
                     SELECT altura_tot as alt,
                            nombre_com
                     FROM df
         ''').to_df()      
fig,axes = plt.subplots(1,4, figsize=(15,5))
axes[0].hist(res_query[res_query['nombre_com']== 'Eucalipto']['alt'], label = 'Eucalipto', color='green')
axes[1].hist(res_query[res_query['nombre_com']== 'Jacarandá']['alt'], label = 'Jacarandá', color='violet')
axes[2].hist(res_query[res_query['nombre_com']== 'Pindó']['alt'], label = 'Pindó', color='brown')
axes[3].hist(res_query[res_query['nombre_com']== 'Ceibo']['alt'], label = 'Ceibo', color='orange')
fig.suptitle('Histogramas de las alturas de los árboles, separado por especie')
for i in range(0,4):
    axes[i].set_xlabel('Altura árbol (m)')
    axes[i].set_ylabel('Nro de individuos')
    axes[i].legend()
    plt.tight_layout()
plt.tight_layout()
plt.show()
#más o menos la de menos a más ordenados por altura: Ceibo, Pindó, Jacarandá, Eucalipto. No es muy exacta la separación
#%%
res_query = db.query('''
                     SELECT diametro as dim,
                            nombre_com
                     FROM df
         ''').to_df()      
fig,axes = plt.subplots(1,4, figsize=(15,5))
axes[0].hist(res_query[res_query['nombre_com']== 'Eucalipto']['dim'], label = 'Eucalipto', color='green',bins='rice')
axes[1].hist(res_query[res_query['nombre_com']== 'Jacarandá']['dim'], label = 'Jacarandá', color='violet',bins='rice')
axes[2].hist(res_query[res_query['nombre_com']== 'Pindó']['dim'], label = 'Pindó', color='brown',bins='rice')
axes[3].hist(res_query[res_query['nombre_com']== 'Ceibo']['dim'], label = 'Ceibo', color='orange',bins='rice')
fig.suptitle('Histogramas de los diámetros de los árboles, separado por especie')
for i in range(0,4):
    axes[i].set_xlabel('Diámetro árbol (cm)')
    axes[i].set_ylabel('Nro de individuos')
    axes[i].legend()
    axes[i].set_xlim(0,200)
    plt.tight_layout()
plt.tight_layout()
plt.show()
#el diametro no separa muy bien. Las cuatro especies se distribuyen de manera similar, 
#teniendo picos cerca de los 50cm
#%%
res_query = db.query('''
                     SELECT inclinacio as incl,
                            nombre_com
                     FROM df
         ''').to_df()      
fig,axes = plt.subplots(1,4, figsize=(15,5))
axes[0].hist(res_query[res_query['nombre_com']== 'Eucalipto']['incl'], label = 'Eucalipto', color='green',bins='rice')
axes[1].hist(res_query[res_query['nombre_com']== 'Jacarandá']['incl'], label = 'Jacarandá', color='violet',bins='rice')
axes[2].hist(res_query[res_query['nombre_com']== 'Pindó']['incl'], label = 'Pindó', color='brown',bins='rice')
axes[3].hist(res_query[res_query['nombre_com']== 'Ceibo']['incl'], label = 'Ceibo', color='orange',bins='rice')
fig.suptitle('Histogramas de las inclinaciones de los árboles, separado por especie')
for i in range(0,4):
    axes[i].set_xlabel('Inclinación árbol (°)')
    axes[i].set_ylabel('Nro de individuos')
    axes[i].legend()
    axes[i].set_xlim(0,60)
    plt.tight_layout()
plt.tight_layout()
plt.show()
#la inclinación es malísima, la mayoría de muestras tienen inclinación nula
del axes,fig
#%%
res_query = db.query('''
                     SELECT altura_tot, 
                             diametro,
                            nombre_com
                     FROM df
         ''').to_df()      
fig,ax = plt.subplots()
ax.scatter(data=res_query[res_query['nombre_com']== 'Eucalipto'], x = 'diametro', y = 'altura_tot', label = 'Eucalipto', c='green')
ax.scatter(data=res_query[res_query['nombre_com']== 'Jacarandá'], x = 'diametro', y = 'altura_tot', label = 'Jacarandá', c='violet')
ax.scatter(data=res_query[res_query['nombre_com']== 'Pindó'], x = 'diametro', y = 'altura_tot', label = 'Pindó', c='brown')
ax.scatter(data=res_query[res_query['nombre_com']== 'Ceibo'], x = 'diametro', y = 'altura_tot', label = 'Ceibo', c='orange')
ax.set_title('Altura total promedio según especie de árbol')
ax.set_xlabel('Diámetro tronco (cm)')
ax.set_ylabel('Altura (m)')
ax.legend()
plt.show()
#muy superpuestos
del ax,fig,res_query
#%%
arbol = DecisionTreeClassifier(criterion='gini', max_depth=None)
X = db.query('''
                     SELECT  altura_tot as alt, 
                             diametro as dim,
                             inclinacio as incl
                     FROM df
         ''').to_df()      
y = db.query('''
                     SELECT 
                     CASE
                      WHEN nombre_com == 'Ceibo'
                              THEN 0
                      WHEN nombre_com == 'Jacarandá'
                              THEN 1
                      WHEN nombre_com == 'Eucalipto'
                              THEN 2
                      WHEN nombre_com == 'Pindó'
                             THEN 3
                     END AS grupo        
                     FROM df
         ''').to_df()      
arbol.fit(X,y)

preds = arbol.predict(X)

n = len(np.unique(y))
cant_samples = len(y)
#matriz confusion
M = np.zeros((n,n))
for i in range(0,cant_samples):
    real = y.iloc[i,0]
    p = preds[i]
    #el modelo clasificó al de clase real en la clase p
    M[real,p] += 1
#mido accuracy
acc = M.trace()/M.sum()
#mido accuracy de cada cada clase
acc_0 = M[0,0]/M[0,:].sum()
acc_1 = M[1,1]/M[1,:].sum()
acc_2 = M[2,2]/M[2,:].sum()
acc_3 = M[3,3]/M[3,:].sum()
#La clasificación es mala en particular al clasificar a los árboles Pindó
del i,real,p,n,preds,cant_samples
#%%
plt.figure(figsize=[20,10])
plot_tree(arbol,feature_names=['altura_tot','diametro','inclinacio'],class_names=df['nombre_com'].unique(),
               filled=True,rounded=True,fontsize=8)