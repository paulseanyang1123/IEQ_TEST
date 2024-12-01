import sys
import pygame
import numpy as np
import testdigit as td
import pandas as pd
from csv import writer
import matplotlib.pyplot as plt
def check_events(prmts, screen,play_button,dgbutton,result,score):#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_stat_button(play_button,screen,result,score)
            return_digit(prmts,screen)

def check_stat_button(play_button,screen,result,score):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    button_clicked = play_button.msg_image_rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        #print("Hul.....")
        td.testdigit()
        score.prep_msg()
list = np.zeros([18,10])
list2 = np.zeros(18)
list3 = np.zeros(21)
testee = input('Please enter the name of the testee: ')
gender = input('Please enter the gender of the testee: ')
def  return_digit(prmts, screen):   # set the functions of those digit bar.
            # list = np.zeros([18, 10])   #千万不能放在这儿，因为为此运行总是重新设置为0 Array。
            # list2 = np.zeros(18)
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i in range(18):   # design score when you hit a certain area
                if 53 +i*86<= mouse_x <= 53+i*86+27 :
                    for j in range(10):
                        if 124 +j*67 <= mouse_y <= 124+j*67 +47:
                            list[i,j] = j+1
                            #print(list[i,j])
                            list2[i]= list[i,j]
                            #list3[i+2] = list2[i]
                            #animalid = int(input('Please enter the ID of the animal: '))
                            #testee = input('Please enter the name of the testee: ')
                            print('list2 = ',list2)
                            average = np.mean(list2)
                            average = round(average,2)  # get two decimals
                            print('averageloop = ', average)

                            return list,list2   #average,
            # list3[0]  = testee
            # list3[1] = gender
            tdaveragetest= float(td.averagetest)
            list3 = [testee, gender, list2[0],list2[1],list2[2],list2[3],list2[4],list2[5],list2[6],list2[7],list2[8],
                      list2[9],list2[10],list2[11],list2[12],list2[13],list2[14],list2[15],list2[16],list2[17],tdaveragetest]
            with open(r'C:\Users\xuyan\Desktop\776-777-project\csv-file-for-776.csv', 'a',
                      newline='') as f_target:
                # newline='', this is used to avoid avery other line problem.
                # Pass this file object to csv.writer()
                # and get a writer object

                writer_object = writer(f_target)

                # Pass the list as an argument into
                # the writerow()
                writer_object.writerow(list3)  # this is the key step #####

                # Close the file object
                f_target.close()

def update_screen(prmts, screen,love,play_button,dgbutton,result,score):
    screen.fill(prmts.bg_color)
    love.drawme()
    play_button.draw_button()
    score.draw_button()
    dgbutton.draw_button()
    pygame.display.update()