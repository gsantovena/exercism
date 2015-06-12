def to_rna(strand):
    complements = { 'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U' }
    rna = ''
    for i in strand:
        rna = rna + complements[i]
    return rna

