#!/usr/bin/python3
# 
# 20210105  Matthew Buchanan Astley
#
# Het liefdevolle listFsfiles script dat ik eerder schreef in 
# de programmeertaal met die speciale karakters, nu herschreven in python3.
# Met alle probeersels zichtbaar eruit gecommentarieerd met "#".
# Waarom is het handig?
# Om van alle bestanden op het bestandsysteem de aanmaakdatum en de sha256 sum 
# te genereren.
# Waarom is dat nou weer handig?
# Met een dergelijke lijst kan op een later moment ontdekt worden of er 
# gerommeld is met een binair bestand door de sha256 sums met elkaar te vergelijken.
# Als de sha256 sum anders is dan is de kans groot dat ermee gerommeld is.
# Met bestanden waarvan de kans klein is dat de sum veranderd is.
# Na een update van een binair bestand is het logisch dat de sum anders is.
# Moet dan wel eenvoudig ergens terug te vinden zijn dat het betreffende bestand is geupdate. 
# 
# Er bestaan wat bestanden waar zelfs de root user moeite mee heeft en die worden 
# gemarkeerd met 'prblmf' als je daarop grept in het output bestand verschijnen
# de problematische bestanden. 
#  
# ./listFsfiles.py 'directory' 

import os,sys
import subprocess 
import hashlib
import time 

def print_mijndate():
   from time import gmtime, strftime
   date = strftime("%Y%m%d.%H%M%S")
   return(date)

def gstat(self):

    a = os.stat(self)
    b = a.st_ctime
    return(b)

def tstat(self):    

    try: 
        a = os.stat(self)
      
        b = a.st_mode
        print("Ja",a)
        c = str(b)
        c2 = a.st_size
        c1 = [ c[0:2], c2 ] 
        return(c1)
    except FileNotFoundError:
        #print("ja")
        next
   



def genhsh(self):

 
    cmd = [ '/usr/bin/sha256sum', self ] 
    
    try:
        output = subprocess.check_output(cmd,stderr=subprocess.DEVNULL)
        outputlist = output.decode().strip()
        return(outputlist)
    
    except subprocess.CalledProcessError:
        output = "Ja prblmfl " + self    
        
        return(output)
   

def checkfiles():

    ctime = print_mijndate()
    f = "./allfiles_with256sums." + ctime + ".tct"
    c = open(f, 'w') 

  
    for (dir,sd,fn) in os.walk(sys.argv[1]):
        for i in fn:
           
            b1 = ""
            try: 
                a = os.path.join(dir, i)
                
                a1 = os.stat(a)
            except FileNotFoundError:
                
                b1 = "fnfe"  
                
            e1 = a1.st_mode 
            e2 = str(e1)
            e3 = e2[0:2] 
            c1 = a1.st_size

          
            if b1 != "fnfe" and e3 == "33" and c1 != 0:
                a = os.path.join(dir, i)
                
                if i != 'core' and i != 'kcore': 
                    b = genhsh(a)
            
                    print(a, b, "\n") 
            
                    e = gstat(a)
                    d = str(e) + " " + b + "\n"
            
                    print(d)
                    c.write(d)
            
    c.close() 

 

checkfiles()


