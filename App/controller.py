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
 """

import config as cf
import model
import time
import csv
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = model.new_data_structs()
    return control


# Funciones para la carga de datos

def load_data(control):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    load_jobs(control)
    load_types(control)
    load_habilidades(control)
    load_map_skills(control)

def load_jobs(control):
    jobsfile = cf.data_dir + 'large-jobs.csv'
    input_file = csv.DictReader(open(jobsfile, encoding='utf-8'), delimiter=';')
    for job in input_file:
        model.add_job(control, job)
    return control

def load_types(control):
    jobsfile = cf.data_dir + 'large-employments_types.csv'
    input_file = csv.DictReader(open(jobsfile, encoding='utf-8'), delimiter=';')
    for job in input_file:
        model.add_job2(control, job)
    return control

def load_habilidades(control):
    jobsfile = cf.data_dir + 'large-skills.csv'
    input_file = csv.DictReader(open(jobsfile, encoding='utf-8'), delimiter=';')
    for job in input_file:
        model.add_job3(control, job)
    return control

def load_map_skills(control):
    jobsfile = cf.data_dir + 'large-skills.csv'
    input_file = csv.DictReader(open(jobsfile, encoding='utf-8'), delimiter=';')
    for job in input_file:
        model.add_skill(control, job)
    return control

#tabulate
def get_jobs_sublist (control):
    sublist1, sublist2 = model.get_jobs_sublist(control)
    return sublist1, sublist2


# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass

def sizu(control):
    return model.sizu(control)

def fechas_canti(control):
    return model.fechas_canti(control)

def tamano_total(control):
    return model.tamano_total(control)

def pruebas(control):
    return model.pruebas(control)

def req_1(control, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    ofertas_rango_de_tiempo, final = model.req_1(control, fecha_inicial, fecha_final)
    return ofertas_rango_de_tiempo, final


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control, n_ofertas, pais, xp):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    final = model.req_3(control, n_ofertas, pais, xp)
    return final


def req_4(control, num_ofertas, ciudad, ubi):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    final = model.req_4(control, num_ofertas, ciudad, ubi)
    return final


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control, n_ciu, fecha_inicial, fecha_final, sal_min, sal_max):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    r1, r2, r3, r4 = model.req_6(control, n_ciu, fecha_inicial, fecha_final, sal_min, sal_max)
    return r1, r2, r3, r4


def req_7(control,anho, pais, propiedad):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    dicc, ofertas_anho = model.req_7(control, anho, pais, propiedad)
    return dicc, ofertas_anho


def req_8(control, nom_estru):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    mapa = folium.Map(location=[0,0], zoom_start=5)
    final = model.req_8(control, mapa, nom_estru)


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
