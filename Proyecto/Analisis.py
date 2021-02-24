import math
import statistics as st
import numpy as np
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
    Función que calcula y retorna los aumentos de la tasa de interes dado el número maximo
    de periodos a analizar
    """

    def definir_intereses(self, periodos):
        interes = []
        datos = self.tasas()
        cv = self.promediosAnio(datos)
        for i in range(len(periodos)):
            interes.append(self.tasa_interes)
            self.tasa_interes += cv 
        return interes

    """
    calcula y retorna la matriz de sensibilidad. (utiliza la función "VPN" para calcular los posibles financiamientos en 
    dados los distintos periodos y las distintas cuotas calculadas en los metodos anteriores)
    """

    def calcular_matriz(self):
        periodos = self.calcular_periodos()
        cuotas = self.calcular_cuotas()
        interes = self.definir_intereses(periodos)
        matriz = []
        print(interes)
        for i in range(len(periodos)):
            fila = []
            self.tasa_interes = interes[i]
            for cuota in cuotas:
                fila.append(round(self.VPN(periodos[i],cuota),0))
            matriz.append(fila)
        return matriz 

    """
    Función que obtiene las tasas de interes obtenidas del banco de la republica.
    """

    def tasas(self):
        datos = pd.read_excel("TasasTarea.xlsx")
        return datos

    """
    Función que calcula el coeficiente de variación para predecir las tasas de interes
    """

    def promediosAnio(self, tasas):
        promedios = []
        for i in range(tasas.anio.min(),tasas.anio.max()+1):
            promedios.append(tasas.tasa[tasas.anio == i].mean())
        promedios = np.array(promedios)
        return (st.stdev(promedios)/np.mean(promedios))/100

            

a = Analisis(0.19,1500,500,100,72,12,12)
#b = a.calcular_matriz()
datos = a.tasas()
print(a.promediosAnio(datos))
#print(datos.anio.value_counts().keys()[0])


