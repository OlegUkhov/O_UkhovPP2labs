import pygame
import random
import time

blue = (50, 153, 213)
black = (0, 0, 0)       #colors
red = (213, 50, 80)
white = (255, 255, 255)
green = (0, 255, 0)      #color for big food

scrWidth = 600 
scrHeight = 400    #screen resolution
snakesize = 20     #size of blocks and food and snake's body

pygame.init()

textfont = pygame.font.SysFont('Impact', 30)    
display = pygame.display.set_mode((scrWidth, scrHeight))   
fps = pygame.time.Clock()

def text(msg, color, x, y):
    mesg = textfont.render(msg, True, color)    #showing the text
    display.blit(mesg, [x, y])

def food(snake):
    while True:
        x = random.randrange(0, scrWidth - snakesize, snakesize)
        y = random.randrange(0, scrHeight - snakesize, snakesize)   #food spawning 
        if [x, y] not in snake:     #doesnt collide with snake
            return x, y             

def main():
    gameOver = False
    x1 = scrWidth / 2
    y1 = scrHeight / 2  #initial coordinates
    changeX = 0 
    changeY = 0     #on which axis is snake going
    snake = []  
    sLength = 1 
    xfood, yfood = food(snake)  #food spawning
    bigFoodActive = False
    bigFoodTime = 0
    xbigfood, ybigfood = 0, 0
    speed = 10
    score = 0
    level = 1
    
    while not gameOver:
        now = time.time()
        display.fill(blue)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and changeX == 0:
                    changeX = -snakesize
                    changeY = 0
                elif event.key == pygame.K_RIGHT and changeX == 0:
                    changeX = snakesize
                    changeY = 0                            #snake control
                elif event.key == pygame.K_UP and changeY == 0:
                    changeY = -snakesize
                    changeX = 0
                elif event.key == pygame.K_DOWN and changeY == 0:
                    changeY = snakesize
                    changeX = 0
        
        if x1 < 0 or x1 >= scrWidth or y1 < 0 or y1 >= scrHeight:   #borders of map
            gameOver = True
        
        x1 += changeX
        y1 += changeY   #coordinates updating
        
        pygame.draw.rect(display, red, [xfood, yfood, snakesize, snakesize], border_radius = 10)    # Draw regular food

        
        if not bigFoodActive and random.randint(1, 100) == 1:  #chance to spawn big food
            xbigfood, ybigfood = food(snake)
            bigFoodActive = True
            bigFoodTime = now
        
        if bigFoodActive:        #big foods drawing
            pygame.draw.rect(display, green, [xbigfood, ybigfood, snakesize*2, snakesize*2], border_radius = 10)
            
            if now - bigFoodTime > 3:        #big foods disappearing
                bigFoodActive = False
        
        head = [x1, y1]     
        snake.append(head)          
        if len(snake) > sLength:    #body's moving 
            del snake[0]               #snakes tail deleting
        
        if head in snake[:-1]:
            gameOver = True    #head's colliding with body
        
        for x in snake:
            pygame.draw.rect(display, black, [x[0], x[1], snakesize, snakesize])    #snake drawing
        
        text(f"Score: {score}", black, 10, 0)
        text(f"Level: {level}", black, 500, 0)
        
        pygame.display.update()
        
        if x1 == xfood and y1 == yfood:        #eats regular food

            xfood, yfood = food(snake)
            sLength += 1
            score += 1
            
            if score % 3 == 0:
                level += 1      #level increasing
                speed += 2
        
        
        if bigFoodActive and xbigfood <= x1 < xbigfood + snakesize*2 and ybigfood <= y1 < ybigfood + snakesize*2:
            bigFoodActive = False
            sLength += 2    #eats big food
            score += 2
            
        fps.tick(speed) 
    
    pygame.quit()

main()