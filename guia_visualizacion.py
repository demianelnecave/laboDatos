'''guía 12 visualización '''

import seaborn
import matplotlib.pyplot as plt
import pandas as pd
import duckdb as db 
#%%
data_ping = seaborn.load_dataset('penguins')

i = data_ping['island'].unique()

cant_T = data_ping[data_ping['island'] == 'Torgersen']
cant_B = data_ping[data_ping['island'] == 'Biscoe']
cant_D = data_ping[data_ping['island'] == 'Dream']
 

cont_T = db.query('''
                 SELECT species, COUNT(*) as cantidad
                 FROM cant_T
                 GROUP BY species
         ''').to_df()
         

                 
cont_B = db.query('''
                 SELECT species, COUNT(*) as cantidad
                 FROM cant_B
                 GROUP BY species
         ''').to_df()

cont_D = db.query('''
                 SELECT species, COUNT(*) as cantidad
                 FROM cant_D
                 GROUP BY species
         ''').to_df()
                 
#%% GRÁFICOS

fig,ax = plt.subplots()

ax.pie(data=cont_T, x = 'cantidad', labels = 'species', autopct = '%1.1f%%')
ax.set_title('Proporción cantidad pinguinos por especie en Torgersen')
plt.show()

fig,ax = plt.subplots()

ax.bar(data=cont_T, height = 'cantidad', x = 'species')
ax.set_title('Proporción cantidad pinguinos por especie en Torgersen')
plt.show()

fig, ax = plt.subplots()
ax.pie(data=cont_B, x = 'cantidad', labels = 'species', autopct = '%1.1f%%')
ax.set_title('Proporción cantidad pinguinos por especie en Biscoe')
plt.show()
fig, ax = plt.subplots()
ax.bar(data=cont_B, height = 'cantidad', x = 'species')
ax.set_title('Proporción cantidad pinguinos por especie en Biscoe')
plt.show()


fig, ax = plt.subplots()
ax.pie(data=cont_D, x = 'cantidad', labels = 'species', autopct = '%1.1f%%')
ax.set_title('Proporción cantidad pinguinos por especie en Dream')
plt.show()
fig, ax = plt.subplots()

ax.bar(data=cont_D, height = 'cantidad', x = 'species', color = ['red','green'])
ax.set_title('Proporción cantidad pinguinos por especie en Dream')
ax.set_xlabel('Especies de pinguinos')
ax.set_ylabel('Cantidad especímenes')
plt.show()
#%% separar por especies

Ade = db.query('''
                 SELECT *
                 from data_ping
                 WHERE species = 'Adelie'
         ''').to_df()
         

                 
Chin = db.query('''
                 SELECT *
                 from data_ping
                 WHERE species = 'Chinstrap'
         ''').to_df()
Gen = db.query('''
                 SELECT *
                 from data_ping
                 WHERE species = 'Gentoo'
         ''').to_df()

#%% histograma

fig,ax = plt.subplots()
ax.hist([data_ping['bill_depth_mm']], histtype = 'bar', label= ['Pinguinos'], 
        color = 'darkred', rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (12.0,22.0))
ax.set_ylim(0,75)
ax.set_xlabel('Grosor del pico (mm)')
ax.set_ylabel('Especímenes')
ax.set_title('Grosor del pico')
plt.legend()
plt.show()
#%% hist segun especie
fig,ax = plt.subplots()
ax.hist([Ade['bill_depth_mm'],Chin['bill_depth_mm'],Gen['bill_depth_mm']], histtype = 'bar',bins = 'sqrt', label= ['Adelie', 'Chinstrap','Gentoo'], 
        color = ['aqua','purple','darkgreen'], rwidth = 1, edgecolor = 'black', align = 'mid')
ax.set_xlabel('Grosor del pico (mm)')
ax.set_ylabel('Especímenes')
ax.set_title('Grosor del pico de los según la isla')
plt.legend()
plt.show()
#%% por separado
fig,ax = plt.subplots()
ax.hist([Ade['bill_depth_mm']], histtype = 'bar', label= ['Adelie'], 
color = ['darkred'], rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (12.0,22.0))
ax.set_ylim(0,75)
ax.set_xlabel('Grosor del pico (mm)')
ax.set_ylabel('Especímenes')
ax.set_title('Grosor del pico de los pinguino Adelie')
plt.legend()
plt.show()

