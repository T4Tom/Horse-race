import pygame, time
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 90)
text = font.render('PLAYER 2 WINS!!', True, (0, 255, 0))
textRect = text.get_rect()
textRect.center = (400, 60)

text2 = font.render('PLAYER 1 WINS!!', True, (0, 255, 0))
textRect2 = text2.get_rect()
textRect2.center = (400, 60)


horseImg = pygame.image.load('horse1.png')
horseImg = pygame.transform.scale(horseImg, (180, 140))

horseImg2 = pygame.image.load('horse2.png')
horseImg2 = pygame.transform.scale(horseImg2, (180, 140))

backgroundImg = pygame.image.load('background.webp')
backgroundImg = pygame.transform.scale(backgroundImg, (800, 600))



def winp1():
  screen.blit(text, textRect)

def winp2():
  screen.blit(text2, textRect2)

def game_loop():

  horsex = 30
  horsey = 285

  horsex2 = 30
  horsey2 = 135


  done = False
  while not done:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit()
      if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        exit()


      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        horsex += 6
      if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        horsex2 += 5
    
    screen.blit(backgroundImg, (0, 0))

    
    screen.blit(horseImg, (horsex, horsey))
    screen.blit(horseImg2, (horsex2, horsey2))

    if horsex >= 590:
      winp1()
      pygame.display.flip()
      time.sleep(3)
      game_loop()
    elif horsex2 >= 590:
      winp2()
      pygame.display.flip()
      time.sleep(3)
      game_loop()
    
    pygame.display.flip()
    clock.tick(60)

game_loop()
