import cap as cap
import cv2
import pyqrcode
import png
from pyqrcode import QRCode
from pyzbar.pyzbar import decode
import numpy as np

camara = cv2.VideoCapture(0)

while True:
    #Empezamos a abrir la camara para leer los códigos
    ret, frame = camara.read()  # Sirve para verificar si se ha leido correctamente un fps para almacenarlo

    #Leemos los código qr

    # Decodificamos el código mientras este activo el Frame
    for codes in decode(frame):
        #Decoficamos el contenido del QR
        info = codes.data.decode('utf-8')

        #Sacamos el tipo de personal
        tipo=info[0:2]
        tipo=int(tipo)

        #EXtraemos coordenadas

        pts = np.array([codes.polygon], np.int32)
        xi, yi = codes.rect.left, codes.rect.top

        #Redimensionamos
        pts=pts.reshape((-1,1,2))

        if tipo==74:
            #empezamos a dibujar
            cv2.polylines(frame,[pts],True,(0,255,255),5)
            cv2.putText(frame,'SO'+str(info[2:]),(xi-15,yi-15),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)
            print("El usuario es un estudiante \n"
                "Numero de control: G",str(info[2:]))


    cv2.imshow("Lector de QR", frame)

    esc = cv2.waitKey(5)
    if esc==27:
        break

cv2.destroyAllWindows()
cap.release()

