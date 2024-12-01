import pygame.font
class Button():
    def __init__(self,prmts, screen,msg):
        self.screen = screen
        self.screen_rect =  screen.get_rect()
        self.width,self.height = 200,100
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font =  pygame.font.SysFont('conmicsans',70)    #None
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.prep_msg(msg)
    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        #self.msg_image_rect.center = self.rect.center
        self.msg_image_rect.x = 43*37
        self.msg_image_rect.y = 43
    def draw_button(self):
        self.screen.blit(self.msg_image,self.msg_image_rect)