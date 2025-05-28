# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 18:46:06 2025

@author: Usuario
"""
import pandas as pd

archivo = 'arbolado-en-espacios-verdes.csv'


df = pd.read_csv(archivo, index_col = 2)
df

jacs_df = df[df['nombre_com'] == 'Jacarandá']

palos_borr_df = df[df['nombre_com'] == 'Palo Borracho']

palos_borr_df = df[df['nombre_com'].str.contains('Palo borracho')]

### JACARANDÁS
cant_jacs = jacs_df.shape[0]

jac_alt_max = jacs_df["altura_tot"].max()

jac_alt_min = jacs_df["altura_tot"].min()

jax_alt_prom = jacs_df["altura_tot"].mean()

jac_dim_stats = jacs_df["diametro"].agg(['max','min','mean'])  #igual pero en una serie




### PALOS BORRACHOS
cant_palos = palos_borr_df.shape[0]


palos_alt_stats = palos_borr_df["altura_tot"].agg(['max','min','mean'])

palos_dim_stats = palos_borr_df["diametro"].agg(['max','min','mean'])  



def cant_arboles(parque):
  res = (df['espacio_ve'] == parque).sum()
  return res
cant_arboles("GENERAL PAZ")


def cant_nativos(parque):
    return ((df["espacio_ve"] == parque) & (df["origen"].str.contains("Nativo"))).sum()

cant_nativos("AVELLANEDA, NICOLÁS, Pres.")


'''
GUIA EJERCICIOS
'''

#%% ej1 
def leer_parque(nombre_archivo, parque):
    df = pd.read_csv(nombre_archivo, index_col=2)
    res = (df[df['espacio_ve']== parque]).to_dict(orient='records')
    return res
arboles_cente = leer_parque(archivo, 'CENTENARIO')
arboles_andes = leer_parque(archivo,'ANDES, LOS' )
#%%

#%% ej2 
def dar_especies(lista_arboles):
    res = []
    for elem in lista_arboles:
        res.append(elem['nombre_com'])
    res = list(dict.fromkeys(res))    
    return res
dar_especies(arboles_cente)
#%% ej 3

def dar_contadores(lista_arboles):
    especies = dar_especies(lista_arboles)
    res = []
    for elem in especies:
        cont = 0
        for i in range(len(lista_arboles)):
            if lista_arboles[i]['nombre_com'] == elem:
                cont += 1
        res.append(cont)
    return res
def contar_ejemplares(lista_arboles):
    res = {}
    especies = dar_especies(lista_arboles)
    contadores = dar_contadores(lista_arboles)
    for i in range(len(especies)):
        res[especies[i]] = contadores[i]
    return res
contar_ejemplares(arboles_cente)
#%%

#%% ej 4
def obtener_alturas(lista_arboles, especie):
    ejemplares = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            ejemplares.append(arbol)
    res = []
    for ejemplar in ejemplares:
        res.append(ejemplar['altura_tot'])
    return res
jac_alt = obtener_alturas(arboles_cente,'Jacarandá')

jac_alt_prom = sum(jac_alt) / len(jac_alt)

jac_alt_maxi = max(jac_alt)
#%%

#%% ej 5
def obtener_inclinaciones(lista_arboles, especie):
    ejemplares = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            ejemplares.append(arbol)
    res = []
    for ejemplar in ejemplares:
        res.append(ejemplar['inclinacio'])
    return res
#%%

#%% ej 6
def especimen_mas_inclinado(lista_arboles):
    especies = dar_especies(lista_arboles)
    res = [0,0]
    df = pd.DataFrame(lista_arboles)    #se hace un df desde una lista de diccionarios
    for especie in especies:
        max_incl = max(obtener_inclinaciones(lista_arboles, especie))
        if max_incl > res[1]:
            res[0] = especie
            res[1] = max_incl
    return res
especimen_mas_inclinado(arboles_cente)         
#%%
#%% ej 7
def especie_promedio_mas_inclinada(lista_arboles):
    especies = dar_especies(lista_arboles)
    res = [0,0]
    df = pd.DataFrame(lista_arboles)    #se hace un df desde una lista de diccionarios
    for especie in especies:
        mean_incl = df[df['nombre_com'] == especie]['inclinacio'].mean()
        if mean_incl > res[1]:
            res[0] = especie
            res[1] = mean_incl
    return res
especie_promedio_mas_inclinada(arboles_cente)

especie_promedio_mas_inclinada(arboles_andes)
#%%

archivo2 = 'arbolado-publico-lineal-2017-2018.csv'

data_arboles_veredas = pd.read_csv(archivo2)[['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']]

especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']

df_tipas_parques = df[df['nombre_cie'] == 'Tipuana Tipu'][['diametro','altura_tot']]

df_tipas_veredas = data_arboles_veredas[data_arboles_veredas['nombre_cientifico'] == 'Tipuana tipu'][['diametro_altura_pecho','altura_arbol']]

df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'vereda'

df_tipas_veredas.rename(columns= {'diametro_altura_pecho':'diametro','altura_arbol': 'altura_tot'},  inplace=True)

a= df_tipas_parques.merge(df_tipas_veredas, how='outer')

alt_max_vereda = a[a['ambiente'] == 'vereda']['altura_tot'].max()
diam_max_vereda = a[a['ambiente'] == 'vereda']['diametro'].max()
alt_mean_vereda = a[a['ambiente'] == 'vereda']['altura_tot'].mean()
diam_mean_vereda = a[a['ambiente'] == 'vereda']['diametro'].mean()

alt_max_parque = a[a['ambiente'] == 'parque']['altura_tot'].max()
diam_max_parque = a[a['ambiente'] == 'parque']['diametro'].max()
alt_mean_parque = a[a['ambiente'] == 'parque']['altura_tot'].mean()
diam_mean_parque = a[a['ambiente'] == 'parque']['diametro'].mean()

# se observa que tanto para altura como diametro los árboles "tipas" crecidos en parques suelen llegar a mayores números