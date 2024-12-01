'''
This code is used to calculate the score
'''


import pygame
from Parameters import Settings
import running_function as rf
import numpy as np
from csv import writer
import pandas as pd
parameters = Settings()
prmts = parameters
screen = pygame.display.set_mode((prmts.screen_width, prmts.screen_height)) # 设置屏幕长和宽
averagetest = np.zeros(1)   # single number does not work, but [] works well!!!!!!!!!  this is the amazing discovery.
def testdigit():
    averagetest1 = np.mean(rf.list2)
    averagetest1 = round(averagetest1, 2)
    #averagetest = np.zeros(1)
    averagetest[0] = averagetest1
    #print('rf.list2 = ',rf.list2 )
    print('averagetest = ',averagetest )
    return averagetest

# testee = input('Please enter the name of the testee: ')
# gender = input('Please enter the gender of the testee: ')
