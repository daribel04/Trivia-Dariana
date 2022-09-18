BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
import random
import time

iniciar_trivia = True
puntaje = 0
intentos = 0

print(BLUE + "Bienvenido a mi trivia sobre Harry Potter " + RESET)
print(CYAN + "pondremos a prueba todo lo que sabes de la saga " + RESET)

print(RED + "Vas a comenzar con ", puntaje, "puntos" + RESET)
print("")
nombre = input("Ingresa tu nombre:  ")
print("")
casa = input(
    "¿Cual es tu casa?(Gryffindor, Hufflepuff, Ravenclaw y Slytherin)  \n")
print("")

fan = input("Del 1 al 10 que tan fan eres de la saga:\n  ")
print("")

print("FANTASTICO UN", casa, "!!\n")
print("")
print(
    "Hola", nombre,
    "responde las siguientes preguntas escribiendo la letra de la alternativa y presionado 'ENTER ' para enviar tu respuesta:\n"
)

while iniciar_trivia == True:
    intentos += 1
    puntaje = 0
    print("\nIntento número:", intentos)

    print(GREEN + "1) ¿Cuando es el cumpleaños de Harry?" + RESET)
    print("a) 28 de Junio")
    print("b) 8 de Octubre")
    print("c) 31 de Julio ")
    print("d) 15 de Diciembre")
    respuesta_1 = input("\nTu respuesta: ")

    while respuesta_1 not in ("a", "b", "c", "d"):
        respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente")
        print("")
    if respuesta_1 == "c":
        print(YELLOW + "excelente mago!" + RESET)
        puntaje += random.randint(0, 10)
    else:
        puntaje -= random.randint(0, 10)
        print(YELLOW + "incorrecto sangre sucia" + RESET)

    print("puntaje actual:  ", puntaje)

    time.sleep(3)

    print(GREEN + "2) ¿Cuál es el hechizo que se usa contra los dementores?" +
          RESET)
    print("a) Expelliarmus")
    print("b) Accio")
    print("c) Expecto Patronum")
    print("d) Avada Kedavra")

    respuesta_2 = input("\nTu respuesta: ")

    while respuesta_2 not in ("a", "b", "c", "d", "w"):
        respuesta_2 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_2 == "a":
        puntaje -= random.randint(0, 10)
        print("Incorrecto!", nombre, "Expelliarmus es un hechizo de desarme")
    elif respuesta_2 == "b":
        puntaje -= random.randint(0, 10)
        print(
            "Incorrecto!", nombre,
            "Accio se utiliza para que un objeto se aproxime a aquel mago que lo visualice y requiera"
        )
    elif respuesta_2 == "c":
        print(YELLOW + "Muy bien", nombre, "!" + RESET)
        puntaje += random.randint(0, 10)

    elif respuesta_2 == "w":
        puntaje += random.randint(50, 100)
        print("Winky es una elfa domestica que solo existe en libros :(")
    else:
        puntaje -= random.randint(0, 10)
        print("Incorrecto", nombre, "Avada Kedavra es el hechizo asesino")

    print("puntaje actual:  ", puntaje)

    print(RED + "Gracias", nombre, "por jugar mi trivia, alcanzaste", puntaje,
          "puntos" + RESET)

    print("\n¿Deseas intentar la trivia nuevamente?")
    repetir_trivia = input(
        "Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower(
        )
    if repetir_trivia != "si":
        print("\nEspero", nombre, "que lo hayas disfrutado!")
        iniciar_trivia = False
