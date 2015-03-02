import pygame
from random import randint

ORIGIN = 0
BOUND_HT = 16
SCREEN_WID_HT = 800
PUCK_SPEED = 4
CENTER = SCREEN_WID_HT/2
PLAYER_WID = 48

pygame.mixer.init()

class drawableBoundObject(pygame.Rect):
    __xspeed = None
    __yspeed = None
    __P1score = 0
    __P2score = 0
    
    def __init__(self, xpos, ypos, wid, ht, xspeed, yspeed):
        super(drawableBoundObject, self).__init__(xpos, ypos, wid, ht)
        self.__xspeed = xspeed
        self.__yspeed = yspeed

    def drawRect(self, screen, color):
        pygame.draw.rect(screen, color, self)
    
    def checkAndMovePlayer(self, direction):
        if (direction == "MOVE_UP" and self.y >= BOUND_HT):
            self.y -= self.__yspeed
        elif (direction == "MOVE_DOWN" and self.y <= SCREEN_WID_HT-BOUND_HT - self.height):
            self.y += self.__yspeed

    def checkPuck(self, playerOne, playerTwo, boundTop, boundBottom):
        if (self.colliderect(playerOne) or self.colliderect(playerTwo)):
            pygame.mixer.Sound("boop.wav").play()
            self.__xspeed *= -1
        
        if (self.colliderect(boundTop) or self.colliderect(boundBottom)):
            pygame.mixer.Sound("boop.wav").play()
            self.__yspeed *= -1

    def checkOOB(self):
        if (self.x <= ORIGIN):
            self.setP2Score()
            self.resetPuck()
            
        if (self.x >= SCREEN_WID_HT):
            self.setP1Score()
            self.resetPuck()
        
    def checkGameOver(self):    
        if ((self.getP1Score() or self.getP2Score()) == 11):
            self.setGameOver()

    def movePuck(self):
        self.x += self.__xspeed
        self.y += self.__yspeed
        
    # Return to center x, flip direction, random y for variety
    def resetPuck(self):
        self.__xspeed *= -1
        self.x = CENTER
        self.y = randint(BOUND_HT,SCREEN_WID_HT-BOUND_HT)
        
    def setP1Score(self):
        self.__P1score += 1
    
    def setP2Score(self):
        self.__P2score += 1
        
    def getP1Score(self):
        return self.__P1score
    
    def getP2Score(self):
        return self.__P2score
    
    def setGameOver(self):
        self.__P1score = 0
        self.__P2score = 0
    