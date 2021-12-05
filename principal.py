#! /usr/bin/env python
import os
import random
import sys
import math
import json

import pygame
from pygame.event import post
from pygame.locals import *

from configuracion import *
from funcionesVACIAS import *
from extras1 import *

f = open("Record.json", "r")
c = f.read()

js = json.loads(c)

# Funcion principal


def main():
    # Centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.mixer.music.load("./soundFx/soundtrack.mp3")
    pygame.mixer.music.play(-1, 0, 0)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.init()

    # Preparar la ventana
    pygame.display.set_caption("Bubbly Words")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    # tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    fps = FPS_inicial
    puntos = 0
    candidata = ""
    # listas y posiciones
    listaIzq = []
    listaMedio = []
    listaDer = []
    posicionesIzq = []
    posicionesMedio = []
    posicionesDer = []
    lista = []
    # rachas
    rachas = []
    # seleccion de dificultad y modo
    gameModeIndex = []
    gameDificultiesIndex = []
    status = [1]
    postStatus = []
    # palabras repetidas
    repetidas = []
    # nombre
    nombre = []
    # Record
    puntosPartida = 0

    playing = False

    while playing == False:
        res = menu(gameModeIndex, gameDificultiesIndex, status, nombre)
        if res == True:
            playing = True

    # Lemario
    if len(gameModeIndex) == 1:
        lemario = "Normal"
        archivo = open("lemarios\lemario.txt", "r")
    elif len(gameModeIndex) == 2:
        lemario = "Animales"
        archivo = open("lemarios\lemarioAnimales.txt", "r")
    elif len(gameModeIndex) == 3:
        lemario = "FoV"
        archivo = open("lemarios\lemarioFrutasYVerudas.txt", "r")
    elif len(gameModeIndex) == 4:
        lemario = "Nombres"
        archivo = open("lemarios\lemarioNombres.txt", "r")
    elif len(gameModeIndex) == 5:
        lemario = "PoP"
        archivo = open("lemarios\lemarioPaisOProvincia.txt", "r")

    # Dificultad
    if len(gameDificultiesIndex) == 1:
        dificultad = "Facil"
    elif len(gameDificultiesIndex) == 2:
        dificultad = "Medio"
    elif len(gameDificultiesIndex) == 3:
        dificultad = "Dificil"

    background = pygame.image.load("./img/background.jpg").convert()

    for linea in archivo.readlines():
        lista.append(linea[0:-1])

    cargarListas(lista, listaIzq, listaMedio, listaDer,
                 posicionesIzq, posicionesMedio, posicionesDer)

    dibujar(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq,
            posicionesMedio, posicionesDer, puntos, segundos)

    while segundos > fps / 1000:
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        if True:
            fps = 3

        # Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():

            # QUIT es apretar la X en la ventana
            if e.type == QUIT:
                pygame.quit()
                return()

            # Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                letra = dameLetraApretada(e.key)
                candidata += letra
                if e.key == K_BACKSPACE:
                    candidata = candidata[0:len(candidata) - 1]
                if e.key == K_RETURN:
                    puntos += procesar(lista, candidata, listaIzq, listaMedio,
                                       listaDer, posicionesIzq, posicionesMedio, posicionesDer, rachas, repetidas)
                    candidata = ""

        segundos = TIEMPO_MAX - pygame.time.get_ticks() / 1000

        # Limpiar pantalla anterior
        screen.blit((background), [0, 0])

        # Dibujar de nuevo todo
        dibujar(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq,
                posicionesMedio, posicionesDer, puntos, segundos)

        pygame.display.flip()

        actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq,
                   posicionesMedio, posicionesDer, segundos, gameDificultiesIndex)

        while len(postStatus) == 0 and segundos <= 0:
            GameOver(postStatus)

        best = js["record"]["best"]

        if segundos <= 0:
            puntosPartida = puntos

        if puntosPartida > best:
            js["record"]["best"] = puntosPartida
            s = json.dumps(js)
            f = open("Record.json", "w")
            f.write(s)
            f.close()

        best = js["record"]["best"]

        nombre2 = nombre[0]
        if len(postStatus) == 1:
            records(puntosPartida, best, dificultad, nombre2, lemario)

    while 1:
        # Esperar el QUIT del usuario
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return


# Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
