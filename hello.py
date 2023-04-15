import pygame
import numpy

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
RUNNING = True
DY = 0

rotationMatrix01 = numpy.array([[0.999848 , -0.0174524], [0.0174524, 0.999848]])
rotationMatrix02 = numpy.array([[0.999391, -0.0348995], [0.0348995,  0.999391]])

vector01 = pygame.Vector2(200, 300)
vector02 = pygame.Vector2(100, 400)

while RUNNING:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.line(screen, "red", [0, 0], vector01, 10)
    pygame.draw.line(screen, "green", [0, 0], vector02, 10)

    vector01 = numpy.matmul(vector01, rotationMatrix01)
    vector02 = numpy.matmul(vector02, rotationMatrix02)

    # flip() the display to put your work on screen
    pygame.display.flip()

# limits FPS to 60
# dt is delta time in seconds since last frame, used for framerate-
# independent physics.
dt = clock.tick(60) / 1000

pygame.quit()
