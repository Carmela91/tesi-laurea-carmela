import pandas as pd

# Percorsi dei file
path_security = "data/raw/estat_isoc_cisce_ra.tsv.gz"
path_cloud = "data/raw/estat_isoc_cicce_use.tsv.gz"
path_ict = "data/raw/estat_isoc_ci_it_en2.tsv.gz"

# Caricamento dataset
df_security = pd.read_csv(path_security, sep="\t", compression="gzip")
df_cloud = pd.read_csv(path_cloud, sep="\t", compression="gzip")
df_ict = pd.read_csv(path_ict, sep="\t", compression="gzip")

# Stampa prime righe
print("ICT Security:")
print(df_security.head(), "\n")

print("Cloud Computing:")
print(df_cloud.head(), "\n")

print("ICT Usage:")
print(df_ict.head(), "\n")
