# -*- coding: utf-8 -*-
"""
Materia: Laboratorio de datos - FCEyN - UBA
Clase  : Clase SQL. Script clase. 
Autor  : Pablo Turjanski
Fecha  : 2025-02-03
"""

# Importamos bibliotecas
import pandas as pd
import duckdb as dd


#%%===========================================================================
# Importamos los datasets que vamos a utilizar en este programa
#=============================================================================

carpeta = "~/Downloads/sql/"

# Ejercicios AR-PROJECT, SELECT, RENAME
empleado       = pd.read_csv("empleado.csv")
# Ejercicios AR-UNION, INTERSECTION, MINUS
alumnosBD      = pd.read_csv("alumnosBD.csv")
alumnosTLeng   = pd.read_csv("alumnosTLeng.csv")
# Ejercicios AR-CROSSJOIN
persona        = pd.read_csv("persona.csv")
nacionalidades = pd.read_csv("nacionalidades.csv")
# Ejercicios ¿Mismos Nombres?
se_inscribe_en=pd.read_csv("se_inscribe_en.csv")
materia       =pd.read_csv("materia.csv")
# Ejercicio JOIN múltiples tablas
vuelo      = pd.read_csv("vuelo.csv")    
aeropuerto = pd.read_csv("aeropuerto.csv")    
pasajero   = pd.read_csv("pasajero.csv")    
reserva    = pd.read_csv("reserva.csv")    
# Ejercicio JOIN tuplas espúreas
empleadoRol= pd.read_csv("empleadoRol.csv")    
rolProyecto= pd.read_csv("rolProyecto.csv")    
# Ejercicios funciones de agregación, LIKE, Elección, Subqueries 
# y variables de Python
examen     = pd.read_csv("examen.csv")
# Ejercicios de manejo de valores NULL
examen03 = pd.read_csv("examen03.csv")



#%%===========================================================================
# Ejemplo inicial
#=============================================================================

print(empleado)

consultaSQL = """
               SELECT DISTINCT DNI, Salario
               FROM empleado;
              """

dataframeResultado = dd.sql(consultaSQL).df()

print(dataframeResultado)


#%%===========================================================================
# Ejercicios AR-PROJECT <-> SELECT
#=============================================================================
# a.- Listar DNI y Salario de empleados 
consultaSQL = """
                SELECT DISTINCT DNI, Salario
                FROM empleado;
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%%-----------
# b.- Listar Sexo de empleados 
consultaSQL = """
                SELECT DISTINCT Sexo
                FROM empleado;
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%%-----------
#c.- Listar Sexo de empleados (sin DISTINCT)
consultaSQL = """
                    SELECT Sexo
                    FROM empleado;
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%%===========================================================================
# Ejercicios AR-SELECT <-> WHERE
#=============================================================================
# a.- Listar de EMPLEADO sólo aquellos cuyo sexo es femenino
consultaSQL = """
                SELECT Sexo
                FROM empleado
                WHERE Sexo = 'F';
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%% -----------
#b.- Listar de EMPLEADO aquellos cuyo sexo es femenino y su salario es mayor a $15.000
consultaSQL = """
                SELECT Sexo
                FROM empleado
                WHERE Sexo = 'F' AND Salario > 15000;
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%%===========================================================================
# Ejercicios AR-RENAME <-> AS
#=============================================================================
#a.- Listar DNI y Salario de EMPLEADO, y renombrarlos como id e Ingreso
consultaSQL = """
                
                SELECT DISTINCT DNI as id, Salario AS Ingreso
                FROM empleado;
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)


