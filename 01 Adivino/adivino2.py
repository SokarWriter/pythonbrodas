from random import randint 
#recoger trys del parametro
trys = 3
num_trys = 0
#recoger num_max del parametro
num_max = 100
#generar numero aleatorio entre 0 - num_max
result = randint(0, num_max)

print(result)
#menu de incio
print ("¿¿Hola jugador, tu mision es adivinar el numero en el que piensa la maquina...podras hacerlo??")
#saludo = input ()
print ("recuerda que debes pensar bien tu pregunta.. solo dispones de " + str(trys) + " intentos para conseguirlo")
#advertencia = input ()
print ("")
#entramos partida
while True: 
    trys_left = trys - num_trys
    print("Intentos: "+str(trys_left))
    #pedir al usuario su num
    num = int (input())
    #por cada input del jugon 1 try - (num_trys: num_trys += 1)
    num_trys = num_trys + 1
    #comprobar el input del jugon si es el correcto
    if num_trys == trys:
        print("You lose")
        break

    if num == result:
        print("you win")
        break
    if num > num_max:
        print("Te has pasado pero si sgues intentandolo el resultado es inferior a " + str (num_max) )
        
    elif num_trys == 1: 
        print("Templado")
    # ha surgido un problema, tmb tiene que comprobar si se ha pasado 
    

#comprobar el input del jugon si es el correcto
    #si el num es correcto "gana" 
    #si no acierta en el primer try la pista es "templado"
    #si no acierta en el resto de trys la pista es "frio" si el num que a dicho esta mas lejos que el num que dijo en el try anterior.
    #si no acierta en el resto de trys la pista es "caliente" si el num que a dicho esta mas cerca que el num que dijo en el try anterior.

#volver a  pedir input hasta que: hasta que acierte o gaste los intentos.
#hacer print score + print inputs jugon.
#vuelve al menu de inicio: para elegir volver a jugar 






