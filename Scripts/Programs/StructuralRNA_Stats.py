import pandas as pd

"""
This script calculates the number of trna and rna based on feature tables
"""

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