#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 01                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#%%===========================================================================
# EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 01
#=============================================================================
# Ejercicio 01.1.- Retornar Codigo y Nombre de los aeropuertos de Londres
consultaSQL = """
                SELECT Codigo, Nombre
                FROM aeropuerto
                WHERE Ciudad = 'Londres';
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%% -----------
# Ejercicio 01.2.- ¿Qué retorna 
#                       SELECT DISTINCT Ciudad AS City 
#                       FROM aeropuerto 
#                       WHERE Codigo='ORY' OR Codigo='CDG'; ?
consultaSQL = """
                SELECT DISTINCT Ciudad AS City 
                FROM aeropuerto 
               WHERE Codigo='ORY' OR Codigo='CDG';
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%% -----------
# Ejercicio 01.3.- Obtener los números de vuelo que van desde CDG hacia LHR
consultaSQL = """
                SELECT DISTINCT Numero
                FROM vuelo
                WHERE Origen ='CDG' AND Destino = 'LHR'
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%% -----------
# Ejercicio 01.4.- Obtener los números de vuelo que van desde CDG hacia LHR o viceversa
consultaSQL = """
                 SELECT DISTINCT Numero
                 FROM vuelo
                 WHERE (Origen ='CDG' AND Destino = 'LHR' ) OR (Origen ='LHR' AND Destino = 'CDG' )
                 ORDER BY Salida DESC
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%% -----------
# Ejercicio 01.5.- Devolver las fechas de reservas cuyos precios son mayores a $200
consultaSQL = """
                SELECT DISTINCT Fecha
                FROM reserva
                WHERE Precio > 200
                ORDER BY STRPTIME(Fecha,'%d-%m-%y' )
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)


#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 01                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
#=============================================================================
# Ejercicios AR-UNION, INTERSECTION, MINUS <-> UNION, INTERSECT, EXCEPT
#=============================================================================
# a1.- Listar a los alumnos que cursan BDs o TLENG

consultaSQL = """
                SELECT * 
                FROM alumnosBD 
                UNION 
                select *
                from alumnosTLeng
              """

dataframeResultado = dd.sql(consultaSQL).df()

print(dataframeResultado)

#%% -----------
# a2.- Listar a los alumnos que cursan BDs o TLENG (usando UNION ALL)

consultaSQL = """
                 SELECT * 
                 FROM alumnosBD 
                 UNION ALL
                 select *
                 from alumnosTLeng
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%% -----------
# b.- Listar a los alumnos que cursan simultáneamente BDs y TLENG

consultaSQL = """
                
                 SELECT * 
                 FROM alumnosBD 
                 INTERSECT
                 select *
                 from alumnosTLeng
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%% -----------
# c.- Listar a los alumnos que cursan BDs y no cursan TLENG 

consultaSQL = """
                SELECT * 
                FROM alumnosBD 
                EXCEPT
                select *
                from alumnosTLeng
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 02                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#=============================================================================
#  EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 02
#=============================================================================
# Ejercicio 02.1.- Devolver los números de vuelo que tienen reservas generadas (utilizar intersección)
consultaSQL = """
                    select Numero
                     from vuelo
                     INTERSECT
                    SELECT NroVuelo
                    FROM reserva   
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%%-----------
# Ejercicio 02.2.- Devolver los números de vuelo que aún no tienen reservas
consultaSQL = """
                SELECT Numero
                FROM vuelo
                EXCEPT
                SELECT NroVuelo
                FROM reserva   
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%%-----------
# Ejercicio 02.3.- Retornar los códigos de aeropuerto de los que parten o arriban los vuelos
consultaSQL = """
                SELECT Codigo
                FROM aeropuerto
                INTERSECT
               (SELECT Origen
               FROM vuelo
               UNION
               SELECT Destino
               FROM vuelo)
              
                """
              
dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)



#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 02                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#=============================================================================
# Ejercicios AR-... JOIN <-> ... JOIN
#=============================================================================
# a1.- Listar el producto cartesiano entre las tablas persona y nacionalidades

consultaSQL = """
                SELECT *
                FROM persona
                CROSS JOIN 
                nacionalidades
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)


#%%-----------
# a2.- Listar el producto cartesiano entre las tablas persona y nacionalidades (sin usar CROSS JOIN)

consultaSQL = """
                SELECT DISTINCT *
                FROM persona,nacionalidades;
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)


