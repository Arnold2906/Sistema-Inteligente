from random import randrange


class Individuo:
    def __init__(self, cursos):
        # Número de variables del individuo
        self.cromosoma = [None]*420
        # Fitness del individuo
        self.fitness = 0
        # Cursos para asignar
        self.cursos = cursos
        # horario Random
        self.horaH = []
        #Contador de errores en labo
        self.contadorDeErrores = 0
        #Porcentaje
        self.porcentaje=0
        #Probabilidad Acumulada
        self.PAcumulada=0

    def random_individuo(self):
        cont=0
        while cont != 145:
            hora=randrange(420)
            if self.cromosoma[hora:0] != None:
                self.cromosoma[hora] = self.cursos.values[cont]
                self.horaH.append(hora)
                cont += 1

    
            
    
    def ObtenerDiayHorario(self, i):
        #Obtener labo
        labo= (i//42) 
        horarios= {
                1:8,
                2:10,
                3:12,
                4:14,
                5:16,
                6:18,
                0:20,
                7:20
            }
        if i>=0 and i<=6:
            horario = horarios[i+1]
            dia = "Lunes"
        else:
            horario=horarios[(i+1)%7]

        temporal = i//7 + 1
        dias = {
                0: "Sabados",
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
        valores=[horario,dia,labo]
        return valores 

    def ImprimirResultado(self):
        resultado={}
        self.horaH.sort()
        codigo=[]
        curso=[]
        Profesor=[]
        horaInicio=[]
        horaFin=[]
        dia=[]
        labo=[]
        for i in range(len(self.horaH)):
            Horario_y_Dia= self.ObtenerDiayHorario(self.horaH[i])
            numLabo = Horario_y_Dia[2]+1
            print(numLabo)
            codigo.append(self.cromosoma[self.horaH[i]][0])
            curso.append(self.cromosoma[self.horaH[i]][1])
            Profesor.append(self.cromosoma[self.horaH[i]][2])
            horaInicio.append(self.cromosoma[self.horaH[i]][3])
            horaFin.append(self.cromosoma[self.horaH[i]][4])
            dia.append(self.cromosoma[self.horaH[i]][5])
            labo.append(numLabo)
            resultado={'codigo':codigo,
                       'curso': curso,
                       'Profesor': Profesor,
                       'horaInicio': horaInicio,
                       'horaFin': horaFin,
                       'dia': dia,
                       'Labo_Asignado':labo
                      }
        return resultado

    def evaluar_individuo(self): 
        #Para evaluar por horario , dia y cantidad de laboratorio
        cantidad_Laboratorio = {
            0:41,
            1:30,
            2:41,
            3:41,
            4:41,
            5:36,
            6:36,
            7:41,
            8:20,
            9:41
        }
        for i in range(len(self.horaH)):
            for j in range(len(self.horaH)):
                Horario_y_Dia= self.ObtenerDiayHorario(self.horaH[i])
                if self.cromosoma[self.horaH[i]][0] == self.cursos.values[j][0]:
                    #Evaluar la cantidad de personas
                    numLabo = Horario_y_Dia[2]+1
                    #print("El numero de laboratorio es: {}".format(numLabo))
                    #print("Lo que se resta es: {} - {}".format(self.cromosoma[self.horaH[i]][6],cantidad_Laboratorio[Horario_y_Dia[2]]))
                    resto = self.cromosoma[self.horaH[i]][6] - cantidad_Laboratorio[Horario_y_Dia[2]]
                    #print("El resto es {}".format(resto))
                    if resto >=0 and resto <=10:
                        self.fitness += 3

                    elif resto >=10 and resto <=20:
                        self.fitness += 2

                    elif resto >=20 and resto <=30:
                        self.fitness += 1

                    elif resto < 0 and resto > -10:
                        self.fitness += -1
                    
                    elif resto < -10 and resto > -20:
                        self.fitness += -2

                    elif resto < -20 and resto > -30:
                        self.fitness += -3

                    else:
                        self.contadorDeErrores +=1
                        
                    
                    #Evalular el horario y el día
                    if Horario_y_Dia[0] ==  self.cursos.values[j][3]:
                        #print("Los valores comparados son: {} == {}".format(Horario_y_Dia[0],self.cursos.values[j][3]))
                        self.fitness += 3
                    else:
                        #print("Los valores comparados son: {} != {}".format(Horario_y_Dia[0],self.cursos.values[j][3]))
                        self.fitness -= 3

                    if Horario_y_Dia[1] ==  self.cursos.values[j][5]:
                        #print("Los valores comparados son: {} == {}".format(Horario_y_Dia[1],self.cursos.values[j][5]))
                        self.fitness += 3
                    else:
                        #print("Los valores comparados son: {} != {}".format(Horario_y_Dia[1],self.cursos.values[j][5]))
                        self.fitness -= 3
                    break

        #print("Para el cromosoma su fitnees es {}".format(self.fitness))


