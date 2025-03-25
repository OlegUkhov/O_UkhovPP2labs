import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

radius = 15
mode = 'blue'
drawing_mode = 'free'
startPos = None
shapes = []
drawing = False
lastPos = None

colorPick = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'purple': (128, 0, 128),
    'orange': (255, 165, 0),
    'cyan': (0, 255, 255),
    'eraser': (0, 0, 0)
}

colorKeys = {
    'red': 'R',
    'green': 'G', 
    'blue': 'B',
    'yellow': 'Y',
    'purple': 'P',
    'orange': 'O',
    'cyan': 'C',
    'eraser': 'E'
}

def getColor():
    return colorPick.get(mode, (255, 255, 255))

def palette():
    x = 10
    y = 10
    size = 30
    font = pygame.font.Font(None, 20)
    
    for colorName, colorValue in colorPick.items():
        pygame.draw.rect(screen, colorValue, (x, y, size, size))
        
        if colorName == mode:
            pygame.draw.rect(screen, (255, 255, 255), (x, y, size, size), 2)
        
        text = font.render(colorKeys[colorName], True, (255, 255, 255) if colorName != 'eraser' else (255, 0, 0))
        text_rect = text.get_rect(center=(x + size/2, y + size/2))
        screen.blit(text, text_rect)
        
        x += size + 5

def thick():
    pygame.draw.circle(screen, (255, 255, 255), (550, 25), radius, 2)

def is_color_pos(pos):
    x = 10
    y = 10
    size = 30
    for color_name in colorPick.keys():
        if x <= pos[0] <= x + size and y <= pos[1] <= y + size:
            return True
        x += size + 5
    return False

def interface(pos):
    return pos[1] < 40

while True:
    pressed = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == pygame.K_r:
                mode = 'red'
            elif event.key == pygame.K_g:
                mode = 'green'
            elif event.key == pygame.K_b:
                mode = 'blue'
            elif event.key == pygame.K_y:
                mode = 'yellow'
            elif event.key == pygame.K_p:
                mode = 'purple'
            elif event.key == pygame.K_o:
                mode = 'orange'
            elif event.key == pygame.K_c:
                mode = 'cyan'
            elif event.key == pygame.K_e:
                mode = 'eraser'
            elif event.key == pygame.K_v:
                drawing_mode = 'rectangle'
            elif event.key == pygame.K_x:
                drawing_mode = 'circle'
            elif event.key == pygame.K_f:
                drawing_mode = 'free'
            elif event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                radius = min(50, radius + 2)
            elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                radius = max(1, radius - 2)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if interface(event.pos) and is_color_pos(event.pos):
                x = 10
                for color_name in colorPick.keys():
                    if x <= event.pos[0] <= x + 30:
                        mode = color_name
                        break
                    x += 35
            elif not interface(event.pos):
                startPos = event.pos
                lastPos = event.pos
                drawing = True
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing and startPos and not interface(event.pos):
                end_pos = event.pos
                current_color = getColor()
                
                if drawing_mode == 'rectangle':
                    rect = pygame.Rect(min(startPos[0], end_pos[0]), min(startPos[1], end_pos[1]), abs(end_pos[0] - startPos[0]), abs(end_pos[1] - startPos[1]))
                    shapes.append(('rectangle', current_color, rect, radius))
                elif drawing_mode == 'circle':
                    center = ((startPos[0] + end_pos[0]) // 2, (startPos[1] + end_pos[1]) // 2)
                    rad = max(abs(end_pos[0] - startPos[0]) // 2, abs(end_pos[1] - startPos[1]) // 2)
                    shapes.append(('circle', current_color, center, rad, radius))
            
            startPos = None
            lastPos = None
            drawing = False
        
        if event.type == pygame.MOUSEMOTION and drawing:
            position = event.pos
            current_color = getColor()
            if drawing_mode == 'free' and not interface(position):
                shapes.append(('dot', current_color, position, radius))
                lastPos = position

    screen.fill((0, 0, 0))
    palette()
    thick()
    
    for shape in shapes:
        if shape[0] == 'rectangle':
            pygame.draw.rect(screen, shape[1], shape[2], radius)
        elif shape[0] == 'circle':
            pygame.draw.circle(screen, shape[1], shape[2], shape[3], shape[4])
        elif shape[0] == 'dot':
            pygame.draw.circle(screen, shape[1], shape[2], shape[3])
    
    pygame.display.flip()
    clock.tick(360)