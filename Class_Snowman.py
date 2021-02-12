# Import a libraries of functions called 'pygame' and 'random'
import pygame as pg
import random as rd

# Initialize the game engine
pg.init()

# All varibals
class All_Varibals:

    def __init__(self):
    
        #Definind the colors we will use in RGB format
        self.color_black = (0, 0, 0)
        self.color_white = (255, 255, 255)
        self.color_gray = (230, 200, 200)
        
        # Size visible window
        self.size_screen = [600, 500]
        
        # Coordinates and dimensions ground
        self.ground = [0, 360, 600, 200]

        # Coordinates and dimensions snowman
        self.size_lower_ball = 80
        self.size_middle_ball = 60
        self.size_ball_head = 40

        self.coord_lower_ball = [300, 400]
        self.coord_middle_ball = [300, 270]
        self.coord_ball_head = [300, 180]

        #Defining other objects
        self.done = False

# Event handling. Closing the window by clicking on the "Close window" button
class Check_Events(All_Varibals):

    def _init__(self):
        pass
    
    # Constantly check for pressing the button to close the window.
    def check_event(self):

        all_var = All_Varibals()
                   
        while not all_var.__init__.done:
            for self.event in pg.event.get():
                if self.event.type == pg.QUIT:
                    all_var.__init__.done = True

        # Number of events per second
        clock = pg.time.Clock()

        clock.tick(20)

# Create  ground space
class Ground():

    def __init__(self):

        pass


    def ground(self):
        
        all_var = All_Varibals()

        self.screen = pg.display.set_mode(all_var.size_screen)

        pg.draw.rect(self.screen, all_var.color_white, all_var.ground)

        
        pg.display.flip()   


# class Snowman(Ground):

    
#     def snowman(self):

#         all_var = All_Varibals()

        


#         pg.draw.circle(pg.display.set_mode(all_var.size_screen), all_var.color_gray, all_var.coord_lower_ball, all_var.size_lower_ball)
#         pg.display.flip() 
#         # pg.draw.circle(pg.display.set_mode(all_var.size_screen), all_var.color_gray, all_var.coord_middle_ball, all_var.size_middle_ball)
        
#         # pg.draw.circle(pg.display.set_mode(all_var.size_screen), all_var.color_gray, all_var.coord_ball_head, all_var.size_ball_head)

#         # pg.display.flip()  

# Creating all space
class  Create_Game_Space(Ground):
   
    # Create a visible space
    def draw_window(self):

        all_var = All_Varibals()

        c_e = Check_Events()

        grd = Ground()

        # s_n = Snowman()

        
        self.screen = pg.display.set_mode(all_var.size_screen)

        pg.display.set_caption("--- My Snowman ---")

        self.screen.fill(all_var.color_black)

        # Create ground
        grd.ground()

        # Fix Mi
        

        # s_n.ground()

        # s_n.snowman()

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
