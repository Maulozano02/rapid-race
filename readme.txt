Rapid Race - Juego de Carreras en Python con Pygame
====================================================

Descripción:
-------------
Rapid Race es un juego de carreras en Python creado utilizando la biblioteca Pygame. En este juego, controlas un carro que debe evitar obstáculos en la carretera y tratar de recorrer la mayor distancia posible sin chocar.

Instrucciones:
--------------
- Tecla Izquierda: Mueve el carro hacia la izquierda.
- Tecla Derecha: Mueve el carro hacia la derecha.

Funciones Principales:
----------------------
- `car(x, y)`: Dibuja el carro en la pantalla en la posición `(x, y)`.

- `background()`: Dibuja el fondo de la carretera y las franjas amarillas en la pantalla.

- `obstacle(obs_x, obs_y, obs_type)`: Dibuja obstáculos en la pantalla en la posición `(obs_x, obs_y)` según el tipo de obstáculo especificado.

- `create_obstacle()`: Genera obstáculos de forma aleatoria en la parte superior de la pantalla.

- `game_loop()`: La función principal del juego que controla la lógica del juego y la interacción del usuario. Administra el movimiento del carro, los obstáculos, la detección de colisiones y el aumento de velocidad gradual.

Personalización:
----------------
Puedes personalizar el juego agregando tus propias imágenes para el carro y los obstáculos. Asegúrate de proporcionar imágenes adecuadamente dimensionadas para que se ajusten al juego.

Ejecución del Juego:
---------------------
Para ejecutar el juego, asegúrate de tener instalada la biblioteca Pygame. Puedes instalarla con el siguiente comando:

```bash
pip install pygame

Luego, ejecuta el archivo `rapid_race.py` para comenzar a jugar.

¡Diviértete jugando Rapid Race y buena suerte tratando de establecer un nuevo récord de distancia recorrida!
