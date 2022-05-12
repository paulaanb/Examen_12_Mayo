import pandas as pd
df = pd.read_csv('conversiones.csv')

#Separamos la columna campaña
df["camp"].str.split()
