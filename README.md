# Dodge-Game

**Dodge-Game** es un juego simple en Python utilizando la biblioteca Pygame. 
El objetivo del juego es controlar un triángulo (representando al jugador) y 
evitar que colisione con los círculos rojos que caen desde la parte superior de la pantalla.

# Requisitos

Para ejecutar este juego, necesitarás tener Python instalado en tu sistema junto con la biblioteca Pygame. Si no tienes Pygame instalado, puedes instalarlo utilizando `pip`:

pip install pygame

# Descripción del juego

En Dodge-Game, el jugador controla un triángulo que se mueve hacia la izquierda o hacia la derecha para evitar las colisiones con los enemigos (círculos rojos). Los enemigos caen desde la parte superior de la pantalla y se reinician cuando llegan al fondo. Si el jugador colisiona con un enemigo, el juego termina y se muestra un mensaje de "GAME OVER".

## Características:
- Movimiento del jugador: Usa las teclas de flecha izquierda y derecha para mover el triángulo.
- Enemigos: Círculos rojos que caen desde la parte superior.
- Estrellas: Un fondo con estrellas que le da una atmósfera más visual al juego.
- Colisiones: Cuando el jugador colisiona con un enemigo, el juego termina.
- Pantalla de Game Over: Muestra un mensaje de "GAME OVER" cuando el jugador pierde.

## Instrucciones
- Mueve el triángulo (jugador) usando las flechas izquierda y derecha.
- Evita que los círculos rojos toquen el triángulo.
- Si una colisión ocurre, el juego termina y se muestra el mensaje de "GAME OVER".

## Cómo ejecutar el juego
- Descarga o clona este repositorio.
- Asegúrate de tener Python y Pygame instalados en tu sistema.
- Ejecuta el script Python para iniciar el juego:

## Funcionalidad

Estructura del código:
- Inicialización de Pygame: Se configura la ventana del juego, se inicializan las variables necesarias y se establece el reloj del juego.
- Jugador: El jugador es representado por un triángulo que se dibuja en la pantalla.
- Enemigos: Los enemigos (círculos rojos) caen desde la parte superior de la pantalla.
- Colisiones: La función detect_collision() verifica si el triángulo ha colisionado con algún enemigo. Si hay una colisión, se llama a la función show_game_over(), que muestra el mensaje de "GAME OVER".
- Estrellas: Un fondo de estrellas se genera aleatoriamente para darle un toque visual al juego.

## Funciones principales:

- draw_player(player_rect): Dibuja al jugador (triángulo) en la pantalla.
- move_enemies(enemies): Mueve a los enemigos (círculos rojos) hacia abajo. Si llegan al fondo, se reposicionan en la parte superior.
- detect_collision(player_rect, enemies): Verifica si el jugador ha colisionado con alguno de los enemigos.
- show_game_over(): Muestra el mensaje "GAME OVER" cuando el jugador pierde.

Autor
Joan Flórez
