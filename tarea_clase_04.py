empleado_01 = [[20_222_333,45,2,20_000],[33_456_234,40,0,25_000],[45_250_323, 41, 2, 10_000]]

def superanSalarioActividad01(A, umbral):
    res = []
    for fila in A:
        if fila[3] > umbral:
            res.append(fila)
    return res

umbral = 15000

superanSalarioActividad01(empleado_01, umbral)

#Costó poco implementarla

#Si se agregan más filas la función sigue sirviendo

empleado_02 = [[20_222_333,45,2,20_000],[33_456_234,40,0,25_000],[45_250_323, 41, 2, 10_000], [42_689_554,36,0,18000]]

superanSalarioActividad01(empleado_02, umbral)

empleado_03 = [[20_222_333,45,20_000,2],[33_456_234,40,25_000,0],[45_250_323, 41, 10_000,1], [42_689_554,36,18000,0]]

superanSalarioActividad01(empleado_03, umbral)
#La función ya no sirve, cambió la forma en la que se guardaban los datos

def superanSalarioActividad03(A, umbral):
    res = []
    for fila in A:
        if fila[2] > umbral:
            res.append(fila)
    return res


empleado_04 = [[20_222_333,33_456_234,45_250_323,42_689_554],
               [45,40,41,36],
               [20000,25000,10000,18000],
               [2,0,1,0]    
               ]

#Las anteriores funciones no sriven


def superanSalarioActividad04(A, umbral):
    res = []
    for col in range(len(A[2])):
        empleado= []
        if A[2][col] > umbral:
            for fila in A:
                empleado.append(fila[col])
            res.append(empleado)
    return res
superanSalarioActividad04(empleado_04, umbral)

"""
ej 5
1) a- La cantidad de las filas que se pasaban no afectó el funcionamiento de la función
   b- Cuando se alteró el orden de las columnas, en cambio, sí modificó la eficacia de la función, volviéndola inútil. El cambio que se debió hacer fue relativamente chico.
2) Cuando se representó a la matriz como una lista de columnas, además de afectar a la función nuevamente hizo que modificara bastante la estructura del código de la función para que esta funcionase.
3) Encapsula, hace que el usuario que quiere hacer la query no deba preocuparse por el cómo acceder (que cambia según la estructura de almacenamiento elegida) sino en simplemente la "función" de la función, valga la redundancia.
   

"""