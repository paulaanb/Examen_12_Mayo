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

#Ahora unimos estos datos a la tabla navegacion para ver si convierten o no
data = []
only_user = navegacion["id_user"]
for user in only_user:
    convierte = False
    for i in conversiones["id_user"]:
        if user == i:
            convierte = True
    
    if convierte:
        data.append(1)
    else:
        data.append(0)

navegacion["convierte"] = data

#Comprobamos el coche más visitado de la página usando la direccion http del enunciado
cars = {
    
}

for i in range(navegacion.shape[0]):
    m = re.search("http(?:s?):\/(?:\/?)www\.metropolis\.com\/es\/(.+?)\/.*", str(navegacion._get_value(i, "url_landing")))
    if m != None:
        if m.groups()[0] in cars:
            cars[m.groups()[0]] += 1
        else:
            cars[m.groups()[0]] = 1
        
for car in cars.keys():
    print("El coche", car, "ha sido buscado un total de", cars[car], "veces")


#Ahora separamos las columnas de la tabla
campaña = []
adg = []
adv = []
sl = []
urls = navegacion["url_landing"]
#Id campaña
for url in urls:
    try:
        esp = str(url).split("camp=")
        bueno = esp[1].split("&")
        campaña.append(bueno[0])
    except:
        campaña.append(0)
#Id adgroup
for url in urls:
    try:
        esp = str(url).split("adg=")
        bueno = esp[1].split("&")
        adg.append(bueno[0])
    except:
        adg.append(0)
#adv
for url in urls:
    try:
        esp = str(url).split("adv=")
        bueno = esp[1].split("&")
        adv.append(bueno[0])
    except:
        adv.append(0)
#sl
for url in urls:
    try:
        esp = str(url).split("sl=")
        bueno = esp[1].split("&")
        sl.append(bueno[0])
    except:
        sl.append(0)
navegacion["id_camp"] = campaña
navegacion["id_adg"] = adg
navegacion["id_adv"] = adv
navegacion["id_sl"] = sl

print(navegacion)

#Una vez hemos modificado los datos de la tabla, procededmos a guardarlos
navegacion.to_csv("navegacion_corregido.csv", index = False)
