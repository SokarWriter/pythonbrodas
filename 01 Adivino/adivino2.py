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

def init_round(trys, num_trys, current) :
    trys_left = trys - num_trys
    print("Intentos: "+str(trys_left))
    last_try = current

    return last_try, trys_left

def player_input():
    try:
        current = int (input())
    except ValueError:
        print("solo acepto numeros, gracias")
        current = player_input()
    return current

def interface_mid_game(current, num_max, num_trys, result, last_try):
    if current > num_max:
        print("Te has pasado pero si sgues intentandolo el resultado es inferior a " + str (num_max) )    
    elif num_trys == 1: 
        print("Templado")
    elif abs(result - current) < abs(result - last_try):    
            print("Caliente")
    elif abs(result - current) > abs(result - last_try):    
            print("Frio")

def interface_end_game(num_trys, trys, current, result):
    is_finished = False
    if num_trys == trys:
        print("You lose")
        is_finished = True  
    if current == result:
        print("you win")
        is_finished = True  
        return is_finished

def interface_replay_game():
    print("Quieres volver a jugar? SI o NO)")
    if  input().upper() == "SI":
        num_trys, current, result = init_game()
        game_engine(trys, num_trys, current, num_max, result)
        interface_replay_game()
    else:
        print( "Adios!") 

def game_engine(trys, num_trys, current, num_max, result):
    interface_initial_game(trys)
    while True: 
        last_try, try_left = init_round(trys, num_trys, current)
        current = player_input()
        num_trys = num_trys + 1
        is_finished = interface_end_game(num_trys, trys, current, result)
        if  is_finished == True:
            break
        interface_mid_game(current, num_max, num_trys, result, last_try)



trys, num_max = config_game()
num_trys, current, result = init_game()

game_engine(trys, num_trys, current, num_max, result)
interface_replay_game() 



    

       
   
    
    
    
    





