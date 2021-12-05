from principal import *
from configuracion import *

import random
import math
import pygame
import pygame.locals

# Elige una palabra aleatoria de la lista, la divide y les crea posiciones aleatorias en cada una de las columnas


def cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq, posicionesMedio, posicionesDer):
    # elige una palabra de la lista y la carga en las 3 listas
    # y les inventa una posicion para que aparezca en la columna correspondiente

    # inicializo con una palabra random de la lista
    palabra = lista[random.randrange(0, len(lista))]
    lenght = len(palabra)
    primeraInstancia = lenght//3
    segundaInstancia = 2*(lenght//3)
    fraccion = ANCHO//3
    for i in range(0, lenght):
        alto = random.randrange(30, 40)
        anchoIzq = random.randrange(0+30, (fraccion-30))
        anchoMedio = random.randrange(fraccion+30, ((2*fraccion)-30))
        anchoDer = random.randrange((2*fraccion)+30, (ANCHO-30))
    # Mete las primeras 2 letras en la listaIzq, las 2 siguientes en listaMedio y las restantes en listaDer
        if i >= 0 and i <= primeraInstancia-1:
            if not estaCerca([anchoIzq, alto], posicionesIzq):
                listaIzq.append(palabra[i])
                posicionesIzq.append([anchoIzq, alto])
            else:
                alto = random.randrange(30, 40)
                anchoIzq = random.randrange(0+30, (fraccion-30))
                listaIzq.append(palabra[i])
                posicionesIzq.append([anchoIzq, alto])

        if i >= primeraInstancia and i <= segundaInstancia-1:
            if not estaCerca([anchoMedio, alto], posicionesMedio):
                listaMedio.append(palabra[i])
                posicionesMedio.append([anchoMedio, alto])
            else:
                alto = random.randrange(30, 40)
                anchoMedio = random.randrange(fraccion+30, ((2*fraccion)-30))
                listaMedio.append(palabra[i])
                posicionesMedio.append([anchoMedio, alto])

        if i >= segundaInstancia and i <= lenght-1:
            if not estaCerca([anchoDer, alto], posicionesDer):
                listaDer.append(palabra[i])
                posicionesDer.append([anchoDer, alto])
            else:
                alto = random.randrange(30, 40)
                anchoDer = random.randrange((2*fraccion)+30, (ANCHO-30))
                listaDer.append(palabra[i])
                posicionesDer.append([anchoDer, alto])
    print("cheats:", palabra)

# Con cada actualizacion baja la posicion de las letras en el eje y


def bajar(lista, posiciones, segundos, dificultad):
    # Hace bajar las letras y las borra cuando llegan a determinada altura
    # El derecho bajaba mas rapido
    for i in range(0, len(lista)):
        posiciones[i][1] = posiciones[i][1] + velocidad(segundos, dificultad)

    for pos in posiciones:
        if pos[1] > 500:
            lista.pop(posiciones.index(pos))
            posiciones.pop(posiciones.index(pos))

    return lista, posiciones

# Hace bajar las letras y carga nuevas aleatoriamente


def actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq, posicionesMedio, posicionesDer, segundos, dificultad):
    # Actualiza la posicion de las letras y cada un tiempo aleatorio carga nuevas letras
    # Trantamos de usar los segundos
    dificuladBase = 15
    dificultadExtra = 0
    rand1 = random.randrange(0, dificuladBase - dificultadExtra)
    rand2 = random.randrange(0, dificuladBase - dificultadExtra)
    if rand1 == rand2:
        cargarListas(lista, listaIzq, listaMedio, listaDer,
                     posicionesIzq, posicionesMedio, posicionesDer)
    bajar(listaIzq, posicionesIzq, segundos, dificultad)
    bajar(listaMedio, posicionesMedio, segundos, dificultad)
    bajar(listaDer, posicionesDer, segundos, dificultad)

# Chequea si hay una letra en la zona de spawn


def estaCerca(elem, lista):
    # Chequea si hay letras dentro del rango de spawn
    # No sabiamos donde iba
    # Crasheaba si usabamos while
    # no aparecian letras de las palabras
    for posLista in lista:
        if elem[0] in range(int(posLista[0])-30, int(posLista[0])+30) and elem[1] in range(int(posLista[1])-30, int(posLista[1])+30):
            return True
    return False

# Devuelve puntos dependiendo de las caracteristicas de la candidata


def Puntos(candidata):
    # Recibe la candidata y otorga puntos segun sus caracteristicas
    puntaje = 0
    vocales = "aeiou"
    cons_dificil = "jkqwxyz"
    for letra in candidata:
        if letra in vocales:
            puntaje += 1
        if letra not in cons_dificil and letra not in vocales:
            puntaje += 2
        if letra in cons_dificil:
            puntaje += 5

    return puntaje

# Procesar devuelve puntos chequea si se repiten, erran o aciertan palabras, devolviendo los puntos correspondientes


def procesar(lista, candidata, listaIzq, listaMedio, listaDer, posicionesIzq, posicionesMedio, posicionesDer, rachas, repetidas):
    # Chequea con la funcion esValida si la candidata es correcta, incorrecta o repetida y devuelve los puntos correspondientes
    # Podiamos repetir y daba puntos
    if esValida(lista, candidata, listaIzq, listaMedio, listaDer, posicionesIzq, posicionesMedio, posicionesDer, rachas) and candidata not in repetidas:
        repetidas.append(candidata)
        eliminarLetras(candidata, listaIzq, listaMedio, listaDer,
                       posicionesIzq, posicionesMedio, posicionesDer)
        rachaTrue(lista, candidata, listaIzq, listaMedio, listaDer,
                  posicionesIzq, posicionesMedio, posicionesDer, rachas)
        sonidoRachas(lista, candidata, listaIzq, listaMedio, listaDer,
                     posicionesIzq, posicionesMedio, posicionesDer, rachas)
        print(repetidas)
        return Puntos(candidata)
    elif candidata in repetidas:
        return -Puntos(candidata)
    else:
        rachaFalse(lista, candidata, listaIzq, listaMedio, listaDer,
                   posicionesIzq, posicionesMedio, posicionesDer, rachas)
        error = pygame.mixer.Sound("./soundFx/error.mp3")
        error.play()
        return 0

