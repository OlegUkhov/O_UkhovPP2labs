import pygame
import math

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
radius = 15
curColor = (0, 0, 255)
drawMode = 'free'  #starting tool 
shapes = []

colors = [
    (255, 0, 0),
    (0, 255, 0),    #colors to iterate through 
    (0, 0, 255),
]
tools = [
    ('free', '-'),
    ('circle', 'O'),
    ('rect', 'sq'),
    ('rhombus', 'R'),       #items to draw bar
    ('rTriangle', 'T'),
    ('eq', 'eq'),
    ('erase', 'X')
]

def buttons():
    x = 10
    for color in colors:
        pygame.draw.rect(screen, color, (x, 10, 30, 30))    #color on bar drawing 
        x += 35

    x = 640 - len(tools) *35 - 10
    for tool, symbol in tools:
        pygame.draw.rect(screen, (100, 100, 100), (x, 10, 30, 30))
        font = pygame.font.SysFont(None, 20)                        #tools boxes drawing
        text = font.render(symbol, True, (255, 255, 255))
        screen.blit(text, (x + 10, 15))
        x += 35

def clicked(pos):
    return pos[1] <= 40

def Rhombus(surface, color, center, size):      #func to draw polygon
    points = [
        (center[0], center[1] - size * 2),  #top
        (center[0] + size, center[1]),  #right
        (center[0], center[1] + size * 2),  #bottom
        (center[0] - size, center[1])   #left
    ]
    pygame.draw.polygon(surface, color, points)

def rightTriangle(surface, color, center, size):
    points = [
        (center[0] - size, center[1] + size),  #bottom left
        (center[0] + size, center[1] + size),  #bottom right
        (center[0] - size, center[1] - size)   #top left
    ]
    pygame.draw.polygon(surface, color, points)

def eqTriangle(surface, color, center, size): 
    height = int(size * math.sqrt(3) / 2)
    points = [
        (center[0], center[1] - height),             #top
        (center[0] - size + 8 , center[1] + height // 2), #bottom left
        (center[0] + size - 8, center[1] + height // 2)   #bottom right
    ]
    pygame.draw.polygon(surface, color, points)

working = True
while working:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #windows closing 
            working = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if clicked(pos):                    #if mouse clicked in the bar zone
                x = 10
                for color in colors:
                    if x <= pos[0] <= x + 30:
                        curColor = color        #which color was picked
                        break
                    x += 35
                
                x = 640 - len(tools) * 35 - 10
                for tool, _ in tools:
                    if x <= pos[0] <= x + 30:
                        drawMode = tool         #which tool was clicked 
                        break
                    x += 35

            else:                           #if mouse clicked in the working sheet
                if drawMode == 'free':
                    pass
                elif drawMode == 'circle':
                    shapes.append(('circle', curColor, pos, 30)) #adding to first index in list...
                elif drawMode == 'rect':                                #...values to conctruct figure
                    shapes.append(('rect', curColor, (pos[0]-15, pos[1]-15, 30, 30)))
                elif drawMode == 'rhombus':
                    shapes.append(('rhombus', curColor, pos, 30))
                elif drawMode == 'rTriangle':
                    shapes.append(('rTriangle', curColor, pos, 30))     
                elif drawMode == 'eq':
                    shapes.append(('eq', curColor, pos, 30))
                elif drawMode == 'erase':
                    shapes.append(('circle', (0, 0, 0), pos, 20))
        
        if event.type == pygame.MOUSEMOTION:
            if event.buttons[0] and not clicked(event.pos):     #if clicked with left mouse button in working area
                if drawMode == 'free':
                    shapes.append(('dot', curColor, event.pos, radius))     #add every position to the list
                elif drawMode == 'erase':                                   
                    shapes.append(('dot', (0, 0, 0), event.pos, 15)) #if eraser is picked
    
    for shape in shapes:        #drawing each element in lists
        if shape[0] == 'dot':           #with checking for first index which is shape
            pygame.draw.circle(screen, shape[1], shape[2], shape[3])    
        elif shape[0] == 'circle':
            pygame.draw.circle(screen, shape[1], shape[2], shape[3])
        elif shape[0] == 'rect':
            pygame.draw.rect(screen, shape[1], shape[2])    
        elif shape[0] == 'rhombus':
            Rhombus(screen, shape[1], shape[2], shape[3])
        elif shape[0] == 'rTriangle':
            rightTriangle(screen, shape[1], shape[2], shape[3])
        elif shape[0] == 'eq':
            eqTriangle(screen, shape[1], shape[2], shape[3])
    
    buttons()
    pygame.display.flip()
    clock.tick(360)

pygame.quit()