#%% 
# Carga los nuevos datos del dataframe persona para los ejercicios de AR-INNER y LEFT OUTER JOIN
# ----------------------------------------------------------------------------------------------
persona = pd.read_csv("persona_ejemplosJoin.csv")
# ----------------------------------------------------------------------------------------------
# b1.- Vincular las tablas persona y nacionalidades a través de un INNER JOIN

consultaSQL = """
     SELECT DISTINCT *
     FROM persona
     INNER JOIN 
     nacionalidades
     ON Nacionalidad = IDN
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%%-----------
# b2.- Vincular las tablas persona y nacionalidades (sin usar INNER JOIN)

consultaSQL = """
                SELECT DISTINCT *
                FROM persona,nacionalidades
                WHERE Nacionalidad=IDN;
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%%-----------
# c.- Vincular las tablas persona y nacionalidades a través de un LEFT OUTER JOIN

consultaSQL = """
     SELECT DISTINCT *
     FROM persona
     LEFT OUTER JOIN 
     nacionalidades
     ON Nacionalidad = IDN
                
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%%===========================================================================
# Ejercicios SQL - ¿Mismos Nombres?
#=============================================================================
# a.- Vincular las tablas Se_inscribe_en y Materia. Mostrar sólo LU y Nombre de materia

consultaSQL = """
            SELECT DISTINCT LU, Nombre
            FROM se_inscribe_en as s
            INNER JOIN 
            materia as m
            ON s.Codigo_materia = m.Codigo_materia
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

    
#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 03                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#%%===========================================================================
# EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 03
#=============================================================================
# Ejercicio 03.1.- Devolver el nombre de la ciudad de partida del vuelo número 165

consultaSQL = """
                SELECT Nombre
                FROM vuelo
                INNER JOIN
                aeropuerto
                ON Origen = Codigo
                WHERE Numero = 165
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%%-----------
# Ejercicio 03.2.- Retornar el nombre de las personas que realizaron reservas a un valor menor a $200

consultaSQL = """
                SELECT Nombre
                FROM pasajero AS p
                INNER JOIN
                reserva AS r
                ON p.DNI = r.DNI
                WHERE Precio < 200
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%%-----------
# Ejercicio 03.3.- Obtener Nombre, Fecha y Destino del Viaje de todos los pasajeros que vuelan desde Madrid

vuelosAMadrid = dd.sql("""
                           SELECT * 
                           from vuelo
                           where Origen = 'MAD'
              """).df()

dniPersonasDesdeMadrid = dd.sql("""
                                    SELECT DNI, Fecha, Destino
                                    from reserva as r
                                    INNER JOIN
                                    vuelosAMadrid as v
                                    ON r.NroVuelo = v.Numero
              """).df()

consultaSQL = """
                SELECT Nombre, Fecha, Destino
                from dniPersonasDesdeMadrid as d
                INNER JOIN
                pasajero as p
                ON  d.DNI = p.DNI
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)


#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 03                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    
#%%===========================================================================
# Ejercicios SQL - Join de varias tablas en simultáneo
#=============================================================================
# a.- Vincular las tablas Reserva, Pasajero y Vuelo. Mostrar sólo Fecha de reserva, hora de salida del vuelo y nombre de pasajero.
    
consultaSQL = """
                SELECT Fecha, Salida, Nombre
                from reserva AS r
                INNER JOIN 
                pasajero as p
                ON r.DNI = p.DNI
                INNER JOIN
                vuelo as v
                ON r.NroVuelo = v.Numero
                
              """

dataframeResultado = dd.sql(consultaSQL).df()

print(dataframeResultado)

#%%===========================================================================
# Ejercicios SQL - Tuplas espúreas
#=============================================================================
# a.- Vincular (JOIN)  EmpleadoRol y RolProyecto para obtener la tabla original EmpleadoRolProyecto
    
consultaSQL = """
                SELECT e.empleado, e.rol, r.proyecto 
                FROM empleadoRol AS e
                INNER JOIN
                rolProyecto AS r
                ON e.rol = r.rol
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

