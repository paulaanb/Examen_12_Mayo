# Examen_12_Mayo
La direccion de Github de este repositorio es : [https://github.com/paulaanb/Examen_12_Mayo]

# ENUNCIADO
Análisis de datos de navegación y conversión de usuarios.
Los usuarios cuando quieren contratar un producto lo buscan en internet, y llegan en la mayoría de los casos a unas páginas web especializadas en conversión llamadas landings. Estas landings suelen contener un teléfono al cual el usuario puede llamar al call center de la compañía y/o también un formulario en el cual dejan su nombre y su teléfono para que dicho call center se ponga en contacto con ellos.

Existen diferentes tipos de conversiones siendo los más comunes:

 ·        simplemente el contacto con el call center ya sea a través de una llamada o del envío del formulario.

·        Contratación del producto 

Nuestro ejercicio
El cliente es una compañía de coches y nos pide que le realicemos informes sobre las visitas a las landings de sus productos y las conversiones.

Datos
 Tenemos dos tipos de ficheros:

1) De navegación, en el que se recogen los datos de navegación de los usuarios. Este fichero contiene las siguientes columnas:

uuid(string): Es utilizado para crear identificadores únicos universales que permitan reconocer e distinguir un objeto dentro de un sistema, o el mismo objeto en diferentes contextos. En este caso el objeto es el usuario. gclid(string): El ID de clic de Google (GCLID) es un parámetro que se transfiere a la URL a través de los clics en anuncios.
id_user(string): identificador único de usuario de la aplicación que se comunica con el call center
user_recurrent(boolean): nos indica si el usuario es recurrente (true), es decir, si ha entrado más de una vez al conjunto de landings de la compañía. Si no es recurrente (false), significa que el usuario está entrando por primera vez al conjunto de landings.
url_landing (string): cuando el usuario hace click en un anuncio o sitelink se lo envía a una landing con una url que contiene varios datos interesantes para su análisis. A continuación, explicamos cada parte de esta url.
Ejemplo:
https://www.metropolis.com/es/home/gclid=Cj0KCQjw1dGJBhD4ARIsANb6OdmV6XYIc MpvAhDvnmHLRGVelRzIeciTG3j1ItnthWfYtV_XFWKDhLsaAr4sEALw_wcB&iduser=ec 1eef0d-6141-4a85-86cc-979a653362eb&uuid=1a05bd93-b939-4661-924b- a643cfcec3de&camp=732187328&adg=46724581628&device=m&sl=&adv=533655604 703&rec=false
https://www.metropolis.com/es/ es la url base
 

Después de la url base le sigue la landing específica a la cual ha ido el usuario: home (que sería la web principal), o una landing de algún modelo de coche.

Luego siguen: gclid, iduser, uuid que ya los hemos definido anteriormente Finalmente tenemos los datos de las campañas:

camp: id de la campaña
adg: id del adgroup
 device: dispositivo desde el cual el usuario está accediendo a la landing. c: computer, t: tablet, m: móvil
adv: id del anuncio
  sl: id del sitelink. Este puede ser un número si el usuario ha hecho click en el sitelink, o 0 o vacío si el usuario ha hecho click en el anuncio.
2)    En el caso del fichero de conversiones tenemos las siguientes columnas:

date: fecha de la conversión hour: hora de la conversión
id_lead: identificador único de la conversión
lead_type: tipo de conversión, CALL el usuario llama directamente al call center, FORM el usuario rellena un formulario y espera que el call center lo llame
result: resultado después de haber hablado con el call center
·        ilocalizable: no logran hablar con el usuario porque justo el usuario cuelga la llamada o no atiende

·        Positivo: que le interesa y va a contratar

·        No le interesa

Pistas
Una campaña puede contener uno o varios grupos de anuncios. Y un grupo de anuncios puede contener uno o varios anuncios.
Los sitelinks suelen depender solo de la campaña. Es decir, una campaña puede contener uno o varios sitelinks.
 Preguntas a responder

Cuántas visitas recibe en el día el cliente y de estas,   cuántas de ellas convierten y cuántas no (en %)
Por tipo de conversión (CALL o FORM), ¿Cuántas hay de cada una?
Porcentaje de usuarios recurrentes sobre el total de usuarios
Coche más visitado. ¿Es el que más convierte?
La justificación de estas respuestas será un informe con datos gráficos y analíticos donde nos den las conclusiones de los mismos. Además se acompañará de código para apoyar la solución


 

 

Descripción de la actividad
Pasos para realizar la práctica

1) Leer los datos con python. Ficheros de navegación y de conversión

2)Separar los datos en columnas, y obtener para cada línea de navegación: campaña, adgoup, advertisement y site link que se obtiene de la columna URL.

3)Identificar si hay usuarios repetidos: id_user, gclid, cookie

Para los que no tienen id_user, hay que mirar el gclid, y si tampoco está hay que mirar la cookie

Y ordenar los datos según ts

4)Unir los datos de navegación ya tratados con los datos de conversiones,creando una columna de 0 y 1 indicando si el usuario no ha convertido o si ha convertido. La unión se hace a partir de la columna id_suite, si esta está vacía sería por la de gclid, y si esta está vacía también por cookie.

Nota: tenemos 2 opciones

a)Si hay usuarios repetidos nos quedamos con un solo dato

b)Si nos quedamos con todos los datos repetidos buscar el más cercano a la conversión (este punto es más complicado, es solo para quienes se atrevan)

1)Con estos datos ya unidos y tratados debemos realizar diferentes informes que se proponen en el apartado siguiente (Entrega individual)


# SOLUCION
Las soluciones de este ejercicio estan resueltas en el código siguiente:
 ```


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

