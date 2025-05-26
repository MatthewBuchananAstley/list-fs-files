#!/usr/bin/python3
#
# SPDX-License-Identifier: Apache-2.0
# FileCopyrightText: 2021 - 2025 Matthew Buchanan Astley (matthewbuchanan@astley.nl,mbastley@gmail.com)
# List files on the filesystem including stat information

import os,sys
import hashlib
import time 
import json
import argparse
import pprint
import lzma
import zlib
import syslog


class listFsFiles():

    def print_mijndate():
       from time import gmtime, strftime
       date = strftime("%Y%m%d.%H%M%S")
       return(date)

    def gstat(self):

        a = os.stat(self)
        b = a.st_ctime
        #c = json.dumps([ a.st_mode, a.st_ino, a.st_dev, a.st_nlink, a.st_uid, a.st_gid, a.st_size, a.st_atime, a.st_mtime, a.st_ctime ])   

        c = [ a.st_mode, a.st_ino, a.st_dev, a.st_nlink, a.st_uid, a.st_gid, a.st_size, a.st_atime, a.st_mtime, a.st_ctime ]  
        return(str(c).strip('[]').replace(',',''))

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
        try:
            a2 = open(self, "rb").read()    
            #a = hashlib.sha256(bytes(self, encoding='UTF-8')).hexdigest()
            a = hashlib.sha256(a2).hexdigest()
            a1 = a + "  " + self
            return(a1) 
        except PermissionError:
            return("PermissionError " + self)
        except OSError:
            return("OSError " + self)
         

        #cmd = [ '/usr/bin/sha256sum', self ] 
        #try:
        #    output = subprocess.check_output(cmd,stderr=subprocess.DEVNULL)
        #    outputlist = output.decode().strip()
        #    return(outputlist)
        #except subprocess.CalledProcessError:
        #    output = "Ja prblmfl " + self    
        #    return(output)

     #password = sys.argv[2]


    def cfiles(self):
        #a_fileList = open( "LFF.FileList." + print_mijndate(), 'w' )
        #a_FileNFoundList = open( "LFF.FileNFoundList." + print_mijndate(), 'w' ) 
        #a_PermissionErrorList = open( "LFF.PermissionErroList." + print_mijndate(), 'w') 

        a1 = open(self[1], "w")
        for i in self[0]:
            a1.write(i)

        a1.close()
     
    def checkfiles(self):

        ErrorList = [ 'ErrorList' ]
        FileNotFoundList =  [ 'FileNotFoundList' ] 

        ctime = listFsFiles.print_mijndate()
        c2 = [ 'Result' ] 
        for (dir,sd,fn) in os.walk(self):
            for i in fn:
                b1 = ""
                b7 = ""
                try: 
                    a = os.path.join(dir, i)
                    a1 = os.stat(a)
                    e1 = a1.st_mode
                    e2 = str(e1)
                    e3 = e2[0:2]
                    c1 = a1.st_size

                except FileNotFoundError:
                    FileNotFoundList.append([dir, i])
                    b1 = "fnfe" 
                except PermissionError:
                    b7 = "e" 
                    ErrorList.append([dir,i])
                except OSError:
                    b7 = "e"
                    ErrorList.append([dir,i]) 
                
                #e1 = a1.st_mode 
                #e2 = str(e1)
                #e3 = e2[0:2] 
                #c1 = a1.st_size

                ##if b1 != "fnfe" and e3 == "33" and c1 != 0 and b7 != "e":
                if b1 != "fnfe" and b7 != "e":
                  ##      a = os.path.join(dir, i)
                  ##    if i != 'core' and i != 'kcore':
                 
                    b = listFsFiles.genhsh(a)
                    if "Error" in b:
                        b1_1 = b.split()
                        ErrorList.append([dir,str(" " + b)])
 
                    #b1 = b.split("  ",1)
                    
                    e = listFsFiles.gstat(a)
                        #b2 = [ e, json.dumps(b) ] 
                        #b2 = [ enc(e,password), enc(b,password) ] 
                    b2 = [ e, b ] 
                        #print("Ja",json.dumps(' '.join(b2)))
                     
                        #print(json.dumps(b2))
  
                    c2.append(b2)

        #print(c2, "\n\n", b3)
        return([ c2, FileNotFoundList, ErrorList] )
        #print(c2)
        #print(json.dumps(c2), "\n\n", b3)

    #def rlen(self):
    #    a1 = len(self)
    #    return(a1)

    #def rl(self):
        #    print("Ja",a[0])
        #print('JaA', rlen(a))
        #sys.exit()
    #    for i in range(1,len(self)):
    #        if rlen(self[i]) > 1:
    #           print("Ja", self[i][0] )

    def comprD(self):
        d = bytes(str(self[1]), encoding='UTF-8')
        a4 = lzma.LZMAFile(self[0] + ".xz",mode='w')
        a4.write(d)

    def compZlib(self):
        #a5 = open(a, "rb").read()
        a5 = bytes(str(self[1]), encoding='UTF-8')
        a1 = zlib.compress(a5, level=9)
        a6 = open(str(self[0]) + ".zlib", "wb")
        a6.write(a1)

    def lg_funct(self):
        dt = listFsFiles.print_mijndate()
        syslog.syslog(syslog.LOG_INFO, str(dt)+ " " + str(self)) 

    def dfResult(self):
        b6 = dict()
        b6["directory"] = str(self[1])

        for i in self[0]:
            b5 = len(i)
            if b5 == 1:
                b5 = 0

            if b5 > 1:
                b5 = b5 - 1
                #print("Ja", i[0], ": ", b5 )
                #print(i[0], ": ", b5 )
                b6[i[0]] = b5

        #print(json.dumps(b6))
        return(json.dumps(b6))
    

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('directory')
    parser.add_argument('-p', action='store_true', help='Print all scan results to stdout')
    parser.add_argument('-fnf', action='store_true', help='Print filenotfound result to stdout')
    parser.add_argument('-e', action='store_true', help='Print error result to stdout')
    parser.add_argument('-j', action='store_true', help='Print result in json to stdout')
    parser.add_argument('-f', action='store_true', help='Save scan results, filenotfoundlist and errorlist results' )
    parser.add_argument('-b', action='store_true', help='List of results'  )
    args = parser.parse_args()   

    #print("JAAA", args)
    #print("JAAAAaA", args.j)

    pth = args.directory
