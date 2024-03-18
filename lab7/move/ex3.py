import pygame
import os
screen = pygame.display.set_mode((600, 600))
done = False
clock = pygame.time.Clock()
n1=300
n2=300
while not done:
       
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                        if n1<575:
                            n1+=20
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                        if n1>25:
                            n1-=20
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                        if n2>25:
                            n2-=20
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                        if n2<575:
                            n2+=20
                    
        pygame.draw.circle(screen, (255,0,0), (n1, n2), 25)
        pygame.display.flip()
        clock.tick(60)