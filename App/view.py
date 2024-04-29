"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
assert cf
#from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    controller.load_data(control)
    #tama = om.size(data["countries"])
    mbappe = controller.sizu(control)
    cr7 = controller.tamano_total(control)
    messi = controller.fechas_canti(control)
    haaland = controller.pruebas(control)
    print(cr7)
    print(mbappe)
    print(messi)
    print(haaland)

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    fecha_inicial =  str(input("Que fecha minima le interesa?: "))
    fecha_final = str(input("Que fecha maxima le interesa?: "))
    ofertas_rango_de_tiempo, final = controller.req_1(control, fecha_inicial, fecha_final)
    print("Total de ofertas publicadas durante el rango de fechas: " + str(ofertas_rango_de_tiempo))
    size = ofertas_rango_de_tiempo    
    sample = size
    if size == 1:
        job = lt.getElement(final, 0)
        print("Los", size, "Trabajos ordenados por fecha (mas reciente a menos reciente) son:")
        print('Fecha de publicacion: ' + job["published_at"] + ' Titulo: ' + job['title'] +  
                ' Nombre de la compañia: ' + job['company_name'] + ' Nivel de XP: ' + job['experience_level'] + " Pais: " + job["country_code"] + ' Ciudad: ' + 
                job['city'] + " Tamaño de la empresa: " + job["company_size"] + ' Tipo de ubicacion de trabajo: ' + job['workplace_type'] + 
                ' Contratan Ucranianos?: ' + job['open_to_hire_ukrainians'])
    elif size <= sample*2:
        print("Los", size, "Trabajos ordenados por fecha (mas reciente a menos reciente) son:")
        for job in lt.iterator(final):
            print('Fecha de publicacion: ' + job["published_at"] + ' Titulo: ' + job['title'] +  
                ' Nombre de la compañia: ' + job['company_name'] + ' Nivel de XP: ' + job['experience_level'] + " Pais: " + job["country_code"] + ' Ciudad: ' + 
                job['city'] + " Tamaño de la empresa: " + job["company_size"] + ' Tipo de ubicacion de trabajo: ' + job['workplace_type'] + 
                ' Contratan Ucranianos?: ' + job['open_to_hire_ukrainians'])
    else:
        print("Los", sample, "Trabajos ordenados por fecha (mas reciente a menos reciente) son:")
        i = 1
        while i <= sample:
            job = lt.getElement(final, i)
            print('Fecha de publicacion: ' + job["published_at"] + ' Titulo: ' + job['title'] +  
                ' Nombre de la compañia: ' + job['company_name'] + ' Nivel de XP: ' + job['experience_level'] + " Pais: " + job["country_code"] + ' Ciudad: ' + 
                job['city'] + " Tamaño de la empresa: " + job["company_size"] + ' Tipo de ubicacion de trabajo: ' + job['workplace_type'] + 
                ' Contratan Ucranianos?: ' + job['open_to_hire_ukrainians'])
            i += 1


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    n_ofertas = int(input("cantidad de ofertas a mostrar: "))
    xp = str(input("Nivel de xp: "))
    pais = str(input("Codigo pais: "))
    final = controller.req_3(control, n_ofertas, pais.lower(), xp)
    print(final)


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    num_ofertas = int(input("cantidad de ofertas a mostrar: "))
    ubi = str(input("Tipo de ubicacion: "))
    ciudad = str(input("CIUDAD: "))
    final = controller.req_4(control, num_ofertas, ciudad, ubi)
    print(final)


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    n_ciu = int(input("cantidad de ciudades a consultar: "))
    fecha_inicial =  str(input("Que fecha minima le interesa?: "))
    fecha_final = str(input("Que fecha maxima le interesa?: "))
    sal_min =  int(input("Que salario minimo le interesa?: "))
    sal_max = int(input("Que salario maximo le interesa?: "))
    
    r1, r2, r3, r4 = controller.req_6(control, n_ciu, fecha_inicial, fecha_final, sal_min, sal_max)
    print("Total de ofertas publicadas durante el rango de fechas y salario: " + str(r1))
    print(" ")
    print("Numero total de ciudades que cumplen con las condiciones: " + str(r2))
    print(" ")
    print("Cantidad de ciudades deseada: ")
    for i in lt.iterator(r3):
        print(i)
    print(" ")
    if lt.size(r4) > 10:
        r4 = lt.subList(r4, 1,10)
    size = lt.size(r4)    
    sample = size
    if size == 1:
        job = lt.getElement(r4, 0)
        print("Los", size, "Trabajos ordenados por fecha (mas reciente a menos reciente) son:")
        print('Fecha de publicacion: ' + str(job["fecha_publi"]) + ' Titulo: ' + job['title'] +  
                ' Nombre de la compañia: ' + job['compania'] + ' Nivel de XP: ' + job['xp'] + " Pais: " + job["pais"] + " Ciudad: " + job["city"] + " Tamaño de la empresa: " + 
                str(job["company_size"]) + ' Tipo de ubicacion de trabajo: ' + job['workplace_type'] + ' Oferta minima: ' + str(job['oferta_minima']) + 
                ' Habilidad: ' + str(job['habilidad'])  + ' ID: ' + job['id'])
    elif size <= sample*2:
        print("Los", size, "Trabajos ordenados por fecha (mas reciente a menos reciente) son:")
        for job in lt.iterator(r4):
            print('Fecha de publicacion: ' + str(job["fecha_publi"]) + ' Titulo: ' + job['title'] +  
                ' Nombre de la compañia: ' + job['compania'] + ' Nivel de XP: ' + job['xp'] + " Pais: " + job["pais"] + " Ciudad: " + job["city"] + " Tamaño de la empresa: " + 
                str(job["company_size"]) + ' Tipo de ubicacion de trabajo: ' + job['workplace_type'] + ' Oferta minima: ' + str(job['oferta_minima']) + 
                ' Habilidad: ' + str(job['habilidad'])  + ' ID: ' + job['id'])
    else:
        print("Los", sample, "Trabajos ordenados por fecha (mas reciente a menos reciente) son:")
        i = 1
        while i <= sample:
            job = lt.getElement(r4, i)
            print('Fecha de publicacion: ' + str(job["fecha_publi"]) + ' Titulo: ' + job['title'] +  
                ' Nombre de la compañia: ' + job['compania'] + ' Nivel de XP: ' + job['xp'] + " Pais: " + job["pais"] + " Ciudad: " + job["city"] + " Tamaño de la empresa: " + 
                str(job["company_size"]) + ' Tipo de ubicacion de trabajo: ' + job['workplace_type'] + ' Oferta minima: ' + str(job['oferta_minima']) + 
                ' Habilidad: ' + str(job['habilidad'])  + ' ID: ' + job['id'])
            i += 1
    
    


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    nom_estru = str(input("estrucutra (): "))
    final = controller.req_8(control, nom_estru)
    print(final)


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    default_limit = 1000
    sys.setrecursionlimit(default_limit*10)
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)
            controller.sizu(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
