import random
import os

#Método para repartir cartas al azar
def reparto_cartas():
  """Elige una carta de la baraja al azar y la devuelve"""
  baraja = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  carta = random.choice(baraja)
  return carta

#Método para calcular la puntuación 
def calcular_puntuacion(baraja):
  """Toma una lista de cartas y devuelve la puntuación"""

  if sum(baraja) == 21 and len(baraja) == 2:
    return 0
  
  if 11 in baraja and sum(baraja) > 21:
    baraja.remove(11)
    baraja.append(1)
  
  return sum(baraja)

def comparacion(mi_puntuacion,puntuacion_banca):
  if mi_puntuacion == puntuacion_banca:
    return "Empate "
  elif puntuacion_banca == 0:
    return 'Has perdido. La banca ha sacado un BlackJack!'
  elif mi_puntuacion == 0:
    return 'Has ganado! Tienes un BlackJack!'
  elif mi_puntuacion > 21:
    return 'Has perdido. Te has pasado de 21'
  elif puntuacion_banca > 21:
    return 'Tu ganas, la banca ha pasado de 21'
  elif mi_puntuacion > puntuacion_banca:
    return 'Tu ganas!'
  else:
    return 'Tu pierdes'

def partida():
  mis_cartas = []
  cartas_banca = []
  game_over = False
    
  #Repartimos dos cartas al azar y las agregamos en la lista de cada jugador.
  for i in range(2):
    mis_cartas.append(reparto_cartas())
    cartas_banca.append(reparto_cartas())


  while not game_over:
    mi_puntuacion = calcular_puntuacion(mis_cartas)
    puntuacion_banca = calcular_puntuacion(cartas_banca)
    print()
    print(f'Tus cartas son {mis_cartas} y tienes {mi_puntuacion} puntos')
    print(f'La primera carta de la banca es {cartas_banca[0]}')
    print()

    if mi_puntuacion == 0 or puntuacion_banca == 0 or mi_puntuacion > 21:
      game_over = True
    else:
      
      eleccion_usuario = input('Aprieta la tecla "y" si quieres otra carta y la tecla "n" si prefieres pasar: ')
      if eleccion_usuario == 'y':
        mis_cartas.append(reparto_cartas())
      else:
        game_over = True
        
      
  while puntuacion_banca != 0 and puntuacion_banca < 17:
      cartas_banca.append(reparto_cartas())
      puntuacion_banca = calcular_puntuacion(cartas_banca)
      
  print()
  print(f'Tu mano final es {mis_cartas} y la puntuación final {mi_puntuacion}')
  print(f'La mano final de la banca es {cartas_banca} y su puntuación final {puntuacion_banca}')
  print(comparacion(mi_puntuacion,puntuacion_banca)) 
  print()

  pregunta = input('Otra partida?: ')
  if pregunta == "y":
    os.system("cls")
    partida()
  else:
    print('Hasta la próxima!!')
    exit(0)
    
partida()








  

    
    



