# Import pliku GeotagPixhawk.py - musi znajdowac sie w katalogu projektu
import GeotagPixhawk as gp

# Odczytuje dane z Pixhawka
GPSData = gp.readDataFromPixhawk("/dev/ttyUSB0", "57600") # Zwraca (latitude, longitude, relative_altitude, heading)

# Geotagowanie zdjecia
gp.geotagPhoto(GPSData[0], GPSData[1], GPSData[2], GPSData[3], "./capt0000.jpg") # Przyjmuje argumenty (latitude, longitude, relative_altitude, heading, sciezka)

