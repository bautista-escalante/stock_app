from datos import *
import datetime
import re

while True:
    print("1-actualizar_precios \n2-actualizar cantidad\n3-consultar precios\n4-consultar cantidad",
          "\n5-agregar elemento\n6-crear tabla\n7-salir")
    eleccion=int(input("ingrese una opcion: "))
    while re.findall(r"([1-7])",eleccion):
        print("error")
    match eleccion:
        case 1:
            categoria=input("ingrese la categoria ")
            inflacion=float(input("ingrese la inflacion "))
            fecha=datetime.datetime.now()
            actualizar_precios(categoria,inflacion)
            print("la base de datos se actualizo")
        case 2:
            elemento=input("ingrese el nombre del elemento ")
            cantidad=int(input("ingrese la catidad "))
            actualizar_cantidad(elemento,cantidad)
            print("la base de datos se actualizo")
        case 3:
            categoria=input("ingrese la categoria ")
            tupla=mostrar_categoria(categoria)
            for lista in tupla:
                print(f"elemento: {lista[3]}\nprecio de alquiler {lista[4]}\nprecio de reposicion {lista[5]}\nultima actualizacion: {fecha}")
        case 4:
            elemento=input("ingrese el nombre del elemento ")
            lista=mostrar_elemento(elemento)
            print(f"cantidad: {lista[1]}\ncategoria: {lista[2]}\nelemento: {lista[3]}")
        case 5:
            elemento=input("ingrese el nombre del elemento ")
            cantidad=int(input("ingrese la catidad "))
            categoria=input("ingrese la categoria ")
            reposicion=int(input("ingrese el precio de reposicion "))
            alquiler=int(input("ingrese el precio del alquiler "))
            agregar_datos(cantidad,categoria,elemento,reposicion,alquiler)
        case 6:
            crear_tabla()
        case 7:
            break

