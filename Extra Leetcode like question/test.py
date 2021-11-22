dna = 'CAAATGCAGGCGTAA'
start_codon: str = "AUG"
stop_codon: str = "STOP"
codon_to_amino_acid= {
    "AUG": "Met",
    "CAA": "Gln",
    "CAG": "Gln",
    "GGU": "Gly",
    "GCG": "Ala",
    "UUU": "Phe",
    "UUC": "Phe",
    "UGG": "Trp",
    "UAA": stop_codon,
    "UAG": stop_codon,
    "UGA": stop_codon,
}


def protein_synthesis_part_one(dna):
    # Write your code here
    rna = ''
    for i in range(len(dna)):
        if dna[i] == "T":
            rna += "U"
        else:
            rna += dna[i]
    dna = dna.strip()
    rna_list = []

    for i in range(0, len(rna), 3):
        rna_list.append(rna[i:i + 3])

    print(rna_list)

    res = []
    translation = False

    while rna_list:
        rna = rna_list.pop(0)
        if codon_to_amino_acid[rna] == "Met":
            translation = True
            res.append(codon_to_amino_acid[rna])

        if translation == True and codon_to_amino_acid[rna] == stop_codon:
            translation = False
            break

        if translation == True:
            res.append(codon_to_amino_acid[rna])

    res = ' '.join(res)
    print(res)
    return res


def protein_synthesis_part_two(dna):
    rna = ''
    for i in range(len(dna)):
        if dna[i] == "T":
            rna += "U"
        else:
            rna += dna[i]
    rna_list = []

    for i in range(0, len(rna), 3):
        if rna[i:i + 3].isupper():
            rna_list.append(rna[i:i + 3])
    print(rna_list)

    res = []
    translation = False

    while rna_list:
        rna = rna_list.pop(0)

        if translation == True and codon_to_amino_acid[rna] == stop_codon:
            translation = False
            break

        if translation == True:
            res.append(codon_to_amino_acid[rna])

        elif codon_to_amino_acid[rna] == "Met":
            translation = True
            res.append(codon_to_amino_acid[rna])

    res = ' '.join(res)
    print(res)
    return res
x = 'uagATGcagCAGuaaGCGugaTAA'
x2 = 'ATGATGATGATGATGugg'
protein_synthesis_part_one(dna)
print(protein_synthesis_part_two(x2))