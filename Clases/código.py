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

#Ahora respondemos a la pregunta de que tipo de conversion, CALL o FORM, la cantidad de cada una
#Comprobamos que no hay ningun dato repetido
call = 0
form = 0
tipoconversion = conversiones["lead_type"]
for type in tipoconversion:
    if type == "CALL":
        call += 1
    else:
        form += 1

print("EL numero de conversiones generadas del tipo CALL es:", call)
print("EL numero de conversiones generadas del tipo FORM es:", form)


#Respondemos a la pregunta del porcentaje de usuarios recurrentes sobre el total de usuarios
#Como solo podemos contabilizar al usuario una vez creamos una funcion para tal tarea
usuariorecurrente={()}
numerodeusuario={()}

for i in range(navegacion.shape[0]):
    numerodeusuario.add(navegacion._get_value(i, "id_user"))
    if navegacion._get_value(i, "recurrente") == True:
        usuariorecurrente.add(navegacion._get_value(i, "id_user"))
print("El porcentaje de usuarios recurrentes en comparacion con los usuarios totales es del ", len(usuariorecurrente)/len(numerodeusuario)*100, end="%\n")


