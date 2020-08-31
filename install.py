#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Modules

#External Modules
import itertools
import time
import os
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

def clean():
    """ Limpia la consola de comandos. """

    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')
    else:
        pass

def logo():
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

def install():
    """ Inicia el proceso de instalación. """

    bucle = itertools.cycle("/-\|")
    for i in range(30):
        print("{}[{}*{}] {}Installing Modules...{}{}".format(color.cyanColor, color.whiteColor, color.cyanColor, color.greenColor, next(bucle),color.whiteColor), end='\r')
        time.sleep(0.1)
    print("")
    print("")
    os.system("python3 -m pip install requests")
    print("")
    print("                     {}>> Installation Complete <<{}".format(color.blueColor, color.resetColor))
    print("")
    time.sleep(1)

#Start
clean()
logo()
install()
