# Import a libraries of functions called 'pygame' and 'random'
import pygame as pg
import random as rd

# Initialize the game engine
pg.init()

# All varibals
class All_Varibals:
    
    #Definind the colors we will use in RGB format
    color_black = (0, 0, 0)
    size_screen = [600, 500]

    #Defining other objects
    done = False

# Event handling. Closing the window by clicking on the "Close window" button
class Check_Events: 
    
    # Constantly check for pressing the button to close the window.
    def check_event(self):

        all_var = All_Varibals()
                   
        while not all_var.done:
            for self.event in pg.event.get():
                if self.event.type == pg.QUIT:
                    all_var.done = True

        # Number of events per second
        clock = pg.time.Clock()
        clock.tick(20)

# Creating space
class  Create_Game_Space:
   
    # Create a visible space
    def draw_window(self):
        all_var = All_Varibals()
        self.screen = pg.display.set_mode(all_var.size_screen)
        pg.display.set_caption("--- My Snowman ---")
        self.screen.fill(all_var.color_black)

        # Call call event handler. Closing the window by clicking on the "Close window" button
        c_e = Check_Events()
        c_e.check_event()
                
# Launch manager of the whole project
class Manager:

    # Create game space
    c_g_s = Create_Game_Space()
    c_g_s.draw_window()

# Launch whole project
run = Manager()

# Exit the game engine
pg.quit()