fig,ax = plt.subplots()
ax.hist([Chin['bill_depth_mm']], histtype = 'bar', label= ['Chinstrap'], 
        color = ['darkred'], rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (12.0,22.0))
ax.set_ylim(0,75)
ax.set_xlabel('Grosor del pico (mm)')
ax.set_ylabel('Especímenes')
ax.set_title('Grosor del pico de los pinguino Chinstrap')
plt.legend()
plt.show()


fig,ax = plt.subplots()
ax.hist([Gen['bill_depth_mm']], histtype = 'bar', label= ['Gentoo'], 
        color = ['darkred'], rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (12.0,22.0))
ax.set_ylim(0,75)
ax.set_xlabel('Grosor del pico (mm)')
ax.set_ylabel('Especímenes')
ax.set_title('Grosor del pico de los pinguino Gentoo')
plt.legend()
plt.show()
#%% todo en un lienzo
fig, axes = plt.subplots(2, 2, figsize=(15,10))  # 1 fila, 3 columnas
axes[0,0].hist([Ade['bill_depth_mm']], histtype = 'bar', label= ['Adelie'], 
        color = ['darkred'], rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (12.0,22.0))
axes[0,0].set_ylim(0,75)
axes[0,0].set_xlabel('Grosor del pico (mm)')
axes[0,0].set_ylabel('Especímenes')
axes[0,0].set_title('Grosor del pico de los pinguino Adelie')
axes[0,1].hist([Chin['bill_depth_mm']], histtype = 'bar', label= ['Chinstrap'], 
        color = ['darkred'], rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (12.0,22.0))
axes[0,1].set_ylim(0,75)
axes[0,1].set_xlabel('Grosor del pico (mm)')
axes[0,1].set_ylabel('Especímenes')
axes[0,1].set_title('Grosor del pico de los pinguino Chinstrap')
axes[1,0].hist([Gen['bill_depth_mm']], histtype = 'bar', label= ['Gentoo'], 
        color = ['darkred'], rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (12.0,22.0))
axes[1,0].set_ylim(0,75)
axes[1,0].set_xlabel('Grosor del pico (mm)')
axes[1,0].set_ylabel('Especímenes')
axes[1,0].set_title('Grosor del pico de los pinguino Gentoo')
axes[1,1].hist([data_ping['bill_depth_mm']], histtype = 'bar', label= ['Pinguinos'], 
        color = 'darkred', rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (12.0,22.0))
axes[1,1].set_xlabel('Grosor del pico (mm)')
axes[1,1].set_ylabel('Especímenes')
axes[1,1].set_title('Grosor del pico de los pinguinos')
fig.suptitle('Grosor del pico de los pinguinos, general y separado por especie')
plt.tight_layout()
plt.legend()
plt.show()
#%% Otras características
''''
Veo largo del pico
'''
fig, axes = plt.subplots(2, 2, figsize=(15,10))  # 1 fila, 3 columnas
axes[0,0].hist([Ade['bill_length_mm']], histtype = 'bar', 
        color = ['darkblue'], rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (32.0,60.0))
axes[0,0].set_ylim(0,65)
axes[0,0].set_xlabel('Largo del pico (mm)')
axes[0,0].set_ylabel('Especímenes')
axes[0,0].set_title('Largo del pico de los pinguinos Adelie')
axes[0,1].hist([Chin['bill_length_mm']], histtype = 'bar', 
        color = ['darkblue'], rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (32.0,60.0))
axes[0,1].set_ylim(0,65)
axes[0,1].set_xlabel('Largo del pico (mm)')
axes[0,1].set_ylabel('Especímenes')
axes[0,1].set_title('Largo del pico de los pinguino Chinstrap')
axes[1,0].hist([Gen['bill_length_mm']], histtype = 'bar', 
        color = ['darkblue'], rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (32.0,60.0))
axes[1,0].set_ylim(0,65)
axes[1,0].set_xlabel('Largo del pico (mm)')
axes[1,0].set_ylabel('Especímenes')
axes[1,0].set_title('Largo del pico de los pinguino Gentoo')
axes[1,1].hist([data_ping['bill_length_mm']], histtype = 'bar',
        color = 'darkblue', rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (32.0,60.0))
