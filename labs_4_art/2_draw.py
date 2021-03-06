import pygame
from pygame.draw import *

pygame.init()
pygame.font
FPS = 30
screen = pygame.display.set_mode((1131, 870))

rect(screen, (211, 211, 211), (0, 0, 1131, 938))
polygon(screen, (255, 228, 196), [(244, 699), (286, 689), (125, 145), (83, 154), (244, 699)])
polygon(screen, (255, 228, 196), [(860, 698), (1050, 160), (1005, 158), (820, 678), (860, 698)])

circle(screen, (255, 69, 0), (550, 938), 296)
polygon(screen, (255, 69, 0), [(774, 848), (716, 745), (785, 651), (887, 695), (881, 819), (774, 848)])
polygon(screen, (0, 0, 0), [(774, 848), (716, 745), (785, 651), (887, 695), (881, 819), (774, 848)], 1)
polygon(screen, (255, 69, 0), [(333, 843), (223, 828), (211, 709), (313, 651), (388, 735), (333, 843)])
polygon(screen, (0, 0, 0), [(333, 843), (223, 828), (211, 709), (313, 651), (388, 735), (333, 843)], 1)
circle(screen, (255, 228, 196), (550, 495), 280)
circle(screen, (135, 206, 235), (460, 444), 58)
circle(screen, (0, 0, 0), (460, 444), 58, 1)
circle(screen, (135, 206, 235), (637, 444), 58)
circle(screen, (0, 0, 0), (637, 444), 58, 1)
circle(screen, (0, 0, 0), (641, 449), 17)
circle(screen, (0, 0, 0), (459, 449), 17)
polygon(screen, (139, 69, 19), [(550, 550), (525, 508), (575, 508), (550, 550)])
polygon(screen, (139, 0, 0), [(550, 550), (525, 508), (575, 508), (550, 550)], 1)
polygon(screen, (255, 25, 0), [(400, 570), (550, 665), (700, 570), (400, 570)])
polygon(screen, (139, 0, 0), [(400, 570), (550, 665), (700, 570), (400, 570)], 1)
polygon(screen, (148, 0, 211), [(312, 350), (275, 275), (356, 281), (312, 350)])
polygon(screen, (0, 0, 0), [(312, 350), (275, 275), (356, 281), (312, 350)], 1)
polygon(screen, (148, 0, 211), [(338, 300), (319, 223), (408, 255), (338, 300)])
polygon(screen, (0, 0, 0), [(338, 300), (319, 223), (408, 255), (338, 300)], 1)
polygon(screen, (148, 0, 211), [(382, 266), (377, 184), (455, 225), (382, 266)])
polygon(screen, (0, 0, 0), [(382, 266), (377, 184), (455, 225), (382, 266)], 1)
polygon(screen, (148, 0, 211), [(424, 242), (430, 160), (500, 210), (424, 242)])
polygon(screen, (0, 0, 0), [(424, 242), (430, 160), (500, 210), (424, 242)], 1)
polygon(screen, (148, 0, 211), [(475, 220), (504, 145), (554, 210), (475, 220)])
polygon(screen, (0, 0, 0), [(475, 220), (504, 145), (554, 210), (475, 220)], 1)
polygon(screen, (148, 0, 211), [(533, 217), (558, 150), (613, 221), (533, 217)])
polygon(screen, (0, 0, 0), [(533, 217), (558, 150), (613, 221), (533, 217)], 1)
polygon(screen, (148, 0, 211), [(600, 227), (639, 157), (667, 227), (600, 227)])
polygon(screen, (0, 0, 0), [(600, 227), (639, 157), (667, 227), (600, 227)], 1)
polygon(screen, (148, 0, 211), [(653, 228), (725, 192), (721, 273), (653, 228)])
polygon(screen, (0, 0, 0), [(653, 228), (725, 192), (721, 273), (653, 228)], 1)
polygon(screen, (148, 0, 211), [(704, 249), (783, 230), (759, 308), (704, 249)])
polygon(screen, (0, 0, 0), [(704, 249), (783, 230), (759, 308), (704, 249)], 1)
polygon(screen, (148, 0, 211), [(746, 282), (827, 279), (790, 351), (746, 282)])
polygon(screen, (0, 0, 0), [(746, 282), (827, 279), (790, 351), (746, 282)], 1)
ellipse(screen, (255, 228, 196), (50, 37, 108, 129))
ellipse(screen, (255, 248, 220), (50, 37, 108, 129), 1)
ellipse(screen, (255, 228, 196), (967, 45, 128, 134))
ellipse(screen, (255, 248, 220), (967, 45, 128, 134), 1)
rect(screen, (127, 255, 0), (2, 2, 1127, 110))
rect(screen, (0, 0, 0), (2, 2, 1127, 110), 1)


f1 = pygame.font.Font(None, 150)
text1 = f1.render('PYTHON is AMAZING', True,
                  (0, 0, 0))
screen.blit(text1, (20, 10))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
