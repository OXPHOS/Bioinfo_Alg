'''
Fitting Alignment
     Input: Two nucleotide strings v and w, where v has length at most 1000 and w has length at most 100.
     Output: A highest-scoring fitting alignment between v and w. Use the simple scoring method in which
     matches count +1 and both the mismatch and indel penalties are 1
The total length is the same as the shorter sequence.
Actually the score was deduced from len(seq_shorter) whereever there's a mismatch or indel
'''
import urllib2


def compute_editing_dist(seq1, seq2):
    
    """
    Use Dynamic Programming to find optimal alignment. Save in list
    Global_flag = True: global alignment
    Global_flag = False: local alignment. If alignment score < 0, make it = 0
    """
    alignment_matrix = []
    alignment_matrix.append([])
    alignment_matrix[0].append(0)
    
    for length in range(1, len(seq_x) + 1):
        alignment_matrix.append([])
        value = alignment_matrix[length-1][0] - 1
        alignment_matrix[length].append(value)  
        
    for length in range(1, len(seq_y) + 1):
#        print length,alignment_matrix[0][length-1]
        value = alignment_matrix[0][length-1] - 1
        alignment_matrix[0].append(value)
        
    for len_x in range(1, len(seq_x) + 1):
        for len_y in range(1, len(seq_y) + 1):
            value = max(alignment_matrix[len_x-1][len_y-1] + (- 1 + int(seq_x[len_x - 1] == seq_y[len_y - 1])),
                        alignment_matrix[len_x-1][len_y] - 1,
                        alignment_matrix[len_x][len_y-1] - 1)
#            print len_x, len_y, alignment_matrix[len_x-1][len_y-1] + (- 1 + int(seq_x[len_x - 1] == seq_y[len_y - 1])), alignment_matrix[len_x-1][len_y] - 1,alignment_matrix[len_x][len_y-1] - 1
            alignment_matrix[len_x].append(value)

#    for i in range(len_x + 1):
#        print alignment_matrix[i]
    print alignment_matrix[len(seq_x)][len(seq_y)]
    return alignment_matrix

seq_x = 'PLEASANTLY'
seq_y = 'MEANLY'

seq_x = 'TGCATAT'
seq_y = 'ATCCGAT'

seq_x = 'YECILTESGQPVMSDDIRHMWVMIHQYTKESQWALCDPIPWLMKGLYLHGYPEAYHLLGSWPRRMDAWAGWEEISNANFVVTVVGCGNPNEARSCEPKCNDVGECVEQTSEHKAMAFCEDKLCCHDLQMGRDRACYCIVSAANEKILKWIRVADQSWKFMRQSAEINHNSAEISSDKASCTCRHKCMVRGADKGRCGRGIHQMQWYRVQGADYAPWVGDQTVGMPALYICHEWNERYDNGQECHWTALLGRVTHQARPRAMLHPICLYWEWHTHQKFPDCDTGTDLFITMHHGFNNSKESQDGEQYTQFFVRWKVPDPVDFWGCGDSEGVRLGVTRDMQRMAQIADEPYWRFYGVRDEDQHGGPAYNMWGVAGGFLHLIGNMHQWTQFCDLLMNDALDHKDGKHKQFRGQHGAWFFFTHCQHDHNVTIALDCQWHYKNTVRMCPVWFKICQLAQKKLRHGFYHPGGRMSYKPDVYYLCDFAYTKIRVEEFIEGTHARFMRNKKCPRWEAQRSDYYPPFLFYSTSSPLYTAENHRRYPDSKVTCRSVFCYYHGTVFEMAWLKWFDTMTTFWQEWFLRDHWVDRHKHEMEMYEGITTQLFKYFREFDNWQPAFMGWLRYPIIKHTWWLVCFYHATHEWQTQCTVVLFQGPKMCYHKGEQIARGCKYCAWTGQHYPKEYWWKRKGWWTPWLDPALYNVCAIFRPDAHVRERFLSIPIAAGHHQEIAVLQKEWATYRGADPHPCRWWFEATQWSMRSSYDLKWLFWPALRWQFMGIADQLQAFAQSEKS'
seq_y = 'YECILTESGQPVMSDDIRHMWVMIHQYTKESMWPIPWLMKVMYYHGGPERTFGFNIMAWEEVRAKNLYMHEQICYNANFVVTVVGCGNPNEARSCEPKCGIGSFFRGECVEQHSEDKAMAFCEDKLGCHDLQMNRGHYGLMWNPRACDCTIVSNATNDAERILKWIRVAKQSWQSAEINHNSEEISSVKHKCMVFQMQWYRVQGADYACWVGDDFQYKTVGMPALNTVGSYYICEERCHWTAARVRAMLHPMQIFGTCLYWEWGTHQKFPDCDTGTDLFITMHHGFNNSKESQDAEQYHCFLWTGLVVPDPVDFWGCGDSEGVRLGVTRYWRFYGVRDEDQHGWPAYNMGGVAGWHVFGLHLIGNMHQWTQFCDLLMNDDGKHKQFRGQHGAWFFFTHCQHVEIALICQWHYKNCPVWFKICFFYHPGGRLIEVDCGMSDKPDFAYTIRHARFEKCPSWEAENDRSDYPPWPRGAMFYSTQSWAHHRKYMHRYPNSKVTCRHWLGCGFCYYHGTCFWHNLKWFDTMTTFWQEWFLFDHWDCCCSHCHQIWQRITTQLFKYFRETDNWQSRKFRDAFMGWLRYPIIKHTWGRFLVCFYPATHEWQTQCTVWDNAHLFQGPKMCYHKGVSHIARGCKNCLWTGQHYHKIPRPPRMWSLHELDVINMMYMLKGWWGRNSHTRPFQWLDFADAWVRYRFLSIPIASGHATWFPLTFEQEIAVLQFEWATYRGRSAPCRWWFEATQWSMRSSYWLKWLFWPACPRWQFMQAQLWDGLIAQSEKS'

alignment_matrix = compute_editing_dist(seq_x, seq_y)
