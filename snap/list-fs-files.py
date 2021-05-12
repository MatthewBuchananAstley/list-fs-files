#!/usr/bin/python3

import os,sys
import subprocess 
import hashlib
import time 
import json

def print_mijndate():
   from time import gmtime, strftime
   date = strftime("%Y%m%d.%H%M%S")
   return(date)

def gstat(self):

    a = os.stat(self)
    b = a.st_ctime
    c = json.dumps([ a.st_mode, a.st_ino, a.st_dev, a.st_nlink, a.st_uid, a.st_gid, a.st_size, a.st_atime, a.st_mtime, a.st_ctime ])   
    return(c)

def tstat(self):    
    try: 
        a = os.stat(self)
        b = a.st_mode
        c = str(b)
        c2 = a.st_size
        c1 = [ c[0:2], c2 ] 
        return(c1)
    except FileNotFoundError:
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
    c2 = [] 
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
                    b1 = b.split("  ",1)
                    
                    e = gstat(a)
                    b2 = [ e, json.dumps(b1) ] 
                    c2.append(b2)
    print(json.dumps(c2)) 


checkfiles()

