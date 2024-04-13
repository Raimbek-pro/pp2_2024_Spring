import pygame

def getRectangle(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x1-x2)
    h = abs(y1-y2)
    return (x, y, w, h)


pygame.init()
screen = pygame.display.set_mode((400, 300))
another_layer = pygame.Surface((400, 300))

done = False
clock = pygame.time.Clock()

x1 = 10
y1 = 10
x2 = 10
y2 = 10

w = 100
h = 100
color = (0, 128, 255)
isMouseDown = False
screen.fill((0,0,0))
figure='R'
points=[]
while not done:
        
        for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                        done = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # left click
                        x1 = event.pos[0]
                        y1 = event.pos[1]
                        isMouseDown = True
                if event.type==pygame.KEYDOWN:
                      if event.key == pygame.K_c:
        
                            figure='C'
                      if event.key==pygame.K_r:
                            figure='R'
                      if event.key==pygame.K_e:
                            figure='E'  
                      if event.key == pygame.K_1:
        
                            color=(0, 128, 255)
                      if event.key==pygame.K_2:
                            color=(64,200,100)
                      if event.key==pygame.K_3:
                            color=(211, 3, 252)

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        isMouseDown = False
                        another_layer.blit(screen, (0, 0))

                        
                if event.type == pygame.MOUSEMOTION:
                         
                         if isMouseDown:
                            
                            if figure=='R':
                                x2 = event.pos[0]
                                y2 = event.pos[1]
                                screen.blit(another_layer, (0, 0))
                                pygame.draw.rect(screen, color, pygame.Rect(getRectangle(x1, y1, x2, y2)), 1)
                            elif figure=='C':
                                  x2 = event.pos[0]
                                  y2 = event.pos[1]
                                  screen.blit(another_layer, (0, 0))
                                  pygame.draw.circle(screen, color, (x1, y1), abs(x1-x2),1)
                            elif figure=='E':
                                  x1=event.pos[0]
                                  y1=event.pos[1]
                                  pygame.draw.circle(screen, (0,0,0), (x1, y1), 20)
                                  
                                  
                            

        
        pygame.display.flip()
        clock.tick(60)