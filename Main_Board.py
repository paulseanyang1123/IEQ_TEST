'''
This is the version of both English and Chinese in it.
'''
import pygame
from Parameters import Settings
import running_function as rf
from traits import Love
from button import Button
from dgbutton import DgButton
from result import Result
from score import Score

def main():

    pygame.init()
    # 初始化pygame,为使用硬件做准备
    parameters = Settings()
    prmts = parameters
    screen = pygame.display.set_mode((prmts.screen_width, prmts.screen_height)) # 设置屏幕长和宽
    #screen.fill(pts.bg_color)
    pygame.display.set_caption("CIIE (Complex index for IQ & EQ)/综合情商智商自测表")
    #pygame.display.set_caption("GTI (God's traits index)/神性自测表")
    love=Love(prmts, screen)
    play_button = Button(prmts, screen,"Statistics")  # set up name of button.
    dgbutton = DgButton(prmts, screen,"  ")    #
    result = Result(prmts, screen,' ')
    score = Score(prmts,screen)
    while True:
      rf.check_events(prmts, screen,play_button,dgbutton,result,score)
      rf.update_screen(prmts, screen,love,play_button,dgbutton,result,score)

main()
#testee = input('Please enter the name of the testee: ')