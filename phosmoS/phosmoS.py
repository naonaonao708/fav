#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 14:45:43 2017

@author: Carina
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 13:34:22 2017

@author: Carina
"""
#creating a program for SnRK1 phopshorylation motifs in python 2

#to run the program you need to downnload and put in the same file the following:
#TAIR file TAIR10_pep_20110103_representative_gene_model_updated.txt
#this python file

#the SnRK1 phosphorylation sites are: (Halfrod et al., 2003)
#MLVFI – X – RKH – XX – S/T – XXX – LFIMV
#MLVFI–RKH-XXX-S/T-XXX- LFIMV

#the program will take as input an UPPERCASE representative gene model for
#the locus you are looking from (from TAIR)

#for example ABI5 locus is AT2G36270, but representative gene model is AT2G36270.1

#import appropriate packages including Biopython which needs to be downloaded separately
#to do this, use terminal and enter 
#pip install biopython

import sys
from Bio import SeqIO
import collections

#takes the TAIR file that contains all representative gene models
#and turns it into a list called records
#file downloaded from TAIR, using representative gene models so that all the 
#Gene IDs are the locus with .1
#i.e. AT3G01090.1

records = list(SeqIO.parse("TAIR10_pep_20110103_representative_gene_model_updated.txt", "fasta"))

#length of the records list
records_length = len(records)

#we will be using this program from terminal, so must tell it to read the 
#arguments from the command line

#argument given will be the locus (so missing the .1)
args = sys.argv

#these lists will keep count of the SnRK1 and core SnRK sites for ALL the genes ran at once
#i.e. a specific list of genes

core_b4_7 = []
core_b4_6 = []  
core_b4_5 = []
core_b4_4 = []
core_b4_3 = []
core_b4_2 = []
core_b4_1 = []
core_ST = []
core_plus1 = []
core_plus2 = []
core_plus3 = []
core_plus4 = []
core_plus5 = []
core_plus6 = []
core_plus7 = []
gene_ids = []
full_SnRK1_all = []
core_SnRK_all = []

#args[0] is the file name , so gene_id is starting at args[1]
#so the range has to be from 1 on 

for argument in range(1, len(args)):
    str_args = str(args[argument])


#if an incomplete, or no gene ID is given, the user is told so
#if the gene ID is not given in upper case letter, the user is also told so.
    if len(str_args) < 9 :
        print "You did not input a proper gene ID (AGI). Please use full ID."
    else:
        #turns it to uppercase so that case does not matter
        gene_id = str_args.upper()
        gene_ids.append(gene_id)
    
    #loop, for every index in records, if the id matches what was inputed by the user,
    #then that index, i, becomes equal to ind so that we can use it later to extract
    #and use the protein sequence 
    
        for index in range(records_length):
    #reads the first 9 charachters of the locus (excluding the .1 or whatever)
            if gene_id == records[index].id[0:9]:
                ind = index
                print "The gene details are: %s" % records[index].description
        
                prot_seq = str(records[ind].seq)
                #print "The protein sequence is: %s." % prot_seq
                    
                aa_length = len(prot_seq)
                    
                aliphatic_aa = ["L", "M", "F", "V", "I"]
                    
                charged_aa = ["R", "K", "H"]
                    
                    #make empty lists necessary for the for loop so that we can count the number
                    #of each kind of phosphorylation site present
                    
                core_count = []
                partial_count = []
                full_count = []
    
                    
                for i in range(aa_length):
                    #first it identifies all the possible S and T 
                    #that it can be phosphorylated at
                    if (i > 9) and (i < (aa_length-9)) and (prot_seq[i] in ["S","T"]):
                         #if there is an R, K, or H 3 or 4 aa away from the S/T
                         #position i+1 becuase the first amino acid is 0 otherwise
                         #if i is 5 before the end, becuause otherwise it cannot retrieve +5 aa and gives error
                        if ((prot_seq[i-3] in charged_aa or prot_seq[i-4] in charged_aa)):
                                core_count.append(prot_seq[i-7:i] + " " + prot_seq[i] + str(i+1) + " " + prot_seq[i+1:i+8])
                                #print "Core SnRK P site at position", i+1, prot_seq[i-5:i], prot_seq[i]
                                
                                #create a list with the amino acid at each position, from -7 from the S or T 
                                #to plus 7 from the S or T
                                core_b4_7.append(prot_seq[i-7])
                                core_b4_6.append(prot_seq[i-6])
                                core_b4_5.append(prot_seq[i-5])
                                core_b4_4.append(prot_seq[i-4])
                                core_b4_3.append(prot_seq[i-3])
                                core_b4_2.append(prot_seq[i-2])
                                core_b4_1.append(prot_seq[i-1])
                                core_ST.append(prot_seq[i])
                                core_plus1.append(prot_seq[i+1])
                                core_plus2.append(prot_seq[i+2])
                                core_plus3.append(prot_seq[i+3])
                                core_plus4.append(prot_seq[i+4])
                                core_plus5.append(prot_seq[i+5])
                                core_plus6.append(prot_seq[i+6])
                                core_plus7.append(prot_seq[i+7])
                                core_SnRK_all.append(gene_id)
                                
                                 #if there is an LMFVI 5 before OR 4 after the S/T, then that is a partial site
                                if (i < (aa_length-9)) and ((prot_seq[i-5] in aliphatic_aa) or (prot_seq[i+4] in aliphatic_aa)):
                                    partial_count.append(prot_seq[i-7:i] + " " + prot_seq[i] + str(i+1) + " " + prot_seq[i+1:i+8])
                                    #print "Partial SnRK1 P site at position", i+1, prot_seq[i-7:i], prot_seq[i], prot_seq[i+1:i+8]
                                
                                  
                                 #if the aa is at least 5 away from the end of the prothein sequence
                                 #and 5 before AND 4 after the aa acid is LMFVI, then that's a full SnRK1 site
                                    if (i < (aa_length-9)) and (prot_seq[i-5] in aliphatic_aa) and (prot_seq[i+4] in aliphatic_aa):
                                        full_count.append(prot_seq[i-7:i] + " " + prot_seq[i] + str(i+1)+ " " + prot_seq[i+1:i+8])
                                        full_SnRK1_all.append(gene_id)
                                        #print "Full SnRK1 P site at position", i+1, prot_seq[i-7:i], prot_seq[i], prot_seq[i+1:i+8]
                                        
                                       
                    
            #delete the full SnRk1 sites from the list of SnRK1 partial sites
            #crate a loop that compares the partial and full list and deltes any items in partial_count that are found in full_count
    
                for item in partial_count:
                    if item in full_count:
                        partial_count.remove(item)                                                             
                                        
            #print the counts for each type of phospho site present in this protein sequence
                print "There are %d core SnRK phosphorylation sites." % len(core_count)
                for sequence in core_count:
                    print sequence
                print "There are %d partial SnRK1 phosphorylation sites. They are:" % len(partial_count)
                for sequence in partial_count:
                    print sequence
                print "There are %d full SnRK1 phosphorylation sites. They are: " % len(full_count)
                for sequence in full_count:
                    print sequence

#need to take the core SnRK in the input proteins and create a summary of the frequency of each amino acid 
#at each position from -7 to +7 from the S/T
#using the collections.Counter functions where it will count the number of occurances of each amino acid
#the output is in dictionary format

a = collections.Counter(core_b4_7)
b = collections.Counter(core_b4_6)
c = collections.Counter(core_b4_5)
d = collections.Counter(core_b4_4)
e = collections.Counter(core_b4_3)
f = collections.Counter(core_b4_2)
g = collections.Counter(core_b4_1)
h = collections.Counter(core_ST)
i = collections.Counter(core_plus1)
j = collections.Counter(core_plus2)
k = collections.Counter(core_plus3)
l = collections.Counter(core_plus4)
m = collections.Counter(core_plus5)
n = collections.Counter(core_plus6)
o = collections.Counter(core_plus7)

print "The total number of genes you ran is: ", len(gene_ids)
#the code below is for a summary of the type of amino acids found around the partial
#phosphorylation sites
#since this is not a phosphoproteomics study, we do not need that
#print "The summary of the data set you just ran are:"

#print "At position S/T -7 the amino acids are: ", a.most_common()
#print "At position S/T -6 the amino acids are: ", b.most_common()
#print "At position S/T -5 the amino acids are: ", c.most_common()
#print "At position S/T -4 the amino acids are: ", d.most_common()
#print "At position S/T -3 the amino acids are: ", e.most_common()
#print "At position S/T -2 the amino acids are: ", f.most_common()
#print "At position S/T -1 the amino acids are: ", g.most_common()
#print "The most common potentially phosphorylated amino acid: ", h.most_common()
#print "At position S/T +1 the amino acids are: ", i.most_common()
#print "At position S/T +2 the amino acids are: ", j.most_common()
#print "At position S/T +3 the amino acids are: ", k.most_common()
#print "At position S/T +4 the amino acids are: ", l.most_common()
#print "At position S/T +5 the amino acids are: ", m.most_common()
#print "At position S/T +6 the amino acids are: ", n.most_common()
#print "At position S/T +7 the amino acids are: ", o.most_common()

common_o = o.most_common()

#calculate the total number of occurances counted so that we can calculate a % if needed for each
#amino acid at each position
sum_occurances = sum(h.values())

print "The total number of core SnRK phosphorylation sites is: ", sum_occurances

full_SnRK1_noduplicates= []

for i in full_SnRK1_all:
    if i not in full_SnRK1_noduplicates:
        full_SnRK1_noduplicates.append(i)

print "The number of proteins with at least 1 full predicted SnRK1 phosphorylation site is: ", len(full_SnRK1_noduplicates)
print "The list of proteins with at least 1 full predicted SnRK1 phosphorylation sites is: ", full_SnRK1_noduplicates

core_SnRK_noduplicates= []

for i in core_SnRK_all:
    if i not in core_SnRK_noduplicates:
        core_SnRK_noduplicates.append(i)
        
print "The number of proteins with at least 1 core SnRK phosphorylation site is: ", len(core_SnRK_noduplicates)
           




                    