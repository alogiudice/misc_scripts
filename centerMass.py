import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

"""
Cálculo (sencillo y poco optimizado) del centro de masa de una imagen 2D
Se toma una imagen 2D en blanco y negro y se convierte la escala de blancos y negros a valores entre 0 y 1
(0 siendo blanco (m=0) y 1 siendo negro (m = 1)
Luego, para cada pixel y sus coordenadas, se va realizando la suma correspondiente a sum(m_ij * (x_ij, y_ij)) y 
se va guardando este resultado en un vector.
Finalmente, se lo divide por las "masas" de todos los pixeles.
"""


img_array_cv2 = cv2.imread('anillo.png', 0)
img_reverted = cv2.bitwise_not(img_array_cv2)

new_img = img_reverted / 255.0
print(img_array_cv2.shape)

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


cm = get_center_mass(new_img)
print(get_center_mass(new_img))


img = mpimg.imread('anillo.png')
plt.imshow(img)
plt.scatter(cm[0], cm[1], c='red', s=70, label='Centro de Masa del sistema')
plt.xlabel('eje X')
plt.ylabel('eje Y')
plt.legend()
plt.show()