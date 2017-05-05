import subprocess
import os.path
import piexif

def geotagPhotoWithPixhawkData(device, image_path):
	args = ("./mavlink_control", "-d", device, "-b", "57600")
	popen = subprocess.Popen(args, stdout=subprocess.PIPE)
	popen.wait()
	output = popen.stdout.read()
	GPSData = output.split()
	latitude = longitude = relative_altitude = heading = 0
	
	if len(GPSData) > 9:
		latitude = float(GPSData[1])
		longitude = float(GPSData[3])
		relative_altitude = int(float(GPSData[7]))
		heading = int(float(GPSData[9]))
	
	if (relative_altitude < 0):  # Sprawdza czy wysokosc jest wieksza od 0 - musi byc zeby dzialala funkcja piexfi.dump
	    relative_altitude = 0
	    
	if (latitude < 0):    		 # Szerokosc i dlugosc geograficzna musza byc dodatnie, a zmienia sie N->S, W->E
		latitude = latitude * -1
		latitudeRef = "S"
	else:
		latitudeRef = "N"
	
	if (longitude < 0):
		longitude = longitude * -1
		longitudeRef = "W"
	else:
		longitudeRef = "E"
	
	if (not os.path.exists(image_path)): # Jesli plik nie istnieje
		print "No file found to geotag"
		return;
	
	exif_dict = piexif.load(image_path) # Wczytuje dane EXIF ze zdjecia
	    
	gps_ifd = {
	          piexif.GPSIFD.GPSLatitude: ( (latitude*10000000,10000000) ,(0,1), (0,1)),
			  piexif.GPSIFD.GPSLatitudeRef: (latitudeRef),
	          piexif.GPSIFD.GPSLongitude: ( (longitude*10000000,10000000), (0,1), (0,1)),
	          piexif.GPSIFD.GPSLongitudeRef: (longitudeRef),
	          piexif.GPSIFD.GPSAltitude: (relative_altitude,1),
	          piexif.GPSIFD.GPSImgDirection: (heading,1)
	          }
	           
	exif_dict["GPS"] = gps_ifd
	exif_bytes = piexif.dump(exif_dict)
	piexif.insert(exif_bytes, image_path) 		 # Zapisuje dane EXIF do zdjecia
	

#geotagPhotoWithPixhawkData("/dev/ttyACM0", "./a.jpg")
