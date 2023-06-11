import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd


def estimate_b0_b1(x, y):
    # Contamos el tamaño de x
    n = np.size(x)
    
    #obtener los promedios de X y de Y
    m_x, m_y = np.mean(x), np.mean(y)
    
    #Calcular sumatoria de XY y mi sumatoria de XX 
    sumatoria_xy = np.sum((x-m_x)*(y-m_y))
    sumatoria_xx = np.sum(x*(x-m_x)) # x*(x-m_x) == (x-m_x)**2

    #coeficientes de regersion 
    b_1 = sumatoria_xy/sumatoria_xx 
    b_0 = m_y - b_1*m_x
    
    return(b_0, b_1)

#Funcion de graficado
def plot_regression(x,y,b,ylabel): # b viene de b_1 y b_0
    # marker => diseño de los puntos, s => tamaño del marker
    plt.scatter(x, y, color = "g", marker = "o", s=10) 
    
    # Formula(ecuacion) linea de regresion
    y_pred = b[0] + b[1]*x
    print(f"Y = {b[0]} + {b[1]} X")
    plt.plot(x, y_pred, color = "b")

    #etiquetado
    plt.xlabel('Familias')
    plt.ylabel(ylabel)

    plt.show()

#Codigo main
def main():

    opcion = int(input("1 - Total envases \n2 - Total Co2\n "))

    #DATASET
    datos=pd.read_csv('datos.csv')
    integrantes = datos['¿Cuántos integrantes conforman su núcleo familiar?'].to_numpy()
    pet = datos['PET '].to_numpy()
    pead = datos['PEAD'].to_numpy()
    ps = datos['PS '].to_numpy()
    ldpe = datos['LDPE '].to_numpy()

    total = []
    ylabel = ""

    if(opcion == 1):
        for j in range(integrantes.size):
            total.append(pet[j]+pead[j]+ps[j]+ldpe[j])
        ylabel="Total envases" 
    else:
        for j in range(integrantes.size):
            total.append((pet[j]*9*1343000/1000000)+(pead[j]*115*1478000/1000000)+(ps[j]*24*2763000/1000000)+(ldpe[j]*24*1477000/1000000))
        ylabel="Total Co2" 

    x = np.array(integrantes)
    y = np.array(total)

    #Obtenemos b1 y b2
    b = estimate_b0_b1(x, y)


    #Graficamos nuestra linea de regresion
    plot_regression(x, y, b, ylabel)

if __name__ == "__main__":
    main()