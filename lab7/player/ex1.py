import pygame
import os
import random 
pygame.display.set_caption("Music")
_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image
images=['pfp3.jpg','pfp4.jpg','jady.jpg','yepfp.jpg']
n=3
def next_image():
       global images
       images=images[1:]+[images[0]]
       return images[0]
def prev_image():
       global images
       images = images[n:] + images[:n] 
       return images[0]
_songs=['songn2.mp3','songn4.mp3','songn3.mp3','yesong.mp3']

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]] # move current song to the back of the list
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
def previous_song():
    global _songs
    _songs = _songs[n:] + _songs[:n] 
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
pygame.init()
screen = pygame.display.set_mode((600, 600))
done = False
clock = pygame.time.Clock()
pause=True
image=get_image(images[0])
buttonmain=get_image('turnoff.png')
buttonmain_res = pygame.transform.scale(buttonmain, (75, 75))
buttonnext=get_image('next.png')
buttonnext_res=pygame.transform.scale(buttonnext, (75, 75))
buttonprev=get_image('prev.png')
buttonprev_res=pygame.transform.scale(buttonprev, (75, 75))

font = pygame.font.SysFont("chalkduster", 30)
font2 = pygame.font.SysFont("chalkduster", 20)
titles=['Perfect star','GONE,GONE','5 pack',"Can't tell me nothing"]
text = font.render(titles[0], True, (184, 244, 245))

def next_title():
       global titles
       titles=titles[1:]+[titles[0]]
       return titles[0]
def prev_title():
       global titles
       titles=titles[n:]+titles[:n]
       return titles[0]
singers=['Pooka','Tyler,The Creator',"Jady's Birthday",'Ye']
sing = font2.render(singers[0], True, (184, 244, 245))
def next_singer():
       global singers
       singers=singers[1:]+[singers[0]]
       return singers[0]
def prev_singer():
       global singers
       singers=singers[n:]+singers[:n]
       return singers[0]

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load(_songs[0])
pygame.mixer.music.play()
pygame.mixer.music.pause()

while not done:
       
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        if not pause:
                            
                            pygame.mixer.music.pause()
                            pause=True
                            buttonmain=get_image('turnoff.png')
                            buttonmain_res=pygame.transform.scale(buttonmain, (75, 75))
                        else:
                            pygame.mixer.music.unpause()
                            pause=False
                            buttonmain=get_image('turnon.png')
                            buttonmain_res=pygame.transform.scale(buttonmain, (75, 75))
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                       play_next_song()
                
                       text = font.render(next_title(), True, (184, 244, 245))
                       sing = font2.render(next_singer(), True, (184, 244, 245))
                       image=get_image(next_image())
                       screen.blit(pygame.transform.scale(get_image('nextpressed.png'),(75,75)),(350,500))
                       if  pause:
                              buttonmain=get_image('turnon.png')
                              buttonmain_res=pygame.transform.scale(buttonmain, (75, 75))
                       pause=False
        
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                       previous_song()  
                           
                       text = font.render(prev_title(), True, (184, 244, 245))
                       sing = font2.render(prev_singer(), True, (184, 244, 245))                
                       image=get_image(prev_image())
                       screen.blit(pygame.transform.scale(get_image('prevpressed.png'),(75,75)), (150, 500))
                       if pause:
                              buttonmain=get_image('turnon.png')
                              buttonmain_res=pygame.transform.scale(buttonmain, (75, 75))
                       pause=False
                if event.type == SONG_END:
                       text = font.render(next_title(), True, (184, 244, 245))
                       sing = font2.render(next_singer(), True, (184, 244, 245))
                       play_next_song()
                       image=get_image(next_image())
                       pause=False
        screen.blit(get_image('backg.jpg'), (0, 0))
        screen.blit(pygame.transform.scale(image,(400,400)), (100, 0))
        screen.blit(buttonmain_res, (250, 500))
        screen.blit(buttonnext_res, (350, 500))
        screen.blit(buttonprev_res, (150, 500))
        screen.blit(text,(250-text.get_width()/2+30,420))
        screen.blit(sing,(250-sing.get_width()/2+30,470))
    
     
        pygame.display.flip()
        clock.tick(60)