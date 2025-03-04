# -*- coding: utf-8 -*-
# Faca um programa em python que abra e reproduza o audio de um arquivo mp3
import pygame
import time

# pygame setup

pygame.init()
pygame.mixer.init()  # Inicializa o mixer especificamente
pygame.mixer.music.load("C:/Users/Bruno/Desktop/Coding/Sounds/que-ota_-17.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play()
print("Reproduzindo...")

while pygame.mixer.music.get_busy():
     pygame.time.Clock().tick(10)
print('O som acabou...')

