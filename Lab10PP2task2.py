import pygame
import random
import psycopg2

pygame.init()
w = 600
h = 400
size = 20
blue = (50, 153, 213)
black = (0, 0, 0)
red = (213, 50, 80)
white = (255, 255, 255)

screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Impact', 30)

try:
    db = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="123",
        host="localhost",
        port="5432"
    )
    cur = db.cursor()
except:
    print("Connection Problem")
    exit()

walls = {
    1: [],
    2: [[200, 200], [220, 200], [240, 200]],
    3: [[100, 100], [100, 120], [100, 140], [300, 300], [320, 300], [340, 300]],
    4: [[x, 180] for x in range(100, 500, 20)],
    5: [[280, y] for y in range(100, 300, 20)] + [[x, 180] for x in range(100, 500, 20)]
}

def savePlayer(name):
    try:
        cur.execute("SELECT username FROM users WHERE username = %s", (name,))
        if cur.fetchone() is None:
            cur.execute("INSERT INTO users (username) VALUES (%s)", (name,))
            print("Added new user: " + name)
        else:
            print("User already exists!")
        db.commit()
    except:
        print("Something went wrong with the database")

def loadGame(name):
    try:
        savePlayer(name)
        cur.execute(
            "SELECT level, score FROM user_score WHERE username = %s ORDER BY id DESC LIMIT 1",
            (name,)
        )
        data = cur.fetchone()
        
        if not data:
            cur.execute(
                "INSERT INTO user_score (username, score, level) VALUES (%s, %s, %s)",
                (name, 0, 1)
            )
            db.commit()
            return 1, 0
        return data[0] or 1, data[1] or 0
    except:
        print("Progress loading Error")
        return 1, 0

def saveGame(name, score, level):
    try:
        cur.execute(
            "INSERT INTO user_score (username, score, level) VALUES (%s, %s, %s)",
            (name, score, level)
        )
        db.commit()
        print("Progress is saved")
    except:
        print("Progress saving Error")

def showText(txt, color, x, y):
    msg = font.render(txt, True, color)
    screen.blit(msg, [x, y])

def getFood(snake, wallss):
    while True:
        x = random.randrange(0, w - size, size)
        y = random.randrange(0, h - size, size)
        food = [x, y]
        
        if food not in snake and food not in wallss:
            return x, y

name = input("Enter your name: ").strip().lower()
level, score = loadGame(name)
print(f"Level: {level}, Score: {score}")

x = w // 2
y = h // 2
snake = []
length = 1
dx = 0
dy = 0
levelWalls = walls.get(level, [])
foodX, foodY = getFood(snake, levelWalls)
speed = 10 + (level - 1) * 2
paused = False

waiting = True
while waiting:
    screen.fill(blue)
    showText("PRESS ANY ARROW", black, 180, 180)
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                waiting = False

gameRunning = True
while gameRunning:
    screen.fill(blue)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and dx == 0:
                dx = -size
                dy = 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx = size
                dy = 0
            elif event.key == pygame.K_UP and dy == 0:
                dy = -size
                dx = 0
            elif event.key == pygame.K_DOWN and dy == 0:
                dy = size
                dx = 0
            elif event.key == pygame.K_p:
                paused = not paused
                if paused:
                    saveGame(name, score, level)

    if paused:
        showText("PAUSE", red, 250, 180)
        pygame.display.update()
        continue

    x += dx
    y += dy

    if x < 0 or x >= w or y < 0 or y >= h:
        gameRunning = False

    head = [x, y]
    snake.append(head)
    if len(snake) > length:
        del snake[0]

    if head in snake[:-1] or head in levelWalls:
        gameRunning = False

    if x == foodX and y == foodY:
        foodX, foodY = getFood(snake, levelWalls)
        length += 1
        score += 1
        
        if score % 3 == 0:
            level += 1
            speed += 2
            levelWalls = walls.get(level, [])

    pygame.draw.rect(screen, red, [foodX, foodY, size, size], border_radius=10)
    
    for wall in levelWalls:
        pygame.draw.rect(screen, white, [wall[0], wall[1], size, size])
        
    for part in snake:
        pygame.draw.rect(screen, black, [part[0], part[1], size, size])

    showText(f"Score: {score}", black, 10, 0)
    showText(f"Level: {level}", black, 500, 0)
    
    pygame.display.update()
    clock.tick(speed)

saveGame(name, score, level)
print("Game over. Progress is saved.")
pygame.quit()