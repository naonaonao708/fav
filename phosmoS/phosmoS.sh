#!/bin/bash

#shell script which calls phosmoS_final.py for several gene IDs

# list of gene IDs will go where ${1} i

#uses each gene ID with the phosmoS_final.py program
#it will append the output to a text file called phosmoS_results.txt
#***the python script, and the shell script, as well as the TAIR database must
#be in the same folder for the program to work
#OPEN TERMINAL, go to the folder where everything is
#example on how to use it from terminal:
#source phosmoS.sh AT3G01090
#EXAMPLE MULTIME AGIS:
#source phosmoS.sh AT1G22190 AT1G52880 AT1G52890 AT1G73920 AT1G74930 AT2G15970 AT2G33380 
#AT2G39050 AT3G14230 AT3G56090 AT3G61890 AT4G05100 AT5G17490 AT5G48240
#just need to separate them by 1 whitespace

python phosmoS.py "$@" >> phosmoS_results.txt

#prints the temporary text file, temp.txt with the output to the screen in terminal
cat phosmoS_results.txt

#this will be in the same folder with the rest of your files