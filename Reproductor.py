"""import numpy as np
import cv2

# Cargamos la imagen
original = cv2.imread("C:/Users/Usuario/PycharmProjects/Proyecto#2_SO/Projects/Cartago/Images/frame2.jpg")
original = cv2.resize(original,(800, 600))
original = seg = cv2.pyrMeanShiftFiltering(original,50,50)
cv2.imshow("original", original)

# Convertimos a escala de grises
gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

# Aplicar suavizado Gaussiano
gauss = cv2.GaussianBlur(gris, (5, 5), 0)

cv2.imshow("suavizado", gauss)

# Detectamos los bordes con Canny
canny = cv2.Canny(gauss, 50, 150)

cv2.imshow("canny", canny)

# Buscamos los contornos
(contornos, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Mostramos el número de monedas por consola
print("He encontrado {} objetos".format(len(contornos)))

cv2.drawContours(original, contornos, -1, (0, 0, 255), 2)
cv2.imshow("contornos", original)

cv2.waitKey(0)

"""


import cv2
import numpy as np

#cam = cv2.VideoCapture('C:/Users/Usuario/Downloads/cartago.mp4')

frame = cv2.imread('C:/Users/Usuario/PycharmProjects/Proyecto#2_SO/Projects/Cartago/Images/frame23.jpg', 1)
frame = cv2.resize(frame,(1280, 720))

kernel = np.ones((5, 5), np.uint8)
seg = cv2.pyrMeanShiftFiltering(frame,50,37)
hsv = cv2.cvtColor(seg, cv2.COLOR_BGR2HSV)
#gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY
#ret,binary = cv2.threshold(gris,127,255,cv2.THRESH_BINARY_INV)
# ret, frame = cam.read()
rangomax = np.array([220,198,209])
rangomin = np.array([58,14,36])
mascara = cv2.inRange(hsv, rangomin, rangomax)
opening = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
x, y, w, h = cv2.boundingRect(opening)
crop_img = frame[y:h+y,x:w ]

cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
#crop_img = frame[x:y, w:h]
#cv2.circle(frame, (x + w / 2, y + h / 2), 5, (0, 0, 100), -1)
cv2.imshow('camara', seg)
cv2.imshow('camara1', frame)
cv2.imshow('camara2', hsv)
cv2.imshow('camara3', crop_img)
#cv2.imwrite('C:/Users/Usuario/PycharmProjects/Proyecto#2_SO/Projects/Cartago/Images/framerf.jpg', frame)
cv2.waitKey(0)

