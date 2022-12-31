
"""
This script uses EggNogMapperV2 output to generate stats based on the functional categories

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
    T_cog = df.loc[df['COG_category'] == 'T']
    print("Nb of prot involved in signal transduction mechanisms: " + str(len(T_cog)))
    # Proteins involved in replication, recombination and repair
    L_cog = df.loc[df['COG_category'] == 'L']
    print("Nb of prot involved in replication, recombination and repair: " + str(len(L_cog)))
    # Proteins involved in amino acid metabolism and transport
    E_cog = df.loc[df['COG_category'] == 'E']
    print("Nb of prot involved in amino acid metabolism and transport: " + str(len(E_cog)))
    # Proteins involved in  nucleotide metabolism and transport
    F_cog = df.loc[df['COG_category'] == 'F']
    print("Nb of prot involved in nucleotide metabolism and transport: " + str(len(F_cog)))
    # Proteins involved in  inorganic ion transport and metabolism
    P_cog = df.loc[df['COG_category'] == 'P']
    print("Nb of prot involved in inorganic ion transport and metabolism: " + str(len(P_cog)))


cog_stats("../petrotoga mobilis/eggnog2/eggnog_mobilis.tsv")
cog_stats("../petrotoga miotherma/eggnog2/eggnog.tsv")
cog_stats("../petrotoga halophila/eggnog2/eggnog.tsv" )
cog_stats("../Marinitoga piezophila KA3/eggnog2/eggnog_ka3.tsv" )
cog_stats("../Marinitoga hydrogenitolerans DSM 16785/eggnog2/eggnog.tsv")
