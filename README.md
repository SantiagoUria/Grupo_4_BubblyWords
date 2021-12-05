# Grupo_4_BubblyWords
Informe Bubbly Words
INTRODUCCIÓN:
Este informe fue realizado con el cometido de explicar el desarrollo del Trabajo Práctico que
se nos encargó para la asignatura de Introducción a la Programación. Este consistía en un
juego con su programa principal ya realizado, y con sus consignas a completar con funciones
que ya estaban definidas, y que nosotros debíamos completar para que el programa principal
funcione de manera correcta. Este juego tomó el nombre de “Bubbly Words” y a continuación
estará toda la información necesaria para entender el funcionamiento de este.
EL JUEGO Y SUS REGLAS:
“Bubbly Words” es un juego que tiene como objetivo encontrar la máxima cantidad de
palabras posibles, que se mostrarán en una pantalla, con una suma de letras que estarán en
constante descendencia. Esta pantalla estará dividida en tres columnas diferentes, que las
conoceremos como primera, segunda y tercera, y por cada columna se tendrá distintos tipos
de letra. Esto es importante ya que, como regla del juego, para armar la palabra deseada se
debe tener en cuenta el orden de las columnas por su número. Por ejemplo, para armar la
palabra, puedo elegir letras de la segunda columna, siempre y cuando no se haya elegido
alguna de la tercera. Por otro lado, en este caso, ya no se podrían tomar letras de la primera
columna, ya que quedaría “bloqueada” al usar la segunda.
PUNTAJES:
Para el puntaje del juego, se tomó la decisión de darle prioridad a las letras elegidas para
construir las palabras. Es decir, que cada letra que conforma la palabra sumara una cantidad
de puntos dependiendo que clase de letra sea. En otras palabras, ciertas letras tendrán más
puntos que otras, y estarán representadas a continuación:
Vocales: cada vocal en la palabra sumará un total de 1(uno) punto.
Consonantes: cada consonante en la palabra sumará un total de 2(dos) puntos.
Consonantes difíciles: las consonantes difíciles serán: “j”, “k”, “q”, “w”, “x”, “y”, “z”. Y
sumará un total de 5(cinco) puntos por cada una.
FUNCIONES:
Como fue explicado anteriormente, para el funcionamiento del programa principal, era
necesario realizar ciertas funciones previamente definidas en su totalidad. Por lo que a
continuación estará la presentación de cada función en el programa, con una breve
explicación de su funcionamiento y que rol cumplen en el juego.
cargarLista():
Esta primera función es la que tiene como objetivo elegir la palabra importada desde el
lemario de forma aleatoria, y cargarla en cada lista de una columna. En otras palabras, la
palabra tomada es “dividida” en tres partes, y luego se reparten de forma de que las primeras
letras aparezcan en la primera columna, las del medio en la segunda, y por último mostraría
las letras finales en la columna número tres. Por otro lado, también se ocupa de que estas
letras aparezcan en la parte alta de la pantalla, para que luego al bajar, tengan su recorrido
correspondiente. Esto es gracias a las posiciones que se les asigna de forma medida con cierta
altura.
bajar():
Esta función es llamada para cumplir con la descendencia de las letras mostradas en pantalla.
Esto es logrado gracias a que la función llama a las letras a su posición inicial y luego por
cada segundo va cambiando de forma negativa en su eje “y” cambiando su altura, haciendo
bajar sus posiciones.
Problemas: en el caso de bajar() tuvimos la complicación de que al momento de ejecutar el
programa, la tercera columna bajaba con más velocidad que las demás.
actualizar():
En este caso, esta es la función encargada de llamar a la función bajar() de manera que se
muestren las letras en constante movimiento hacia abajo. Por otro lado, esta misma función
lleva a cabo la eliminación de letras no usadas al llegar al borde inferior de la pantalla. Esto
es porque las letras al llegar a cierta altura verificada por su posición, la función toma que las
letras ya no se puedan usar y las quita de la pantalla. Por último, llama a la función
cargarLista() para actualizar las letras en pantalla.
estaCerca():
El cometido de esta función es verificar que las nuevas letras que aparezcan en la pantalla, no
figuren encima de otras letras ya mostradas. Esto es para que todas las letras tengan su
espacio y se entienda las letras de manera clara. Dicho de otra forma, la función comprueba la
posición de las letras ya mostradas y si están fuera del rango de la posición inicial, aparecerán
nuevas.
Problemas: con estaCerca() tuvimos algunos problemas a la hora de ejecutar el programa,
ya que este se cerraba al usar “while”. De igual manera también tuvimos dificultades para
que aparecieran las letras de las palabras nuevas cuando actualizaba.
Procesar():
Esta función es la encargada de comprobar si la palabra candidata ingresada es válida,
inválida, o repetida en el caso de que ya haya sido usada en juego. Para concluir, más
adelante además se le agregó la funcionalidad de que en el caso de que sea una palabra
candidata repetida, se resten cierta cantidad de puntos al puntaje del usuario.
Problemas: en esta función tuvimos como dificultad la suma de palabras repetidas. Esto
hacía que aunque el usuario ya haya usado una palabra válida, si la volvía a utilizar , se le
otorgaban los puntos nuevamente.
esValida():
En este caso, esta función es la encargada de verificar si la palabra candidata ingresada es
válida para el juego, de forma que cumpla las reglas antes aclaradas. En otros términos,
comprueba que las letras de la palabra hayan cumplido con el orden de las columnas puestas
en pantalla. Para que en caso de que no esté dentro de las normas del juego, no la sume al
puntaje.
Problemas: en función esValida() se nos presentó un problema sobre la validación de
palabras cuando la pantalla no mostraba las letras correspondientes.
Puntos():
En este caso, esta función está ocupada para declarar cuantos puntos le corresponde a cada
letra de la palabra candidata, revisando a qué tipo de letra pertenece. Como ya fue aclarado
anteriormente, en este juego las letras tienen diferentes tipos de puntajes. Las vocales tiene el
valor de un punto, las consonantes el valor de dos puntos, y por último está la categoría de
consonantes difíciles que tienen el valor de cinco puntos. Por lo tanto, esta termina con la
suma final de todas las letras de la palabra ya válida.
eliminarLetras():
Esta función fue agregada con el cometido de eliminar las letras que usamos de la pantalla.
Esto quiere decir, que luego de verificar que la palabra candidata sea correcta, elimine todas
las letras que utilizamos en las diferentes columnas para formarla. Esto es para evitar que se
vuelvan a utilizar posteriormente.
Problemas: en este caso, se nos presentaron varios problemas, ya que provocaba que se
cierre el juego, luego intentaba eliminar la palabra introducida en dos ocasiones, y por
último también borraba letras de más que no correspondían a la palabra valida.
sonidoRachas():
El propósito de esta función es la de crear una tanda de rachas con sus sonidos
correspondientes. La racha se crea cuando el usuario ingresa una o más palabras validas, de
manera continua, en el juego. Esto también ejecuta un sonido al momento en el que se crea la
racha, cada racha tiene un sonido diferente. O sea, que cada vez que vaya aumentando la
racha del usuario, estos sonidos van a ir cambiando, hasta llegar a una racha de seis palabras
correctas de forma seguidas.
velocidad():
Por último, esta función es llamada para cambiar la velocidad del juego, dependiendo de la
dificultad. Esto quiere decir, que según la dificultad que se elija antes de comenzar el juego,
la velocidad con la que caen las letras en pantalla, va a ser menor o mayor.
Decisiones:
Hacia el tramo final, debimos decidir acerca de la implementación de un historial de
jugadores, pero desistimos de la idea y optamos por un único récord, el puntaje más alto y
mostrar los datos de la partida.
