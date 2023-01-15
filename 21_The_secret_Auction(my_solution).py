
def subasta():
  pujadores = {}
  respuesta = 'si'
  
  while respuesta == 'si':
    #solicitamos datos de pujantes
    nombre = input('Escribe tu nombre: ')
    precio = int(input('Indica tu puja: '))
    #solicitamos saber si hay más participantes
    respuesta = input('Hay más participantes? (Indica "si" o "no")')
    
    #agregamos elementos al diccionario
    pujadores[nombre] = precio
    
    #buscamos ganador de la puja
    maximo = 0
  for i in pujadores:
    if pujadores[i] > maximo:
      maximo = pujadores[i]
      ganador = i
    
  print(f'Ha ganado la puja {ganador} con una puja de {maximo} euros')

subasta()