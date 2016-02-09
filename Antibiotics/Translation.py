"""
Translate a RNA into peptides
Calculate a peptides could be translated from in total how many RNAs
"""

codon_table_file =open('RNA_codon_table.txt')
CODON_TABLE = {}
REVERSE_CODON_TABLE ={}

for line in codon_table_file.readlines():
    # Construct CONDON TABLE dict
    entry = line.split()
    if len(entry) > 1:
        CODON_TABLE[entry[0]] = entry[1]
#        REVERSE_CODON_TABLE.update([entry[1], entry[0]])
    else:
        CODON_TABLE[entry[0]] = ''

#print REVERSE_CODON_TABLE

def translation(rna_seq):
    peptide = ''
    while len(rna_seq) > 0:
        aa = CODON_TABLE[rna_seq[0:3]]
        if aa == '':
            return peptide
        peptide += aa
        rna_seq = rna_seq[3:]
    return peptide
        
print translation('CCCAGUACCGAGAUGAAU')


def possibility(peptide):
    # Calculate the peptides could be translated from in total how many RNAs
    times = 1
    for aa in peptide:
        i = 0
        for key in CODON_TABLE:
            if CODON_TABLE[key] == aa:
                i += 1
        times *= i
    return times

#print possibility('G') # should be 4
#print possibility('GAE') # 32
print possibility('SYNGE')  
    
                