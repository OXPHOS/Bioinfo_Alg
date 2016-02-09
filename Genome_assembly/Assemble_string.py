'''
Assemble the kmers in lexicographic order into a complete string
'''

def assemble_seq(Dna):
#    sequence = Dna.splitlines()[0].strip()
    
    kmer_list = []
    for line in Dna.splitlines():
        kmer_list.append(line.strip())
    sequence = kmer_list[0]
    for _ in range(1, len(kmer_list)):
        sequence += kmer_list[_][-1]
    print sequence



Dna = '''ACCGA
CCGAA
CGAAG
GAAGC
AAGCT'''

assemble_seq(Dna)
    