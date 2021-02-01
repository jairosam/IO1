import math
import pandas as pd

"""
La clase "Analisis" es la clase que se va a encargar de calcular la matriz de sensibilidad
"""

class Analisis:

    """
    Constructor de clase
    """
    def __init__(self, interes, cuota_sup, cuota_inf, cuota_int, periodo_sup, periodo_inf,periodo_int):
        self.tasa_interes = interes/100
        self.cuota_sup = cuota_sup
        self.cuota_inf = cuota_inf
        self.cuota_int = cuota_int
        self.periodo_sup = periodo_sup
        self.periodo_inf = periodo_inf
        self.periodo_int = periodo_int
    
    """
    metodo "VPN" que se encarga de calcular el valor presente neto de un financiamiento
    utilizando el numero de cuotas y el valor de las mismas  
    """

    def VPN(self,n_cuotas,valor_cuota):
        valores = []
        for i in range(1,n_cuotas+1):
            valores.append((valor_cuota)/math.pow(1+self.tasa_interes,i))
        return sum(valores)

    """
    Calcula y retorna una lista que contiene los periodos sobre los cuales se va a realizar el análisis
    de sensibilidad
    """

    def calcular_periodos(self):
        periodos = [i for i in range(self.periodo_inf, self.periodo_sup,self.periodo_int)]
        periodos.append(self.periodo_sup)
        return periodos
        
    """
    Calcula los valores de las cuotas sobre los que se va a generar la matriz
    """

    def calcular_cuotas(self):
        cuotas = [i for i in range(self.cuota_inf, self.cuota_sup, self.cuota_int)]
        cuotas.append(self.cuota_sup)
        return cuotas

    """
    calcula y retorna la matriz de sensibilidad. (utiliza la función "VPN" para calcular los posibles financiamientos en 
    dados los distintos periodos y las distintas cuotas calculadas en los metodos anteriores)
    """

    def calcular_matriz(self):
        periodos = self.calcular_periodos()
        cuotas = self.calcular_cuotas()
        matriz = []
        print(periodos)
        for i in range(len(periodos)):
            fila = [] 
            incre = int(periodos[i]/12)
            self.tasa_interes += incre*self.promediosAnio()
            print(self.tasa_interes,incre)
            for cuota in cuotas:
                fila.append(round(self.VPN(periodos[i],cuota),0))
            matriz.append(fila)
        return matriz 

    def tasas(self):
        datos = pd.read_excel("tasas.xlsx")
        datos["tasa"] = datos.tasa/100
        return datos

    def promediosAnio(self):
        datos = self.tasas()
        tasas = []
        for i in range(2006,2017):
            tasas.append(datos.loc[datos.Anio == i].tasa.sum())

        incrementos = []
        for i in range(len(tasas)):
            if i+1 < len(tasas):
                incrementos.append(tasas[i] - tasas[i+1])
        return sum(incrementos)/len(incrementos)

#a = Analisis(1,2,3,4,5,6,7)
#b = a.calcular_matriz()
#datos = a.tasas()



