## 30mb version of pong
## keyboard controls

import pygame, sys, math, random
from pygame.locals import *
## colors
white = (255,255,255)
black = (0,0,0)

pygame.init()

frames = pygame.time.Clock()
vec = pygame.math.Vector2

ACC = 0.5
FRIC = -0.12
FPS = 60
game = False
## change screen size + variables
WIDTH = 800
HEIGHT = 600
top = 50
bottom = 560
p1_src = 0
p2_src = 0
state = "menu"
ballplay = False
P1s = pygame.mixer.Sound("pongP1.wav")
P2s = pygame.mixer.Sound("pongP2.wav")
#font = pygame.font.SysFont('AtariST8x16SystemFont',30)
font = pygame.font.Font('aa.ttf',30)
## add text
def text(text,font,text_colour,x,y):
  img = font.render(text,True,text_colour)
  display.blit(img, (x,y))
 
def S1():
  pygame.mixer.Sound.play(P1s)
  pygame.mixer.music.stop()

def S2():
  pygame.mixer.Sound.play(P2s)
  pygame.mixer.music.stop()
  
def title(display,state,game):
  keys = pygame.key.get_pressed()
  text("AcePong!",font,(255,0,0),HEIGHT//2,WIDTH//2)
  if keys[pygame.K_SPACE]:
    game = True


display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
## top margin
def overlay():
  display.fill(black)
  pygame.draw.line(display,white,(0,top),(WIDTH,top), 10)
  pygame.draw.line(display,white,(0,bottom),(WIDTH,bottom), 10)
  
  pygame.draw.line(display,white,(395,80),(405,80), 20)
  pygame.draw.line(display,white,(395,120),(405,120), 20)
  pygame.draw.line(display,white,(395,160),(405,160), 20)
  pygame.draw.line(display,white,(395,200),(405,200), 20)
  pygame.draw.line(display,white,(395,240),(405,240), 20)
  pygame.draw.line(display,white,(395,280),(405,280), 20)
  pygame.draw.line(display,white,(395,320),(405,320), 20)
  pygame.draw.line(display,white,(395,360),(405,360), 20)
  pygame.draw.line(display,white,(395,400),(405,400), 20)
  pygame.draw.line(display,white,(395,440),(405,440), 20)
  pygame.draw.line(display,white,(395,480),(405,480), 20)
  pygame.draw.line(display,white,(395,520),(405,520), 20)


## paddle 1
class paddle1:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.speed = 12
    self.rect = Rect(x, y ,20, 100)
    
  def control(self):
 
    if keys[pygame.K_w] and self.rect.top > top:
        self.rect.move_ip(0, -1 * self.speed)
      
    if keys[pygame.K_s] and self.rect.bottom < bottom:
        self.rect.move_ip(0, self.speed)
  ## DRAWS paddle
  def main(self):
    pygame.draw.rect(display, (255,255,255), self.rect)
## paddle 2
class paddle2:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.speed = 12
    self.rect = Rect(x, y ,20, 100)
    
  def control(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and self.rect.top > top:
        self.rect.move_ip(0, -1 * self.speed)
      
    if keys[pygame.K_DOWN] and self.rect.bottom < bottom:
        self.rect.move_ip(0, self.speed)
  ## DRAWS paddle
  def main(self):
    pygame.draw.rect(display, (255,255,255), self.rect)

## ball class
class pball:
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.rect = Rect(x,y,10,10)
    self.velocity = [random.randint(1,2),random.randint(-1,2)]
    self.winner = 0
  def main(self):
    pygame.draw.rect(display, (255,255,255), self.rect)
    self.rect.x += self.velocity[0]
    self.rect.y += self.velocity[1]
   # if ball.rect.x>=800:
        #ball.velocity[0] = -ball.velocity[0]
    #if ball.rect.x<=0:
        #ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>bottom - 10:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<top:
        ball.velocity[1] = -ball.velocity[1] 
  ## bounces balls off paddles
    if self.rect.colliderect(playerone):
      S1()
      self.velocity[0] = -self.velocity[0]
      self.velocity[1] = random.randint(-2,2)

    if self.rect.colliderect(playertwo):
      S2()
      self.velocity[0] = -self.velocity[0]
      self.velocity[1] = random.randint(-2,2)
    if self.rect.left < 0:
      self.winner = 1 ## Player 2 wins
    if self.rect.left >= 800:
      self.winner = -1 ## Player 1 wins
    return self.winner

  def reset(self,x,y):
    self.x = x
    self.y = y
    self.rect = Rect(x,y,10,10)
    self.velocity = [random.randint(2,3),random.randint(-2,3)]
    self.winner = 0
## assigning paddle class
playerone = paddle1(20, HEIGHT // 2)
playertwo = paddle2( 760, HEIGHT // 2)
##
ball = pball(WIDTH // 2, HEIGHT // 2)

pygame.mixer.music.load('tt.wav')
pygame.mixer.music.play(-1)
## main screen stuff
while state == "menu":
  frames.tick(FPS)
  keys = pygame.key.get_pressed()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
      pygame.QUIT
  ## title components
  title_screen = pygame.image.load("title.png")
  display.blit(title_screen,(50,0))
  text("AcePong!",font,(255,0,0),HEIGHT//2 + 15,WIDTH//2)
  text("Press Enter to Start!",font,(255,0,0),220,450)
  #text("Press C for Controls!",font,(255,0,0),220,500)
  text("Press Esc to Quit!",font,(255,0,0),240,550)

  #pygame.mixer.music.load('tt.wav')
  #pygame.mixer.music.play(-1)
  #pygame.mixer.music.stop()
  
  if keys[pygame.K_RETURN]:
    state = "game"
  if keys[pygame.K_c]:
    state = "controls"
  if keys[pygame.K_ESCAPE]:
    sys.exit()
    pygame.QUIT
  pygame.display.update()

while state == "controls":
  #display.fill(0,0,0)
  frames.tick(FPS)
  keys = pygame.key.get_pressed()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
      pygame.QUIT
  controller = pygame.image.load("controller.jpg")
  DEFAULT_IMAGE_SIZE = (200,200)
  controller = pygame.transform.scale(controller, DEFAULT_IMAGE_SIZE)
  text("Controls:",font,(255,0,0),HEIGHT//2,WIDTH//2)
  display.blit(controller,(120,25))
  if keys[pygame.K_RETURN]:
    state = "menu"
  if keys[pygame.K_ESCAPE]:
    sys.exit()
    pygame.QUIT
  pygame.display.update()

  
while state == "game":
  frames.tick(FPS)
  keys = pygame.key.get_pressed()
  pygame.mixer.music.stop()
  
  overlay()
  text("Player One: " + str(p1_src),font,white,20,15)
  text("Player Two: " + str(p2_src),font,white,WIDTH - 240,15)
  text("Ace_Pong - V1",font,white,WIDTH//2,bottom + 10)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
      pygame.QUIT
    if keys[pygame.K_SPACE] and ballplay == False:
      ballplay = True
      ball.reset(WIDTH // 2, HEIGHT // 2)
    if keys[pygame.K_ESCAPE]:
      sys.exit()
      pygame.QUIT
  
  if ballplay == False:
    text("[Press Space To Begin]" ,font,(255,0,0),25,HEIGHT//4)
    text("[Press Space To Begin]" ,font,(255,0,0),450,HEIGHT//4)
  ## players
  playerone.main()
  
  playertwo.main()
  

## ball
  if ballplay == True:
    winner = ball.main()
    if winner == 0:
      ball.main()
      playerone.control()
      playertwo.control()
    else:
      ballplay = False
      if winner == -1:
        p1_src = p1_src + 1
      elif winner == 1:
        p2_src = p2_src + 1

 # if playerone.paddle1.colliderect(ball):
    #  ball.bounce()
  
  pygame.display.update()

  