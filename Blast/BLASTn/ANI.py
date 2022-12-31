import pandas as pd


"""
Function to compute bbh length
"""""
def cds_bbh_len (file, blastn_res_table):
    df = pd.read_csv(blastn_res_table, sep='\t')
    seq_id = df[df.columns[0]]  #blast seq id
    seq_id = seq_id.values.tolist()
    header = None
    length = 0
    count = 0
    with open(file) as fasta:  #CDS from genomic file
        for line in fasta :
            line = line.rstrip()
            if (line.startswith('>')) and (line in seq_id):
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
EN:Function to calculate ANI using best hits only
FR: Fonction pour calculer ANI en utilisant les best hits 
"""""
def ANI (blastn_res_table, file) :
    df = pd.read_csv(blastn_res_table, sep='\t')
    p_identity = df[df.columns[4]]
    alignement_len = df[df.columns[5]]
    numerateur = (p_identity * alignement_len).sum()
    res = numerateur/ cds_bbh_len(file, blastn_res_table)
    print("l'ANI est de : ", res)


print("Petrotoga miotherma:")
ANI("blast_mobilis_miotherma.csv","miotherma_cds_from_genomic.fna")
print("Petrotoga halophila:")
ANI("blast_mobilis_halophila.csv","halophila_cds_from_genomic.fna")
print("Marinitoga piezophila KA3:")
ANI("blast_mobilis_piezo.csv","piezophila_cds_from_genomic.fna")
print("Marinitoga hydrogenitolerans DSM 16785:")
ANI("blast_mobilis_hydro.csv","hydro_cds_from_genomic.fna")







