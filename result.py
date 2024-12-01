
'''
design a score board
'''
import pygame.font

class Result():
    def __init__(self,prmts, screen,msg):
        self.screen = screen
        self.screen_rect =  screen.get_rect()
        self.width,self.height = 400,100
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font =  pygame.font.SysFont('conmicsans',70)    #None
        self.rect = pygame.Rect(0,0,self.width,self.height)
        #self.rect.center = self.screen_rect.center
        self.prep_msg(msg)
    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.x = 43*37   #-10
        self.msg_image_rect.y = 735
    def draw_button(self):
        self.screen.blit(self.msg_image,self.msg_image_rect)