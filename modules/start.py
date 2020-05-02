#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Inicio de la herramienta GeoTrackerIP. """

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
    
    def logo(self):
        """ Imprime logo de la herramienta GeoTrackerIP. """

        print("")
        print("     {} __ ___ __ {}_____ ___  __   ____  _____ ___   {} _ ___ ".format(self.blue, self.green, self.cyan))
        print("     {}/ _] __/__\{}_   _| _ \/  \ / _/ |/ / __| _ \{}__{}| | _,\ ".format(self.blue, self.green, self.white, self.cyan))
        print("    {}| [/\ _| \/ |{}| | | v / /\ | \_|   <| _|| v /{}__{}| | v_/ ".format(self.blue, self.green, self.white, self.cyan))
        print("     {}\__/___\__/ {}|_| |_|_\_||_|\__/_|\_\___|_|_\  {}|_|_|   {}v2.0 ".format(self.blue, self.green, self.cyan, self.white))
        print("")
        print("               {}<<< {}Tool coded by:{} @JRIC2002 {}>>>{}".format(self.red, self.yellow, self.white, self.red, self.white))
        print("    {}<<< {}Description:{} Geolocate an IP address or Domain {}>>>{}".format(self.red, self.yellow, self.white, self.red, self.white))
        print("")

    def help_menu(self):
        """ Imprime el menú de ayuda de la herramienta GeoTrackerIP. """

        print("{}Usage: python3 GeoTrackerIP.py [options]".format(self.white))
        print("")
        print("Options:")
        print("   -h, --help              Show this help message and exit.")
        print("   -v, --version           Show program's version number and exit.")
        print("")
        print("   Target:")
        print("      At least one of these options has to be provided to define the target(s).")
        print("")
        print("      -t, --target            IP Address or Domain to be analyzed.")

    def version(self):
        """ Imprime la version de la herramienta GeoTrackerIP. """

        print("{}#GeoTrackerIP version 2.0".format(self.white))
    
    def error_args(self):
        """ Imprime un mensaje de error de argumentos. """

        print("{}Usage: python3 GeoTrackerIP.py [options]".format(self.white))
        print("")
        print("GeoTrackerIP.py: Error: Invalid option.")
        print("Use -h or --help to see the options.")
        
#START
function = MyClass()
if __name__ == "__main__":
    print("{}Esto es un módulo...".format(function.white))
