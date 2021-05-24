El reto consiste en desarrollar un juego de consola. El jugador debe tratar de adivinar el número
en el que la máquina está "pensando". Tras cada intento, la máquina le dará pistas al jugador de si
esta lejos o cerca de acertar. La partida acabará cuando el jugador adivine el numero o se consuman
todos sus intentos. Al final de la partida el jugador verá un resumen de la partida (cuál era el
numero que la máquina pensaba y que numeros ha dicho en cada intento). Por último el jugador podrá
hacer una nueva partida o cerrar el juego.


Configuración:
El juego se lanzará por consola de la siguiente forma:
- adivino.py n m
- Dónde n es el numero máximo de intentos que tiene el jugador para adivinar el numero. Por defecto
el jugador tendrá 5 intentos.
- Dónde el número a adivinar será un valor aleatorio entre 0 y m. por defecto m valdrá 100


Esta es la tabla de pistas:
- Te has pasado. Cuando el jugador ponga un valor mayor de m
- Muy frio
- Frio
- Caliente
- Muy caliente
