'''
Generate skew map from a sequence
Skew map considers the ration of C/G in a seq.
Appearance of C decreasesw the skew value, G increases the value
'''

def skew_diagram(text):
    skew_value = [0]
    for i in text:
        if i == 'C':
            skew_value.append(skew_value[-1] - 1)
        elif i == 'G':
            skew_value.append(skew_value[-1] + 1)
        else: 
            skew_value.append(skew_value[-1])
    minimum_skew = min(skew_value)
    minimum_point = [i for i in range(len(skew_value)) if skew_value[i] == minimum_skew]
    print minimum_point
    return skew_value

print skew_diagram('CATTCCAGTACTTCATGATGGCGTGAAGA')
