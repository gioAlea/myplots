import os
import re
import sys

def parse(regex_file_name,infolder,outfolder,inextension,outextension):
    innames = filter(lambda name:name.split('.')[-1] == inextension,os.listdir(infolder))
    if not os.path.isdir(outfolder):
        os.mkdir(outfolder)
    regex_list = []
    try:
        regex_file = open(regex_file_name,'r')
        regex_lines = regex_file.readlines()
        regex_codes = [line.strip() for line in regex_lines[0::2]]
        regex_extensions = [line.strip() for line in regex_lines[1::2]]
        for i in range(len(regex_codes)):
            regex_list.append((regex_codes[i],regex_extensions[i]))
    except BaseException :
        print 'Error opening regex file, ' 
        return
    for inname in innames:
        try:
            print 'Opening ' + inname
            infile = open(infolder + '/' + inname,'r')
            inlines = infile.readlines()
            for (regex_string,extension) in regex_list:          
                outfile = open(outfolder + '/' + inname.replace('.'+inextension,'') + '_' + extension+'.'+outextension,'w')
                print "\t" + 'Searching for ' + regex_string
                regex = re.compile('\"'+regex_string)
                started = 0
                found = 0
                for line in inlines:
                    if started == 1:
                        columns = line.strip().split()
                        name = columns[0]
                        if regex.match(name) is not None:
                            found += 1
                            outfile.write(','.join(columns)+"\n")
                    else:
                        if line[0] == '$':
                            started = 1
                print "\t\t" + 'Found ' + str(found)
        except IOError :
            print 'IO error (maybe input file ' + inname + ' was not found) '
        except BaseException :
            print 'Unexpected error: ' 

if __name__ == '__main__':
    if len(sys.argv) != 6:
        print "Usage " + sys.argv[0] + " regex_conf in_folder out_folder in_extension out_extension"
    else:
        parse(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
