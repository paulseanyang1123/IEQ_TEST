# import pygame.font
# class Showscore1():
#     def __init__(self,prmts,screen):
#         super().__init__()  #you can also super(Dog_Liz,self).__init__() ,python 2.7
#         self.screen = screen
#         self.prmts = prmts
#         self.image = pygame.image.load('dig1.jpg')
#         self.image = pygame.transform.scale(self.image, (47, 47))
#         self.rect = self.image.get_rect()
#         self.rect.x = 43  #+ i*86
#         self.rect.y = 820
#     def drawme(self):
#         self.screen.blit(self.image, self.rect)