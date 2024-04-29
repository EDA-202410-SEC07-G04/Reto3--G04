"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
from datetime import datetime as dt
#import folium
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos
#data_struct = None

def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    catalog = {'info': None,
               'jobs': None,
               'multilocations': None,
               'skills': None,
               'req7': None,
               "countries": None, 
               "dates": None}
    
    catalog['jobs'] = lt.newList("ARRAY_LIST")

    ##revisar numero elementos 
    catalog["req7"] = mp.newMap(203562,
                                   maptype='CHAINING',
                                   loadfactor=4)
    
    catalog['skills'] = mp.newMap(577166, #tamaño igual al size de jobs
                                  maptype='CHAINING',
                                  loadfactor=4)

    catalog['paises'] = mp.newMap(577166, #tamaño igual al size de jobs
                                  maptype='CHAINING',
                                  loadfactor=4)

    catalog["countries"] = om.newMap(omaptype="BST",
                                      cmpfunction=compareXp2)

    catalog["dates"] = om.newMap(omaptype="BST",
                                      cmpfunction=compareNames)
    #workplace_type
    catalog["cities"] = om.newMap(omaptype="BST",
                                      cmpfunction=compareUbi)

    catalog["types"] = om.newMap(omaptype="BST",
                                      cmpfunction=compareUbi)

    catalog["habilidades"] = lt.newList("ARRAY_LIST")



    return catalog 


# Funciones para agregar informacion al modelo

