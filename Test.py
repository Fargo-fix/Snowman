# Import a libraries of functions called 'pygame' and 'random'
import pygame as pg
import random as rd

# Initialize the game engine
pg.init()

# All varibals
class All_Varibals:

    def __init__(self):
        pass
    
    #Definind the colors we will use in RGB format
    color_black = (0, 0, 0)
    color_white = (255, 255, 255)
    color_gray = (230, 200, 200)
    
    # Size visible window
    size_screen = [600, 500]
    screen = pg.display.set_mode(size_screen)
    
    # Coordinates and dimensions ground
    ground = [0, 360, 600, 200]

    # Coordinates and dimensions snowman
    size_lower_ball = 80
    size_middle_ball = 60
    size_ball_head = 40

    coord_lower_ball = [300, 400]
    coord_middle_ball = [300, 270]
    coord_ball_head = [300, 180]

    # Coordinates and dimensions snowman
    size_moon1 = [500, 60]
    size_moon2 = [475, 60]
    diameter_moon = 40

    #Defining other objects
    done = False

class  Create_Game_Space(All_Varibals):
    
    def __init__(self):
        pass

    # Create a visible space
    def draw_window(self):
        
        
        screen = pg.display.set_mode(All_Varibals.size_screen)

        pg.display.set_caption("--- My Snowman ---")

        screen.fill(All_Varibals.color_black)


# Event handling. Closing the window by clicking on the "Close window" button
class Check_Events(All_Varibals):

    def _init__(self):
        pass
    

    # Constantly check for pressing the button to close the window.
    def check_event(self):

        self.clock = pg.time.Clock()
                           
        
        while not All_Varibals.done:
            for self.event in pg.event.get():
                if self.event.type == pg.QUIT:
                    All_Varibals.done = True        

            # Number of events per second
            self.clock.tick(20)


# Create  ground space
class Ground(All_Varibals):

    def __init__(self):

        pass


    def draw(self):
        
                
        pg.draw.rect(All_Varibals.screen, All_Varibals.color_white, All_Varibals.ground)


       


class Snowman(All_Varibals):

    def __init__(self):
        pass
    

    def draw(self):
       
        pg.draw.circle(All_Varibals.screen, All_Varibals.color_gray, All_Varibals.coord_lower_ball, All_Varibals.size_lower_ball)
        
        pg.draw.circle(All_Varibals.screen, All_Varibals.color_gray, All_Varibals.coord_middle_ball, All_Varibals.size_middle_ball)
        
        pg.draw.circle(All_Varibals.screen, All_Varibals.color_gray, All_Varibals.coord_ball_head, All_Varibals.size_ball_head)


class Moon(All_Varibals):

    def __init__(self):
        pass

    def draw(self):
        pg.draw.circle(All_Varibals.screen, All_Varibals.color_gray, All_Varibals.size_moon1, All_Varibals.diameter_moon)
        pg.draw.circle(All_Varibals.screen, All_Varibals.color_black, All_Varibals.size_moon2, All_Varibals.diameter_moon)


class Snow(Ground, Moon, Snowman, All_Varibals):

    def __init__(self):
        pass

    def draw(self):
        
        
        self.clock = pg.time.Clock()
        self.snow_list = []            
        

        for self.i in range(50):
            self.x = rd.randrange(0, 600)
            self.y = rd.randrange(0, 500)

            self.snow_list.append([self.x, self.y])

        

        while not All_Varibals.done:
            for self.event in pg.event.get():
                if self.event.type == pg.QUIT:
                    All_Varibals.done = True 
                     
            

            All_Varibals.screen.fill(All_Varibals.color_black)

            g = Ground()
            g.draw()

            s = Snowman()
            s.draw()

            m = Moon()
            m.draw()        

            for self.i in range(len(self.snow_list)):

                pg.draw.circle(All_Varibals.screen, All_Varibals.color_white, self.snow_list[self.i], 2)

                self.snow_list[self.i][1] += 1

                if  self.snow_list[self.i][1] > 500:
                    self.y = rd.randrange(-50, -10)
                    self.snow_list[self.i][1] = self.y
                    self.x = rd.randrange(0, 600)
                    self.snow_list[self.i][0] = self.x

            pg.display.flip()
        
        

        # Number of events per second
        # clock = pg.time.Clock()
        
            self.clock.tick(20)

        
class Manager(Snow):      

    def launch(self):
        win = Create_Game_Space()
        # c_e = Check_Events()
        grd = Ground()
        sn = Snowman()
        mn = Moon()
        snow = Snow()


        win.draw_window()
       
        grd.draw()
        sn.draw()
        mn.draw()
        snow.draw()
        pg.display.flip()  
        
        
        
        # c_e.check_event()
        
        

run = Manager()
run.launch()
