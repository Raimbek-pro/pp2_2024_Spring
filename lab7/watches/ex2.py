import pygame
import os
import datetime
current_time = datetime.datetime.now()
print("Current local time:", current_time)


_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image
def blitRotate(surf, image, pos, originPos, angle):

    # offset from pivot to center
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)
screen = pygame.display.set_mode((700, 525))
done = False
clock = pygame.time.Clock()

current_time = datetime.datetime.now()
hour = current_time.hour
minute = current_time.minute
second=current_time.second
angle2=30*hour
angle1=6*minute
while not done:
        # Extract individual components of the time
        current_time = datetime.datetime.now()
        hour = current_time.hour
        minute = current_time.minute
        second=current_time.second

        # hour=14
        # minute=40
        # second=0
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.blit(pygame.transform.scale(get_image('mainclock.png'),(700,525)), (0, 0))
        image = pygame.transform.rotate(pygame.transform.scale(get_image('leftarm.png'),(32,525)),angle1)
        image2=pygame.transform.rotate(pygame.transform.scale(get_image('rightarm.png'),(700,525)),angle2)
        
        w, h = image.get_size()
        w2,h2=image2.get_size()
    
        pos = (screen.get_width()/2, screen.get_height()/2)
        blitRotate(screen, image, pos, (w/2, h/2), angle1)
        blitRotate(screen, image2, pos, (w2/2, h2/2), angle2)
        angle2=-0.25*minute-15*hour-25
        angle1=-3*minute
        pygame.display.flip()
        clock.tick(60)
                       