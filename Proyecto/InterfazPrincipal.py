import numpy as np
from tkinter import *
from Analisis import Analisis
from idlelib.tooltip import Hovertip
from tkinter import messagebox

"""
Metodo encargado de mostrar la matriz construida por la clase de Analisis.
"""

def generar_matriz():
    v1 = int(cuota_sup.get()) < int(cuota_inf.get())
    v2 = int(periodo_sup.get()) < int(periodo_inf.get())

    if v1 or v2:
        messagebox.showinfo("Alerta!!","La cuota o el periodo superiores son menores que los inferiores,"
        +" por favor revise los valores y vuelva a intentarlo")
    else:   
        analisis = Analisis(float(intereses.get()),int(cuota_sup.get()), int(cuota_inf.get()),
                    int(cuota_int.get()),int(periodo_sup.get()),int(periodo_inf.get()),
                    int(periodo_int.get()))
        
        matriz = analisis.calcular_matriz()
        width = (len(matriz)*80)+200
        height = (len(matriz[0])*30)+30
        dimens = str(width)+"x"+str(height)
        popUp = Tk()
        popUp.geometry(str(dimens))
        popUp.title("resultados")
        periodos = analisis.calcular_periodos()
        label = Label(popUp, text="periodos", fg='red', font=("arial", 8))
        label.place(x=15, y=0)
        for fila in range(len(matriz)):
            label = Label(popUp, text=str(periodos[fila]), fg='blue', font=("arial", 10))
            label.place(x=(80 * fila) + 80, y=0)

        cuotas = analisis.calcular_cuotas()
        label = Label(popUp, text="cuotas", fg='red', font=("arial", 8))
        label.place(x=5, y=15)
        for columna in range(len(matriz[0])):
            label = Label(popUp, text=str(cuotas[columna]), fg='blue', font=("arial", 10))
            label.place(x=5, y=(30 * columna) + 30)

        for filas in range(len(matriz)):
            for columnas in range(len(matriz[0])):
                label = Label(popUp, text=str(matriz[filas][columnas]), fg='black', font=("arial", 10))
                label.place(x=(80*filas)+80, y=(30*columnas)+30)


"""
espacio raiz del aplicativo con su titulo
"""
raiz = Tk()
raiz.title("Análisis de sensibilidad financieros")

"""
Frame principal de la vista
"""
ventana = Frame(raiz, width=500, height=450)

"""
Label del titulo de la ventana
"""
mi_label = Label(ventana, text="Analisis Financiero de prestamos",fg='black', font=("arial",24))
mi_label.place(x=15,y=0)
Hovertip(mi_label, text="Puto el que lo lea", hover_delay=200)
#mi_label.grid(row=0, column=0, padx=5, pady=10,columnspan=2)

"""
Label y espacio de texto para la tasa de interes
"""

lab_interes = Label(ventana, text="Tasa de Interes:", font=("arial",16))
lab_interes.place(x=110,y=70)
Hovertip(lab_interes, text="¿Qué tasa de interes le ofrecen?", hover_delay=200)
#lab_interes.grid(row=1,column=0,sticky="E",padx=20)

intereses = StringVar()
text_interes = Entry(ventana, textvariable = intereses)
text_interes.place(x=277,y=77)
#text_interes.grid(row=1,column=1,sticky="W",padx=20,pady=15)

# ------------------------------------------------------------------------------------------

"""
Labels y espacios de texto para los valores requeridos de periodo.
"""

lab_sup_periodo = Label(ventana, text="Rango de periodo Superior:", font=("arial",12))
lab_sup_periodo.place(x=70,y=127)
Hovertip(lab_sup_periodo, text="¿Qué tantos periodos le gustaria extender el pago?", hover_delay=200)
#lab_sup_periodo.grid(row=2,column=0,sticky="E",padx=20)
periodo_sup = StringVar()
text_sup_periodo = Entry(ventana,  textvariable = periodo_sup)
text_sup_periodo.place(x=277,y=131)
#text_sup_periodo.grid(row=2,column=1,sticky="W",padx=20)

lab_inf_periodo = Label(ventana, text="Rango de periodo Inferior:", font=("arial",12))
lab_inf_periodo.place(x=70,y=151)
Hovertip(lab_inf_periodo, text="¿Qué tan poco períodos cree podria necesitar?", hover_delay=200)
#lab_inf_periodo.grid(row=3,column=0,sticky="E",padx=20)
periodo_inf = StringVar()
text_inf_periodo = Entry(ventana,  textvariable = periodo_inf)
text_inf_periodo.place(x=277,y=155)
#text_inf_periodo.grid(row=3,column=1,sticky="W",padx=20)

intervalo_periodo = Label(ventana, text="Tamaño de intervalos:", font=("arial",12))
intervalo_periodo.place(x=70,y=175)
Hovertip(intervalo_periodo, text="¿en que intervalos le gustaria ver las estimaciones?", hover_delay=200)
#intervalo_periodo.grid(row=4,column=0,sticky="E",padx=20)
periodo_int = StringVar()
intervalo_periodo = Entry(ventana,  textvariable = periodo_int)
intervalo_periodo.place(x=277,y=179)
#intervalo_periodo.grid(row=4,column=1,sticky="W",padx=20)

# --------------------------------------------------------------------------------------------

"""
Labels y espacios de texto para los valores requeridos de las cuotas.
"""

lab_sup_cuota = Label(ventana, text="Valor maximo de Cuota:", font=("arial",12))
lab_sup_cuota.place(x=70,y=240)
Hovertip(lab_sup_cuota, text="¿Que tanto podria pagar en cada cuota?", hover_delay=200)
#lab_sup_cuota.grid(row=5,column=0,sticky="E",padx=20)
cuota_sup = StringVar()
text_sup_cuota = Entry(ventana, textvariable = cuota_sup)
text_sup_cuota.place(x=277,y=243)
#text_sup_cuota.grid(row=5,column=1,sticky="W",padx=20)

lab_inf_cuota = Label(ventana, text="Valor minimo de Cuota:", font=("arial",12))
lab_inf_cuota.place(x=70,y=265)
Hovertip(lab_inf_cuota, text="¿Cuanto seria el valor mínimo estimado para la cuota?", hover_delay=200)
#lab_inf_cuota.grid(row=6,column=0,sticky="E",padx=20)
cuota_inf = StringVar()
text_inf_cuota = Entry(ventana,  textvariable = cuota_inf)
text_inf_cuota.place(x=277,y=267)
#text_inf_cuota.grid(row=6,column=1,sticky="W",padx=20)

intervalo_cuota = Label(ventana, text="Tamaño de intervalos:", font=("arial",12))
intervalo_cuota.place(x=70,y=288)
Hovertip(intervalo_cuota, text="¿en que intervalos le gustaria ver las estimaciones?", hover_delay=200)
#intervalo_cuota.grid(row=7,column=0,sticky="E",padx=20)
cuota_int = StringVar()
intervalo_cuota = Entry(ventana,  textvariable = cuota_int)
intervalo_cuota.place(x=277,y=290)
#intervalo_cuota.grid(row=7,column=1,sticky="W",padx=20)

"""
Boton para generar la matriz
"""

boton = Button(ventana, text="Generar matriz de sensibilidad", font=("arial",12),command=generar_matriz)
boton.place(x=140,y=350)

ventana.pack()
raiz.mainloop()