# el primer paso es importar las librerias a usar
import pygame 

#luego tengo que iniciar la libreria pygame para que funcione 

pygame.init() 
###defino algunos colores
Black = (23, 32, 42 ) #no es exactamente negro ya que este se escribe (0,0,0) en RGB pero queda mejor este color 
#yo personalmente saco los codigos RGB de esta pagina https://htmlcolorcodes.com/es/

###

#genero la pantalla con su tamaño de 800x600 pixeles y luego agrego el fondo
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((33, 47, 61))# elijo el color en formato RGB


#cargo imagenes a usar

imp = pygame.image.load("cruz.png")# cargo la imagen 
imp = pygame.transform.scale(imp, (100,100))#cone esto le doy el tamaño 
imp2 = pygame.image.load("circulo.png")
imp2 = pygame.transform.scale(imp2, (100,100))

# agrego la fuente para los textos 
font = pygame.font.SysFont("Arial", 32)

def RedrawGameWindow():# esta funcion me dibuja el fondo del juego 

  screen.fill((213, 245, 227 ))
  
  global G00
  global G01
  global G02
  global G10
  global G11
  global G12
  global G20
  global G21
  global G22
  
  G00 =pygame.draw.rect(screen, Black, (250, 150, 100, 100), 1)

  G01 = pygame.draw.rect(screen, Black, (350, 150, 100, 100), 1)

  G02 = pygame.draw.rect(screen, Black, (450, 150, 100, 100), 1)  

  G10 = pygame.draw.rect(screen, Black, (250, 250, 100, 100), 1)
    
  G11 = pygame.draw.rect(screen, Black, (350, 250, 100, 100), 1)

  G12 =pygame.draw.rect(screen, Black, (450, 250, 100, 100), 1)

  G20 =pygame.draw.rect(screen, Black, (250, 350, 100, 100), 1)

  G21 = pygame.draw.rect(screen, Black, (350, 350, 100, 100), 1)

  G22 = pygame.draw.rect(screen, Black, (450, 350, 100, 100), 1)

  grid = [[" "," "," "],[" "," "," "],[" "," "," "]]
  
  pygame.display.flip()
  
  
###----- defino algunas variables adicionales
x_win = False # booleano para saber si gano cruz
o_win = False #booleano para saber si gano circulo
RowMsg = ''
grid = [[" "," "," "],[" "," "," "],[" "," "," "]] #esto me crea una grilla para control en la consola
Turn = True # esto lo voy a usar para determinar de quien es el turno (True = turno de cruz, False = turno de los circulos)
####----  
 
  
def displayGrid(grid):#con esta funcion hago la grilla del ta te ti para printearla en la consola y asi poder controlar
  print(" " + grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2])
  print("-----------")
  print(" " + grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2])
  print("-----------")
  print(" " + grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2])

def checkGrid0(grid): #esta funcion chequea si gano el circulo 
  global o_win
  if grid[0][0]=="O" and grid[0][1]=="O" and grid[0][2]=="O":
    
    o_win = True
   
  
  if grid[1][0]=="O" and grid[1][1]=="O" and grid[1][2]=="O":
    
    o_win = True

  if grid[2][0]=="O" and grid[2][1]=="O" and grid[2][2]=="O":
    
    o_win = True
  #chequeo las columnas

  if grid[0][0]=="O" and grid[1][0]=="O" and grid[2][0]=="O":
    
    o_win = True
    
  if grid[0][1]=="O" and grid[1][1]=="O" and grid[2][1]=="O":
    
    o_win = True

  if grid[0][2]=="O" and grid[1][2]=="O" and grid[2][2]=="O":
    
    o_win = True
    
  #chequeo las diagonales
  if grid[2][0]=="O" and grid[1][1]=="O" and grid[0][2]=="O":
    
    o_win = True
    
  if grid[0][0]=="O" and grid[1][1]=="O" and grid[2][2]=="O":
    
    o_win = True
  
    
  
