#
#
# Copyright (c) 2020 Adrian Campazas Vega, Ignacio Samuel Crespo Martinez, Angel Manuel Guerrero Higueras.
#
# This file is part of DOROTHEA 
#
# DOROTHEA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DOROTHEA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import absolute_import
from attacks.celery import app
from pexpect import pxssh
import nmap
import os
import random
import time
import subprocess as sp
import time



@app.task
#def scan_ports(start_port,end_port,scanner_type): 
def scan_ports(): 
	#timeSleep = random.randrange(3,5)
	#results = nm.scan(randomize_ip(), str(start_port) + '-'+ str(end_port) ,arguments=scanner_type + ' --scan-delay '+str(timeSleep))
	#nm = nmap.PortScanner()
	#results = nm.scan(randomize_ip(), str(start_port) + '-'+ str(end_port) ,arguments=scanner_type)
        print("Lanzo spam")
        os.system("python3 spam.py")	


def randomize_ip():
        randIP = random.randrange(5,205)
        ip = "140.30.20." + str(randIP)
        print("IP: " + ip)
        return ip
