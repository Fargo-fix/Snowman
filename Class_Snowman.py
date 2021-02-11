# Import a libraries of functions called 'pygame' and 'random'
import pygame as pg
import random as rd

# Initialize the game engine
pg.init()

# All varibals
class All_Varibals:
    
    #Definind the colors we will use in RGB format
    color_black = (0, 0, 0)
    color_white = (255, 255, 255)
    color_gray = (230, 200, 200)
    
    # Size visible window
    size_screen = [600, 500]
    
    # Coordinates and dimensions ground
    ground = [0, 360, 600, 200]

    # Coordinates and dimensions snowman
    size_lower_ball = 80
    size_middle_ball = 60
    size_ball_head = 40

    coord_lower_ball = [300, 400]
    coord_middle_ball = [300, 270]
    coord_ball_head = [300, 180]

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

# Create  ground space
class Ground:

    def ground(self):
        
        all_var = All_Varibals()

        self.screen = pg.display.set_mode(all_var.size_screen)

        pg.draw.rect(self.screen, all_var.color_white, all_var.ground)

        
        pg.display.flip()   


class Snowman(Ground):

    
    def snowman(self):

        all_var = All_Varibals()

        


        pg.draw.circle(pg.display.set_mode(all_var.size_screen), all_var.color_gray, all_var.coord_lower_ball, all_var.size_lower_ball)
        pg.display.flip() 
        # pg.draw.circle(pg.display.set_mode(all_var.size_screen), all_var.color_gray, all_var.coord_middle_ball, all_var.size_middle_ball)
        
        # pg.draw.circle(pg.display.set_mode(all_var.size_screen), all_var.color_gray, all_var.coord_ball_head, all_var.size_ball_head)

        # pg.display.flip()  

# Creating all space
class  Create_Game_Space:
   
    # Create a visible space
    def draw_window(self):

        all_var = All_Varibals()

        c_e = Check_Events()

        # grd = Ground()

        s_n = Snowman()

        
        self.screen = pg.display.set_mode(all_var.size_screen)

        pg.display.set_caption("--- My Snowman ---")

        self.screen.fill(all_var.color_black)

        # Create ground
        # grd.ground()

        # Fix Mi
        

        s_n.ground()

        s_n.snowman()

        # Call call event handler. Closing the window by clicking on the "Close window" button
        c_e.check_event()

# Launch of the whole project
class Launch:

    # Create game space
    c_g_s = Create_Game_Space()

    c_g_s.draw_window()


# Launch whole project
run = Launch()

# Exit the game engine
pg.quit()