def checkGridX(grid): # defino la funcion que chequea si ganó cruz(tres cruz en linea )
  global x_win
  #chequea las filas
  
  if grid[0][0]=="X" and grid[0][1]=="X" and grid[0][2]=="X":
    
    x_win = True
      
  if grid[1][0]=="X" and grid[1][1]=="X" and grid[1][2]=="X":
    
    x_win = True

  if grid[2][0]=="X" and grid[2][1]=="X" and grid[2][2]=="X":
    
    x_win = True
  #chequea las columnas

  if grid[0][0]=="X" and grid[1][0]=="X" and grid[2][0]=="X":
    
    x_win = True
  
  if grid[0][1]=="X" and grid[1][1]=="X" and grid[2][1]=="X":
    # RowMsg = "Cruz gana."
    # text2 = font.render(RowMsg, True, (0, 0, 0))
    # print(RowMsg)
    x_win = True
  
  if grid[0][2]=="X" and grid[1][2]=="X" and grid[2][2]=="X":
    # RowMsg = "Cruz gana."
    # text2 = font.render(RowMsg, True, (0, 0, 0))
    # print(RowMsg)
    x_win = True
  #chequea las diagonales

  if grid[2][0]=="X" and grid[1][1]=="X" and grid[0][2]=="X":
    # RowMsg = "Cruz gana."
    # text2 = font.render(RowMsg, True, (0, 0, 0))
    # print(RowMsg)
    x_win = True
  
  if grid[0][0]=="X" and grid[1][1]=="X" and grid[2][2]=="X":
    # RowMsg = "Cruz gana."
    # text2 = font.render(RowMsg, True, (0, 0, 0))
    # print(RowMsg)
    x_win = True

# esta funcion cheque los espacios vacios, esto es necesiario para poder determinar cuando estamos en un empate
def checkEmptySpaces(grid): 
    for row in range(3):
        for col in range(3):
            if grid[row][col] == " ":
                return True  # Hay al menos un espacio en blanco
    return False 
    
  # esta funcion verifica el estado del juego, detectando cuando tenemos tres en linea y asi modificar el mensaje a mostrar en pantalla 
def check_status(x_win, o_win):
    global RowMsg
    RowMsg = ''#defino en un string vacio, sino cuando reinicio el juego queda guardado el resultado de la partida anterior
    
    #estructura de control para saber si ganan las cruces 
    if x_win == True and o_win == False: 
        RowMsg = "¡Cruz gana!, presiona R para volver a jugar"
        text2 = font.render(RowMsg, True, (0, 0, 0))
        print(RowMsg)
        
    #estructura de control para saber si ganan los circulos  
    if x_win == False and o_win == True:
        RowMsg = "¡Circulo gana!, presiona R para volver a jugar"
        text2 = font.render(RowMsg, True, (0, 0, 0))
        print(RowMsg)
        
    #estructura de control para ver si hay empate, solo pasa si ya no hay grillas vacias y no ganaron ni cruces ni circulos
    if checkEmptySpaces(grid) == False and x_win == False and o_win == False:
        RowMsg = "¡Empate!, presiona R para volver a jugar"
        text2 = font.render(RowMsg, True, (0, 0, 0))
        print(RowMsg)     
        

 


#ahora creo la grilla e inicio el loop


