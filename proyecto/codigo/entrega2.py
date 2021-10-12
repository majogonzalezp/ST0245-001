import numpy as np
import cv2
import matplotlib as plt
    
def compresionImg():
    imagen = cv2.imread("vacasana.jpg") #se "lee" la imagen
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    imagenNueva = []

    for i in range(0, len(imagen)-1, 2): # len(imagen) es el numero de filas, corre de dos en dos
        filaNueva = []
        for a in range(0, len(imagen[0], 2)): # len(imagen[0], es el número de columnas, va de dos en dos
            filaNueva.append(imagen[i][a]) #el arreglo tendrá las filas y columnas que se hicieron en los for
            imagenNueva.append(filaNueva) #arreglo dentro de un arreglo, se crea la matriz

    imagenNuevaNp = np.array(imagenNueva)
    """plt.imshow(imagen)
    plt.show()
    plt.imshow(imagenNueva)
    plt.show()
    """
    cv2.imwrite("vacasanaComprimida.jpg", imagenNuevaNp)


    def main():
        compresionImg()
        print('-'*44, "Se comprimio la imagen!!!" '-'*44)
    main()


    
