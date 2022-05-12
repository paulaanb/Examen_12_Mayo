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

#Imprimimos el numero de visitas que el cliente recibe en el dia, y de ellas, cuantas convierten y cuantas no, en %
print("El número de visitas que recibe el cliente en el dia es:", "/n", navegacion.shape[0], "visitas")

usuariosconvertidos = 0
idusers_navegacion = navegacion["id_user"]
idusers_conversion = conversiones["id_user"]
for user_navegacion in idusers_navegacion:
    for user_conversion in idusers_conversion:
        if user_navegacion == user_conversion:
            usuariosconvertidos += 1

print("El porcentaje de visitas que recibe el cliente que estan convertidas alcanza un porcentaje del " ,usuariosconvertidos/navegacion.shape[0]*100, end="%\n")




