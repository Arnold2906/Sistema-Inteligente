from random import randrange
import random
from individuo import *
import pandas as pd
from pandas import DataFrame

class Poblacion:
    def __init__(self, num_individuos, cursos):
        self.num_individuos= num_individuos
        self.cursos = cursos
        self.ArrayPoblacion=[]
        self.ranking=[]
        self.TotalFitnees=0
        self.Ruleta=num_individuos*(num_individuos+1)/2
        self.Elegidos=[]
        self.AcumuladaRuleta=0
        self.ruletmax=None
        self.Hijos=[]
        self.tasa_De_Reproducción=0.7
        self.tasa_De_Mutacion=0.01


    def Generar_Población(self):
        for i in range(self.num_individuos):
            individuo = Individuo(self.cursos)
            individuo.random_individuo()
            ## Agrega a la población
            self.ArrayPoblacion.append(individuo)
        
    def Evalular_Poblacion(self):
        print("Comienza la Evaluacion con {} Individuos".format(self.num_individuos)) 
        for i in range(self.num_individuos):
            self.ArrayPoblacion[i].evaluar_individuo()
            self.TotalFitnees += self.ArrayPoblacion[i].fitness
    
    def seleccion(self):
        #Se usará el metodo de ranking
        print("Comienza la Selección")
        print("-----------------------")
        self.AcumuladaRuleta=0
        self.ArrayPoblacion.sort(key=lambda individuo: individuo.fitness)
        #ruleta=[0]*self.num_individuos
        for i in range(len(self.ArrayPoblacion)):
            self.ArrayPoblacion[i].porcentaje=(i+1)/self.Ruleta
            self.AcumuladaRuleta = self.ArrayPoblacion[i].porcentaje + self.AcumuladaRuleta
            self.ArrayPoblacion[i].PAcumulada=self.AcumuladaRuleta
            print("La acumulada del {} es : {}".format(i,self.ArrayPoblacion[i].PAcumulada))
        
        for i in range(len(self.ArrayPoblacion)): 
            print("Comienza la eleccion {}".format(i))    
            Valor_Ruleta=random.random()
            print("el valor de la ruleta es {}".format(Valor_Ruleta))
            if Valor_Ruleta >= 0 and Valor_Ruleta < self.ArrayPoblacion[0].PAcumulada:
                self.Elegidos.append(self.ArrayPoblacion[0])
                print("El individuo numero 0 ha sido elegido")

            for i in range(len(self.ArrayPoblacion)-1):
                if Valor_Ruleta >= self.ArrayPoblacion[i].PAcumulada and Valor_Ruleta < self.ArrayPoblacion[i+1].PAcumulada:
                    self.Elegidos.append(self.ArrayPoblacion[i+1])
                    print("El Individuo {} ha sido elegido".format(i+1))
            print("La cantidad de Elegidos: {}".format(len(self.Elegidos)))

        print("Cantidad de elegidos {}".format(len(self.Elegidos)))


   
    def recombinacion(self):
        print("Comienza la reproducción")
        print("----------------------------")
        print("La cantidad es : {}".format(len(self.Elegidos)))
        for i in range(0,len(self.Elegidos)-1,2):
            tasaRandom=random.random()
            print("La tasa de reproducción es {}".format(tasaRandom))
            if self.tasa_De_Reproducción > tasaRandom:
                hijo1 = self.Elegidos[i]
                hijo2 = self.Elegidos[i+1]
                print("El fitnes de los padres es: {} y {}".format(self.Elegidos[i].fitness,self.Elegidos[i+1].fitness))
                corte=randrange(420)
                print("El corte para la reproducción es {} y el indice es {}".format(corte,i))
                puntero1=self.Elegidos[i].horaH
                puntero2=self.Elegidos[i+1].horaH
                puntero1.sort()
                puntero2.sort()
                for k in range(len(puntero1)):
                    if corte >= puntero1[k]:
                        hijo2.cromosoma[puntero1[k]] = self.Elegidos[i].cromosoma[puntero1[k]]
                        hijo2.horaH[k] = puntero1[k]

                for k in range(len(puntero2)):
                    if corte >= puntero2[k]:
                        hijo1.cromosoma[puntero2[k]] = self.Elegidos[i+1].cromosoma[puntero2[k]]
                        hijo1.horaH[k] = self.Elegidos[i+1].horaH[k]
                hijo1.evaluar_individuo
                hijo2.evaluar_individuo
                self.Hijos.append(hijo1)
                self.Hijos.append(hijo2)
            

    def mutacion(self):
        print("Comienza la mutacion")
        print("-----------------------------------------")
        Bmutacion=False
        contMutacion=0
        print("La cantidad de hijos es: {}".format(len(self.Hijos)))
        for i in range(len(self.Hijos)):
            randomMutacion=random.random()
            if self.tasa_De_Mutacion > randomMutacion:
                valor1=randrange(145)
                valor2=randrange(145)
                indice1=self.Hijos[i].horaH[valor1]
                indice2=self.Hijos[i].horaH[valor2]
                print("EL valor del valor1 es : {}".format(self.Hijos[i].cromosoma[indice1]))
                temporal=self.Hijos[i].cromosoma[indice1]
                print("EL valor del valor2 es : {}".format(self.Hijos[i].cromosoma[indice2]))
                self.Hijos[i].cromosoma[valor1]=self.Hijos[i].cromosoma[indice2]
                self.Hijos[i].cromosoma[valor2]=temporal
                print(temporal)
                Bmutacion=True
                contMutacion += 1

        if Bmutacion:
            print("Hubo {} mutaciones".format(contMutacion))
        else:
            print("NO HUBO MUTACIONES")
            

    def reemplazo(self):
        print("Comienza el reemplazo")
        if len(self.Hijos) != 0 :
            rankingTemporal=[]
            for i in range(len(self.ArrayPoblacion)):
                rankingTemporal.append(self.ArrayPoblacion[i])

            for i in range(len(self.Hijos)):
                rankingTemporal.append(self.Hijos[i])

            rankingTemporal.sort(key=lambda individuo: individuo.fitness)
            cantidadMaxPoblacion=self.num_individuos-1
            cantidadMaxRanking=len(rankingTemporal)-1
            for i in range(len(self.Hijos)):
                print("El fitness de los hijos es: {}".format(self.Hijos[i].fitness))
            for i in range(len(rankingTemporal)):
                print("El fitness del ranking es: {}".format(rankingTemporal[i].fitness))
            for i in range(len(self.ArrayPoblacion)):
                print("El fitness de la población es: {}".format(self.ArrayPoblacion[i].fitness))

            while cantidadMaxPoblacion != -1:
                self.ArrayPoblacion[cantidadMaxPoblacion]=rankingTemporal[cantidadMaxRanking]
                cantidadMaxPoblacion -=1  
                cantidadMaxRanking -=1

            for i in range(len(self.ArrayPoblacion)):
                print("El nuevo fitness es: {}".format(self.ArrayPoblacion[i].fitness))
            
            self.Elegidos=[]
            self.Hijos=[]
            rankingTemporal=[]
              



    def mejorResultado(self):
        mejorIndividuo=self.ArrayPoblacion[self.num_individuos-1]
        respuesta=mejorIndividuo.ImprimirResultado()
        df = DataFrame(respuesta, columns= ['codigo', 'curso','Profesor','horaInicio','horaFin','dia','Laboratorio'])
        export_excel = df.to_excel (r'.\horariofinal.xlsx', index = None, header=True) #Don't forget to add '.xlsx' at the end of the path




print("ALGORITMO GENETICO PARA ASIGNACIÓN DE HORARIOS DE LABORATORIOS ")
print("--------------------------------------------")
print("Tranformando La data del Excel")
xls = pd.ExcelFile('Horarios_Actualizadov2.xlsx')
df=xls.parse('Cursos')
print("Creando Población Inicial")
poblacion1 = Poblacion(4,df)
poblacion1.Generar_Población()
print("Evaluar la población")
poblacion1.Evalular_Poblacion()
"""
poblacion1.seleccion()
poblacion1.recombinacion()
poblacion1.mutacion()
poblacion1.reemplazo()
poblacion1.mejorResultado()
"""
print("Comienza los ciclos")
generacion=0

while generacion != 1:
    generacion += 1
    print("LA GENERACION NUMERO {}".format(generacion))
    poblacion1.seleccion()
    poblacion1.recombinacion()
    poblacion1.mutacion()
    poblacion1.reemplazo()


poblacion1.mejorResultado()

print("Terminó el algoritmo")