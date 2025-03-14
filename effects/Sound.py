import pygame

pygame.init()
pygame.mixer.init()

class Sound:

    def add(self, path, vol):

        self.path = path
        self.sound = pygame.mixer.Sound(self.path)
        self.vol = vol
        self.sound.set_volume(vol)

    def play(self):
        self.sound.play()

    def setVol(self, vol):
        self.sound.set_volume(vol)