displayGrid(grid)
RedrawGameWindow()
running = True
while running:
    # Handle events
  
    for event in pygame.event.get():
      RowMsg = ''
      #deteccion del mouse
      
      if event.type == pygame.KEYDOWN:#deteccion del teclado 
        if event.key == pygame.K_r:#linkeo la tecla R a reiniciar el juego, volviendo todas las variables a su estado inicial.
          RedrawGameWindow()
          grid = [[" "," "," "],[" "," "," "],[" "," "," "]]
          Turn = True
          RowMsg = ''
          x_win = False
          o_win = False
          print('reinicio')
      
          
      #check de que el mouse haga click en los cuadrados 
      if event.type == pygame.MOUSEBUTTONDOWN:        
          if G00.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 0
            col = 0
            if "X" in grid[0][0] or "O" in grid[0][0]: # chequea que este vacia la celda seleccionada 
              print("stop")
            else:
              if Turn == True:#turn = true significa que es el turno de las x y False que es el turno de las O 
                grid[row][col] = "X"
                Turn = False#luego de rellanar con una x cambia el turno a False(circulos)
                screen.blit(imp, (250,150)) #delimita la pantalla que corresponde a esta celda  
              else:
                screen.blit(imp2, (250, 150))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              
              
            
              displayGrid(grid)
            
              pygame.display.flip()
              checkGridX(grid)
              check_status(x_win, o_win)
          if G01.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 0
            col = 1
            if "X" in grid[0][1] or "O" in grid[0][1]:
              print("Stop")
            else:
              if Turn == True:
                grid[row][col] = "X"
                Turn = False
                screen.blit(imp, (350,150))
              else:
                screen.blit(imp2, (350,150))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)

              pygame.display.flip()
              checkGridX(grid)
              check_status(x_win, o_win)
          if G02.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 0
            col = 2
            if "X" in grid[0][2] or "O" in grid[0][2]:
              print("Stop")
            else:
              if Turn == True:
                grid[row][col] = "X"
                Turn = False
                screen.blit(imp, (450,150))
              else:
                screen.blit(imp2, (450,150))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
                displayGrid(grid)
                
              
              pygame.display.flip()
              check_status(x_win, o_win)
          if G10.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 1
            col = 0
            if "X" in grid[1][0] or "O" in grid[1][0]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp, (250,250))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp2, (250,250))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)
                         
              pygame.display.flip()
              checkGridX(grid)
              check_status(x_win, o_win)
          if G11.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 1
            col = 1
            if "X" in grid[1][1] or "O" in grid[1][1]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp, (350,250))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp2, (350,250))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)
            
              pygame.display.flip()
              checkGridX(grid)
              check_status(x_win, o_win)
              
          if G12.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 1
            col = 2
            if "X" in grid[1][2] or "O" in grid[1][2]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp, (450,250))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp2, (450,250))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)
              
              pygame.display.flip()
              checkGridX(grid)
              check_status(x_win, o_win)
              
          if G20.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 2
            col = 0
            if "X" in grid[2][0] or "O" in grid[2][0]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp, (250,350))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp2, (250,350))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)
              
              pygame.display.flip()
              checkGridX(grid)
              check_status(x_win, o_win)
              
          if G21.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 2
            col = 1
            if "X" in grid[2][1] or "O" in grid[2][1]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp, (350,350))
                grid[row][col] = "X"
                Turn = False
                
              else:
                screen.blit(imp2, (350,350))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)
              
              pygame.display.flip()
              checkGridX(grid)
              check_status(x_win, o_win)
              
          if G22.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 2
            col = 2
            if "X" in grid[2][2] or "O" in grid[2][2]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp, (450,350))
                grid[row][col] = "X"
                Turn = False
                checkGridX(grid)
              else:
                screen.blit(imp2, (450,350))
                
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
                
              displayGrid(grid)
              
              pygame.display.flip()
              checkGridX(grid)
              check_status(x_win, o_win)

      if event.type == pygame.QUIT: #Checks whether you pressed the X button
        running = False
    
   
          
            
    
    text = font.render("Ta Te Ti ", True, (0, 0, 0))  # renderiza el texto 1
    text_rect = text.get_rect(center=(screen_width/2, 100))  #agrega un rectangulo para el texto 
    
    text2 = font.render(RowMsg, True, (0, 0, 0))  # renderiza el texto 2
    text_rect2 = text.get_rect(center=(170, 500))
    
    screen.blit(text, text_rect)#aplica el texto en la pantalla 
    screen.blit(text2, text_rect2)
    pygame.display.flip()  # actualiza la pantalla 

  
# cierro pygame 
pygame.quit()