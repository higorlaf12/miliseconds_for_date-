# -*- coding: utf-8 -*-
#python 3.x

import csv
import sys
import datetime

#convert a "comma separated values" file to vcf contact cards

#USAGE:
#CSV_to_Vcards.py CSV_filename


def convert(somefile):
    #assuming file format : lastname,firstname,phonenumber,mail
    with open( somefile, 'r' ) as source:
        Convert = open('Transform.txt', 'w')
        #reader = csv.reader( source )
        for line in source:
            d = datetime.datetime.fromtimestamp(float(line)/1000)
            s = d.strftime('%Y/%m/%d %H:%M:%S')
            Convert.write(s + "\n");

        Convert.close()
        source.close()
        print ("Milisegundo para formato gerado");


def main(args):
    if len(args) != 2:
        print ( "Usage:")
        print ( args[0] + " filename")
        return

    convert(args[1])

if __name__ == '__main__':
    main(sys.argv)
