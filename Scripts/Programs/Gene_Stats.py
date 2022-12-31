import pandas as pd

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