axes[1,1].set_ylim(0,65)
axes[1,1].set_xlabel('Largo del pico (mm)')
axes[1,1].set_ylabel('Especímenes')
axes[1,1].set_title('Largo del pico de los pinguinos')
fig.suptitle('Largo del pico de los pinguinos, general y separado por especie')
plt.tight_layout()
plt.show()
#%% 
'''
Veo largo ala
'''
fig, axes = plt.subplots(2, 2, figsize=(15,10))  # 1 fila, 3 columnas
axes[0,0].hist([Ade['flipper_length_mm']], histtype = 'bar', 
        color = ['violet'], rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (170.0,235.0))
axes[0,0].set_ylim(0,85)
axes[0,0].set_xlabel('Largo del ala (mm)')
axes[0,0].set_ylabel('Especímenes')
axes[0,0].set_title('Largo del ala de los pinguinos Adelie')
axes[0,1].hist([Chin['flipper_length_mm']], histtype = 'bar', 
        color = ['violet'], rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (170.0,235.0))
axes[0,1].set_ylim(0,85)
axes[0,1].set_xlabel('Largo del ala (mm)')
axes[0,1].set_ylabel('Especímenes')
axes[0,1].set_title('Largo del ala de los pinguino Chinstrap')
axes[1,0].hist([Gen['flipper_length_mm']], histtype = 'bar', 
        color = ['violet'], rwidth = 0.5, edgecolor = 'black', align = 'mid',range =(170.0,235.0))
axes[1,0].set_ylim(0,85)
axes[1,0].set_xlabel('Largo del ala (mm)')
axes[1,0].set_ylabel('Especímenes')
axes[1,0].set_title('Largo del ala de los pinguino Gentoo')
axes[1,1].hist([data_ping['flipper_length_mm']], histtype = 'bar',
        color = 'violet', rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (170.0,235.0))
axes[1,1].set_ylim(0,85)
axes[1,1].set_xlabel('Largo del ala (mm)')
axes[1,1].set_ylabel('Especímenes')
axes[1,1].set_title('Largo del ala de los pinguinos')
fig.suptitle('Largo del ala de los pinguinos, general y separado por especie')
plt.tight_layout()
plt.show()
#%%
'''
Veo masa 
'''
fig, axes = plt.subplots(2, 2, figsize=(15,10))  # 1 fila, 3 columnas
axes[0,0].hist([Ade['body_mass_g']], histtype = 'bar', 
        color = ['purple'], rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (2600.0,6500.0))
axes[0,0].set_ylim(0,80)
axes[0,0].set_xlabel('Masa (g)')
axes[0,0].set_ylabel('Especímenes')
axes[0,0].set_title('Masa de los pinguinos Adelie')
axes[0,1].hist([Chin['body_mass_g']], histtype = 'bar', 
        color = ['purple'], rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (2600.0,6500.0))
axes[0,1].set_ylim(0,80)
axes[0,1].set_xlabel('Masa (g)')
axes[0,1].set_ylabel('Especímenes')
axes[0,1].set_title('Masa de los pinguinos Chinstrap')
axes[1,0].hist([Gen['body_mass_g']], histtype = 'bar', 
        color = ['purple'], rwidth = 0.5, edgecolor = 'black', align = 'mid',range =(2600.0,6500.0))
axes[1,0].set_ylim(0,80)
axes[1,0].set_xlabel('Masa (g)')
axes[1,0].set_ylabel('Especímenes')
axes[1,0].set_title('Masa de los pinguins Gentoo')
axes[1,1].hist([data_ping['body_mass_g']], histtype = 'bar',
        color = 'purple', rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (2600.0,6500.0))
axes[1,1].set_ylim(0,80)
axes[1,1].set_xlabel('Masa (g)')
axes[1,1].set_ylabel('Especímenes')
axes[1,1].set_title('Masa de los pinguinos')
fig.suptitle('Masa de los pinguinos, general y separado por especie')
plt.tight_layout()
plt.show()
#%%
'''
Veo masa separado por sexo
'''
'''
Hembras
'''
fig, axes = plt.subplots(1, 2, figsize=(15,5))  # 1 fila, 3 columnas

axes[0].hist([data_ping[data_ping['sex']=='Female']['body_mass_g']], histtype = 'bar',
        color = 'purple', rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (2600.0,6500.0))
axes[0].set_ylim(0,80)
axes[0].set_xlabel('Masa (g)')
axes[0].set_ylabel('Especímenes')
axes[0].set_title('Masa de los pinguinos hembras')
''' 
Machos
'''
axes[1].hist([data_ping[data_ping['sex']=='Male']['body_mass_g']], histtype = 'bar',
        color = 'blue', rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (2600.0,6500.0))
