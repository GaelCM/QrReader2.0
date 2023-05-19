import pyqrcode
import png
from pyqrcode import QRCode
from datetime import datetime



# Creamos los ID de los código QR, utilizamos código ASCCI para generar los qr
# creamos nuestra variable

cantidad=20920101

# En esta parte del código le decimos cuantos QR vamos a generar



while cantidad <= 20920105:
    now = datetime.now()  # Obtener la fecha y hora actuales
    fecha = now.strftime("%Y-%m-%d")  # Obtener la fecha actual en formato AAAA-MM-DD

    roster = cantidad  # guardamos la información
    numControl = '74' + str(cantidad)  # creamos el número de control
    info = numControl + "-" + fecha   # Combinamos el número de control y la fecha

    qr = pyqrcode.create(info, error='L')  # Generamos nuestro codigo QR con la información combinada
    qr.png('G' + str(roster) + '.png', scale=6)  # Creamos nuestro QR en formato PNG
    cantidad = cantidad + 1  # Aumento

