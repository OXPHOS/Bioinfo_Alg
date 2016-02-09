'''
Find candidate proteins via leaderboard mathod
Each round score the newly generated peptides. 
Only takes the first N peptides (take all ties) with highest scores 
'''

import urllib2

URL = 'https://stepic.org/media/attachments/lessons/98/integer_mass_table.txt'
file = urllib2.urlopen(URL)
PEP_MASS = set([])
for line in file.readlines():
    entry = line.split()
    PEP_MASS.add(int(entry[1]))
PEP_MASS = list(PEP_MASS)

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
        if len(trimmed_peptides) >= N:
#            print len(trimmed_peptides)
            return trimmed_peptides
    return trimmed_peptides

    
def leaderboard_sequencing(spectrum):
    spectrum = map(int, spectrum.split(' '))
    
    # Set up of leaderboard (temp results) and leaderpeptide (final results)
    leaderboard = []
    leaderpeptides = []
    
    # Initiate single amino acid into peptides list
    #Score = 1 screening
    leaderboard = [[PEP_MASS[i]] for i in range(len(PEP_MASS)) if PEP_MASS[i] in spectrum]
    print PEP_MASS
 
    # Iterate further list. Confirm every new aa added to the peptide fits the spectrum
    i = 0
    while leaderboard != []:
        print '-----------------------------',i, '-----------------------------'
        i += 1
        temp_peptides = []
        for peptide in leaderboard:
            for aa in PEP_MASS:
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

    return leaderpeptides

N = 464
answer = leaderboard_sequencing('0 71 87 87 97 99 103 103 103 103 113 113 128 129 129 129 131 137 137 147 163 163 163 163 186 190 190 199 200 206 216 216 228 230 234 240 242 250 250 260 260 266 266 276 277 291 292 300 317 319 328 343 345 347 349 353 353 353 359 362 363 363 365 379 387 388 389 397 403 405 416 440 440 448 456 456 459 460 462 466 475 478 480 490 490 491 492 496 506 508 525 526 526 543 545 563 569 577 579 585 588 588 591 593 593 593 596 603 609 611 613 619 625 638 654 655 656 680 682 691 694 696 706 706 708 708 716 722 725 725 726 735 740 742 748 748 751 753 756 779 783 797 803 809 813 819 821 824 825 835 837 843 843 845 845 848 854 854 854 872 884 896 911 916 924 928 932 934 938 941 942 942 946 946 950 951 953 955 956 966 974 985 998 1001 1003 1017 1025 1027 1044 1049 1053 1059 1059 1065 1070 1071 1084 1087 1088 1095 1097 1100 1101 1103 1104 1105 1114 1114 1131 1141 1156 1162 1162 1164 1166 1184 1184 1188 1188 1190 1201 1206 1207 1213 1217 1228 1231 1232 1233 1234 1251 1270 1275 1287 1287 1291 1293 1293 1294 1294 1303 1304 1304 1309 1315 1316 1327 1335 1338 1344 1347 1351 1362 1374 1380 1390 1391 1404 1406 1414 1417 1418 1422 1430 1431 1433 1433 1438 1441 1447 1450 1454 1456 1457 1467 1475 1479 1505 1509 1517 1527 1528 1530 1534 1537 1543 1546 1551 1551 1553 1554 1562 1566 1567 1570 1578 1580 1593 1594 1604 1610 1622 1633 1637 1640 1646 1649 1657 1668 1669 1675 1680 1680 1681 1690 1690 1691 1691 1693 1697 1697 1709 1714 1733 1750 1751 1752 1753 1756 1767 1771 1777 1778 1783 1794 1796 1796 1800 1800 1818 1820 1822 1822 1828 1843 1853 1870 1870 1879 1880 1881 1883 1884 1887 1889 1896 1897 1900 1913 1914 1919 1925 1925 1931 1935 1940 1957 1959 1967 1981 1983 1986 1999 2010 2018 2028 2029 2031 2033 2034 2038 2038 2042 2042 2043 2046 2050 2052 2056 2060 2068 2073 2088 2100 2112 2130 2130 2136 2139 2139 2141 2141 2147 2149 2159 2160 2163 2165 2171 2175 2181 2187 2201 2205 2228 2231 2233 2236 2236 2242 2244 2249 2258 2259 2259 2262 2268 2276 2276 2278 2278 2288 2290 2293 2302 2304 2328 2329 2330 2346 2359 2365 2371 2373 2375 2381 2388 2391 2391 2391 2393 2396 2396 2399 2405 2407 2415 2421 2439 2441 2458 2458 2459 2476 2478 2488 2492 2493 2494 2494 2504 2506 2509 2518 2522 2524 2525 2528 2528 2536 2544 2544 2568 2579 2581 2587 2595 2596 2597 2605 2619 2621 2621 2622 2625 2631 2631 2631 2635 2637 2639 2641 2656 2665 2667 2684 2692 2693 2707 2708 2718 2718 2724 2724 2734 2734 2742 2744 2750 2754 2756 2768 2768 2778 2784 2785 2794 2794 2798 2821 2821 2821 2821 2837 2847 2847 2853 2855 2855 2855 2856 2871 2871 2881 2881 2881 2881 2885 2887 2897 2897 2913 2984')
print answer

