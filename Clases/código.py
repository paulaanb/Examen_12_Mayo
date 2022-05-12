#Importamos las librerias que tenemos que utilizar
import re
from numpy import shares_memory
from numpy.lib.function_base import append
import pandas as pd
from pandas import tseries

#Separamos el archivo por columnas como nos pedian
conversiones = pd.read_csv("conversiones.csv", sep = ";")
navegacion = pd.read_csv("navegacion.csv", sep = ";")

index = []
for i in range(conversiones.shape[0]):
    if conversiones._get_value(i, "id_user") == "None":
        index.append(i)

conversiones = pd.DataFrame(conversiones.drop(conversiones.index[index]), columns = conversiones.columns)
conversiones = conversiones.reset_index()




