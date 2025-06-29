# Juego Piedra, Papel o Tijera en Python

## Objetivo del Programa

Este programa tiene como finalidad implementar el clásico juego de **Piedra, Papel o Tijera**, donde un jugador humano compite contra la computadora en una serie al mejor de tres rondas. 
El juego permite repetir partidas y ofrece una interfaz sencilla en consola para la interacción del usuario.

## Funcionalidades Principales

- **Entrada validada del usuario**:  
  El jugador introduce su elección ("piedra", "papel" o "tijera") y el programa valida que la entrada sea correcta.

- **Selección aleatoria de la computadora**:  
  El sistema utiliza la biblioteca random para elegir aleatoriamente una opción para la computadora.

- **Determinación del ganador por ronda**:  
  Se implementa la lógica del juego a través de reglas almacenadas en un diccionario, comparando las elecciones del jugador y la computadora.

- **Sistema de partidas al mejor de tres**:  
  El juego continúa hasta que uno de los dos jugadores (jugador - computadora) gane 2 rondas, asegurando un sistema competitivo justo.

- **Posibilidad de repetir el juego**:  
  Al finalizar una partida, se pregunta al usuario si desea jugar otra vez.

- **Código modular y estructurado**:  
  El programa está dividido en funciones reutilizables que hacen más fácil su mantenimiento y comprensión.

- **Uso de estructuras clave**:
  - ´Funciones´: Para dividir tareas lógicas del programa.
  - Condicionales: Para comparar elecciones y manejar decisiones.
  - Ciclos repetitivos: Para repetir rondas y juegos completos.
  - Tuplas: Para definir las opciones válidas de juego como estructura inmutable.

## Historial de Desarrollo

- **Fecha de creación:** 23 de mayo de 2025  
- **Última modificación:** 29 de junio de 2025  
  - Cambios realizados:
    - Se cambió el tipo de estructura de las opciones de lista a **tupla** para mayor eficiencia.
    - Se incorporó un **diccionario de reglas** para determinar al ganador de manera más estructurada y clara.
    - Se centralizó la definición de las opciones válidas para evitar duplicación de código.

## Requisitos

- Python 3.x
- Editor de código como Visual Studio Code (u otro entorno compatible con Python)

## Ejecución

Para ejecutar el programa, abre una terminal en el directorio del archivo y corre:

```bash
python TrabAut.py
