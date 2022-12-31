import pandas as pd


"""
la longueur des bbh 
"""""
def prots_len (file, blastp_res_table):
    df = pd.read_csv(blastp_res_table, sep='\t')
    seq_id = df[df.columns[0]]  #blast seq id
    seq_id = seq_id.values.tolist()
    header = None
    length = 0
    count = 0
    with open(file) as fasta:  #prot file
        for line in fasta:
            line = line.rstrip()
            if (line.startswith('>')) and (line[1:] in seq_id):
                if header is not None:
                    print(length)
                    count += length
                    length = 0
                header = line[1:]
            else:
                length += len(line)

    # Don't forget the last one
    if length:
        count += length
        return count


"""
Fonction pour calculer AAI en utilisant les best hits
"""""
def AAI (blastp_res_table, file) :
    df = pd.read_csv(blastp_res_table, sep='\t')
    p_identity = df[df.columns[4]]
    # select identity >30% because blastp version couldn't filter directly based on id
    p_identity30 = p_identity[p_identity>30]
    alignement_len = df[df.columns[5]]
    numerateur = (p_identity30 * alignement_len).sum()
    res = numerateur/ prots_len (file, blastp_res_table)
    print("l'AAI est de : ", res)

print("Petrotoga miotherma:")
AAI("blast_mobilis_miotherma.csv","miotherma_protein.faa")
print("Petrotoga halophila:")
AAI("blast_mobilis_halophila.csv","halophila_protein.faa")
print("Marinitoga piezophila KA3:")
AAI("blast_mobilis_piezo.csv","piezophila_protein.faa")
print("Marinitoga hydrogenitolerans DSM 16785:")
AAI("blast_mobilis_hydro.csv","hydro_protein.faa")





