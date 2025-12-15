import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
from scipy import ndimage

"""
Cálculo (sencillo y poco optimizado) del centro de masa de una imagen 2D
Se toma una imagen 2D en blanco y negro y se convierte la escala de blancos y negros a valores entre 0 y 1
(0 siendo blanco (m=0) y 1 siendo negro (m = 1)
Luego, para cada pixel y sus coordenadas, se va realizando la suma correspondiente a sum(m_ij * (x_ij, y_ij)) y 
se va guardando este resultado en un vector.
Finalmente, se lo divide por las "masas" de todos los pixeles.
"""




def get_center_mass(imgArray):
    # Calcs center of mass from the left bottom pixel of the screen as the center of coordinates.
    x_coords = np.arange(0, imgArray.shape[0], 1, dtype=int)
    y_coords = np.arange(0, imgArray.shape[1], 1, dtype=int)
    vec = 0
    for x in x_coords - 1:
        for y in y_coords - 1:
            m = imgArray[x, y]
            vec += m * np.array([x, y])

    total_mass = np.sum(imgArray)
    finalVec = vec / total_mass
    return finalVec


def plot_cm(img):
    # Esta función plottea la imagen y su correspondiente centro de masa.
    img_array_cv2 = cv2.imread(img, 0)
    img_reverted = cv2.bitwise_not(img_array_cv2)

    new_img = img_reverted / 255.0
    print(img_array_cv2.shape)

    cm = get_center_mass(new_img)
    print(get_center_mass(new_img))

    fig, ax = plt.subplots()
    img = mpimg.imread(img)
    ax.imshow(img)

    cm2 = ndimage.center_of_mass(new_img)
    ax.scatter(cm2[0], cm2[1], c='blue', s=70, marker='x', label='Centro de Masa del sistema (scipy)')
    # Invert the y-axis
    ax.invert_yaxis()
    ax.scatter(cm[0], cm[1], c='red', s=70, marker='x', label='Centro de Masa del sistema')
    ax.set_xlabel('eje X')
    ax.set_ylabel('eje Y')
    ax.legend()
    plt.show()




def main():
    if __name__ == '__main__':
        plot_cm('manybody.png')


main()