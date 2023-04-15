import pygame
import numpy

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
RUNNING = True
DY = 0

rotationMatrix01 = numpy.array([[0.999848 , -0.0174524], [0.0174524 , 0.999848]])
rotationMatrix02 = numpy.array([[0.999391 , -0.0348995], [0.0348995 , 0.999391]])
rotationMatrix03 = numpy.array([[0.999391, 0.0348995],[-0.0348995, 0.999391]])
rotationMatrix04 = numpy.array([[0.994522, 0.104528], [-0.104528, 0.994522]])

origin = [400,400]

vector01 = pygame.Vector2(40, 40)
vector02 = pygame.Vector2(40, 40)
vector03 = pygame.Vector2(80, 20)
vector04 = pygame.Vector2(50, 20)

while RUNNING:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        origin = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            RUNNING = False
        

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.circle(screen, "purple",origin,70)


    pygame.draw.circle(screen, "purple",vector01 + origin,60)
    pygame.draw.circle(screen, "purple",vector02 + origin,60)
    pygame.draw.circle(screen, "purple",vector03 + origin,60)
    pygame.draw.circle(screen, "purple",vector04 + origin,60)
    


    pygame.draw.circle(screen, "red",vector01 + origin,10)
    pygame.draw.circle(screen, "green",vector02 + origin,10)
    pygame.draw.circle(screen, "blue",vector03 + origin,10)
    pygame.draw.circle(screen, "yellow",vector04 + origin,10)
    

    pygame.draw.line(screen, "red",    [0 + origin[0], 0 + origin[1]], vector01 + origin, 10)
    pygame.draw.line(screen, "green",  [0 + origin[0], 0 + origin[1]], vector02 + origin, 10)
    pygame.draw.line(screen, "blue",   [0 + origin[0], 0 + origin[1]], vector03 + origin, 10)
    pygame.draw.line(screen, "yellow", [0 + origin[0], 0 + origin[1]], vector04 + origin, 10)

    pygame.draw.circle(screen, "brown", origin, 10)

    vector01 = numpy.matmul(vector01, rotationMatrix01)
    vector02 = numpy.matmul(vector02, rotationMatrix02)
    vector03 = numpy.matmul(vector03, rotationMatrix03)
    vector04 = numpy.matmul(vector04, rotationMatrix04)
   
    # flip() the display to put your work on screen
    pygame.display.flip()

# limits FPS to 60
# dt is delta time in seconds since last frame, used for framerate-
# independent physics.
dt = clock.tick(60) / 1000

pygame.quit()
