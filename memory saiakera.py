import random
import time
import os

def clear():
    os.system("cls")

clear()

def game():
    velocidad = 3
    print ("Bienvenido al juego de memoria.")
    print ("Instrucciones:")
    print ("1- (x,0,0)")
    print ("2- (0,x,0)")
    print ("1- (0,0,x)")
    time.sleep(10)
    print ("Listo")
    time.sleep(3)
    print ("YA")
    time.sleep(1)
    clear()
    while True:
        level = 1
        secuencias = [("x",0,0), (0,"x",0), (0,0,"x")]
        tempS = []
        intentos = []

        for x in range(velocidad):
            rand = random.randrange(3)
            tempS.append(secuencias[rand])

        for i in tempS:
            print (i, "a")
            time.sleep(2)
            clear()

        contador = 1

        for j in range(velocidad):
            print ("Introduzca el ", contador)
            usuario = input(": ")
            intentos.append(secuencias[usuario-1])
            contador += 1

        if intentos == tempS:
            print ("Ganaste")
            velocidad += 1
            print ("Subiste a ", velocidad)
            time.sleep(1)
            print ("Listo")
            time.sleep(1)
            print ("ya")
            time.sleep(1)
        else:
            print ("Perdiste")
            if velocidad > 2:
                velocidad -= 1
                print ("Bajaste a ", velocidad)
                time.sleep(1)
                print ("Listo")
                time.sleep(1)
                print ("ya")
                time.sleep(1)
            else:
                print ("Perdiste el juego chau")
                break

        clear()


if __name__ == '__main__':
    game().run()