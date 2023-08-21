# -*- coding: utf-8 -*-
"""
Created on Thurs Feb  2 20:35:51 2023

@author: Alan
"""
#ING. Tecnologías de la Información
#Sistemas Inteligentes 
#Alumno: Alan Zaid Hernandez Cruz.
#8°C 
#Matrícula: 2031119042 
#Docente: Dr. Julio Cesar Valdez Ahuatzi 
#07/02/23
                    
#Actividad: Regresión Lineal Simple en Python.
#Problema a resolver: Predicción del consumo energético en electrodoméstico en función de la temperatura.

#Agregamos las librerias correspondientes, matplotlib para graficar 
# Y Numpy as para manejar los datos 
import matplotlib.pyplot as plt
import numpy as np

print('Regresion Lineal Simple.\n')
print('Problema a resolver: Predicción del consumo energético en electrodoméstico en función de la temperatura.\n')

#Declaramos variables que nos permitan guardar los datos en los arreglos, le pasamos los datos recolectados a dos arreglos, 
#datos de temperatura y consumo energetico, dichos datos permitiran generar la grafica
temperatura= np.array([28.9, 30.00, 31.7, 32.2, 32.8, 33.9, 34.4, 34.4, 33.3, 32.2, 30.6, 29.4, 30.4, 31.5, 33.2])
ConsumoEnergetico= np.array([2893.54, 2714.04, 3171.77, 3123.3, 3283.06, 3284.5, 3449.99, 3449.99, 3231.00, 3227.41, 2961.75, 2949.19, 2897.59, 2620.07, 3259.02])


#Calculamos la media de la temperatura y la del consumo energético
mean_temp= np.mean(temperatura)
mean_consumo= np.mean(ConsumoEnergetico)


#Calculamos la suma de los productos cruzados (xi)(yi)
sum_xy= np.sum((temperatura-mean_temp)*(ConsumoEnergetico-mean_consumo))

#Calculamos la suma de los cuadrados de la temperatura(xi-media)^2
sum_xx= np.sum(np.power(temperatura-mean_temp, 2))


#Asignamos la variable (m) y guardamos en ella, para el calculo de la pendiente
m= sum_xy/sum_xx

#Calculamos el intercepto (b)
b= mean_consumo-m*mean_temp

#Creamos la variable predicciones y las calculamos, en base a la pendiente, temperatura e intercepto b
predicciones = m*temperatura+b

# Graficamos los resultados con la ayuda de la libreria matplotlib
plt.scatter(temperatura, ConsumoEnergetico)
plt.title('Predicción del Consumo Energético en Base a la Temperatura', color='red')
plt.plot(temperatura, predicciones, color='green')
plt.xlabel("Temperatura (°C)", color='red')
plt.ylabel("Consumo energético (kWh)", color='violet')


#Mandamos a llamar a la variable temperatura, la cual se le asignara un tipo de dato flotante
#para la entrada de datos y se pueda ingresar datos mediante el input 
temperatura= float(input("Ingresa la temperatura, para predecir el consumo energètico:" ))

#Creamos las predicciones, predi1 almacenara el calculo en base a la pendiente, temperatura e intercepto b
predi1= m*temperatura+b

#Imprimimos el resultado 
print("En base a la temperatura: {}°C,".format(temperatura), "El consumo energètico serà de: {:.1f} kWh".format(predi1))

#Mostramos la grafica 
plt.show()
