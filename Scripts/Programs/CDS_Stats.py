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
