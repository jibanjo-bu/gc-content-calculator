def gc_content(seq):
    seq = seq.upper()
    return (seq.count('G') + seq.count('C')) / len(seq) * 100

dna = input("Enter DNA sequence: ")
print("GC Content:", gc_content(dna))