'''
CÓMO rol no es una superclave de ninguna tabla se 
'''

#%%===========================================================================
# Ejercicios SQL - Funciones de agregación
#=============================================================================
# a.- Usando sólo SELECT contar cuántos exámenes fueron rendidos (en total)
    
consultaSQL = """
                SELECT COUNT(*) AS CantidadExámenes
                FROM examen;
              """

dataframeResultado = dd.sql(consultaSQL).df()

print(dataframeResultado)

#%%-----------
# b1.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia
    
consultaSQL = """
               SELECT Instancia, COUNT(*) AS Asistieron
               FROM examen
               GROUP BY Instancia;
                """


dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)


#%%-----------
# b2.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia (ordenado por instancia)
    
consultaSQL = """
                SELECT Instancia, COUNT(*) AS Asistieron
                FROM examen
                GROUP BY Instancia
                ORDER BY Instancia DESC;
              """

dataframeResultado = dd.sql(consultaSQL).df()

print(dataframeResultado)

#%%-----------
# b3.- Ídem ejercicio anterior, pero mostrar sólo las instancias a las que asistieron menos de 4 Estudiantes
    
consultaSQL = """
                SELECT Instancia, COUNT(*) AS Asistieron
                FROM examen
                GROUP BY Instancia
                HAVING Asistieron < 4
                ORDER BY Instancia DESC;
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%%-----------
# c.- Mostrar el promedio de edad de los estudiantes en cada instancia de examen
    
consultaSQL = """
                 SELECT Instancia, AVG(Edad) AS PromedioEdad
                 FROM examen
                 GROUP BY Instancia
                 ORDER BY Instancia ASC;
              """

dataframeResultado = dd.sql(consultaSQL).df()

print(dataframeResultado)

#%%===========================================================================
# Ejercicios SQL - LIKE")
#=============================================================================
# a1.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial.
    
consultaSQL = """
                SELECT Instancia, AVG(Nota) as PromedioNota
                FROM examen
                WHERE Instancia LIKE 'Parcial%'
                GROUP BY Instancia
                ORDER BY Instancia
              """

dataframeResultado = dd.sql( consultaSQL).df()
print(dataframeResultado)

#%%-----------
# a2.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial. Esta vez usando LIKE.
    
consultaSQL = """
                SELECT Nombre, 'Equipo de Fútbol' as ColumnaFutbol
                FROM examen
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)


#%%===========================================================================
# Ejercicios SQL - Eligiendo
#=============================================================================
# a1.- Listar a cada alumno que rindió el Parcial-01 y decir si aprobó o no (se aprueba con nota >=4).
    
consultaSQL = """
                SELECT Nombre, Nota,
                CASE WHEN Nota >= 4
                    THEN 'APROBÓ'
                    ELSE 'NO APROBÓ'
                END
                FROM exaconsultaSQL """

dataframeResultado = dd.sql(consultaSQL).df()

print(dataframeResultado)

#%%-----------
# a2.- Modificar la consulta anterior para que informe cuántos estudiantes aprobaron/reprobaron en cada instancia.
    
consultaSQL = """
                        SELECT Instancia,
                            CASE WHEN Nota >= 4
                                THEN 'APROBÓ'
                                ELSE 'NO APROBÓ'
                            END AS Estado,
                        COUNT(*) AS Cantidad
                        FROM examen
                        GROUP BY Instancia, Estado
                        ORDER BY Instancia, Estado
                                
              """

dataframeResultado = dd.sql(consultaSQL).df()

print(dataframeResultado)

#%%===========================================================================
# Ejercicios SQL - Subqueries
#=============================================================================
#a.- Listar los alumnos que en cada instancia obtuvieron una nota mayor al promedio de dicha instancia

