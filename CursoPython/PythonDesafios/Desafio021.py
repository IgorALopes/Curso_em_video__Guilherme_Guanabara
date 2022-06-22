#Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.
'''from playsound import playsound
playsound('desafio021.mp3')'''

#RESOLUÇÃO PROFESSOR:
import pygame
pygame.init()
pygame.mixer.music.load('desafio021.mp3')
pygame.mixer.music.play()
input() #Linha adicionada devido a uma atualização.
pygame.event.wait()
