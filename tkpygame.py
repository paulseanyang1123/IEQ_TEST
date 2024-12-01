import tkinter as tk
import pygame


class TkPygame:
    def __init__(self):
        self.tk_root = tk.Tk()

        self.make_tk_widgets()

        self.tk_root.mainloop()

    def make_tk_widgets(self):
        btn = tk.Button(self.tk_root, text='Start', command=self.toggle_to_pygame)
        btn.pack()

    def toggle_to_pygame(self):
        #self.tk_root.withdraw()
        self.make_pygame_window()

    def make_pygame_window(self):
        pygame_root = pygame.display.set_mode((500, 500))
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame_root.fill((255, 255, 255))
            pygame.display.update()
        pygame.quit()


TkPygame()