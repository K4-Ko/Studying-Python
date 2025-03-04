# -*- coding: utf-8 -*-
# Create a Python program that opens and plays the audio of an MP3 file
import pygame
import time

# pygame setup

pygame.init()
pygame.mixer.init()  # Initializes the mixer specifically
pygame.mixer.music.load("C:/Users/Bruno/Desktop/Coding/Sounds/que-ota_-17.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play()
print("Playing...")

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

print('The sound has ended...')
