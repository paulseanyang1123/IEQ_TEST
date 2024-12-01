'''
This is used to design 180 score hitting buttons
'''

import pygame.font
import numpy as np
class DgButton():
    def __init__(self,prmts, screen,msg1):
        self.screen = screen
        self.screen_rect =  screen.get_rect()
        self.width,self.height = 200,100
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font =  pygame.font.SysFont('conmicsans',70)    #None
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.prep_msg(msg1)
    def prep_msg(self, msg1):
        self.msg_image1 = self.font.render(msg1,True,self.text_color,self.button_color)
        self.msg_image_rect1 = self.msg_image1.get_rect()

    def draw_button(self):   # set the positions of those digit bar.
        self.x = np.zeros(18)
        self.y = np.zeros(11)

        for i in range(1, 11):

            for j in range(18):
                self.x[j] = 53 + j * 86
                self.y[i] = 90  + 34 * (i * 2-1)
                self.msg_image_rect1.x = self.x[j]
                self.msg_image_rect1.y = self.y[i]
                self.screen.blit(self.msg_image1,self.msg_image_rect1)