def add_job(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    lt.addLast(data_structs["jobs"],data)
    #update_req7(data_structs["req7"], data)
    updateCountries(data_structs["countries"], data)
    updateDates(data_structs["dates"], data)
    updateCities(data_structs["cities"], data)
    
    return data_structs

def add_job2(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    updateTypes(data_structs["types"], data)

    return data_structs

def add_job3(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    lt.addLast(data_structs["habilidades"], data)

    return data_structs

def add_skill(datastructs, skill):
    update_skills(datastructs["skills"], skill)

def update_skills(map, data):
    id = data["id"]

    if mp.contains(map, id):
        value = me.getValue(mp.get(map,id))
        lt.addLast(value, data)
    else:
        lista_skills = lt.newList("ARRAY_LIST")
        lt.addLast(lista_skills, data)
        mp.put(map, id, lista_skills)

def update_req7(map, data):
    pais = data["country_code"]

    if mp.contains(map, pais):
        value = me.getValue(mp.get(map, pais)) #obtener arbol del mapa
        update_arbol7(value, data)
    else:
        new_arbol = nuevo_arbol7()
        update_arbol7(new_arbol, data)
        mp.put(map, pais, new_arbol)

def nuevo_arbol7():
    return om.newMap() #definir funcion de comparación y tipo de arbol

def update_arbol7(new_arbol, data):
    anho = data["date"] #cambiar para filtrar el año

    if om.contains(new_arbol, anho):
        value= me.getValue(om.get(new_arbol, anho))
        lt.addLast(value, data)
    else:
        lista_jobs = lt.newList("ARRAY_LIST")
        lt.addLast(lista_jobs, data)
        om.put(new_arbol, anho, lista_jobs)




def updateCountries(mapa, job):
    countryName = job["country_code"].lower()
    entry = om.get(mapa, countryName)
    if entry is None:
        namentry = newDataEntry(job)
        om.put(mapa, countryName, namentry)
    else:
        namentry = me.getValue(entry)
    addNameEntry(namentry, job)
    return mapa

def addNameEntry(namentry, job):  
    lst = namentry["lstjobs"]
    #print(namentry)
    lt.addLast(lst, job)
    name = namentry['name']
    #print(name)
    xp = str(job['experience_level'].lower())
    offentry = mp.get(name, xp)
    if (offentry is None):
        entry = newNameEntry(xp, job)
        lt.addLast(entry['lstjobs'], job)
        mp.put(name, xp, entry)
    else:
        entry = me.getValue(offentry)
        lt.addLast(entry['lstjobs'], job)
    return namentry
"""
def addDateEntry(namentry, job):  
    lst = namentry["lstjobs"]
    #print(namentry)
    lt.addLast(lst, job)
    companyName = namentry['name']
    #print(companyName)
    nome = job["company_name"]
    offentry = mp.get(companyName, nome)
    if (offentry is None):
        entry = newNameEntry2(nome, job)
        lt.addLast(entry['lstjobs'], job)
        mp.put(companyName, nome, entry)
    else:
        entry = me.getValue(offentry)
        lt.addLast(entry['lstjobs'], job)
    return namentry
"""
def newDataEntry(job):
    #print(job)
    entry = {'name': None, 'lstjobs': None}
    entry['name'] = mp.newMap(numelements=30,
                                     maptype='PROBING',
                                     cmpfunction=compareXp)
    entry['lstjobs'] = lt.newList('SINGLE_LINKED', compareNames)
    lt.addLast(entry["lstjobs"], job)
    return entry
"""
def newDataEntry2(job):
    #print(job)
    entry = {'name': None, 'lstjobs': None}
    entry['name'] = mp.newMap(numelements=30,
                                     maptype='PROBING',
                                     cmpfunction=compareNames2)
    entry['lstjobs'] = lt.newList('SINGLE_LINKED', compareDates2)
    lt.addLast(entry["lstjobs"], job)
    return entry
"""
def newNameEntry(offensegrp, crime):
    """
    Crea una entrada en el indice por tipo de crimen, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    ofentry = {"job": None, "lstjobs": None}
    ofentry["job"] = offensegrp
    ofentry["lstjobs"] = lt.newList("SINGLE_LINKED", compareNames)
    lt.addLast(ofentry["lstjobs"], crime)
    return ofentry
"""
def newNameEntry2(offensegrp, crime):
    ofentry = {"job": None, "lstjobs": None}
    ofentry["job"] = offensegrp
    ofentry["lstjobs"] = lt.newList("SINGLE_LINKED", compareDates2)
    lt.addLast(ofentry["lstjobs"], crime)
    return ofentry
"""
def updateDates(mapa, job):
    date = dt.strptime(job['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
    fecha_final = str(date.strftime("%Y-%m-%d"))
    entry = om.get(mapa, fecha_final)
    if entry is None:
        namentry = newDataEntry2(job)
        om.put(mapa, fecha_final, namentry)
    else:
        namentry = me.getValue(entry)
    addDateEntry(namentry, job)
    return mapa

def addDateEntry(namentry, job):  
    lst = namentry["lstjobs"]
    #print(namentry)
    lt.addLast(lst, job)
    companyName = namentry['name']
    #print(companyName)
    nome = job["id"]
    offentry = mp.get(companyName, nome)
    if (offentry is None):
        entry = newNameEntry2(nome, job)
        lt.addLast(entry['lstjobs'], job)
        mp.put(companyName, nome, entry)
    else:
        entry = me.getValue(offentry)
        lt.addLast(entry['lstjobs'], job)
    return namentry
    
def newDataEntry2(job):
    #print(job)
    entry = {'name': None, 'lstjobs': None}
    entry['name'] = mp.newMap(numelements=30,
                                     maptype='PROBING',
                                     cmpfunction=compareNames2)
    entry['lstjobs'] = lt.newList('SINGLE_LINKED', compareDates2)
    lt.addLast(entry["lstjobs"], job)
    return entry

def newNameEntry2(offensegrp, crime):
    ofentry = {"job": None, "lstjobs": None}
    ofentry["job"] = offensegrp
    ofentry["lstjobs"] = lt.newList("SINGLE_LINKED", compareDates2)
    lt.addLast(ofentry["lstjobs"], crime)
    return ofentry

def updateCities(mapa, job):
    ciuu = str(job["city"].lower())
    entry = om.get(mapa, ciuu)
    if entry is None:
        namentry = newDataEntry3(job)
        om.put(mapa, ciuu, namentry)
    else:
        namentry = me.getValue(entry)
    addDateEntry2(namentry, job)
    return mapa

def addDateEntry2(namentry, job):  
    lst = namentry["lstjobs"]
    #print(namentry)
    lt.addLast(lst, job)
    companyName = namentry['name']
    #print(companyName)
    nome = str(job["workplace_type"].lower())
    offentry = mp.get(companyName, nome)
    if (offentry is None):
        entry = newNameEntry3(nome, job)
        lt.addLast(entry['lstjobs'], job)
        mp.put(companyName, nome, entry)
    else:
        entry = me.getValue(offentry)
        lt.addLast(entry['lstjobs'], job)
    return namentry
    
def newDataEntry3(job):
    #print(job)
    entry = {'name': None, 'lstjobs': None}
    entry['name'] = mp.newMap(numelements=30,
                                     maptype='PROBING',
                                     cmpfunction=compareCities)
    entry['lstjobs'] = lt.newList('SINGLE_LINKED', compareUbi)
    lt.addLast(entry["lstjobs"], job)
    return entry

def newNameEntry3(offensegrp, crime):
    """
    Crea una entrada en el indice por tipo de crimen, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    ofentry = {"job": None, "lstjobs": None}
    ofentry["job"] = offensegrp
    ofentry["lstjobs"] = lt.newList("SINGLE_LINKED", compareUbi)
    lt.addLast(ofentry["lstjobs"], crime)
    return ofentry

def updateTypes(mapa, job):
    c1 = (job["salary_from"])
    c2 = (job["salary_to"])
    if job["salary_from"] == "" or job["salary_from"] == " " or job["salary_from"] == None:
        c1 = int(1)
    if job["salary_to"] == "" or job["salary_to"] == " " or job["salary_to"] == None:
        c2 = int(1)
    else: 
        c1 = int(job["salary_from"])
        c2 = int(job["salary_to"])
    prom = (c1 + c2)/2
    entry = om.get(mapa, prom)
    if entry is None:
        namentry = newDataEntry4(job)
        om.put(mapa, prom, namentry)
    else:
        namentry = me.getValue(entry)
    addDateEntry3(namentry, job)
    return mapa

def addDateEntry3(namentry, job):  
    lst = namentry["lstjobs"]
    #print(namentry)
    lt.addLast(lst, job)
    companyName = namentry['name']
    #print(companyName)
    nome = str(job["id"])
    offentry = mp.get(companyName, nome)
    if (offentry is None):
        entry = newNameEntry4(nome, job)
        lt.addLast(entry['lstjobs'], job)
        mp.put(companyName, nome, entry)
    else:
        entry = me.getValue(offentry)
        lt.addLast(entry['lstjobs'], job)
    return namentry
    
def newDataEntry4(job):
    #print(job)
    entry = {'name': None, 'lstjobs': None}
    entry['name'] = mp.newMap(numelements=30,
                                     maptype='PROBING',
                                     cmpfunction=compareCities)
    entry['lstjobs'] = lt.newList('SINGLE_LINKED', compareUbi)
    lt.addLast(entry["lstjobs"], job)
    return entry

def newNameEntry4(offensegrp, crime):
    """
    Crea una entrada en el indice por tipo de crimen, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    ofentry = {"job": None, "lstjobs": None}
    ofentry["job"] = offensegrp
    ofentry["lstjobs"] = lt.newList("SINGLE_LINKED", compareUbi)
    lt.addLast(ofentry["lstjobs"], crime)
    return ofentry

# Funciones para creacion de datos

def sizu(data_struct):
    return om.size(data_struct["countries"])

def fechas_canti(data_struct):
    return om.size(data_struct["dates"])

def tamano_total(data_struct):
    return lt.size(data_struct["jobs"])

def pruebas(data_struct):
    var1 = om.values(data_struct["countries"], "co", "co")
    for i in lt.iterator(var1):
        print(i)

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    final = lt.newList("ARRAY_LIST")
    lst = om.values(data_structs["dates"], fecha_inicial, fecha_final)
    ofertas_rango_de_tiempo = 0
    for i in lt.iterator(lst):
        ofertas_rango_de_tiempo += lt.size(i["lstjobs"])
        for x in lt.iterator(i["lstjobs"]):
            lt.addFirst(final, x)
    
    return ofertas_rango_de_tiempo, final



def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs, num_ofertas, pais, xp):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    final = lt.newList("ARRAY_LIST")
    pai = om.get(data_structs["countries"], str(pais))
    #print(pai)
    if pai["key"] is not None:
        mapa = me.getValue(pai)["name"]
        fifa = mp.get(mapa, xp)
        if fifa is not None:
            var1 = me.getValue(fifa)["lstjobs"]
            for i in lt.iterator(var1):
                lt.addLast(final, i)

    if lt.size(final) >= 2:
        sortiao = merg.sort(final, sort_r3)
    elif lt.size(final) <= 1:
        sortiao = final 
    elif lt.isEmpty(final):
        print("Ningun resultado encontrado")
        sys.exit(0)

    if num_ofertas > lt.size(sortiao):
        num_ofertas = lt.size(sortiao)
    elif num_ofertas <= lt.size(sortiao):
        num_ofertas = num_ofertas 
    
    sublista = lt.subList(sortiao, 1, num_ofertas)

    return sublista

    


def req_4(data_structs, num_ofertas, ciudad, ubi):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    final = lt.newList("ARRAY_LIST")
    ciu = om.get(data_structs["cities"], str(ciudad))
    #print(ciu)
    if ciu["key"] is not None:
        mapa = me.getValue(ciu)["name"]
        fifa = mp.get(mapa, ubi)
        if fifa is not None:
            var1 = me.getValue(fifa)["lstjobs"]
            for i in lt.iterator(var1):
                lt.addLast(final, i)

    if lt.size(final) >= 2:
        sortiao = merg.sort(final, sort_r3)
    elif lt.size(final) <= 1:
        sortiao = final 
    elif lt.isEmpty(final):
        print("Ningun resultado encontrado")
        sys.exit(0)

    if num_ofertas > lt.size(sortiao):
        num_ofertas = lt.size(sortiao)
    elif num_ofertas <= lt.size(sortiao):
        num_ofertas = num_ofertas 
    
    sublista = lt.subList(sortiao, 1, num_ofertas)

    return sublista
    


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs, n_ciu, fecha_inicial, fecha_final, sal_min, sal_max):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    final = lt.newList("ARRAY_LIST")
    lst = om.values(data_structs["dates"], fecha_inicial, fecha_final)
    ofertas_rango_de_tiempo = 0
    for i in lt.iterator(lst):
        ofertas_rango_de_tiempo += lt.size(i["lstjobs"])
        for x in lt.iterator(i["lstjobs"]):
            ide = x["id"]
            lt.addFirst(final, x)

    final2 = lt.newList("ARRAY_LIST")
    lst2 = om.values(data_structs["types"], sal_min, sal_max)
    for i in lt.iterator(lst2):
        for x in lt.iterator(i["lstjobs"]):
            lt.addFirst(final2, x)

    
    e1 = req63(final)
    r2 = lt.size(e1)
    sortiao = lt.newList("ARRAY_LIST")
    if lt.size(e1) >= 2:
        sortiao = merg.sort(e1, sort_alfa)
    elif lt.size(e1) <= 1:
        sortiao = e1 
    elif lt.isEmpty(e1):
        print("Ningun resultado encontrado")
        sys.exit(0)

    if n_ciu > lt.size(sortiao):
        num_ofertas = lt.size(sortiao)
    elif n_ciu <= lt.size(sortiao):
        num_ofertas = n_ciu 
    
    r3 = lt.subList(sortiao, 1, num_ofertas)
    repe = req61(final)
    var1 = req62(final, final2, repe, data_structs["habilidades"])
    r4 = lt.newList("ARRAY_LIST")
    if lt.size(var1) >= 2:
        r4 = merg.sort(var1, sort_r6)
    elif lt.size(var1) <= 1:
        r4 = var1 
    elif lt.isEmpty(var1):
        print("Ningun resultado encontrado")
        sys.exit(0)

    r1 = lt.size(final2)
    
    return r1, r2, r3, r4


def req61(lt1):
    ciu = {}
    for a in lt.iterator(lt1):
        nome = a["city"]
        ciu[nome] = ciu.get(nome, 0) + 1

    repe = max(ciu, key=ciu.get)
    return repe
    
def req62(lt1, lt2, repe, lt3):
    ofertas_ciudad = lt.newList("ARRAY_LIST")
    for i in lt.iterator(lt1):
        if i['city'] == repe:
            lt.addLast(ofertas_ciudad, i)

    salmin_por_id = {}
    for q in lt.iterator(lt2):
        salmin_por_id[q['id']] = q['salary_to']

    habi_por_id = {}
    for k in lt.iterator(lt3):
        id_oferta = k["id"]
        if id_oferta not in habi_por_id:
            habi_por_id[id_oferta] = []
        habi_por_id[id_oferta].append(k["name"])

    
    
    finalissima = lt.newList("ARRAY_LIST")
    for of in lt.iterator(ofertas_ciudad):
        habilidad = habi_por_id.get(of['id'], [])
        salario_min = salmin_por_id.get(of['id'], None)
        """
        if salario_min == "" or salario_min == " " or salario_min == None:
            salario_min = int(0)
        else:
            salario_min = int(salario_min)
        """

        if salario_min is not None:
            lt.addLast(finalissima,{
                "fecha_publi": of["published_at"],
                "title": of["title"],
                'compania': of["company_name"],
                "xp": of["experience_level"],
                'pais': of["country_code"],
                "city": repe,
                "company_size": of["company_size"],
                "workplace_type": of["workplace_type"],
                'oferta_minima': int(salario_min),
                "habilidad": habilidad,
                "id": of["id"]
            })


    return finalissima


def req63(lst):
    cr7 = lt.newList("ARRAY_LIST")

    for i in lt.iterator(lst):
        if lt.isPresent(cr7, i["city"]) == 0:
            lt.addLast(cr7, i["city"])
        else:
            batman = 0
    
    return cr7


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs, mapa, nom_estru, parent_loc=None):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    root = om.minKey(data_structs[nom_estru])
    if root is not None:
        info = root["lstjobs"]
        for i in lt.iterator(info):
            longi = i["longitude"]
            lati= i["latitude"]

        loca = (lati, longi)
        folium.Marker(location=loca, popup=str(info).add_to(mapa))

        if parent_loc is not None:
            folium.Polyline(locations=[parent_loc, loca], color="blue").add_to(mapa)

        hijos = 32




# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    date2 = me.getKey(date2)
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

# Funciones de ordenamiento

def compareNames(name1, name2):
    #name2 = me.getKey(name2)
    if (name1 == name2):
        return 0
    elif (name1 > name2):
        return 1
    else:
        return -1

def compareDates2(date1, date2):
    """
    Compara dos fechas
    """
    #date2 = me.getKey(date2)
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

# Funciones de ordenamiento

def compareNames2(name1, name2):
    name2 = me.getKey(name2)
    if (name1 == name2):
        return 0
    elif (name1 > name2):
        return 1
    else:
        return -1

def compareXp(xp1, xp2):
    xp2 = me.getKey(xp2)
    if (xp1 == xp2):
        return 0
    elif (xp1 > xp2):
        return 1
    else:
        return -1

def compareCities(c1, c2):
    c2 = me.getKey(c2)
    if (c1 == c2):
        return 0
    elif (c1 > c2):
        return 1
    else:
        return -1

def compareXp2(xp1, xp2):
    if (xp1 == xp2):
        return 0
    elif (xp1 > xp2):
        return 1
    else:
        return -1

def compareUbi(ubi1, ubi2):
    #name2 = me.getKey(name2)
    if (ubi1 == ubi2):
        return 0
    elif (ubi1 > ubi2):
        return 1
    else:
        return -1

def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass

def sort_r3(oferta1, oferta2):
    date1 = dt.strptime(oferta1['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
    date2 = dt.strptime(oferta2['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
    name1 = oferta1['country_code']
    name2 = oferta2['country_code']
    if date1 > date2:
        return True
    elif date1 == date2:
        if name1 < name2:
            return True
        else:
            return False
    else:
        return False

def sort_r6(oferta1, oferta2):
    date1 = dt.strptime(oferta1['fecha_publi'], '%Y-%m-%dT%H:%M:%S.%fZ')
    date2 = dt.strptime(oferta2['fecha_publi'], '%Y-%m-%dT%H:%M:%S.%fZ')
    name1 = oferta1['oferta_minima']
    name2 = oferta2['oferta_minima']
    if date1 > date2:
        return True
    elif date1 == date2:
        if name1 < name2:
            return True
        else:
            return False
    else:
        return False

def sort_alfa(oferta1, oferta2):
    date1 = oferta1
    date2 = oferta2
    if date1 > date2:
        return True
    else:
        return False

def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
