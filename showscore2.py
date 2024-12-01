import pygame.font
class Showscore2():
    def __init__(self,prmts,screen):
        super().__init__()  #you can also super(Dog_Liz,self).__init__() ,python 2.7
        self.screen = screen
        self.prmts = prmts
        # impose image and its rect outside this image
        #from random import choice   select one dog
        # l = [1, 2]
        # if choice(l)==1:
        #     self.image = pygame.image.load('dogliz.jpg')   #.convert()
        # else:
        #     self.image = pygame.image.load('liz2.jpg')
        # # self.image.resize(40,50)
        # self.image = pygame.transform.scale(self.image, (47, 47))
        # rect1 = pygame.Rect(0, 0, 47, 47)
        self.image = pygame.image.load('dig2.jpg')
        self.image = pygame.transform.scale(self.image, (47, 47))
        self.rect = self.image.get_rect()
        self.rect.x = 43  +86  #+ i*86
        self.rect.y = 820
    def drawme(self):
        #self.screen.blit(self.image_copy, (self.x, self.y))
        self.screen.blit(self.image, self.rect)