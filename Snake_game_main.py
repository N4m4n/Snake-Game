import pygame
import random
import colours
pygame.init()
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake game")
snake_length = 25
snake_width = 25
font = pygame.font.SysFont(None,40)
howToPlayFont = pygame.font.SysFont("Calibri",30)
titleFont = pygame.font.SysFont("Algerian",50)
home = pygame.image.load(r"images\welcome.png")
def textScreenTitle(text,colour,x,y):
    screen_text = titleFont.render(text,True,colour)
    gameWindow.blit(screen_text,(x,y))
def textScreenInst(text,colour,x,y):
    screen_text = howToPlayFont.render(text,True,colour)
    gameWindow.blit(screen_text,(x,y))
def textScreen(text,colour,x,y):
    screen_text = font.render(text,True,colour)
    gameWindow.blit(screen_text,(x,y))
def plotSnake(points):
    for i in range(len(points)):
        pygame.draw.rect(gameWindow,colours.red,pygame.Rect([points[i][0],points[i][1],snake_length,snake_width]))
        if i==0:
            pygame.draw.rect(gameWindow,colours.black,pygame.Rect([points[i][0],points[i][1],20,20]))
            pygame.draw.rect(gameWindow,colours.red,pygame.Rect([points[i][0],points[i][1],20,20]))
clock = pygame.time.Clock()
def onStart():
    exit_game=False
    gameWindow.fill(colours.white)
    gameWindow.blit(home,((screen_width-home.get_width())/2,(screen_height-home.get_height())/2))
    pygame.draw.circle(gameWindow,colours.lightGreen,(300,500),60)
    pygame.draw.circle(gameWindow,colours.lightGreen,(600,500),60)
    textScreen("PLAY",colours.white,265,485)
    textScreen("HOW TO",colours.white,546,480)
    textScreen("PLAY",colours.white,565,505)
    pygame.display.update()
    while not exit_game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_focused():
                    currPos = pygame.mouse.get_pos()
                    if (currPos[0] in range(260,350)) and (currPos[1] in range(480,550)):
                        gameloop()
                    elif (currPos[0] in range(540,630)) and (currPos[1] in range(480,550)):
                        howToPlay()

        clock.tick(10)
    pygame.quit()
    quit()
def howToPlay():
    exit_game=False
    gameWindow.fill(colours.white)
    pygame.draw.circle(gameWindow,colours.black,(25,170),5)
    pygame.draw.circle(gameWindow,colours.black,(25,210),5)
    pygame.draw.circle(gameWindow,colours.black,(25,250),5)
    pygame.draw.circle(gameWindow,colours.black,(25,290),5)
    pygame.draw.circle(gameWindow,colours.black,(25,330),5)
    textScreenTitle("HOW TO PLAY",colours.blue,250,20)
    textScreenInst("Move the snake using the arrow keys.",colours.blue,40,150)
    textScreenInst("Your aim is to maximize score my eating more no of fool pellets",colours.blue,40,190)
    textScreenInst("As the snake eats, it will get longer.",colours.blue,40,230)
    textScreenInst("If the snake collides with any of the walls or eats itself, the game ends.",colours.blue,40,270)
    textScreenInst("Note: If you try to directly go in the opposite direction of current direction,",colours.blue,40,310)
    textScreenInst("it is considered as if the snake ate itself",colours.blue,40,340)
    pygame.draw.rect(gameWindow,colours.blue,pygame.Rect(700,500,130,50))
    pygame.draw.rect(gameWindow,colours.blue,pygame.Rect(20,500,130,50))
    textScreenInst("PLAY",colours.white,725,510)
    textScreenInst("BACK",colours.white,35,510)
    pygame.display.update()
    while not exit_game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.MOUSEBUTTONUP:

                if pygame.mouse.get_focused():
                    currPos = pygame.mouse.get_pos()
                    if (currPos[0] in range(700,830)) and (currPos[1] in range(500,550)):
                        gameloop()
                    elif (currPos[0] in range(20,150)) and (currPos[1] in range(500,550)):
                        onStart()
        clock.tick(10)
def gameEnd():
    exit_game = False
    while exit_game==False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True

            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_RETURN:
                    gameloop()
                    break
                if event.key==pygame.K_TAB:
                    break
        gameWindow.fill(colours.white)
        gameOverMessage = "GAME OVER PRESS ENTER TO RESTART"
        textScreen(gameOverMessage,colours.red,200,100)
        pygame.display.update()
        clock.tick(10)
    pygame.quit()
    quit()
def gameloop():
    food_length = 15
    food_width = 15
    food_x = random.randint(15,880)
    food_y = random.randint(15,580)
    eaten = False
    score = 0
    exit_game = False
    snake_xpos= 0
    snake_ypos = 40
    velocity_x = 0
    velocity_y = 0
    snake_velocity = 20
    snake_points = []
    snake_points_length = 1
    highscore = 0
    fps = 10
    try:
        f = open("highscore.txt", "r")
    except:
        f = open("highscore.txt", "w")
        f.write("0")
        f.close()
        f = open("highscore.txt", "r")
    finally:
        highscore = int(f.read())
        f.close()
    while exit_game==False:
        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                exit_game=True
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    velocity_x = snake_velocity
                    velocity_y=0
                if event.key==pygame.K_LEFT:
                    velocity_x= -snake_velocity
                    velocity_y=0
                if event.key==pygame.K_DOWN:
                    velocity_y=snake_velocity
                    velocity_x=0
                if event.key==pygame.K_UP:
                    velocity_y= -snake_velocity
                    velocity_x=0
        if snake_xpos+velocity_x not in range(screen_width):
            velocity_x=0
        if snake_ypos+velocity_y not in range(screen_height):
            velocity_y=0
        snake_xpos+=velocity_x
        snake_ypos+=velocity_y
        head = [snake_xpos,snake_ypos]
        snake_points.append(head)
        if len(snake_points)>snake_points_length:
            snake_points = snake_points[1:]
        if food_x in range(snake_xpos-5,snake_xpos+26) and food_y in range(snake_ypos-5,snake_ypos+26):
            eaten = True
        if eaten:
            score+=1
            food_x = random.randint(15,880)
            food_y = random.randint(15,580)
            snake_points_length+=3
            eaten = False

        if(score>=4):
            fps = 15
        if(score>=4):
            fps = 20

        if score>highscore:
            highscore = score
            f = open("highscore.txt", "w")
            f.write(str(highscore))
            f.close()
        gameWindow.fill(colours.grassGreen)
        textScreen("Score: "+str(score)+"  High Score: "+str(highscore), colours.black,5,5)
        plotSnake(snake_points)
        temp = snake_points.copy()
        del temp[len(temp)-1]
        if head in temp:
            break
        pygame.draw.rect(gameWindow,colours.black,pygame.Rect([food_x,food_y,food_length,food_width]))
        pygame.display.update()
        clock.tick(fps)
    gameEnd()
onStart()
