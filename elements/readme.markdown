"elements" folder readme
=======================

The "elements" folder generates the .csv files that the Python script uses to plot elements and apertures, from a MAD-X output (.tfs).
The program will issue .csv files, with only the elements you choose.


Steps
-----

1. Put a MAD-X output file (i.e. tfs) in the folder __"in"__ with the following columns (in this order, if you want the plotting script to work properly):

    `NAME   S   L   APER_1  APER_2  APER_3  APER_4  APERTYPE`   

    You can add several files to this folder, for example one for beam 1 and one for beam 2.

2. Open __"regex.conf"__ and write there the elements you are interested in (that's the regex that the program will look for), and below the name you want to add to the output file. The program will issue the .csv file with a name like this: __"aperture_b1_nameofelement"__ and __"aperture_b2_nameofelement"__.

Example of content of "regex.conf":

                MBAW
                mbaw
                MBLW
                mblw
                MBRB
                mbrb
                MBRC
                mbrc
                MBRS
                mbrs
                MBW
                mbw
                MBWMD
                mbwmd
                MBX
                mbx
                MBXW
                mbxw
                MBXWH
                mbxwh
                MK
                mk
                MC
                mc
                MQXA
                mqxa
                MQXB
                mqxb
                B
                b
                V
                v
                TAN
                tan
                TAS
                tas
                TC
                tc


3. Once __"regex.conf"__ is written, you just have to run __"run.py"__, and the .csv files will be generated in the __"out"__ folder. Ready to be easily used by a Python script.