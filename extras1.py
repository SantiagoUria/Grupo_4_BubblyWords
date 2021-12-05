import pygame
from pygame.locals import *
from configuracion import *
from principal import *
import json

f = open("Record.json", "r")
c = f.read()

js = json.loads(c)


def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SPACE:
        return(" ")
    else:
        return("")


def escribirEnPantalla(screen, palabra, posicion, tamano, color):
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), tamano)
    ren = defaultFont.render(palabra, 1, color)
    screen.blit(ren, posicion)


def dibujar(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq,
            posicionesMedio, posicionesDer, puntos, segundos):

    defaultFont = pygame.font.Font("bubbleFont.ttf", TAMANNO_LETRA)
    borderFont = pygame.font.Font("bubbleFont.ttf", TAMANNO_LETRA+1)

    # Linea del piso
    pygame.draw.line(screen, (255, 255, 255),
                     (0, ALTO-70), (ANCHO, ALTO-70), 5)

    # linea vertical
    pygame.draw.line(screen, (255, 255, 255),
                     (ANCHO//3, ALTO-70), (ANCHO//3, 0), 5)

    # linea vertical
    pygame.draw.line(screen, (255, 255, 255),
                     (2*ANCHO//3, ALTO-70), (2*ANCHO//3, 0), 5)

    ren1 = defaultFont.render(candidata, 1, COLOR_TEXTO)
    ren2 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
    if(segundos < 15):
        ren3 = defaultFont.render(
            "Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren3 = defaultFont.render(
            "Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)

    for i in range(len(listaIzq)):
        # carga bordes
        screen.blit(borderFont.render(
            listaIzq[i], 1, COLOR_BORDE2), (posicionesIzq[i][0]+3, posicionesIzq[i][1]))
        screen.blit(borderFont.render(
            listaIzq[i], 1, COLOR_BORDE2), (posicionesIzq[i][0]-3, posicionesIzq[i][1]))
        screen.blit(borderFont.render(
            listaIzq[i], 1, COLOR_BORDE2), (posicionesIzq[i][0], posicionesIzq[i][1]+3))
        screen.blit(borderFont.render(
            listaIzq[i], 1, COLOR_BORDE2), (posicionesIzq[i][0], posicionesIzq[i][1]-3))
        screen.blit(borderFont.render(
            listaIzq[i], 1, COLOR_BORDE), (posicionesIzq[i][0]+1, posicionesIzq[i][1]))
        screen.blit(borderFont.render(
            listaIzq[i], 1, COLOR_BORDE), (posicionesIzq[i][0]-1, posicionesIzq[i][1]))
        screen.blit(borderFont.render(
            listaIzq[i], 1, COLOR_BORDE), (posicionesIzq[i][0], posicionesIzq[i][1]+1))
        screen.blit(borderFont.render(
            listaIzq[i], 1, COLOR_BORDE), (posicionesIzq[i][0], posicionesIzq[i][1]-1))
        # carga letras
        screen.blit(defaultFont.render(
            listaIzq[i], 1, COLOR_LETRAS_IZQ), posicionesIzq[i])

    for i in range(len(listaMedio)):

        screen.blit(borderFont.render(
            listaMedio[i], 1, COLOR_BORDE2), (posicionesMedio[i][0]+3, posicionesMedio[i][1]))
        screen.blit(borderFont.render(
            listaMedio[i], 1, COLOR_BORDE2), (posicionesMedio[i][0]-3, posicionesMedio[i][1]))
        screen.blit(borderFont.render(
            listaMedio[i], 1, COLOR_BORDE2), (posicionesMedio[i][0], posicionesMedio[i][1]+3))
        screen.blit(borderFont.render(
            listaMedio[i], 1, COLOR_BORDE2), (posicionesMedio[i][0], posicionesMedio[i][1]-3))
        screen.blit(borderFont.render(
            listaMedio[i], 1, COLOR_BORDE), (posicionesMedio[i][0]+1, posicionesMedio[i][1]))
        screen.blit(borderFont.render(
            listaMedio[i], 1, COLOR_BORDE), (posicionesMedio[i][0]-1, posicionesMedio[i][1]))
        screen.blit(borderFont.render(
            listaMedio[i], 1, COLOR_BORDE), (posicionesMedio[i][0], posicionesMedio[i][1]+1))
        screen.blit(borderFont.render(
            listaMedio[i], 1, COLOR_BORDE), (posicionesMedio[i][0], posicionesMedio[i][1]-1))

        screen.blit(defaultFont.render(
            listaMedio[i], 1, COLOR_LETRAS_MEDIO), posicionesMedio[i])

    for i in range(len(listaDer)):

        screen.blit(borderFont.render(
            listaDer[i], 1, COLOR_BORDE2), (posicionesDer[i][0]+3, posicionesDer[i][1]))
        screen.blit(borderFont.render(
            listaDer[i], 1, COLOR_BORDE2), (posicionesDer[i][0]-3, posicionesDer[i][1]))
        screen.blit(borderFont.render(
            listaDer[i], 1, COLOR_BORDE2), (posicionesDer[i][0], posicionesDer[i][1]+3))
        screen.blit(borderFont.render(
            listaDer[i], 1, COLOR_BORDE2), (posicionesDer[i][0], posicionesDer[i][1]-3))
        screen.blit(borderFont.render(
            listaDer[i], 1, COLOR_BORDE), (posicionesDer[i][0]+1, posicionesDer[i][1]))
        screen.blit(borderFont.render(
            listaDer[i], 1, COLOR_BORDE), (posicionesDer[i][0]-1, posicionesDer[i][1]))
        screen.blit(borderFont.render(
            listaDer[i], 1, COLOR_BORDE), (posicionesDer[i][0], posicionesDer[i][1]+1))
        screen.blit(borderFont.render(
            listaDer[i], 1, COLOR_BORDE), (posicionesDer[i][0], posicionesDer[i][1]-1))

        screen.blit(defaultFont.render(
            listaDer[i], 1, COLOR_LETRAS_DER), posicionesDer[i])

    screen.blit(ren1, (190, 570))
    screen.blit(ren2, (545, 10))
    screen.blit(ren3, (10, 10))


def menu(gameModeIndex, gameDificultiesIndex, status, nombre):
    import os
    import sys

    screen = pygame.display.set_mode((ANCHO, ALTO))
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    defaultFont = pygame.font.Font("bubbleFont.ttf", TAMANNO_LETRA+5)

    screen = pygame.display.set_mode((ANCHO, ALTO))
    os.environ["SDL_VIDEO_CENTERED"] = "1"

    menuBackground = pygame.image.load("img\menuBackground.png").convert()
    screen.blit(menuBackground, [0, 0])

    menuBackground = pygame.image.load("img/backgroundConLogo.png").convert()
    screen.blit(menuBackground, [0, 0])
    user = ""
    while len(status) == 1:
        screen.blit(menuBackground, [0, 0])

        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == KEYDOWN:
                letra = dameLetraApretada(e.key)
                user += letra
                if e.key == K_BACKSPACE:
                    user = user[0:len(user) - 1]
                if e.key == K_RETURN:
                    nombre.clear()
                    nombre.append(user)
                    status.append(1)

        if len(status) == 1:
            usernameText = defaultFont.render(
                user, True, (255, 255, 255), (255, 0, 0))
            usernameTextDisplay = usernameText.get_rect()
            usernameTextDisplay.centerx = screen.get_rect().centerx
            usernameTextDisplay.centery = 450
            screen.blit(usernameText, usernameTextDisplay)
            hint = defaultFont.render(
                "Escribe tu nombre de usuario", True, (255, 255, 255))
            hintDisplay = hint.get_rect()
            hintDisplay.centerx = screen.get_rect().centerx
            hintDisplay.centery = 525
            screen.blit(hint, hintDisplay)

        pygame.display.flip()

    # boton izquierda

    leftButton = [(20, 450), (50, 420), (50, 480)]
    leftButtonBorder = [(15, 450), (55, 410), (55, 490)]

    pygame.draw.polygon(screen, (255, 255, 255), leftButtonBorder)
    pygame.draw.polygon(screen, (255, 161, 0), leftButton)

    # boton derecha

    rightButton = [(780, 450), (750, 420), (750, 480)]
    rightButtonBorder = [(785, 450), (745, 410), (745, 490)]
    pygame.draw.polygon(screen, (255, 255, 255), rightButtonBorder)
    pygame.draw.polygon(screen, (255, 161, 0), rightButton)

    defaultFont = pygame.font.Font("bubbleFont.ttf", TAMANNO_LETRA+5)
    # # PANTALLA MODO DE JUEGO
    if len(status) == 2:
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
        if e.type == KEYDOWN:
            if e.key == K_LEFT:
                if len(gameModeIndex) > 0:
                    gameModeIndex.pop(-1)
            if e.key == K_RIGHT:
                if len(gameModeIndex) < 5:
                    gameModeIndex.append(1)
            if e.key == K_RETURN:
                if len(gameModeIndex) != 0:
                    status.append(1)

        gameModes = ["Elige el modo de juego", "Predeterminado", "Animales",
                     "Frutas y Verduras", "Nombres", "Países o Provincias"]
        gameModeText = defaultFont.render(gameModes[len(gameModeIndex)],

                                          True, (255, 255, 255), (255, 0, 0))
        # display del texto
        gamemodeDisplay = gameModeText.get_rect()
        gamemodeDisplay.centerx = screen.get_rect().centerx
        gamemodeDisplay.centery = 450
        screen.blit(gameModeText, gamemodeDisplay)
        hint = defaultFont.render(
            "Selecciona el modo de juego usando las fechas del teclado", True, (255, 255, 255))
        hintDisplay = hint.get_rect()
        hintDisplay.centerx = screen.get_rect().centerx
        hintDisplay.centery = 525
        continuar = defaultFont.render(
            "Presiona enter para continuar", True, (255, 255, 255))
        continuarDisplay = hint.get_rect()
        continuarDisplay.centerx = screen.get_rect().centerx
        continuarDisplay.centery = 560
        screen.blit(hint, hintDisplay)
        screen.blit(continuar, continuarDisplay)
        pygame.display.flip()

    if len(status) == 3:
        # PANTALLA DIFICULTAD
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == KEYDOWN:
                if e.key == K_LEFT:
                    if len(gameDificultiesIndex) > 0:
                        gameDificultiesIndex.pop(-1)
                if e.key == K_RIGHT:
                    if len(gameDificultiesIndex) < 3:
                        gameDificultiesIndex.append(1)
                if e.key == K_RETURN:
                    if len(gameDificultiesIndex) != 0:
                        status.append(1)
        dificulties = ["Dificultad", "facil", "medio", "dificil"]
        dificultiesText = defaultFont.render(
            dificulties[len(gameDificultiesIndex)], True, (255, 255, 255), (255, 0, 0))
        dificultiesDisplay = dificultiesText.get_rect()
        dificultiesDisplay.centerx = screen.get_rect().centerx
        dificultiesDisplay.centery = 450
        screen.blit(dificultiesText, dificultiesDisplay)
        hint = defaultFont.render(
            "Selecciona la dificultad de juego usando las fechas del teclado", True, (255, 255, 255))
        hintDisplay = hint.get_rect()
        hintDisplay.centerx = screen.get_rect().centerx
        hintDisplay.centery = 525
        continuar = defaultFont.render(
            "Presiona enter para continuar", True, (255, 255, 255))
        continuarDisplay = hint.get_rect()
        continuarDisplay.centerx = screen.get_rect().centerx
        continuarDisplay.centery = 560
        screen.blit(hint, hintDisplay)
        screen.blit(continuar, continuarDisplay)
        pygame.display.flip()

    if len(status) == 4:
        return True
    pygame.display.flip()

    pass


def GameOver(postStatus):
    import os
    import sys

    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()
        if e.type == KEYDOWN:
            postStatus.append(1)

    screen = pygame.display.set_mode((ANCHO, ALTO))
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    defaultFont = pygame.font.Font("bubbleFont.ttf", TAMANNO_LETRA+5)

    menuBackground = pygame.image.load("img\gameOver.png").convert()
    screen.blit(menuBackground, [0, 0])

    hint = defaultFont.render(
        "Presiona cualquier tecla para continuar", True, (255, 255, 255))
    hintDisplay = hint.get_rect()
    hintDisplay.centerx = screen.get_rect().centerx
    hintDisplay.centery = 525
    screen.blit(hint, hintDisplay)

    pygame.display.flip()


def records(record, best, dificultad, nombre, lemario):
    import os
    import sys

    screen = pygame.display.set_mode((ANCHO, ALTO))
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    defaultFont = pygame.font.Font("bubbleFont.ttf", TAMANNO_LETRA+5)
    recordsBackground = pygame.image.load("img/records.png").convert()
    screen.blit(recordsBackground, [0, 0])

    hint = defaultFont.render(
        "Gracias por jugar!", True, (255, 255, 255))
    hintDisplay = hint.get_rect()
    hintDisplay.centerx = screen.get_rect().centerx
    hintDisplay.centery = 525
    screen.blit(hint, hintDisplay)
    top1Text = defaultFont.render(
        "Tus Puntos: "+str(record), True, (255, 255, 255))
    top1Display = top1Text.get_rect()
    top1Display.centerx = screen.get_rect().centerx
    top1Display.centery = 250
    screen.blit(top1Text, top1Display)
    top2Text = defaultFont.render(
        "Mejor Puntaje: "+str(best), True, (255, 255, 255))
    top2Display = top2Text.get_rect()
    top2Display.centerx = screen.get_rect().centerx
    top2Display.centery = 300
    screen.blit(top2Text, top2Display)
    top3Text = defaultFont.render(
        "| "+nombre+" | "+lemario+" | "+dificultad+" |", True, (255, 255, 255))
    top3Display = top3Text.get_rect()
    top3Display.centerx = screen.get_rect().centerx
    top3Display.centery = 350
    screen.blit(top3Text, top3Display)

    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()
        if e.type == KEYDOWN:
            sys.exit()
    pygame.display.flip()

#     # animalsGameModeText = defaultFont.render("Animales", 1, (255,255,255))
#     # fruitsGameModeText = defaultFont.render("Frutas y Verduras", 1, (255,255,255))
#     # namestGameModeText = defaultFont.render("Nombres", 1, (255,255,255))
#     # countriestGameModeText = defaultFont.render("Países y Provincias", 1, (255,255,255))
#     pass
