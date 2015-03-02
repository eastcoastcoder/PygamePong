import sys
import pygame
from drawableBoundObject import *

pygame.init()

SCREEN_WID_HT = 800
CENTER = SCREEN_WID_HT/2

PLAYER_WID = 48
PLAYER_HT = 256
PADDING = 40
PLAYER_ONE_X = PADDING
PLAYER_TWO_X = SCREEN_WID_HT-PLAYER_WID-PADDING
PLAYER_Y = (SCREEN_WID_HT/2)-(PLAYER_HT/2)

PLAYER_SPEED = 20
PUCK_SPEED = 14

ORIGIN = 0
BOUND_HT = 16

PUCK_WD_HT = 16

pygame.display.set_caption("Classic Pong")
scoreBoard = pygame.font.SysFont( "arial", 30 )
screen = pygame.display.set_mode((SCREEN_WID_HT, SCREEN_WID_HT))
clock = pygame.time.Clock()

playerOne = drawableBoundObject(PLAYER_ONE_X, PLAYER_Y, PLAYER_WID, PLAYER_HT, 0, PLAYER_SPEED)    # Create the player
playerTwo = drawableBoundObject(PLAYER_TWO_X, PLAYER_Y, PLAYER_WID, PLAYER_HT, 0, PLAYER_SPEED)   # Create the opponent
boundTop = drawableBoundObject(ORIGIN, ORIGIN, SCREEN_WID_HT, BOUND_HT, 0, 0)         # Create the top
boundBottom = drawableBoundObject(ORIGIN, SCREEN_WID_HT-BOUND_HT, SCREEN_WID_HT, BOUND_HT, 0, 0)    # Create the bottom
puck = drawableBoundObject(CENTER, CENTER, PUCK_WD_HT, PUCK_WD_HT, -PUCK_SPEED, PUCK_SPEED)     # Create the puck

def moveIt(key):
    #Player Control
    if key[pygame.K_UP]:
        playerOne.checkAndMovePlayer("MOVE_UP")
    if key[pygame.K_DOWN]:
        playerOne.checkAndMovePlayer("MOVE_DOWN")
    
    #Opponent Control
    if key[pygame.K_w]:
        playerTwo.checkAndMovePlayer("MOVE_UP")
    if key[pygame.K_s]:
        playerTwo.checkAndMovePlayer("MOVE_DOWN")
    
def drawIt():
    screen.fill((0, 0, 0))
    
    playerOne.drawRect(screen, (255, 0, 0))
    playerTwo.drawRect(screen, (255, 200, 0))
    
    boundTop.drawRect(screen, (255, 255, 255))
    boundBottom.drawRect(screen, (255, 255, 255))
    
    puck.drawRect(screen, (255, 255, 255))
    
    playerOneDrawScore = scoreBoard.render(str(puck.getP1Score()), 1, (255, 255, 255))
    playerTwoDrawScore = scoreBoard.render(str(puck.getP2Score()), 1, (255, 255, 255))
    screen.blit(playerOneDrawScore, (CENTER-100, 20))
    screen.blit(playerTwoDrawScore, (CENTER+100, 20))
    
    pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()
    
    moveIt(pygame.key.get_pressed())
    
    puck.checkPuck(playerOne, playerTwo, boundTop, boundBottom)
    puck.checkOOB()
    puck.checkGameOver()
    puck.movePuck()
    
    drawIt()
    clock.tick(59)