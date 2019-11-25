from random import randrange
import pandas as pd
from Entidades import Individuo

xls = pd.ExcelFile('Horarios_Actualizado.xlsx')
df=xls.parse('Cursos')
individuo = [None]*20
cont = 0
print(df.values[0])
print(df.values[9])
print(cont)
while cont != 10:
    hora=randrange(20)
    if individuo[hora:0] != None :
        individuo[hora] = df.values[cont]
    cont += 1

print(cont)
print(individuo)
for ind in individuo:
    if type(ind) is 'NoneType':
        print(type(ind))


#-------------------------------------------------------------------------------

class Poblacion:
    def __init__(self, num_individuos, cursos):
        self.num_individuos= num_individuos
        self.cursos = cursos

    def Generar_Población():
        print("Generando población de {} Individuos".format(self.num_individuos))
        for i in range(self.num_individuos):
            individuo = Individuo(cursos)



            
    
"""
    def ObtenerDiayHorario(self, i):
        if i>=0 and i<=6:
            horario = i
            dia = "Lunes"
        else:
            horario=(i+1)%7
        print(horario)

        temporal = i%7 + 1
        dias = {
                1: "Lunes",
                2: "Martes",
                3: "Miercoles",
                4: "Jueves",
                5: "Viernes",
                6: "Sabados"
            }
        if  temporal >= 0 and temporal <=6:
            dia = dias[temporal]

        else:
            dia= dias[temporal%6]

        print("Los valores son: {} {}".format(horario,dia))
        valores=[horario,dia]
        

        return valores
"""

            

