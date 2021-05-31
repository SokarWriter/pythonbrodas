def random_number(result)
    from random import *

print(randint(1, 100))

result = random_number
trys = 5
max_value = 100
#---------------------------------------------------------------------------------------------------------------#
def inicio(saludo):
    print ("hola", saludo)

def preparación(advertencia):
    print ("En este juego no ganaras si no piensas con elocuencia")


print ("¿¿Hola jugador, tu mision es adivinar el numero en el que piensa la maquina...podras hacerlo??")
saludo = input ()
print ("recuerda que debes pensar bien tu pregunta.. solo dispones de 5 intentos para conseguirlo")
advertencia = input ()
print ("")
#---------------------------------------------------------------------------------------------------------------#
while True:
    value = raw_input(5)
    try:
       value = int(value)
    except ValueError:
       print 'Vuelve a intentarlo'
       continue
    if 0 <= value <= 5:
       break
    else:
       print 'Juego terminado'

finished = False
while not finished:
    num = int (input ())

    if num > max_value:
        print("Muy frio")
    if num  < (0.20 * result):
        print ("frio")
    if (num > 98 and num <= 100):
        print ("caliente")
    if (num > 98 and num <= 100):
        print ("Muy caliente")    
        finished = True
    else:
        print ("sigue intentadolo...pringadx")




