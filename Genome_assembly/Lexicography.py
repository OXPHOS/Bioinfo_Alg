'''
 Input: An integer k and a string Text.
 Output: Compositionk(Text), where the k-mers are written in lexicographic order.
'''

def lexi(string, k):
    code_list = []
    for i in range(len(string) - k + 1):
        code_list.append(string[i:i+k])
    code_list.sort()
    return code_list
    
kmer_list = lexi('CAATCCAAC',5)
output = ''
for kmer in kmer_list:
    output += kmer + '\n'
print output[:-1]
        