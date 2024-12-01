
'''
This code is used to show  the score on score board
'''
import pygame.font
import testdigit as td
from Parameters import Settings
class Score():
    def __init__(self,prmts,screen):
        parameters = Settings()
        prmts = parameters
        self.screen = screen
        self.screen_rect =  screen.get_rect()
        self.width,self.height = 400,100
        self.button_color = (0,255,0)
        self.text_color = (255,0,0)
        self.font =  pygame.font.SysFont('conmicsans',120)    #None
        self.rect = pygame.Rect(0,0,self.width,self.height)
        #self.rect.center = self.screen_rect.center
        self.prep_msg()
    def prep_msg(self):
        #print('td.averagetest=',td.averagetest)
        adjust = td.averagetest+0.01
        if adjust>=10:
            adjust = 9.99
        score_str=str(adjust)   #score_str = "{:,}".format(rounded_score)
        self.msg_image = self.font.render(score_str,True,self.text_color,self.button_color) #关键的一句，把文字数字加在方框上
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.x = 43*37+10
        self.msg_image_rect.y = 705+75
    def draw_button(self):
        self.screen.blit(self.msg_image,self.msg_image_rect)