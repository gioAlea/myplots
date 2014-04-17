import os
import sys

def parse(infolder,outfolder,inextension,outextension):
    innames = filter(lambda name:name.split('.')[-1] == inextension,os.listdir(infolder))
    if not os.path.isdir(outfolder):
        os.mkdir(outfolder)
    for inname in innames:
        try:
            print 'Opening ' + inname
            infile = open(infolder + '/' + inname,'r')
            inlines = infile.readlines()
            for line in inlines:
                if started == 1:
                    columns = line.strip().split()
                    name = columns[0]
            print "\t\t" + 'Found ' + str(found)
 
