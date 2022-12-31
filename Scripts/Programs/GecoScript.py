import pandas as pd

def CDS_stats(feature_table, genome_size) :
    # read data from feature table in .csv format
    df = pd.read_csv(feature_table, sep='\t')
    # retrieve all CDS
    all_CDS = df.loc[df['# feature'] == 'CDS']
    # retrieve all CDS with proteins
    protein_CDS = all_CDS.loc[df['class'] == 'with_protein']
    # select the lengths of CDS with proteins
    df_new = protein_CDS[['# feature', 'feature_interval_length']]
    # max value in feature_interval_length column
    max = df_new['feature_interval_length'].max()
    # mean cds length
    mean = round(df_new['feature_interval_length'].sum() / len(df_new['feature_interval_length']),3)
    # result
    print("The number of CDS:", len(df_new) , ", mean CDS length:", mean ,", max CDS length:", max)
    print("The coding density is:", round(((df_new['feature_interval_length'].sum() / genome_size) * 100), 3))


print("petrotoga mobilis stats:")
CDS_stats("petrotoga_mobilis_feature_table.csv",2169548)
print("petrotoga miotherma stats:")
CDS_stats("petrotoga_miotherma_feature_table.csv", 2107090)
print("petrotoga halophila stats:")
CDS_stats("petrotoga_halophila_feature_table.csv",2820836 )
print("marinitoga piezophila stats:")
CDS_stats("marinitoga_piezophila_feature_table.csv", 2244793)
print("marinitoga hydrogenitolerans stats:")
CDS_stats("Marinitoga_hydrogenitolerans _feature_table.csv", 2312367)


##################################################################################################################
##################################################################################################################

def verify_rna_stats(feature_table) :
    # read data from feature table in .csv format
    df = pd.read_csv(feature_table, sep='\t')
    # trna
    trna = df.loc[df['class'] == 'tRNA']
    # rrna
    rrna = df.loc[df['class'] == 'rRNA']
    print("The number of tRNA is:", len(trna), ", the number of rRNA is:" , len(rrna))

print("##########")
print("petrotoga mobilis rna stats:")
verify_rna_stats("petrotoga_mobilis_feature_table.csv")
print("petrotoga miotherma rna stats:")
verify_rna_stats("petrotoga_miotherma_feature_table.csv")
print("petrotoga halophila rna stats:")
verify_rna_stats("petrotoga_halophila_feature_table.csv")
print("marinitoga piezophila rna stats:")
verify_rna_stats("marinitoga_piezophila_feature_table.csv")
print("marinitoga hydrogenitolerans rna stats:")
verify_rna_stats("Marinitoga_hydrogenitolerans _feature_table.csv")

##################################################################################################################
##################################################################################################################


def gene_stats(feature_table) :
    # read data from feature table in .csv format
    df = pd.read_csv(feature_table, sep='\t')
    # genes
    genes = df.loc[df['# feature'] == 'gene']
    print("The number of genes is:" , len(genes))
    mean = round(genes['feature_interval_length'].sum() / len(genes['feature_interval_length']), 3)
    print("Avg gene length:", mean)


print("##########")
print("petrotoga mobilis gene stats:")
gene_stats("petrotoga_mobilis_feature_table.csv")
print("petrotoga miotherma gene stats:")
gene_stats("petrotoga_miotherma_feature_table.csv")
print("petrotoga halophila gene stats:")
gene_stats("petrotoga_halophila_feature_table.csv")
print("marinitoga piezophila gene stats:")
gene_stats("marinitoga_piezophila_feature_table.csv")
print("marinitoga hydrogenitolerans gene stats:")
gene_stats("Marinitoga_hydrogenitolerans _feature_table.csv")

##################################################################################################################
##################################################################################################################
"""
Classification of the COGs by functional categories. One-letter abbreviations for the functional categories: 
J, translation, including ribosome structure and biogenesis; 
L, replication, recombination and repair; K, transcription;
O, molecular chaperones and related functions; M, cell wall structure and biogenesis and outer membrane; 
N, secretion, motility and chemotaxis; T, signal transduction; P, inorganic ion transport and metabolism; 
C, energy production and conversion; G, carbohydrate metabolism and transport; E, amino acid metabolism and transport; 
F, nucleotide metabolism and transport; H, coenzyme metabolism; 
I, lipid metabolism; D, cell division and chromosome partitioning; R, general functional prediction only; 
S, no functional prediction.

"""
def cog_stats(filename):
    df = pd.read_csv(filename, sep='\t')
    # retrieve cog column
    df_new = df[['COG_category']]
    sans_cog = df.loc[df['COG_category'] == '-']
    no_functional_pred = df.loc[df['COG_category'] == 'S']
    print("########COG SECTION#######")
    print("Nb of prot assigned to cog categories: " + str(len(df_new)-len(sans_cog)-3))
    print("Nb of prot with no cog categories: "+ str(len(sans_cog)))
    # Predicted fct: cog categories - S category
    print("Proteins with predicted functions: " + str((len(df_new)-len(sans_cog)-3)-len(no_functional_pred)))
    # Proteins involved in signal transduction
    transd_cog = df.loc[df['COG_category'] == 'T']
    print("Nb of prot involved in signal transduction mechanisms: " + str(len(transd_cog)))
    # Proteins involved in replication, recombination and repair
    repl_cog = df.loc[df['COG_category'] == 'L']
    print("Nb of prot involved in replication, recombination and repair: " + str(len(repl_cog)))
    # Proteins involved in amino acid metabolism and transport
    E_cog = df.loc[df['COG_category'] == 'E']
    print("Nb of prot involved in amino acid metabolism and transport: " + str(len(E_cog)))

    # Proteins involved in  nucleotide metabolism and transport
    F_cog = df.loc[df['COG_category'] == 'F']
    print("Nb of prot involved in nucleotide metabolism and transport: " + str(len(F_cog)))

    # Proteins involved in  inorganic ion transport and metabolism
    p_cog = df.loc[df['COG_category'] == 'P']
    print("Nb of prot involved in inorganic ion transport and metabolism: " + str(len(p_cog)))


cog_stats("../petrotoga mobilis/eggnog2/eggnog_mobilis.tsv")
cog_stats("../petrotoga miotherma/eggnog2/eggnog.tsv")
cog_stats("../petrotoga halophila/eggnog2/eggnog.tsv" )
cog_stats("../Marinitoga piezophila KA3/eggnog2/eggnog_ka3.tsv" )
cog_stats("../Marinitoga hydrogenitolerans DSM 16785/eggnog2/eggnog.tsv")