axes[1].set_ylim(0,80)
axes[1].set_xlabel('Masa (g)')
axes[1].set_ylabel('Especímenes')
axes[1].set_title('Masa de los pinguinos machos')
fig.suptitle('Masa de los pinguinos, general y separado por sexo')
plt.tight_layout()
plt.show()
#%%
'''
Veo largo pico separado por sexo
'''
'''
Hembras
'''
fig, axes = plt.subplots(1, 2, figsize=(15,5))  # 1 fila, 3 columnas

axes[0].hist([data_ping[data_ping['sex']=='Female']['bill_length_mm']], histtype = 'bar',
        color = 'purple', rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (32.0,60.0))
axes[0].set_ylim(0,80)
axes[0].set_xlabel('Largo pico (mm)')
axes[0].set_ylabel('Especímenes')
axes[0].set_title('Largo pico de los pinguinos hembras')
''' 
Machos
'''
axes[1].hist([data_ping[data_ping['sex']=='Male']['bill_length_mm']], histtype = 'bar',
        color = 'blue', rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (32.0,60.0))
axes[1].set_ylim(0,80)
axes[1].set_xlabel('Largo pico (mm)')
axes[1].set_ylabel('Especímenes')
axes[1].set_title('Largo pico de los pinguinos machos')
fig.suptitle('Largo pico de los pinguinos, general y separado porsexo')
plt.tight_layout()
plt.show()
#%%
'''
Veo grosor pico separado por sexo
'''
'''
Hembras
'''
fig, axes = plt.subplots(1, 2, figsize=(15,5))  # 1 fila, 3 columnas

axes[0].hist([data_ping[data_ping['sex']=='Female']['bill_depth_mm']], histtype = 'bar',
        color = 'purple', rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (12.0,22.0))
axes[0].set_ylim(0,80)
axes[0].set_xlabel('Grosor pico (mm)')
axes[0].set_ylabel('Especímenes')
axes[0].set_title('Grosor pico de los pinguinos hembras')
''' 
Machos
'''
axes[1].hist([data_ping[data_ping['sex']=='Male']['bill_depth_mm']], histtype = 'bar',
        color = 'blue', rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (12.0,22.0))
axes[1].set_ylim(0,80)
axes[1].set_xlabel('Grosor pico (mm)')
axes[1].set_ylabel('Especímenes')
axes[1].set_title('Grosor pico de los pinguinos machos')
fig.suptitle('Grosor pico de los pinguinos, general y separado porsexo')
plt.tight_layout()
plt.show()
#%%
'''
Veo largo ala separado por sexo
'''
'''
Hembras
'''
fig, axes = plt.subplots(1, 2, figsize=(15,5))  # 1 fila, 3 columnas

axes[0].hist([data_ping[data_ping['sex']=='Female']['flipper_length_mm']], histtype = 'bar',
        color = 'purple', rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (170.0,235.0))
axes[0].set_ylim(0,80)
axes[0].set_xlabel('Largo del ala (mm)')
axes[0].set_ylabel('Especímenes')
axes[0].set_title('Largo del ala de los pinguinos hembras')
''' 
Machos
'''
axes[1].hist([data_ping[data_ping['sex']=='Male']['flipper_length_mm']], histtype = 'bar',
        color = 'blue', rwidth = 0.5, edgecolor = 'black', align = 'mid',range = (170.0,235.0))
axes[1].set_ylim(0,80)
axes[1].set_xlabel('Largo del ala (mm)')
axes[1].set_ylabel('Especímenes')
axes[1].set_title('Largo del ala de los pinguinos machos')
fig.suptitle('Largo del ala de los pinguinos, general y separado porsexo')
plt.tight_layout()
plt.show()
#%% scatterplots
fig,ax = plt.subplots()
ax.scatter(data = Ade[Ade['sex'] == 'Female'], x = 'bill_length_mm', y = 'bill_depth_mm',c='purple',
           edgecolor='k', label = 'Hembra')

ax.scatter(data = Ade[Ade['sex'] == 'Male'], x = 'bill_length_mm', y = 'bill_depth_mm',c='lightblue',
           edgecolor='k', label = 'Macho')
