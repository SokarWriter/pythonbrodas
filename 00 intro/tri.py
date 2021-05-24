def triangulo (letter, size):
    angulo = ""
    for u in range (size):
        angulo = "\t" + angulo + letter * size
        for u in range (size):
            print (angulo)

triangulo ("#", 5)