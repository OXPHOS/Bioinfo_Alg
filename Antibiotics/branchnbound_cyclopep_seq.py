import urllib2

URL = 'https://stepic.org/media/attachments/lessons/98/integer_mass_table.txt'
file = urllib2.urlopen(URL)
PEP_MASS = set([])
for line in file.readlines():
    entry = line.split()
    PEP_MASS.add(int(entry[1]))
PEP_MASS = list(PEP_MASS)

def output(seq_list):
    string = ''
    for i in seq_list:
        string += str(i)+'-'
    return string[:-1]
        
##### DIDN'T CONSIDER WHTETHER THE NEWLY ADDED AA WOULD FIT ALL PREVIOUS SPECTRUM DATA#####
#def cyclopeptide_sequencing(spectrum):
#    counter = 0
#    results_string = ''
#    #spectrum_list = spectrum.split(' ')
#    spectrum_list = map(int, spectrum.split(' '))
#    aa_list = [[PEP_MASS[i]] for i in range(len(PEP_MASS)) if PEP_MASS[i] in spectrum_list]
#    peptide_list = list(aa_list)
##    print peptide_list
#    while peptide_list != []:
#        temp_peptide_list = []
#        print len(peptide_list)
#        print peptide_list
#        for peptide in peptide_list:
#            for aa in aa_list:
#                new_score = sum(peptide) + sum(aa)
#                if new_score in spectrum_list:   
#                    if new_score == spectrum_list[-1]:
#                        counter += 1
#                        results_string += output(peptide + aa) + ' '
#                    else:
#                        temp_peptide_list.append(peptide + aa)
#        peptide_list = list(temp_peptide_list)
    
#    #print results_string, counter

'''
Find candidate peptides via branch and bound method
Doesn't take errors into account
'''

def bound_search(peptide_pool, curr_peptide, new_aa):
    # Confirm the new peptide fits all existed spec data
    for i in range(len(curr_peptide)):
#        print curr_peptide[0 : i] + curr_peptide[i + 1 : ] + new_aa
        if (curr_peptide[0 : i] + curr_peptide[i + 1 : ] + new_aa) not in peptide_pool:
            return False    
        return True

def cyclopeptide_sequencing(spectrum):
    counter = 0
    results_string = ''
    spectrum_list = map(int, spectrum.split(' '))
    
    #Initiate single amino acid into peptides list
    aa_list = [[PEP_MASS[i]] for i in range(len(PEP_MASS)) if PEP_MASS[i] in spectrum_list]
    peptide_list = []
    peptide_list.append(list(aa_list))
    
    #Iterate further list. Confirm every new aa added to the peptide fits the spectrum
    iter = 1
    while len(peptide_list) == iter:
        #Construct new list for peptide+1 to append
        peptide_list.append([])#temp_peptide_list = []
        
        # Iterate peptide
        for peptide in peptide_list[iter - 1]:
            # Add new amino acid
            for aa in aa_list:
                new_score = sum(peptide) + sum(aa)
                # Confirm every subpeptide fits the spectrum    
                if new_score in spectrum_list and bound_search(peptide_list[iter - 1], peptide, aa):   
                    # If this is full length : ouput; if not: extend current peptide
                    if new_score == spectrum_list[-1]:
                        counter += 1
                        results_string += output(peptide + aa) + ' '
                    else:
                        peptide_list[iter].append(peptide + aa)
        if peptide_list[-1] == []:
            peptide_list.remove([])
        iter += 1
#        print peptide_list
    
    print results_string, counter

        
cyclopeptide_sequencing('0 71 113 101 131 184 202 214 232 285 303 315 345 416')
#cyclopeptide_sequencing('0 71 97 99 103 113 113 114 115 131 137 196 200 202 208 214 226 227 228 240 245 299 311 311 316 327 337 339 340 341 358 408 414 424 429 436 440 442 453 455 471 507 527 537 539 542 551 554 556 566 586 622 638 640 651 653 657 664 669 679 685 735 752 753 754 756 766 777 782 782 794 848 853 865 866 867 879 885 891 893 897 956 962 978 979 980 980 990 994 996 1022 1093')
#cyclopeptide_sequencing('0 87 97 103 113 115 131 131 147 147 163 186 200 200 218 228 244 250 278 294 301 310 315 317 331 347 347 365 375 413 414 432 441 446 462 478 478 480 494 501 510 544 545 565 575 593 595 625 627 632 632 641 657 678 690 708 712 730 742 763 779 788 788 793 795 825 827 845 855 875 876 910 919 926 940 942 942 958 974 979 988 1006 1007 1045 1055 1073 1073 1089 1103 1105 1110 1119 1126 1142 1170 1176 1192 1202 1220 1220 1234 1257 1273 1273 1289 1289 1305 1307 1317 1323 1333 1420')