consultaSQL = """
                SELECT e1.Nombre,e1.Instancia,e1.Nota
                From examen AS e1
                WHERE e1.Nota > (
                    SELECT AVG(e2.Nota)
                    FROM examen AS e2
                    WHERE e2.Instancia = e1.Instancia)
              """


dataframeResultado = dd.sql(consultaSQL).df()


print(dataframeResultado)

#%%-----------
# b.- Listar los alumnos que en cada instancia obtuvieron la mayor nota de dicha instancia

consultaSQL = """
    SELECT e1.Nombre,e1.Instancia,e1.Nota
    From examen AS e1
    WHERE e1.Nota >= (
        SELECT MAX(e2.Nota)
        FROM examen AS e2
        WHERE e2.Instancia = e1.Instancia)
              """
              
'''
OTRA OPCIÓN: USAR ALL

consultaSQL = """
    SELECT e1.Nombre,e1.Instancia,e1.Nota
    From examen AS e1
    WHERE e1.Nota >= ALL(
        SELECT e2.Nota
        FROM examen AS e2
        WHERE e2.Instancia = e1.Instancia)Nota
              """
'''

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)


#%%-----------
# c.- Listar el nombre, instancia y nota sólo de los estudiantes que no rindieron ningún Recuperatorio

consultaSQL = """
                SELECT e1.Nombre,e1.Instancia,e1.Nota
                From examen AS e1
                WHERE NOT EXISTS(
                    SELECT *
                    FROM examen AS e2
                    WHERE e2.Instancia LIKE 'Recuperatorio%' AND e2.Nombre = e1.Nombre)
              """

dataframeResultado = dd.sql(consultaSQL).df()

print(dataframeResultado)

#%%===========================================================================
# Ejercicios SQL - Integrando variables de Python
#=============================================================================
# a.- Mostrar Nombre, Instancia y Nota de los alumnos cuya Nota supera el umbral indicado en la variable de Python um bralNota

umbralNota = 7

consultaSQL = f"""
                 SELECT e1.Nombre,e1.Instancia,e1.Nota
                 From examen AS e1
                 WHERE Nota > {umbralNota}
              """ 

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)


#%%===========================================================================
# Ejercicios SQL - Manejo de NULLs
#=============================================================================
# a.- Listar todas las tuplas de Examen03 cuyas Notas son menores a 9

consultaSQL = """
                SELECT *
                From examen03
                WHERE Nota < 9
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%%-----------
# b.- Listar todas las tuplas de Examen03 cuyas Notas son mayores o iguales a 9

consultaSQL = """
                SELECT *
                From examen03
                WHERE Nota >= 9
              """


dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%%-----------
# c.- Listar el UNION de todas las tuplas de Examen03 cuyas Notas son menores a 9 y las que son mayores o iguales a 9

consultaSQL = """
                SELECT *
                From examen03
                WHERE Nota < 9 
                UNION
                SELECT *
                From examen03
                WHERE Nota >= 9 
              """

# NO METE LOS NULL
dataframeResultado = dd.sql(consultaSQL).df()

print(dataframeResultado)

#%%-----------
# d1.- Obtener el promedio de notas

consultaSQL = """
                SELECT AVG(Nota)
                From examen03
              """
# no mete null

dataframeResultado = dd.sql(consultaSQL).df()

print(dataframeResultado)

#%%-----------
# d2.- Obtener el promedio de notas (tomando a NULL==0)

consultaSQL = """
                SELECT AVG(
                    CASE WHEN (Nota IS NULL) 
                    THEN 0 
                    ELSE Nota
                    END) AS PromedioConNulls
                From examen03
              """


dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)

#%%===========================================================================
# Ejercicios SQL - Mayúsculas/Minúsculas
#=============================================================================
# a.- Consigna: Transformar todos los caracteres de las descripciones de los roles a mayúscula

consultaSQL = """
                SELECT empleado, UPPER(rol) as rol
                From empleadoRol
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# b.- Consigna: Transformar todos los caracteres de las descripciones de los roles a minúscula

