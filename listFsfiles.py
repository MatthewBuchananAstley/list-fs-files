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
   #print(date)
   return(date)

def gstat(self):

    a = os.stat(self)
    b = a.st_ctime
    #print(b)
    return(b)

def tstat(self):    
    #a = os.stat(self)
    #b = a.st_mode
    try: 
        a = os.stat(self)
        #print(b)
        b = a.st_mode
        print("Ja",a)
        #print("Ja",b)
        #print(b[1:2])
        #print(str(b[1:2]))
        c = str(b)
        #print(c[1:2])
        #print(c[0:2])
        c2 = a.st_size
        c1 = [ c[0:2], c2 ] 
        #return(c[0:2])
        return(c1)
    except FileNotFoundError:
        #print("ja")
        next
    #print(b)

#tstat(sys.argv[1])

#gstat(sys.argv[1])
#sys.exit()

def genhsh(self):

    #cmd = [ '/usr/bin/sha256sum', self, stderr=devnull ] 
    #cmd = [ '/usr/bin/sha256sum', self, stderr=subprocess.DEVNULL ] 
    #cmd = [ '/usr/bin/sha256sum', self, '2>/devnull'] 
    #cmd = [ '/usr/bin/sha256sum', self, '2>/dev/null'] 
    cmd = [ '/usr/bin/sha256sum', self ] 
    #output = subprocess.check_output(cmd)
    try:
        output = subprocess.check_output(cmd,stderr=subprocess.DEVNULL)
        outputlist = output.decode().strip()
        return(outputlist)
    #except CalledProcessError:
    except subprocess.CalledProcessError:
        output = "Ja prblmfl " + self    
        #return(outputlist)
        return(output)
    #output = subprocess.check_output(cmd,stderr=suDEVNULL)
    #output.DEVNULL
    #outputlist = output.decode().strip()
    #return(outputlist)

def checkfiles():

    ctime = print_mijndate()
    f = "./allfiles_with256sums." + ctime + ".tct"
    c = open(f, 'w') 

    ##for (dir,sd,fn) in os.walk("/"):
    #for (dir,sd,fn) in os.walk("/run"):
    #for (dir,sd,fn) in os.walk("/sys"):
    for (dir,sd,fn) in os.walk(sys.argv[1]):
        for i in fn:
            #a = os.path.join(dir, i)
            #print(a)
            b1 = ""
            try: 
                a = os.path.join(dir, i)
                #a = tstat(a)
                a1 = os.stat(a)
            except FileNotFoundError:
                #next
                b1 = "fnfe"  
                
            e1 = a1.st_mode 
            e2 = str(e1)
            e3 = e2[0:2] 
            c1 = a1.st_size

            #print("Ja",e3) 
            ##print("Ja",i, e3) 
            #if b1 != "fnfe":
            #if b1 != "fnfe" and e3 != '49':
            #if b1 != "fnfe" and e3 != "49":
            if b1 != "fnfe" and e3 == "33" and c1 != 0:
                a = os.path.join(dir, i)
                #if a != '/dev/core' and a != '/proc/kcore': 
                if i != 'core' and i != 'kcore': 
                    b = genhsh(a)
            #if os.stat(a):
                    print(a, b, "\n") 
            #print(b) 
                    e = gstat(a)
            #d = b + "\n"
            #d = e + " " + b + "\n"
                    d = str(e) + " " + b + "\n"
            #c.write(b)
                    print(d)
                    c.write(d)
            #else:
            #    print(a)
    c.close() 

        #print(dir,sd,fn)
        #if len(sd) > 1 and len(fn) > 1:
        #for i in sd: 
        #for ii in fn:
        #print(dir + i)
        #print(dir + "/" + i + "/" + ii)

checkfiles()

#a = 'test'
#a = "test"
#a = "./test"
#d = hashlib.sha256(a.encode()).hexdigest()
#print("Ja", d)

    #for i in os.walk("/"):
        #print(dir,sd,fn)
        #print(i) 
#        if len(sd) > 0: 
            #for i in fn:
#            for i in sd:
                #print(i)
                #a = dir + sd + i
                #a = str(dir) + str(sd) + str(i)
                #a = dir + i + fn 
                #if len(fn) => 1:
                #if len(fn) >= 1:
                #    for j in fn:
                #        a = dir + i + j
                #        print(a) 
                #else:
                #    a = dir + "/" + fn
                #    print(a)  

    #cmd = [ '/usr/bin/find', '/ -type f -printf "%T@ %Tc %p\n"' ] 
    #cmd = [ '/usr/bin/find', '/', '-type', 'f', '-printf', '"%T@ %Tc %p\n"' ] 
    #output = subprocess.check_output(cmd)
    #output.decode().strip()
    #outputlist = output.decode().split(" ")
    #print(outputlist) 

#checkfiles()
