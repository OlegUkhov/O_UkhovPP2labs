import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
radius = 5
curColor = (0, 0, 255)
drawMode = 'free'
shapes = []

colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
]
tools = [
    ('free', '-'),
    ('circle', 'O'),
    ('rect', '□'),
    ('erase', 'X')
]

def buttons():
    x = 10
    for color in colors:
        pygame.draw.rect(screen, color, (x, 10, 30, 30))
        x += 35

    x = 640 - len(tools) *35 - 10
    for tool, symbol in tools:
        pygame.draw.rect(screen, (100, 100, 100), (x, 10, 30, 30))
        font = pygame.font.SysFont(None, 20)
        text = font.render(symbol, True, (255, 255, 255))
        screen.blit(text, (x + 10, 15))
        x += 35

def clicked(pos):
    return pos[1] <= 40

working = True
while working:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if clicked(pos):
                x = 10
                for color in colors:
                    if x <= pos[0] <= x + 30:
                        curColor = color
                        break
                    x += 35
                
                x = 640 - len(tools) * 35 - 10
                for tool, _ in tools:
                    if x <= pos[0] <= x + 30:
                        drawMode = tool
                        break
                    x += 35
            else:
                if drawMode == 'free':
                    pass
                elif drawMode == 'circle':
                    shapes.append(('circle', curColor, pos, 20))
                elif drawMode == 'rect':
                    shapes.append(('rect', curColor, (pos[0]-15, pos[1]-15, 30, 30)))
                elif drawMode == 'erase':
                    shapes.append(('circle', (0, 0, 0), pos, 20))
        
        if event.type == pygame.MOUSEMOTION:
            if event.buttons[0] and not clicked(event.pos):
                if drawMode == 'free':
                    shapes.append(('dot', curColor, event.pos, radius))
                elif drawMode == 'erase':
                    shapes.append(('dot', (0, 0, 0), event.pos, 15))
    
    for shape in shapes:
        print(shape)
        if shape[0] == 'dot':
            pygame.draw.circle(screen, shape[1], shape[2], shape[3])
        elif shape[0] == 'circle':
            pygame.draw.circle(screen, shape[1], shape[2], shape[3])
        elif shape[0] == 'rect':
            pygame.draw.rect(screen, shape[1], shape[2])
    
    buttons()
    pygame.display.flip()
    clock.tick(360)

pygame.quit()