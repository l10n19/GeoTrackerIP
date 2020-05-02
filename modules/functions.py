#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Funcionalidades de la herramienta GeoTrackerIP. """

__author__ = "JRIC2002"
__copyright__ = "Copyright 2019, JRIC2002"
__credits__ = "JRIC2002"
__license__ = "GNU General Public License v3.0"
__version__ = "2.0"
__maintainer__ = "JRIC2002"
__email__ = "joselito18032002@gmail.com"
__status__ = "Production"

class MyClass:
    def __init__(self):
        """ Variables de instancia. """

        #COLORS

        #Foreground
        self.black = "\033[0;30m"
        self.gray = "\033[1;30m"
        self.red = "\033[1;31m"
        self.green = "\033[1;32m"
        self.yellow = "\033[1;33m"
        self.blue = "\033[1;34m"
        self.magenta = "\033[1;35m"
        self.cyan = "\033[1;36m"
        self.white = "\033[1;37m"

        #Background
        self.b_black = "\033[0;40m"
        self.b_gray = "\033[1;40m"
        self.b_red = "\033[1;41m"
        self.b_green = "\033[1;42m"
        self.b_yellow = "\033[1;43m"
        self.b_blue = "\033[1;44m"
        self.b_magenta = "\033[1;45m"
        self.b_cyan = "\033[1;46m"
        self.b_white = "\033[1;47m"

    def geolocation_ip(self, ip):
        """ Geolocaliza una dirección IP o dominio. """
        #Datos del usuario
        try:
            print("{}IP Address/Domain(URL):{} {}".format(self.blue, self.white, ip))
            while True:
                if "http://" in ip:
                    ip = ip[7:]
                elif "www." in ip:
                    ip = ip[4:]
                elif "https://" in ip:
                    ip = ip[8:]
                else:
                    break
    
            api_url = "http://ip-api.com/json/"
            res = requests.get(api_url+ip)
            datos = json.loads(res.content)
    
            #Resultados almacenados en variables
            target = ip
            direccion_ip = datos['query']
            asn = datos['as']
            ciudad = datos['city']
            pais = datos['country']
            codigo_pais = datos['countryCode']
            isp = datos['isp']
            latitud = datos['lat']
            longitud = datos['lon']
            organizacion = datos['org']
            codigo_region = datos['region']
            region = datos['regionName']
            timezone = datos['timezone']
            codigo_zip = datos['zip']
            google_maps = "https://www.google.com/maps/search/?api=1&query={},{}".format(latitud, longitud)
    
            #Imprime los resultados
            print("")
            print("{}[{}*{}] {}Target:{} {}".format(self.green, self.white, self.green, self.white, self.green, target))
            print("{}[{}*{}] {}IP:{} {}".format(self.green, self.white, self.green, self.white, self.green, direccion_ip))
            print("{}[{}*{}] {}ASN:{} {}".format(self.green, self.white, self.green, self.white, self.green, asn))
            print("{}[{}*{}] {}City:{} {}".format(self.green, self.white, self.green, self.white, self.green, ciudad))
            print("{}[{}*{}] {}Country:{} {}".format(self.green, self.white, self.green, self.white, self.green, pais))
            print("{}[{}*{}] {}Country Code:{} {}".format(self.green, self.white, self.green, self.white, self.green, codigo_pais))
            print("{}[{}*{}] {}ISP:{} {}".format(self.green, self.white, self.green, self.white, self.green, isp))
            print("{}[{}*{}] {}Latitude:{} {}".format(self.green, self.white, self.green, self.white, self.green, latitud))
            print("{}[{}*{}] {}Longitude:{} {}".format(self.green, self.white, self.green, self.white, self.green, longitud))
            print("{}[{}*{}] {}Organization:{} {}".format(self.green, self.white, self.green, self.white, self.green, organizacion))
            print("{}[{}*{}] {}Region Code:{} {}".format(self.green, self.white, self.green, self.white, self.green, codigo_region))
            print("{}[{}*{}] {}Region Name:{} {}".format(self.green, self.white, self.green, self.white, self.green, region))
            print("{}[{}*{}] {}Timezone:{} {}".format(self.green, self.white, self.green, self.white, self.green, timezone))
            print("{}[{}*{}] {}Zip Code:{} {}".format(self.green, self.white, self.green, self.white, self.green, codigo_zip))
            print("{}[{}*{}] {}Google Maps:{} {}".format(self.green, self.white, self.green, self.white, self.green, google_maps))
            print("{}".format(self.white))
        except Exception:
            print("")
            print("{}Error: IP Address/Domain(URL) does not exist.{}".format(self.red, self.white))

#START
function = MyClass()
if __name__ == "__main__":
    print("Esto es un módulo...")
