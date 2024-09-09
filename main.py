import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

#write code between this

#list of colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
PURPLE = (128, 0, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255,0)
RED = (255, 0, 0)
CYAN = (0, 225, 225)
ORANGE = (255, 128, 0)

#fills in background, sets background color
display_surface.fill(PURPLE)

#draw a rect
X =  130
Y = 200
WIDTH = 350
HEIGHT = 200
rect = pygame.Rect(X, Y, WIDTH, HEIGHT)
pygame.draw.rect(display_surface, WHITE, rect)


#draws circle
CENTER = (300, 300)
RADIUS = 75

pygame.draw.circle(display_surface, RED, CENTER, RADIUS,)

#darw a line
START = (100, 100)
END = (500, 500)
#pygame.draw.line(display_surface,WHITE, START, END, 10 )





#and this



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()