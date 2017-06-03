#Importing modules for snake game
import pygame, sys, random, time

#Check errors
check_errors=pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) Pygame sucesfuly initialized!")
#o/p (6,0)

#Play srurface

playsurface=pygame.display.set_mode((720,460))
pygame.display.set_caption('Snake Game!')
#time.sleep(3)


#COLORS
red=pygame.Color(255,0,0)               #GameOver
green=pygame.Color(0,255,0)             #Snake
white=pygame.Color(255,255,255)         #Background
black=pygame.Color(0,0,0)               #Score
brown=pygame.Color(165,42,42)           #Food

#fps controller
fpscontroller=pygame.time.Clock()

#Game Variables
snakePos=[100,50]                       #Starting position of snake
snakeBody=[[100,50],[90,50],[80,50]]    #Snake Body and moving from left to right


#Food Position
foodPos=[random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn=True

direction='RIGHT'
changeto=direction 

score=0  

#Game over function
def gameover():
    myFont=pygame.font.SysFont('monaco', 72)
    GOsurf=myFont.render('Game Over!', True, red)
    GOrect=GOsurf.get_rect()
    GOrect.midtop=(360,15)
    playsurface.blit(GOsurf,GOrect)
    showScore(0)    # showing score after game over
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()   #For Pygame exit
    sys.exit()      #For console exit

#For score
def showScore(choice=1):
    sFont=pygame.font.SysFont('monaco', 24)
    Ssurf=sFont.render('Score : {0} '.format(score), True, black)
    Srect=Ssurf.get_rect()
    if choice == 1:
        Srect.midtop=(80,10)
    else:
        Srect.midtop=(360,120)
    playsurface.blit(Ssurf,Srect)
    pygame.display.flip() #Update screns
    
#Main logic for the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto='RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto='LEFT'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto='DOWN'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto='UP'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    
    
    #Validation for direction
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    
    
    #Updating snake position[X,Y];
    if direction == 'RIGHT':
        snakePos[0] +=10    
    if direction == 'LEFT':
        snakePos[0] -=10
    if direction == 'UP':
        snakePos[1] -=10
    if direction == 'DOWN':
        snakePos[1] +=10
    
    
    
    # Snake body Mechanism
    snakeBody.insert(0,list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()
    
    #Food spawn
    if foodSpawn == False:
        foodPos=[random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodSpawn = True
    
    #Background
    playsurface.fill(white)
    
    #Draw Snake
    for pos in snakeBody:
        pygame.draw.rect(playsurface, green, pygame.Rect(pos[0],pos[1],10,10))
    
    #Food for snake
    pygame.draw.rect(playsurface, brown, pygame.Rect(foodPos[0],foodPos[1],10,10))
    
    #Hitting Bouandries
    if snakePos[0] > 710 or snakePos[0] < 0:
        gameover()

    if snakePos[1] > 450 or snakePos[1] < 0:
        gameover()

    #Hitting snake by itself
    for block in snakeBody[1:]:
        if snakePos[0] ==block[0] and snakePos[1] ==block[1]:
            gameover()
    
    
    showScore()
    pygame.display.flip()
    fpscontroller.tick(15)    
    
    
    
    
    