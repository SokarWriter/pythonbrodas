# var types:
number = 10
decimal = 8.75
text = "hola kar"
booleano = True or False
nulo = None

# Basics Operations:
print (bool(10))
print (bool(-1))
print (bool(text))
print (bool(""))
print (10 + 10.50)
print ((10%15))

# Adv Types:
lista = ["plantanos", "judias", "patatas"]
print(lista)
lista.append(6)
print(lista)
print(lista.count("naranjas"))
print(lista.count("judias"))
lista.append ("judias")
print(lista.count("judias"))
print(lista)
print (list("jodete kar"))

print(list(range(6)))



# Diccionarios {}
diccionario = {"plantanos": 4, "judias": 6,"patatas": 8}
print(diccionario)
print(diccionario["judias"])
diccionario.keys()
diccionario.values()
print (diccionario.keys())

#Flow control
if True:
    print ("hola")
if False:
    print ("adios")

finished = False
while not finished:
    num = int (input ())

    if num < 10 and num > 0:
        print ("hola")
    elif num <= 70 or num > 100:
        print ("casi")
    elif (num > 98 and num <= 100):
        print ("YOU WIN")
        finished = True
    else:
        print ("sigue intentadolo...pringadx")