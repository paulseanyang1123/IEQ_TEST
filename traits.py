import pygame


class Love():
    def __init__(self,prmts,screen):
        super().__init__()
        self.screen = screen
        self.prmts = prmts
        self.image1 = pygame.image.load('love.jpg')
        self.image1 = pygame.transform.scale(self.image1, (47, 47))
        self.rect1 = self.image1.get_rect()
        self.rect1.x = 43
        self.rect1.y = 43

        self.image2 = pygame.image.load('kindness.jpg')
        self.image2 = pygame.transform.scale(self.image2, (47, 47))
        self.rect2 = self.image2.get_rect()
        self.rect2.x = 43*3
        self.rect2.y = 43

        self.image3 = pygame.image.load('pure.jpg')
        self.image3 = pygame.transform.scale(self.image3, (47, 47))
        self.rect3 = self.image3.get_rect()
        self.rect3.x = 43 * 5
        self.rect3.y = 43

        self.image4 = pygame.image.load('fairness.jpg')
        self.image4 = pygame.transform.scale(self.image4, (47, 47))
        self.rect4 = self.image4.get_rect()
        self.rect4.x = 43*7
        self.rect4.y = 43

        self.image5 = pygame.image.load('general.jpg')
        self.image5 = pygame.transform.scale(self.image5, (47, 47))
        self.rect5 = self.image5.get_rect()
        self.rect5.x = 43*9
        self.rect5.y = 43

        self.image6 = pygame.image.load('modesty.jpg')
        self.image6 = pygame.transform.scale(self.image6, (47, 47))
        self.rect6 = self.image6.get_rect()
        self.rect6.x = 43*11
        self.rect6.y = 43

        self.image7 = pygame.image.load('joyce.jpg')
        self.image7 = pygame.transform.scale(self.image7, (47, 47))
        self.rect7 = self.image7.get_rect()
        self.rect7.x = 43*13
        self.rect7.y = 43

        self.image8 = pygame.image.load('tolerence.jpg')
        self.image8 = pygame.transform.scale(self.image8, (47, 47))
        self.rect8 = self.image8.get_rect()
        self.rect8.x = 43*15
        self.rect8.y = 43

        self.image9 = pygame.image.load('faithfulness.jpg')
        self.image9 = pygame.transform.scale(self.image9, (47, 47))
        self.rect9 = self.image9.get_rect()
        self.rect9.x = 43*17
        self.rect9.y = 43

        self.image10 = pygame.image.load('turelyness.jpg')
        self.image10 = pygame.transform.scale(self.image10, (47, 47))
        self.rect10 = self.image10.get_rect()
        self.rect10.x = 43*19
        self.rect10.y = 43

        self.image11 = pygame.image.load('beauty.jpg')
        self.image11 = pygame.transform.scale(self.image11, (47, 47))
        self.rect11 = self.image11.get_rect()
        self.rect11.x = 43*21
        self.rect11.y = 43

        self.image12 = pygame.image.load('forever.jpg')
        self.image12 = pygame.transform.scale(self.image12, (47, 47))
        self.rect12 = self.image12.get_rect()
        self.rect12.x = 43*23
        self.rect12.y = 43

        self.image13 = pygame.image.load('versatile.jpg')
        self.image13 = pygame.transform.scale(self.image13, (47, 47))
        self.rect13 = self.image13.get_rect()
        self.rect13.x = 43*25
        self.rect13.y = 43

        self.image14 = pygame.image.load('wisedom.jpg')
        self.image14 = pygame.transform.scale(self.image14, (47, 47))
        self.rect14 = self.image14.get_rect()
        self.rect14.x = 43*27
        self.rect14.y = 43

        self.image15 = pygame.image.load('richness.jpg')
        self.image15 = pygame.transform.scale(self.image15, (47, 47))
        self.rect15 = self.image15.get_rect()
        self.rect15.x = 43*29
        self.rect15.y = 43

        self.image16 = pygame.image.load('control.jpg')
        self.image16 = pygame.transform.scale(self.image16, (47, 47))
        self.rect16 = self.image16.get_rect()
        self.rect16.x = 43*31
        self.rect16.y = 43

        self.image17 = pygame.image.load('forsee.jpg')
        self.image17 = pygame.transform.scale(self.image17, (47, 47))
        self.rect17 = self.image17.get_rect()
        self.rect17.x = 43*33
        self.rect17.y = 43

        self.image18 = pygame.image.load('create.jpg')
        self.image18 = pygame.transform.scale(self.image18, (47, 47))
        self.rect18 = self.image18.get_rect()
        self.rect18.x = 43*35
        self.rect18.y = 43

        self.image19 = pygame.image.load('digitbar.jpg')
        self.image19 = pygame.transform.scale(self.image19, (97, 620))
        self.rect19 = self.image19.get_rect()
        self.rect19.x = 1670
        self.rect19.y = 124

        self.image20 = pygame.image.load('enlove.jpg')
        self.image20 = pygame.transform.scale(self.image20, (47, 47))
        self.rect20 = self.image20.get_rect()
        self.rect20.x = 43
        self.rect20.y = 900 - 43-43

        self.image21 = pygame.image.load('enkindness.jpg')
        self.image21 = pygame.transform.scale(self.image21, (47, 47))
        self.rect21 = self.image21.get_rect()
        self.rect21.x = 43 * 3
        self.rect21.y = 814

        self.image22 = pygame.image.load('enpure.jpg')
        self.image22 = pygame.transform.scale(self.image22, (47, 47))
        self.rect22 = self.image22.get_rect()
        self.rect22.x = 43 * 5
        self.rect22.y = 814

        self.image23 = pygame.image.load('enfairness.jpg')
        self.image23 = pygame.transform.scale(self.image23, (47, 47))
        self.rect23 = self.image23.get_rect()
        self.rect23.x = 43 * 7
        self.rect23.y = 814

        self.image24 = pygame.image.load('engeneral.jpg')
        self.image24 = pygame.transform.scale(self.image24, (47, 47))
        self.rect24 = self.image24.get_rect()
        self.rect24.x = 43 * 9
        self.rect24.y = 814

        self.image25 = pygame.image.load('enmodesty.jpg')
        self.image25 = pygame.transform.scale(self.image25, (47, 47))
        self.rect25 = self.image25.get_rect()
        self.rect25.x = 43 * 11
        self.rect25.y = 814

        self.image26 = pygame.image.load('enjoyce.jpg')
        self.image26 = pygame.transform.scale(self.image26, (47, 47))
        self.rect26 = self.image26.get_rect()
        self.rect26.x = 43 * 13
        self.rect26.y = 814

        self.image27 = pygame.image.load('entolerence.jpg')
        self.image27 = pygame.transform.scale(self.image27, (47, 47))
        self.rect27 = self.image27.get_rect()
        self.rect27.x = 43 * 15
        self.rect27.y = 814

        self.image28 = pygame.image.load('enfaithfulness.jpg')
        self.image28 = pygame.transform.scale(self.image28, (47, 47))
        self.rect28 = self.image28.get_rect()
        self.rect28.x = 43 * 17
        self.rect28.y = 814

        self.image29 = pygame.image.load('enturelyness.jpg')
        self.image29 = pygame.transform.scale(self.image29, (47, 47))
        self.rect29 = self.image29.get_rect()
        self.rect29.x = 43 * 19
        self.rect29.y = 814

        self.image30 = pygame.image.load('enbeauty.jpg')
        self.image30 = pygame.transform.scale(self.image30, (47, 47))
        self.rect30 = self.image30.get_rect()
        self.rect30.x = 43 * 21
        self.rect30.y = 814

        self.image31 = pygame.image.load('enforever.jpg')
        self.image31 = pygame.transform.scale(self.image31, (47, 47))
        self.rect31 = self.image31.get_rect()
        self.rect31.x = 43 * 23
        self.rect31.y = 814

        self.image32 = pygame.image.load('enversatile.jpg')
        self.image32 = pygame.transform.scale(self.image32, (47, 47))
        self.rect32 = self.image32.get_rect()
        self.rect32.x = 43 * 25
        self.rect32.y = 814

        self.image33 = pygame.image.load('enwisedom.jpg')
        self.image33 = pygame.transform.scale(self.image33, (47, 47))
        self.rect33 = self.image33.get_rect()
        self.rect33.x = 43 * 27
        self.rect33.y = 814

        self.image34 = pygame.image.load('enrichness.jpg')
        self.image34 = pygame.transform.scale(self.image34, (47, 47))
        self.rect34 = self.image34.get_rect()
        self.rect34.x = 43 * 29
        self.rect34.y = 814

        self.image35 = pygame.image.load('encontrol.jpg')
        self.image35 = pygame.transform.scale(self.image35, (47, 47))
        self.rect35 = self.image35.get_rect()
        self.rect35.x = 43 * 31
        self.rect35.y = 814

        self.image36 = pygame.image.load('enforsee.jpg')
        self.image36 = pygame.transform.scale(self.image36, (47, 47))
        self.rect36 = self.image36.get_rect()
        self.rect36.x = 43 * 33
        self.rect36.y = 814

        self.image37 = pygame.image.load('encreate.jpg')
        self.image37 = pygame.transform.scale(self.image37, (47, 47))
        self.rect37 = self.image37.get_rect()
        self.rect37.x = 43 * 35
        self.rect37.y = 814

    def drawme(self):
        #self.screen.blit(self.image_copy, (self.x, self.y))
        self.screen.blit(self.image1, self.rect1)
        self.screen.blit(self.image2, self.rect2)
        self.screen.blit(self.image3, self.rect3)
        self.screen.blit(self.image4, self.rect4)
        self.screen.blit(self.image5, self.rect5)
        self.screen.blit(self.image6, self.rect6)
        self.screen.blit(self.image7, self.rect7)
        self.screen.blit(self.image8, self.rect8)
        self.screen.blit(self.image9, self.rect9)
        self.screen.blit(self.image10, self.rect10)
        self.screen.blit(self.image11, self.rect11)
        self.screen.blit(self.image12, self.rect12)
        self.screen.blit(self.image13, self.rect13)
        self.screen.blit(self.image14, self.rect14)
        self.screen.blit(self.image15, self.rect15)
        self.screen.blit(self.image16, self.rect16)
        self.screen.blit(self.image17, self.rect17)
        self.screen.blit(self.image18, self.rect18)
        self.screen.blit(self.image19, self.rect19)
        self.screen.blit(self.image20, self.rect20)
        self.screen.blit(self.image21, self.rect21)
        self.screen.blit(self.image22, self.rect22)
        self.screen.blit(self.image23, self.rect23)
        self.screen.blit(self.image24, self.rect24)
        self.screen.blit(self.image25, self.rect25)
        self.screen.blit(self.image26, self.rect26)
        self.screen.blit(self.image27, self.rect27)
        self.screen.blit(self.image28, self.rect28)
        self.screen.blit(self.image29, self.rect29)
        self.screen.blit(self.image30, self.rect30)
        self.screen.blit(self.image31, self.rect31)
        self.screen.blit(self.image32, self.rect32)
        self.screen.blit(self.image33, self.rect33)
        self.screen.blit(self.image34, self.rect34)
        self.screen.blit(self.image35, self.rect35)
        self.screen.blit(self.image36, self.rect36)
        self.screen.blit(self.image37, self.rect37)



