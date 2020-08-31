#!/usr/bin/python3
# -*- coding: utf-8 -*-

#[*] Name of the tool: GeoTrackerIP
#[*] Description: Geolocate an IP address or Domain.
#[*] Version: 2.2
#[*] Author: JRIC2002
#[*] Date of creation: 15/03/2019

#Modules

#External modules
import requests
import json
import sys

class Color:
    """ Colores en código ANSI. """

    #Foreground
    blackColor = "\033[0;30m"
    grayColor = "\033[1;30m"
    redColor = "\033[1;31m"
    greenColor = "\033[1;32m"
    yellowColor = "\033[1;33m"
    blueColor = "\033[1;34m"
    purpleColor = "\033[1;35m"
    cyanColor = "\033[1;36m"
    whiteColor = "\033[1;37m"
    resetColor = "\033[0;0m"

    #Background
    blackBackColor = "\033[0;40m"
    grayBackColor = "\033[1;40m"
    redBackColor = "\033[1;41m"
    greenBackColor = "\033[1;42m"
    yellowBackColor = "\033[1;43m"
    blueBackColor = "\033[1;44m"
    purpleBackColor = "\033[1;45m"
    cyanBackColor = "\033[1;46m"
    whiteBackColor = "\033[1;47m"
    resetBackColor = "\033[0;0m"

#Instancia de la clase Color
color = Color()

class Start:
    """ Inicio de la herramienta GeoTrackerIP. """

    def __init__(self):
        """ Variables de instancia. """
        pass

    def logo(self):
        """ Imprime el logo de la herramienta GeoTrackerIP. """
    
        print("")
        print("      {}__ ___ __ {}_____ ___  __   ____  _____ ___   {} _ ___ ".format(color.blueColor, color.greenColor, color.cyanColor))
        print("     {}/ _] __/__\{}_   _| _ \/  \ / _/ |/ / __| _ \{}__{}| | _,\ ".format(color.blueColor, color.greenColor, color.whiteColor, color.cyanColor))
        print("    {}| [/\ _| \/ |{}| | | v / /\ | \_|   <| _|| v /{}__{}| | v_/ ".format(color.blueColor, color.greenColor, color.whiteColor, color.cyanColor))
        print("     {}\__/___\__/ {}|_| |_|_\_||_|\__/_|\_\___|_|_\  {}|_|_|   {}v2.2 ".format(color.blueColor, color.greenColor, color.cyanColor, color.whiteColor))
        print("")
        print("               {}<<< {}Tool coded by:{} @JRIC2002 {}>>>{}".format(color.redColor, color.yellowColor, color.whiteColor, color.redColor, color.whiteColor))
        print("    {}<<< {}Description:{} Geolocate an IP address or Domain {}>>>{}".format(color.redColor, color.yellowColor, color.whiteColor, color.redColor, color.resetColor))
        print("")
    
    def help_menu(self):
        """ Imprime el menú de ayuda de la herramienta GeoTrackerIP. """
    
        print("{}Usage: python3 GeoTrackerIP.py [options]".format(color.whiteColor))
        print("")
        print("Options:")
        print("   -h, --help              Show this help message and exit.")
        print("   -v, --version           Show program's version number and exit.")
        print("")
        print("   Target:")
        print("      At least one of these options has to be provided to define the target(s).")
        print("")
        print("      -t, --target            IP Address or Domain to be analyzed.{}".format(color.resetColor))
    
    def version(self):
        """ Imprime la versión de la herramienta GeoTrackerIP. """
    
        print("{}#GeoTrackerIP version 2.2{}".format(color.whiteColor, color.resetColor))
    
    def error_args(self):
        """ Imprime un mensaje de error de argumentos. """
    
        print("{}Usage: python3 GeoTrackerIP.py [options]".format(color.whiteColor))
        print("")
        print("GeoTrackerIP.py: Error: Invalid option.")
        print("Use -h or --help to see the help menu.{}".format(color.resetColor))

#Instancia de la clase Start
start = Start()

