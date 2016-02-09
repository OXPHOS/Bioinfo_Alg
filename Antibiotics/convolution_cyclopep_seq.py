'''
Amino acid pool increase from 20 to all possible aa.
Any integer between 57 and 200 is taken as a mass of an amino acid
Then search with leaderboard method.
Each round score the newly generated peptides. 
Only takes the first N peptides (take all ties) with highest scores 
'''
import operator

def convolution_calculation(spectrum):
    global AApool
    convolution = [(0) for _ in range(201) ]
    for i in range(len(spectrum) - 1):
        for j in range(i + 1, len(spectrum)):
            # Have to remove 0 in the results!!!!!
            value = spectrum[j] - spectrum[i]
            if 57 <= value <= 200:
                convolution[value] +=1 
    
    convolution_sort = sorted(enumerate(convolution), key=operator.itemgetter(1), reverse = True)
    convolution_sort.append((-1,-1))
    
    i = 0
    AApool = []
    while len(convolution_sort) > i:
        AApool.append(convolution_sort[i][0])
        if convolution_sort[i + 1][1] < convolution_sort[i][1] and len(AApool) >= M:
            break
        i += 1
    
#    # Output convolution results in string
#    output = ''
#    for num in convolution:
#        output += str(num) + ' '
#    print output
#    print len(convolution)
    
    return

def cyclospectrum(peptide):            
    # O(n) = L ** 2
    # Transform mass --> spectrum
    total_mass = sum(peptide)
    spec = [0, total_mass]
    
    for i in range(len(peptide)):
        cyc_seq = peptide[i : ] + peptide[0 : i]
#        print cyc_seq
        mass_j = 0
        for j in range(len(peptide)-1):
            mass_j += cyc_seq[j]
            spec.append(mass_j)
#    print spec
    return spec

def calculate_score(curr_spec, exp_spec):
    #O(n) = L ** 2
    score = 0
    for value in curr_spec:
        if value in exp_spec:
            exp_spec.remove(value)
            score += 1
#    print curr_spec, score
    return score

def trim_by_score(temp_peptides, spectrum):
    global N
    score_space = [[] for _ in range(spectrum[-1] + 1)] 
    trimmed_peptides = []
    
    for i in range(len(temp_peptides)):
        curr_spec = cyclospectrum(temp_peptides[i])
        score_space[calculate_score(curr_spec, list(spectrum))].append(i)
    
    score_space.reverse()

    for rank in score_space[ :-1]: #Doesn't consider score = 0
        trimmed_peptides.extend(temp_peptides[_] for _ in rank)
#        if len(rank) != 0:
#            print (493 - score_space.index(rank)), [temp_peptides[_] for _ in rank]
        if len(trimmed_peptides) >= N:
            return trimmed_peptides
    return trimmed_peptides

    
def leaderboard_sequencing(spectrum):
    
    # Set up of leaderboard (temp results) and leaderpeptide (final results)
    leaderboard = []
    leaderpeptides = []
    
    # Initiate single amino acid into peptides list
    #Score = 1 screening
    leaderboard = [[_] for _ in AApool]
    print leaderboard
 
    # Iterate further list. Confirm every new aa added to the peptide fits the spectrum
    i = 0
    while leaderboard != []:
        i += 1
        print '-----------------------------',i, '-----------------------------'
    
        temp_peptides = []
        for peptide in leaderboard:
            for aa in AApool:
                # Decide whether a peptide goes into 'Final list', stays, or be elimated
                total_mass = sum(peptide) + aa
                if total_mass == spectrum[-1]:
                    # This step only confirms totalmass, but not each mass in spec
                    leaderpeptides.append(peptide + [aa])
                elif total_mass < spectrum[-1]:
                    temp_peptides.append(peptide + [aa])
        leaderboard = trim_by_score(temp_peptides, spectrum)
    # Rank the candidates peptides (with TotalMass = ParentMass) again.
    leaderpeptides = trim_by_score(leaderpeptides, spectrum)
    
#    print leaderpeptides
    return leaderpeptides

M = 16 
N = 387
spectrum_str = '1465 494 163 1441 1174 1447 788 604 1465 933 808 1084 937 128 276 657 1392 1302 250 896 517 1300 1250 921 625 995 1190 682 0 1061 641 1132 1261 131 439 1450 554 391 533 774 260 365 924 645 1578 1302 667 276 882 1350 510 1312 1068 228 696 278 113 129 386 1321 388 1192 1024 163 1074 186 646 1213 115 1449 911 767 1328 1415 1318 1187 811 504 770 1045 974 514 696 137 804 266 1463 528 1064 1139 901 1187 1378 379 767 391 1199 654 1321 291 811 113 200 517 420 932 953 1011 567 446 397 1087 1507 882 404 583 1287 790 257 317 257 795 1158 129 677 1415 1050 328 1449 71 1061 491 1181 783'
spectrum = map(int, spectrum_str.split(' '))
spectrum.sort()
convolution_calculation(spectrum) # Calculate convolution / aa pool
answer = leaderboard_sequencing(spectrum)
output = ''
for i in answer[0]:
    output += str(i) + '-'
print output[ : -1]
