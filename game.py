import pygame as pg
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import time
import cv2

from Duck import *
from geometricShapes import *
from Spaceship import *
from Egg import *
from Bullet import *
from handTracking import *

# Setup menu
def draw_text_centered(text, rect, font, screen, color=(255, 255, 255)):
    rendered = font.render(text, True, color)
    text_rect = rendered.get_rect(center=rect.center)
    screen.blit(rendered, text_rect)

def draw_star_background(screen, star_count, screen_width, screen_height):
    for _ in range(star_count):
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        brightness = random.randint(150, 255)
        color = (brightness, brightness, brightness)
        pygame.draw.circle(screen, color, (x, y), 1)

def menu():
    pg.init()
    
    pg.init()
    pg.mixer.init()

    
    pg.mixer.music.load("assets/sounds/Intro.mp3")
    pg.mixer.music.set_volume(0.5)  
    pg.mixer.music.play(-1)  

    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    width, height = screen.get_size()
    clock = pg.time.Clock()

    # Fonts
    title_font = pg.font.SysFont('Arial', 80, bold=True)
    subtitle_font = pg.font.SysFont('Arial', 40, italic=True)
    button_font = pg.font.SysFont('Arial', 40)

    # Colors
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 100)
    BLACK = (0, 0, 0)

    # Generate random stars
    stars = [(random.randint(0, width), random.randint(0, height)) for _ in range(100)]

    while True:
        screen.fill(BLACK)

        # Draw stars
        for star in stars:
            pg.draw.circle(screen, WHITE, star, 1)

        # Render title and subtitle
        title_surface = title_font.render("Duck Invaders", True, YELLOW)
        subtitle_surface = subtitle_font.render("Aka War of Fayoum", True, WHITE)

        # Center title
        title_rect = title_surface.get_rect(center=(width // 2, height // 4))
        subtitle_rect = subtitle_surface.get_rect(center=(width // 2, height // 4 + 80))

        screen.blit(title_surface, title_rect)
        screen.blit(subtitle_surface, subtitle_rect)

        # Buttons
        start_text = button_font.render("Start", True, WHITE)
        exit_text = button_font.render("Exit", True, WHITE)

        start_rect = start_text.get_rect(center=(width // 2, height // 2))
        exit_rect = exit_text.get_rect(center=(width // 2, height // 2 + 80))

        screen.blit(start_text, start_rect)
        screen.blit(exit_text, exit_rect)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    pg.mixer.music.stop()
                    return  
                elif exit_rect.collidepoint(event.pos):
                    pg.quit()
                    exit()

        pg.display.flip()
        clock.tick(60)

def game():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = HandTracking()

    pg.init()


    entry_sound = pg.mixer.Sound("assets/sounds/entry.mp3")
    shoot_sound = pg.mixer.Sound("assets/sounds/shoot.mp3")
    quack_sound = pg.mixer.Sound("assets/sounds/quack.mp3")
    
    entry_sound.play()
   

    info = pg.display.Info()
    display = (info.current_w, info.current_h)
    pg.display.set_mode(display, pg.DOUBLEBUF | pg.OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    last_update_time = time.time()
    ducks_last_update_time = time.time()
    bullet_ct = time.time()
    bullet_pt = 0

    stars_update_interval = 0.1
    ducks_update_interval = 2
    bullets_cool_down = 0.5

    ducks = []
    eggs = []
    bullets = []

    spaceshipX = 0
    ship = Spaceship(spaceshipX, -1.2, 0.009)

    while True:
        
        current_time = time.time()

        success, img = cap.read()
        img = detector.findHands(img)
        img = cv2.flip(img, 1)
        lmList = detector.findXPosition(img, 0)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (10, 70),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        cv2.imshow("Hand Tracking", img)
        cv2.waitKey(1)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                cv2.destroyAllWindows()
                sys.exit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        bullet_ct = time.time()
        if len(lmList) != 0:
            if lmList[8][2] <= lmList[6][2]:
                fingerPosition = (lmList[8][1] - 0.5) * -4
                spaceshipX = fingerPosition * 2
            if lmList[8][2] <= lmList[6][2] and lmList[12][2] <= lmList[10][2]:
                if bullet_ct - bullet_pt >= bullets_cool_down:
                    bullet_pt = bullet_ct
                    shoot_sound.play()
                    newBullet = Bullet(
                        ship.moveX, ship.startingY + 0.45, 0.2, 0.02)
                    bullets.append(newBullet)

        ship.draw_spaceship(spaceshipX)

        if current_time - ducks_last_update_time > ducks_update_interval:
            new_duck = Duck(0.3, random.randrange(-3, 3), 1.6)
            ducks.append(new_duck)
            ducks_last_update_time = current_time

        for duck in ducks:
            duck.drawDuck()
            newEgg = duck.dropEgg(current_time)
            if newEgg != None:
                eggs.append(newEgg)

        for egg in eggs[:]:
            egg.drawEgg()
            egg.move()
            if egg.startingY <= -4:
                eggs.remove(egg)
                continue
            if ship.checkCollisionWithEgg(egg.startingX, egg.startingY):
                pg.quit()
                cv2.destroyAllWindows()
                sys.exit()

        for bullet in bullets[:]:
            bullet.draw()
            bullet.move()
            if bullet.y >= 4:
                bullets.remove(bullet)
                continue
            for duck in ducks[:]:
                if bullet.checkCollisionWithDuck(duck.startingX, duck.startingY):
                    quack_sound.play()
                    if duck in ducks:
                        ducks.remove(duck)

        if current_time - last_update_time > stars_update_interval:
            for i in range(1, 100):
                randx = random.randint(-11, 11)
                randy = random.randint(-7, 7)
                draw_point(randx, randy)
            last_update_time = current_time

        pg.display.flip()
        pg.time.wait(10)

# Main loop
if __name__ == "__main__":
    menu()
    game()
