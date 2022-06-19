import sys

#Checks if DNA is in fact DNA
def DNA_checker(DNA):
    for i in range(len(DNA)):
        if DNA[i] not in "ACGT":
            return -1

#Gives Nitrogenous base % rounded to first place
def n_percentage(DNA):
    for base in 'AGCT':
        percent = round(DNA.count(base) / len(DNA) * 100, 2)
        print('Base ' + base + ' percentage: ' + str(percent) + "%")


#Makes DNA to RNA (assumed DNA is template strand)
def RNA_polymerase(DNA):
    mRNA = ""
    dna_to_rna = {'A':'U', 'G':'C', 'C':'G','T':'A'}
    for i in range(len(DNA)):
        mRNA += dna_to_rna[DNA[i]]
    return mRNA

#Prints out RNA transcripted from DNA
def DNA_transcription(DNA):
    RNA = RNA_polymerase(DNA)
    print('mRNA: ' + str(RNA))


def Protein_synthesis(DNA):
    table = {
		'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
		'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
		'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
		'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',				
		'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
		'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
		'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
		'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
		'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
		'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
		'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
		'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
		'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
		'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
		'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
		'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
	}

    protein = ""
    size = len(DNA)
    for i in range(0, size, 3):
        codon = DNA[i : i+3]
        protein += table[codon]
    return protein

#DNA translation
def DNA_translation(DNA):
    protein = Protein_synthesis(DNA)
    print("Protein: " + protein)


def main():
    print('Choose Process: \n (1) DNA Transcription \n (2) DNA Translation \n')
    command = input("type '1' or '2' only' \n")

    while command not in ['1', '2']:
        print("Unrecognized Command \n Please select '1' or '2'")
        command = input("type '1' or '2' only' \n")

    DNA = input("DNA: ").upper()

    if DNA_checker(DNA) == -1:
        sys.exit("ERROR unrecognized sequence typed, type DNA with proper base sequences")

    if command == '2' and len(DNA) % 3 != 0:
        sys.exit("Error - DNA Sequence not valid for translation (missing or extra length?)")

    n_percentage(DNA)
    if command == '1':
        DNA_transcription(DNA)
    elif command == '2':
        DNA_translation(DNA)

# main function
main()