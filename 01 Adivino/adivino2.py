import sys
from random import randint 


def config_game() :
    print (sys.argv)
    if len(sys.argv) == 3:
        num_max = int(sys.argv[1])
        trys = int(sys.argv[2])
    
    else:
        trys = 10
        num_max = 200
    return trys, num_max

def init_game() :
    num_trys = 0
    current = None
    result = randint(0, num_max)
    print(result)
    return num_trys, current, result
    
def interface_initial_game(trys) :
    #menu de incio
    print ("¿¿Hola jugador, tu mision es adivinar el numero en el que piensa la maquina...podras hacerlo??")
    #saludo = input ()
    print ("recuerda que debes pensar bien tu pregunta.. solo dispones de " + str(trys) + " intentos para conseguirlo")
    #advertencia = input ()
    print ("")
 
trys, num_max = config_game()
num_trys, current, result = init_game()
interface_initial_game(trys)




def init_round(trys, num_trys, current) :
    trys_left = trys - num_trys
    print("Intentos: "+str(trys_left))
    last_try = current
    return last_try, trys_left



while True: 
    trys_left = trys - num_trys
    print("Intentos: "+str(trys_left))
    last_try = current
    #pedir al usuario su num
    try:
        current = int (input())
    except ValueError:
        print("solo acepto numeros, gracias")
        continue

    #por cada input del jugon 1 try - (num_trys: num_trys += 1)
    num_trys = num_trys + 1
    #comprobar el input del jugon si es el correcto
    if num_trys == trys:
        print("You lose")
        break
    #si el num es correcto "gana" 
    if current == result:
        print("you win")
        break
    if current > num_max:
        print("Te has pasado pero si sgues intentandolo el resultado es inferior a " + str (num_max) )
    #si no acierta en el primer try la pista es "templado"    
    elif num_trys == 1: 
        print("Templado")
    #si no acierta en el resto de trys la pista es "caliente" si el num que a dicho esta mas cerca que el num que dijo en el try anterior.
    elif abs(result - current) < abs(result - last_try):    
            print("Caliente")
    #si no acierta en el resto de trys la pista es "frio" si el num que a dicho esta mas lejos que el num que dijo en el try anterior.
    elif abs(result - current) > abs(result - last_try):    
            print("Frio")
    
    
    #print(abs(result - current))
    #print("intento anterior: "+str(last_try))


    #|(result - current)|<|(result - last_try)| valor absoluto || abs()
    #ha surgido un problema, tmb tiene que comprobar si se ha pasado 
    

    

#hacer print score + print inputs jugon.
#vuelve al menu de inicio: para elegir volver a jugar 






