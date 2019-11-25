from random import randrange
import pandas as pd
from Entidades.poblacion import *


print("ALGORITMO GENETICO PARA ASIGNACIÓN DE HORARIOS DE LABORATORIOS ")
print("--------------------------------------------")
print("Tranformando La data del Excel")
xls = pd.ExcelFile('Horarios_Actualizado.xlsx')
df=xls.parse('Cursos')
print("Creando Población Inicial")
poblacion1 = Poblacion(50,df)
##poblacion1.Generar_Población()


