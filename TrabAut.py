# Juego Piedra, Papel o Tijera mejor de 3 gana.

import random

# Cambio: Se define OPCIONES como tupla (antes era lista)
OPCIONES = ("piedra", "papel", "tijera")

def obtener_eleccion_jugador():
    while True:
        eleccion = input("Elige piedra, papel o tijera: ").lower()
        if eleccion in OPCIONES:  # Cambio: Ahora se compara con la tupla OPCIONES
            return eleccion
        else:
            print("Elección inválida. Intenta nuevamente.")

def obtener_eleccion_computadora():
    return random.choice(OPCIONES)  # Cambio: Ahora se hace uso de la tupla OPCIONES

# Cambio: se usa un diccionario para simplificar la lógica
REGLAS = {
    "piedra": "tijera",
    "papel": "piedra",
    "tijera": "papel"
}

def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "empate"
    elif REGLAS[jugador] == computadora:  # Cambio: Comparación con el diccionario REGLAS
        return "jugador"
    else:
        return "computadora"

def jugar():
    print("Juguemos Piedra, Papel o Tijera (mejor de 3)\n")

    while True:
        victorias_jugador = 0
        victorias_computadora = 0

        while victorias_jugador < 2 and victorias_computadora < 2:
            jugador = obtener_eleccion_jugador()
            computadora = obtener_eleccion_computadora()
            print(f"Tú elegiste: {jugador}")
            print(f"La computadora eligió: {computadora}")

            ganador = determinar_ganador(jugador, computadora)

            if ganador == "jugador":
                victorias_jugador += 1
                print("Ganaste esta ronda!\n")
            elif ganador == "computadora":
                victorias_computadora += 1
                print("La computadora ganó esta ronda!\n")
            else:
                print("Empate.\n")

            print(f"Marcador -> Tú: {victorias_jugador}, Computadora: {victorias_computadora}\n")

        if victorias_jugador == 2:
            print("¡Felicidades! Ganaste.")
        else:
            print("La computadora ganó. ¡Suerte la próxima vez!")

        jugar_otra = input("¿Quieres jugar otra ronda? (s/n): ").lower()
        if jugar_otra != 's':
            print("¡Gracias, vuelve pronto!")
            break

if __name__ == "__main__":
    jugar()