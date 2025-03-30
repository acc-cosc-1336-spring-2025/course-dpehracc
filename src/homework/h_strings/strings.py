#Value return functions
def get_hamming_distance(dna1, dna2):
    hamming_distance = 0
    for i in range(len(dna1)): # Loop through each character in the DNA strings
        if dna1[i] != dna2[i]:
            hamming_distance += 1
    return hamming_distance

def get_dna_complement(dna):
    complement = ""
    for i in range(len(dna) - 1, -1, -1): # Loop through each character in reverse
        if dna[i] == 'A':
            complement += 'T'
        elif dna[i] == 'T':
            complement += 'A'
        elif dna[i] == 'C':
            complement += 'G'
        elif dna[i] == 'G':
            complement += 'C'
    return complement