consultaSQL = """
                SELECT empleado, LOWER(rol) as rol
                From empleadoRol
              """

dataframeResultado = dd.sql(consultaSQL).df()

print(dataframeResultado)



#%%===========================================================================
# Ejercicios SQL - Reemplazos
#=============================================================================
# a.- Consigna: En la descripción de los roles de los empleados reemplazar las ñ por ni

consultaSQL = """CASE
                SELECT empleado, REPLACE(rol,'ñ','ni') as rol
                From empleadoRol
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)


#%%===========================================================================
# Ejercicios SQL - Desafío
#=============================================================================
# a.- Mostrar para cada estudiante las siguientes columnas con sus datos: Nombre, Sexo, Edad, Nota-Parcial-01, Nota-Parcial-02, Recuperatorio-01 y , Recuperatorio-02

# ... Paso 1: Obtenemos los datos de los estudiantes
consultaSQL = """
                SELECT DISTINCT e1.Nombre, e1.Sexo, e1.Edad, e1.Nota AS 'Parcial_01'
                From examen AS e1
                LEFT OUTER JOIN  examen
                on e1.Nombre = examen.Nombre
                AND examen.Instancia='Parcial-01'
              """


desafio_01 = dd.sql(consultaSQL).df()
print(desafio_01)

consultaSQL = """
                SELECT DISTINCT desafio_01.*, examen.Nota AS 'Parcial_02'
                From desafio_01
                LEFT OUTER JOIN  examen
                on desafio_01.Nombre = examen.Nombre
                AND examen.Instancia='Parcial-02'
              """
desafio_01 = dd.sql(consultaSQL).df()
print(desafio_01)

consultaSQL = """
                SELECT DISTINCT desafio_01.*, examen.Nota AS 'Parcial_02'
                From desafio_01
                LEFT OUTER JOIN  examen
                on desafio_01.Nombre = examen.Nombre
                AND examen.Instancia='Recuperatorio-01'
              """
desafio_01 = dd.sql(consultaSQL).df()
print(desafio_01)

consultaSQL = """
                    SELECT DISTINCT desafio_01.*, examen.Nota AS 'Parcial_02'
                    From desafio_01
                    LEFT OUTER JOIN  examen
                    on desafio_01.Nombre = examen.Nombre
                    AND examen.Instancia='Recuperatorio-02'
                  """
desafio_01 = dd.sql(consultaSQL).df()

print(desafio_01)

#%% -----------
# b.- Agregar al ejercicio anterior la columna Estado, que informa si el alumno aprobó la cursada (APROBÓ/NO APROBÓ). Se aprueba con 4.

consultaSQL = """
                 SELECT *,
                 CASE WHEN (Parcial_01 >=4 OR Rescuperatorio_01 >= 4) AND (Parcial_02 >=4 OR Rescuperatorio_02 >= 4)
                 THEN 'APROBÓ'
                 ELSE 'NO APROBÓ'
                 END AS Estado
                 From desafio_01
                 
              """

desafio_02 = dd.sql(consultaSQL).df()

print(desafio_02)


#%% -----------
# c.- Generar la tabla Examen a partir de la tabla obtenida en el desafío anterior.

consultaSQL = """
                    SELECT Nombre, Sexo, Edad, 'Parcial_01' AS Instancia, Parcial_01 As Nota
                    FROM desafio_02
                UNION
                    SELECT Nombre, Sexo, Edad, 'Parcial_02' AS Instancia,Parcial_02 AS Nota
                    FROM desafio_02
                UNION
                    SELECT Nombre, Sexo, Edad, 'Recuperatorio_01' AS Instancia,Recuperatorio_01 AS Nota
                    FROM desafio_02
                UNION
                    SELECT Nombre, Sexo, Edad, 'Recuperatorio_02' AS Instancia,Recuperatorio_02 AS Nota
                    FROM desafio_02
                
              """

desafio_03 = dd.sql(consultaSQL).df()

print(desafio_03)

