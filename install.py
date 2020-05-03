#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#MODULES

#External Modules
import itertools
import time
import os
import sys

#Internal Modules

class Color:
    """ Colores en código ANSI. """

    #Foreground
    black = "\033[0;30m"
    gray = "\033[1;30m"
    red = "\033[1;31m"
    green = "\033[1;32m"
    yellow = "\033[1;33m" 
    blue = "\033[1;34m"
    magenta = "\033[1;35m"
    cyan = "\033[1;36m"
    white = "\033[1;37m"
    
    #Background
    b_black = "\033[0;40m"
    b_gray = "\033[1;40m"
    b_red = "\033[1;41m"
    b_green = "\033[1;42m"
    b_yellow = "\033[1;43m"
    b_blue = "\033[1;44m"
    b_magenta = "\033[1;45m"
    b_cyan = "\033[1;46m"
    b_white = "\033[1;47m"

#Instancia de la clase Color
color = Color()

def clean():
    """ Limpia la consola. """

    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')
    else:
        pass

def logo():
    """ Imprime logo de la herramienta GeoTrackerIP. """

    print("")
    print("     {}__ ___ __ {}_____ ___  __   ____  _____ ___   {} _ ___ ".format(color.blue, color.green, color.cyan))
    print("     {}/ _] __/__\{}_   _| _ \/  \ / _/ |/ / __| _ \{}__{}| | _,\ ".format(color.blue, color.green, color.white, color.cyan))
    print("    {}| [/\ _| \/ |{}| | | v / /\ | \_|   <| _|| v /{}__{}| | v_/ ".format(color.blue, color.green, color.white, color.cyan))
    print("     {}\__/___\__/ {}|_| |_|_\_||_|\__/_|\_\___|_|_\  {}|_|_|   {}v2.0 ".format(color.blue, color.green, color.cyan, color.white))
    print("")
    print("               {}<<< {}Tool coded by:{} @JRIC2002 {}>>>{}".format(color.red, color.yellow, color.white, color.red, color.white))
    print("    {}<<< {}Description:{} Geolocate an IP address or Domain {}>>>{}".format(color.red, color.yellow, color.white, color.red, color.white))
    print("")

def install():
    """ Inicia el proceso de instalación. """

    bucle = itertools.cycle("/-|-\|")
    for i in range(30):
        print("{}[{}*{}] {}Installing Modules...{}{}".format(color.cyan, color.white, color.cyan, color.green, next(bucle),color.white), end='\r')
        time.sleep(0.1) 
    print("")
    print("")
    os.system("python3 -m pip install requests")
    print("")
    print("                     {}>> Installation Complete <<{}".format(color.blue, color.white))
    print("")
    time.sleep(1)

#START
clean()
logo()
install()