# Si acertas agrega la palabra a rachas, aumentando su longitud


def rachaTrue(lista, candidata, listaIzq, listaMedio, listaDer, posicionesIzq, posicionesMedio, posicionesDer, rachas):
    rachas.append(candidata)

# Si erras eliminar el contenido de rachas, cortando la racha de aciertos


def rachaFalse(lista, candidata, listaIzq, listaMedio, listaDer, posicionesIzq, posicionesMedio, posicionesDer, rachas):
    rachas.clear()

# Segun la longitud de la racha ejecuta diferentes sonidos


def sonidoRachas(lista, candidata, listaIzq, listaMedio, listaDer, posicionesIzq, posicionesMedio, posicionesDer, rachas):
    lenght = len(rachas)
    if lenght == 1:
        racha1 = pygame.mixer.Sound("./soundFx/racha1.mp3")
        racha1.play()
    elif lenght == 2:
        racha2 = pygame.mixer.Sound("./soundFx/racha2.mp3")
        racha2.play()
    elif lenght == 3:
        racha3 = pygame.mixer.Sound("./soundFx/racha3.mp3")
        racha3.play()
    elif lenght == 4:
        racha4 = pygame.mixer.Sound("./soundFx/racha4.mp3")
        racha4.play()
    elif lenght == 5:
        racha5 = pygame.mixer.Sound("./soundFx/racha5.mp3")
        racha5.play()
    elif lenght >= 6:
        racha6 = pygame.mixer.Sound("./soundFx/racha6.mp3")
        racha6.play()

# Valida la candidata


def esValida(lista, candidata, listaIzq, listaMedio, listaDer, posicionesIzq, posicionesMedio, posicionesDer, rachas):
    # Al principio hicimos una validacion extraña
    # aveces validaba cuando no habia letras
    candidata = candidata
    lenght = len(candidata)
    candidata1 = ""
    puedoIzq = True
    puedoMedio = True
    puedoDer = True
    for i in range(0, lenght):
        if candidata[i] in listaIzq and puedoIzq:
            indexIzq = listaIzq.index(candidata[i])
            candidata1 += listaIzq[indexIzq]
            if candidata1 == candidata and candidata in lista:
                return True
        elif candidata[i] in listaMedio and puedoMedio and candidata in lista:
            puedoIzq = False
            indexMedio = listaMedio.index(candidata[i])
            candidata1 += listaMedio[indexMedio]
            if candidata1 == candidata:
                return True
        elif candidata[i] in listaDer and puedoDer and candidata in lista:
            puedoMedio = False
            puedoIzq = False
            indexDer = listaDer.index(candidata[i])
            candidata1 += listaDer[indexDer]
            if candidata1 == candidata:
                return True
    if candidata1 not in lista:
        return False

# Elimina las letras, que pertenezcan a la candidata, en la pantalla


def eliminarLetras(candidata, listaIzq, listaMedio, listaDer, posicionesIzq, posicionesMedio, posicionesDer):
    # eliminaba letras demas
    # crasheaba intentaba borrar dos veces la misma palabra
    candidata = candidata
    lenght = len(candidata)
    candidata1 = ""
    puedoIzq = True
    puedoMedio = True
    puedoDer = True
    for i in range(0, lenght):
        if candidata[i] in listaIzq and puedoIzq:
            indexIzq = listaIzq.index(candidata[i])
            candidata1 += listaIzq[indexIzq]
            listaIzq.pop(indexIzq)
            posicionesIzq.pop(indexIzq)
            if candidata1 == candidata:
                return
        elif candidata[i] in listaMedio and puedoMedio:
            puedoIzq = False
            indexMedio = listaMedio.index(candidata[i])
            candidata1 += listaMedio[indexMedio]
            listaMedio.pop(indexMedio)
            posicionesMedio.pop(indexMedio)
            if candidata1 == candidata:
                return
        elif candidata[i] in listaDer and puedoDer:
            puedoMedio = False
            puedoIzq = False
            indexDer = listaDer.index(candidata[i])
            candidata1 += listaDer[indexDer]
            listaDer.pop(indexDer)
            posicionesDer.pop(indexDer)
            if candidata1 == candidata:
                return

# Segun el tiempo y la dificultad seleccionada le da un valor a velocidad diferentes


def velocidad(segundos, dificultad):
    velocidad = 0
    if len(dificultad) == 1:
        if round(segundos) <= 61 and round(segundos) > 40:
            velocidad = 3
        if round(segundos) < 40 and round(segundos) >= 15:
            velocidad = 6
        if round(segundos) < 15:
            velocidad = 10

    elif len(dificultad) == 2:
        if round(segundos) <= 61 and round(segundos) > 40:
            velocidad = 5
        if round(segundos) < 40 and round(segundos) >= 15:
            velocidad = 10
        if round(segundos) < 15:
            velocidad = 15

    elif len(dificultad) == 3:
        if round(segundos) <= 61 and round(segundos) > 40:
            velocidad = 13
        if round(segundos) < 40 and round(segundos) >= 15:
            velocidad = 18
        if round(segundos) < 15:
            velocidad = 25

    return velocidad
