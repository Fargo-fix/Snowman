import pygame as pg
import random as rd

pg.init()



def build_screen():

    color_black = (0, 0, 0)
    color_blue = (0, 0, 255)
    color_white = (255, 255, 255)
    color_gray = (230, 200, 200)


    size_screen = [600, 500]
    screen = pg.display.set_mode(size_screen)

    pg.display.set_caption("--- My Snowman ---")

    

    snow_list = []

    for i in range(50):
        x = rd.randrange(0, 600)
        y = rd.randrange(0, 500)

        snow_list.append([x, y])

    clock = pg.time.Clock()
    done = False

    while not done:


        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        screen.fill(color_black)

        pg.draw.rect(screen, color_white, [0, 360, 600, 200])

        pg.draw.circle(screen, color_gray, [300, 400], 80)
        pg.draw.circle(screen, color_gray, [300, 270], 60)
        pg.draw.circle(screen, color_gray, [300, 180], 40)

        pg.draw.circle(screen, color_gray, [500, 60], 40)
        pg.draw.circle(screen, color_black, [475, 60], 40)


        for i in range(len(snow_list)):
            pg.draw.circle(screen, color_white, snow_list[i], 2)

            snow_list[i][1] += 1

            if snow_list[i][1] > 500:
                y = rd.randrange(-50, -10)
                snow_list[i][1] = y
                x = rd.randrange(0, 600)
                snow_list[i][0] = x

        



        pg.display.flip()
        clock.tick(20)

build_screen()
pg.quit() 