ax.legend()
plt.show()
#%%
fig,ax = plt.subplots()
ax.scatter(data = Ade[Ade['sex'] == 'Female'], x = 'body_mass_g', y = 'flipper_length_mm',c='purple',
           edgecolor='k', label = 'Hembra')

ax.scatter(data = Ade[Ade['sex'] == 'Male'], x = 'body_mass_g', y = 'flipper_length_mm',c='lightblue',
           edgecolor='k', label = 'Macho')
ax.legend()
plt.show()
#%%
fig,ax = plt.subplots()
ax.scatter(data = Ade, x = 'bill_length_mm', y = 'bill_depth_mm',c='yellow',
           edgecolor='k', label = 'Adelie')

ax.scatter(data = Chin, x = 'bill_length_mm', y = 'bill_depth_mm',c='darkgreen',
           edgecolor='k', label = 'Chinstrap')
ax.scatter(data = Gen, x = 'bill_length_mm', y = 'bill_depth_mm',c='darkred',
           edgecolor='k', label = 'Genoo')
ax.set_xlabel('Largo pico (mm)')
ax.set_ylabel('Grosor pico (mm)')
ax.set_title('Relación entre el largo y el grosor del pico, según especie')
ax.legend()
plt.show()
#%%
#una sola caract para separar hembras por especie
fig, axes = plt.subplots(2, 2, figsize=(15,10))  # 1 fila, 3 columnas
axefig, axes = plt.subplots(2, 2, figsize=(15,10))  # 2 filas, 2 columnas

axes[0,0].hist(Ade[Ade['sex'] == 'Female']['flipper_length_mm'], histtype='bar',
               color='darkred', rwidth=0.5, edgecolor='black', align='mid',
               range=(170,235), label='Adelie')
axes[0,0].set_ylim(0,85)
axes[0,0].set_xlabel('Longitud de la aleta (mm)')
axes[0,0].set_ylabel('Especímenes')
axes[0,0].set_title('Adelie')
axes[0,0].legend()

axes[0,1].hist(Chin[Chin['sex'] == 'Female']['flipper_length_mm'], histtype='bar',
               color='darkred', rwidth=0.5, edgecolor='black', align='mid',
               range=(170,235), label='Chinstrap')
axes[0,1].set_ylim(0,85)
axes[0,1].set_xlabel('Longitud de la aleta (mm)')
axes[0,1].set_ylabel('Especímenes')
axes[0,1].set_title('Chinstrap')
axes[0,1].legend()

axes[1,0].hist(Gen[Gen['sex'] == 'Female']['flipper_length_mm'], histtype='bar',
               color='darkred', rwidth=0.5, edgecolor='black', align='mid',
               range=(170,235), label='Gentoo')
axes[1,0].set_ylim(0,85)
axes[1,0].set_xlabel('Longitud de la aleta (mm)')
axes[1,0].set_ylabel('Especímenes')
axes[1,0].set_title('Gentoo')
axes[1,0].legend()

axes[1,1].hist(data_ping[data_ping['sex'] == 'Female']['flipper_length_mm'], histtype='bar',
               color='darkred', rwidth=0.5, edgecolor='black', align='mid',
               range=(170,235), label='Todas')
axes[1,1].set_ylim(0,85)
axes[1,1].set_xlabel('Longitud de la aleta (mm)')
axes[1,1].set_ylabel('Especímenes')
axes[1,1].set_title('Todas las hembras')
axes[1,1].legend()

fig.suptitle('Longitud de la aleta de las hembras, por especie y en general')
plt.tight_layout()
plt.show()

#%%
#Combinando características busco separar según especie a las hembras
fig,ax = plt.subplots()
ax.scatter(data = Ade[Ade['sex']=='Female'], x = 'bill_length_mm', y = 'bill_depth_mm',c='yellow',
           edgecolor='k', label = 'Adelie')

ax.scatter(data = Chin[Chin['sex']=='Female'], x = 'bill_length_mm', y = 'bill_depth_mm',c='darkgreen',
           edgecolor='k', label = 'Chinstrap')
ax.scatter(data = Gen[Gen['sex']=='Female'], x = 'bill_length_mm', y = 'bill_depth_mm',c='darkred',
           edgecolor='k', label = 'Genoo')
ax.set_xlabel('Largo pico (mm)')
ax.set_ylabel('Grosor pico (mm)')
ax.set_title('Relación entre el largo y el grosor del pico para hembras, según especie')
ax.legend()
plt.show()
''' 
Esta combinación de características separa muy bien
'''