#    print("st_mode st_ino st_dev st_nlink st_uid st_gid st_size st_atime st_mtime st_ctime hash file")
    
    b4 = listFsFiles.checkfiles(pth)
    b7 = listFsFiles.dfResult([ b4, pth ])

    if args.p == True:
        #print("jAA", args.j)
        if args.j == True:
            for i in b4:
                if len(i) != 1:
                    print(json.dumps(i))
                elif len(i) >= 2:
                    print(i[0] + ":" + " 0")
        else:
            for i in b4:
                if len(i) != 1:
                    if i[0] == 'Result':
                        print(i[0] + ":")
                        i.pop(0)
                        for ii in i:
                            print(' '.join(ii)) 
                
                    else:
                        print("JAAAAa", i[0])
                        i.pop(0) 
                        for ii in i:
                            #print("JAAAAa", i) 
                            print('/'.join(ii)) 
                            #print(' '.join(ii)) 
                #else: 
                #    print(i[0] + ":" + " 0")
            #print("JAaaAAa",b7)
            #lg_funct("JAaaAAa " + str(b7))
            listFsFiles.lg_funct(str(b7))

    elif args.fnf == True:
        if args.j == True:
            print(json.dumps(b4[1]))
            listFsFiles.lg_funct(str(b7))
        else:
            #print("jaaAA",b4[1])
            print( str(b4[1][0]) + ":")   
            b4[1].pop(0)
            for i in b4[1]:
                print('/'.join(i)) 
            listFsFiles.lg_funct(str(b7))

    elif args.e == True:
        if len(b4[2]) > 1:
            if args.j == True:
                print(json.dumps(b4[2]))
                listFsFiles.lg_funct(str(b7))
            else:
                print(b4[2])
                listFsFiles.lg_funct(str(b7))

    elif args.f == True:
        b7 = "LFS." + str(pth).strip("/") + ".scan_results." + listFsFiles.print_mijndate()
        b8 = [ b7, b4 ]
        #comprD(b8)  
        listFsFiles.compZlib(b8)

    elif args.b == True:
        for i in b4:
            b5 = len(i)
            if b5 == 1:
                b5 = 0
            if b5 > 1:
                b5 = b5 - 1
            #print("Ja", i[0], ": ", b5 )
            print(i[0], ": ", b5 )

        listFsFiles.lg_funct(str(b7))

    else:
        b6 = dict()
        b6["directory"] = str(pth)
 
        for i in b4:
            b5 = len(i) 
            if b5 == 1:
                b5 = 0
            if b5 > 1:
                b5 = b5 - 1
            #print("Ja", i[0], ": ", b5 )
            #print(i[0], ": ", b5 )
            b6[i[0]] = b5 

        print(json.dumps(b6))
        listFsFiles.lg_funct(str(b7))

