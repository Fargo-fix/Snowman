# Import a libraries of functions called 'pygame' and 'random'
import pygame as pg
import random as rd

# Initialize the game engine
pg.init()


class  Create_Game_Space:
    
    def __init__(self):

        #Definind the colors we will use in RGB format
        self.color_black = (0, 0, 0)

        # Size visible window
        self.size_screen = [600, 500]

        # Create a visible space
        self.screen = pg.display.set_mode(self.size_screen)
          
        pg.display.set_caption("--- My Snowman ---")

        self.screen.fill(self.color_black)


# Create  ground space
class Ground(Create_Game_Space):

    def __init__(self):
        
        # Definind the colors we will use in RGB format
        self.color_white = (255, 255, 255)

        # Coordinates and dimensions ground
        self.ground = [0, 360, 600, 200]

    def draw(self):

        Create_Game_Space.__init__(self)

        pg.draw.rect(self.screen, self.color_white, self.ground)
       

class Snowman(Ground, Create_Game_Space):

    def __init__(self):
        
        #Definind the colors we will use in RGB format
        self.color_gray = (230, 200, 200)

        # Coordinates and dimensions snowman
        self.size_lower_ball = 80
        self.size_middle_ball = 60
        self.size_ball_head = 40

        self.coord_lower_ball = [300, 400]
        self.coord_middle_ball = [300, 270]
        self.coord_ball_head = [300, 180]
    

    def draw(self):

        Create_Game_Space.__init__(self)
        Ground.__init__(self)

        Ground.draw(self)
       
        pg.draw.circle(self.screen, self.color_gray, self.coord_lower_ball, self.size_lower_ball)
        
        pg.draw.circle(self.screen, self.color_gray, self.coord_middle_ball, self.size_middle_ball)
        
        pg.draw.circle(self.screen, self.color_gray, self.coord_ball_head, self.size_ball_head)


class Moon(Snowman, Create_Game_Space):

    def __init__(self):

        # #Definind the colors we will use in RGB format
        # self.color_gray = (230, 200, 200)

        # Coordinates and dimensions snowman
        self.size_moon1 = [500, 60]
        self.size_moon2 = [475, 60]
        self.diameter_moon = 40

    def draw(self):

        Create_Game_Space.__init__(self)
        Snowman.__init__(self)
            
        
        Snowman.draw(self)


        pg.draw.circle(self.screen, self.color_gray, self.size_moon1, self.diameter_moon)
        pg.draw.circle(self.screen, self.color_black, self.size_moon2, self.diameter_moon)


# # Event handling. Closing the window by clicking on the "Close window" button
# class Check_Events:

#     def __init__(self):

#         self.done = False

#         self.clock = pg.time.Clock()
    
    # Constantly check for pressing the button to close the window.
    # def check_event(self):
       

    # # while not self.done:
    #     for self.event in pg.event.get():
    #         if self.event.type == pg.QUIT:
    #             self.done = True        

    #         # Number of events per second
    #         self.clock.tick(20)



class Snow(Create_Game_Space):

    def __init__(self):

        self.clock = pg.time.Clock()
        self.snow_list = []   
        self.color_white = (255, 255, 255)

        self.done = False
       
    def draw(self):

        Create_Game_Space.__init__(self)
        Ground.__init__(self)  
        Snowman.__init__(self)
        Moon.__init__(self)   

               

        for self.i in range(80):
            self.x = rd.randrange(0, 600)
            self.y = rd.randrange(0, 500)

            self.snow_list.append([self.x, self.y])


        while not self.done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.done = True
            
            self.screen.fill(self.color_black)
            

            Ground.draw(self)
            Snowman.draw(self)
            Moon.draw(self)     
                

            for self.i in range(len(self.snow_list)):

                pg.draw.circle(self.screen, self.color_white, self.snow_list[self.i], 2)

                self.snow_list[self.i][1] += 1

                if  self.snow_list[self.i][1] > 500:
                    self.y = rd.randrange(-50, -10)
                    self.snow_list[self.i][1] = self.y
                    self.x = rd.randrange(0, 600)
                    self.snow_list[self.i][0] = self.x

            pg.display.flip()
            
            self.clock.tick(20)
        
                  
class Manager:      

    def launch(self):      

        # self.win = Create_Game_Space()
        # self.grd = Ground()
        # self.sn = Snowman()
        # self.mn = Moon()
        self.snow = Snow()


        # self.win.__init__()
        # self.grd.draw()
        # self.sn.draw()
        # self.mn.draw()
        self.snow.draw()
        
        
run = Manager()
run.launch()
