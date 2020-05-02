#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#[*] Name of the tool: GeoTrackerIP
#[*] Description: Geolocate an IP address or Domain.
#[*] Version: 2.0
#[*] Author: JRIC2002
#[*] Date of creation: 15/03/2019
#[*] Date of last update: 01/05/2020

#MODULES

#External Modules
import requests
import json
import sys

#Internal Modules
from modules import logo
from modules import functions

#COLORS

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

#START
if len(sys.argv) == 3:
    if sys.argv[1] == "-t" or sys.argv[1] == "--target":
        logo.function.logo()
        functions.function.geolocation_ip(sys.argv[2])
    else:
        logo.function.logo()
        logo.function.error_args()
elif len(sys.argv) == 2:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        logo.function.logo()
        logo.function.help_menu()
    elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
        logo.function.logo()
        logo.function.version()
    else:
        logo.function.logo()
        logo.function.error_args()
elif len(sys.argv) == 1:
    logo.function.logo()
    logo.functionhelp_menu()
else:
    logo.function.logo()
    logo.function.error_args()
