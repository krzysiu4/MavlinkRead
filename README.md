Kompilacja
========

```
$ git clone https://www.github.com/krzysiu4/MavlinkRead
$ cd Source/
$ make
```

Użycie
========

```
$ ./mavlink_control -d /dev/ttyUSB0 -b 57600
```

Użycie Python
==============

Do użycia potrzebne są następujące pliki: 
- geotagPixhawk.py 
- mavlink_control - zbudowany oraz z nadanymi prawami do wykonywania

Wywołanie funkcji:

```
import geotagPixhawk as gp
gp.geotagPhotoWithPixhawkData("/dev/ttyACM0", "./a.jpg")
```

Przykład wywołania ze skryptu w Pythonie umieszczony w katalogu Example w pliku geotagTest.py