class Functions:
    """ Fucionalidades de la herramienta GeoTrackerIP. """
    
    def __init__(self):
        """ Variables de instancia. """
        pass

    def geolocation_ip(self, ip):
        """ Geolocaliza una dirección IP o dominio. """

        #Datos
        try:
            print("{}IP Address/Domain(URL):{} {}".format(color.blueColor, color.whiteColor, ip))
            while True:
                if "http://" in ip:
                    ip = ip[7:]
                elif "www." in ip:
                    ip = ip[4:]
                elif "https://" in ip:
                    ip = ip[8:]
                else:
                    break

            api_url = "http://ip-api.com/json/{}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,mobile,proxy,query".format(ip)
            res = requests.get(api_url)
            datos = json.loads(res.content)

            #Resultados almacenados en variables
            target = ip
            direccion_ip = datos['query']
            status = datos['status']
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
            mobile = datos['mobile']
            proxy = datos['proxy']
            google_maps = "https://www.google.com/maps/search/?api=1&query={},{}".format(latitud, longitud)

            #Imprime los resultados obtenidos
            print("")
            print("{}[{}*{}] {}Target:{} {}".format(color.greenColor, color.whiteColor, color.greenColor, color.whiteColor, color.greenColor, target))
            print("{}[{}*{}] {}Status:{} {}".format(color.greenColor, color.whiteColor, color.greenColor, color.whiteColor, color.greenColor, status))
            print("{}[{}*{}] {}IP:{} {}".format(color.greenColor, color.whiteColor, color.greenColor, color.whiteColor, color.greenColor, direccion_ip))
            print("{}[{}*{}] {}ASN:{} {}".format(color.greenColor, color.whiteColor, color.greenColor, color.whiteColor, color.greenColor, asn))
            print("{}[{}*{}] {}City:{} {}".format(color.greenColor, color.whiteColor, color.greenColor, color.whiteColor, color.greenColor, ciudad))
            print("{}[{}*{}] {}Country:{} {}".format(color.greenColor, color.whiteColor, color.greenColor, color.whiteColor, color.greenColor, pais))
            print("{}[{}*{}] {}Country Code:{} {}".format(color.greenColor, color.whiteColor, color.greenColor, color.whiteColor, color.greenColor, codigo_pais))
            print("{}[{}*{}] {}ISP:{} {}".format(color.greenColor, color.whiteColor, color.greenColor, color.whiteColor, color.greenColor, isp))
            print("{}[{}*{}] {}Latitude:{} {}".format(color.greenColor, color.whiteColor, color.greenColor, color.whiteColor, color.greenColor, latitud))
            print("{}[{}*{}] {}Longitude:{} {}".format(color.greenColor, color.whiteColor, color.greenColor, color.whiteColor, color.greenColor, longitud))
            print("{}[{}*{}] {}Organization:{} {}".format(color.greenColor, color.whiteColor, color.greenColor, color.whiteColor, color.greenColor, organizacion))
            print("{}[{}*{}] {}Region Code:{} {}".format(color.greenColor, color.whiteColor, color.greenColor, color.whiteColor, color.greenColor, codigo_region))
            print("{}[{}*{}] {}Region Name:{} {}".format(color.greenColor, color.whiteColor, color.greenColor, color.whiteColor, color.greenColor, region))
            print("{}[{}*{}] {}Timezone:{} {}".format(color.greenColor, color.whiteColor, color.greenColor, color.whiteColor, color.greenColor, timezone))
            print("{}[{}*{}] {}Zip Code:{} {}".format(color.greenColor, color.whiteColor, color.greenColor, color.whiteColor, color.greenColor, codigo_zip))
            print("{}[{}*{}] {}Mobile:{} {}".format(color.greenColor, color.whiteColor, color.greenColor, color.whiteColor, color.greenColor, mobile))
            print("{}[{}*{}] {}Proxy:{} {}".format(color.greenColor, color.whiteColor, color.greenColor, color.whiteColor, color.greenColor, proxy))
            print("{}[{}*{}] {}Google Maps:{} {}".format(color.greenColor, color.whiteColor, color.greenColor, color.whiteColor, color.greenColor, google_maps))
            print("{}".format(color.resetColor))
        except Exception:
            print("")
            print("{}Error: IP Address/Domain(URL) does not exist.{}".format(color.redColor, color.resetColor))

#Instancia de la clase Functions
functions = Functions()

#Start
if len(sys.argv) == 1:
    start.logo()
    start.help_menu()
elif len(sys.argv) == 2:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        start.logo()
        start.help_menu()
    elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
        start.version()
    else:
        start.logo()
        start.error_args()
elif len(sys.argv) == 3:
    if sys.argv[1] == "-t" or sys.argv[1] == "--target":
        start.logo()
        functions.geolocation_ip(sys.argv[2])
    else:
        start.logo()
        start.error_args()
else:
    start.logo()
    start.error_args()
