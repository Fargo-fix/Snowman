import pygame as pg
import random as rd


class DrawPostcard:

    def __init__(self):
        self.color_black = (0, 0, 0)
        

    def check_event(self):
        self.clock = pg.time.Clock()
        self.done = False

        while not self.done:
            for self.event in pg.event.get():
                if self.event.type == pg.QUIT:
                    self.done = True
        self.clock.tick(20)

    def draw_window(self):

        self.size_screen = [600, 500]
        self.screen = pg.display.set_mode(self.size_screen)

        pg.display.set_caption("--- My Snowman ---")

        self.screen.fill(self.color_black)



d = DrawPostcard()
d.draw_window()
d.check_event()
