import random
import os
numero = random.randint(1,100)

def dificultad():
    nivel = input('Elige entre "facil" o "dificil": ')
    oportunidades = 0
    if nivel == 'facil':
        oportunidades = 10
    elif nivel == 'dificil':
        oportunidades = 5
    return oportunidades
        
def partida():
    game_over = False
    while not game_over:
        oportunidades = dificultad()
        print()
        print(f'Tienes {oportunidades} oportunidades')
        print()
        
        
        while oportunidades != 0:
            mi_numero = int(input('Adivina el numero: '))
            if mi_numero < numero:
                print('El numero es mas alto')
                oportunidades -=1
                print(f'Te quedan {oportunidades} oportunidades')
            elif mi_numero > numero:
                print('El numero es mas bajo')
                oportunidades -=1
                print(f'Te quedan {oportunidades} oportunidades')
            else:
                print(f'Has acertado! El numero era {numero}')
                game_over = True
                
        print(f'Lo siento, has perdido.El numero era {numero}')
        game_over = True
        pregunta = input('Otra partida? : ')
        if pregunta == 'y':
            os.system('cls')
            partida()
        else:
            exit(0)

partida()