import sys
import pygame
import time

pygame.init()
win = pygame.display.set_mode((1200, 800))


green = (0, 200, 0)
white = (255, 255, 255)

def loadimages():
    image1 = pygame.image.load("drum.png")
    win.blit(image1, (200, 100))
    image2 = pygame.image.load("guitarlogo.jpg")
    win.blit(image2, (500, 100))
    image3 = pygame.image.load("cymbals.jpg")
    win.blit(image3, (800, 100))
    image4 = pygame.image.load("trumpet.jpg")
    win.blit(image4, (200, 500))
    image5 = pygame.image.load("clap.png")
    win.blit(image5, (500, 500))
    image6 = pygame.image.load("piano.jpg")
    win.blit(image6, (800, 500))

def progloop(run):
    while(run == True):
        loadimages()
        cursor = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        pygame.display.update()
        
        if(200<cursor[0] and cursor[0]<425 and 100<cursor[1] and cursor[1]<325):
            if(press[0] == 1):
                time.sleep(0.5)
            #print("1")
            #s.play()
            
                pygame.mixer.music.load("drum2.wav")
                pygame.mixer.music.play()
            #  time.sleep()
            #pygame.mixer.music.load("drum2.wav")
            #pygame.mixer.music.play()
            
        if(500<cursor[0] and cursor[0]<725 and 100<cursor[1] and cursor[1]<343):
            if(press[0]==1):
                time.sleep(0.5)
                pygame.mixer.music.load("guitar.wav")
                pygame.mixer.music.play()
        if(800<cursor[0] and cursor[0]<1025 and 100<cursor[1] and cursor[1]<306):
            if(press[0]==1):
                time.sleep(0.5)
                pygame.mixer.music.load("cymbals.wav")
                pygame.mixer.music.play()
        if(200<cursor[0] and cursor[0]<425 and 500<cursor[1] and cursor[1]<658):
            if(press[0]==1):
                pygame.mixer.music.load("trumpet.wav")
                pygame.mixer.music.play()
        if(500<cursor[0] and cursor[0]<725 and 500<cursor[1] and cursor[1]<725):
            if(press[0]==1):
                pygame.mixer.music.load("clap.wav")
                pygame.mixer.music.play()
        if(800<cursor[0] and cursor[0]<1025 and 500<cursor[1] and cursor[1]<734):
            if(press[0]==1):
                pygame.mixer.music.load("piano.wav")
                pygame.mixer.music.play()
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()
            pygame.display.update()

    # time.sleep(10)
progloop(True)

