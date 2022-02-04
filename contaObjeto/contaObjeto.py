#sistema que faz a contagem de objetos desconsiderando a cor
#pg 245

import cv2
import numpy as np

totalAnterior = 0
video = cv2.VideoCapture(0)

while True:
    _, frameRGB = video.read()
    frameCinza = cv2.cvtColor(frameRGB, cv2.COLOR_BGR2GRAY)
    tipo = cv2.THRESH_BINARY_INV
    _, frameBinarizado = cv2.threshold(frameCinza, 200, 255, tipo)

    contornos, hierarquia = cv2.findContours(frameBinarizado, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    totalAtual = len(contornos)
    if totalAtual != totalAnterior:
        totalAnterior = totalAtual

        cv2.imshow("Video", frameRGB)
        cv2.imshow("Threshold", frameBinarizado)
        if cv2.waitKey(1) & 0xFF == ("q"):
            break

            video.release()
            cv2.destroyAllWindows()