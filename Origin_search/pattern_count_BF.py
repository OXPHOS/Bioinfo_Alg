"""
The 1st version.
Given a seq, search a pattern (kmer) that appears t times in the sequence
Doesn't consider blur match or reverse complement 
"""

def pattern_count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count


def frequent_word(text, k):
    count = []
    frequent_pattern = set([])
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        count.append(pattern_count(text, pattern))
    max_count = max(count)
     
    for i in range(len(text) - k + 1):
        if count[i] == max_count:
            frequent_pattern.add(text[i:i+k])
    return frequent_pattern
text = 'GAGTGGCCCACGCATCTCAGAGTGGCCCACTAGACCAGAGTGGCCCACGCATCTCACTAGACCATATTCACTTATTCACTCGCATCTCACTAGACCAGAGTGGCCCAGAGTGGCCCAGGGTTGCCCGGGGTTGCCCGTATTCACTGGGTTGCCCGCTAGACCATATTCACTTATTCACTCTAGACCAGGGTTGCCCGGAGTGGCCCATATTCACTCTAGACCACTAGACCACGCATCTCACTAGACCAGAGTGGCCCAGGGTTGCCCGGAGTGGCCCAGAGTGGCCCACGCATCTCATATTCACTCTAGACCATATTCACTGAGTGGCCCATATTCACTCGCATCTCACTAGACCACTAGACCATATTCACTCTAGACCAGAGTGGCCCAGGGTTGCCCGCTAGACCACTAGACCAGGGTTGCCCGGAGTGGCCCACGCATCTCACTAGACCATATTCACTGAGTGGCCCATATTCACTTATTCACTGGGTTGCCCGTATTCACTGAGTGGCCCACTAGACCATATTCACTGGGTTGCCCGGGGTTGCCCGGGGTTGCCCGCGCATCTCAGAGTGGCCCACTAGACCACTAGACCATATTCACTTATTCACTGAGTGGCCCAGAGTGGCCCAGAGTGGCCCAGAGTGGCCCAGAGTGGCCCAGAGTGGCCCACGCATCTCAGGGTTGCCCGGAGTGGCCCAGGGTTGCCCGCGCATCTCAGAGTGGCCCAGGGTTGCCCGGGGTTGCCCGCTAGACCATATTCACTTATTCACTTATTCACTCTAGACCATATTCACTCTAGACCACTAGACCAGGGTTGCCCGGAGTGGCCCACTAGACCATATTCACTGAGTGGCCCAGGGTTGCCCGGGGTTGCCCGCGCATCTCATATTCACTCGCATCTCAGGGTTGCCCG'
frequent_pattern = frequent_word(text, 14)
for i in frequent_pattern:
    print i
