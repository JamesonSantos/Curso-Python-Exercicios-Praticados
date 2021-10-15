'''
import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()):pass
'''

from playsound import playsound
playsound('ex021.mp3')
