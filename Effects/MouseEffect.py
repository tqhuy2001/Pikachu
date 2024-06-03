import pygame

pygame.init()

class MouseEffect():

    isPressed = False

    def getPosMouse(self):
        return pygame.mouse.get_pos()

    def getPressedMouse(self):
        if pygame.mouse.get_pressed()[0] == True and self.isPressed == False:
            self.isPressed = True
            return pygame.mouse.get_pos()
        if  pygame.mouse.get_pressed()[0] == False and self.isPressed == True:
            self.isPressed = False

