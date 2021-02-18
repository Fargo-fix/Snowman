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
        self.size_screen = (600, 500)

        # Create a visible space
        self.screen = pg.display.set_mode(self.size_screen)
          
        pg.display.set_caption("--- My Snowman ---")

        self.screen.fill(self.color_black)


# Create  ground space
class Ground(Create_Game_Space):

    def __init__(self):

        Create_Game_Space.__init__(self)
        
        # Definind the colors we will use in RGB format
        self.color_white = (255, 255, 255)

        # Coordinates and dimensions ground
        self.ground = [0, 360, 600, 200]

    def draw(self):

        pg.draw.rect(self.screen, self.color_white, self.ground)
       

class Snowman(Create_Game_Space):

    def __init__(self):

        Create_Game_Space.__init__(self)
        Ground.__init__(self)
        
        #Definind the colors we will use in RGB format
        self.color_gray = (230, 200, 200)
        self.color_red = (209, 25, 25)
        # self.color_green = (0, 255, 0)

        # Coordinates and dimensions body snowman
        self.size_lower_ball = 80 # starting value
        self.size_middle_ball = self.size_lower_ball - 20
        self.size_ball_head = self.size_lower_ball - 40

        self.x = 300
        self.y = 400
        self.coord_lower_ball = [self.x, self.y]
        self.coord_middle_ball = [self.x, self.y - 130]
        self.coord_ball_head = [self.x, self.y - 220]

        # Coordinates and dimensions eyes snowman
        self.size_eyes = self.size_lower_ball - 74

        self.coord_right_eye = [self.x - 15, self.y - 230]
        self.coord_left_eye = [self.x + 15, self.y - 230]

        # Coordinates and dimensions buttons
        self.size_button = self.size_lower_ball - 76

        self.coord_button1 = [self.x, self.y - 20]
        self.coord_button2 = [self.x, self.y - 60]
        self.coord_button3 = [self.x, self.y - 100]
        self.coord_button4 = [self.x, self.y - 140]

        # Coordinates and dimensions nose
        self.size_nose = self.size_lower_ball - 76
        self.coord_nose = [self.x, self.y - 215]
      
        # Coordinates and dimensions mouth

    def draw(self):
        
        Ground.draw(self) 

        # Draw body snowman
        pg.draw.circle(self.screen, self.color_gray, self.coord_lower_ball, self.size_lower_ball)
        pg.draw.circle(self.screen, self.color_gray, self.coord_middle_ball, self.size_middle_ball)
        pg.draw.circle(self.screen, self.color_gray, self.coord_ball_head, self.size_ball_head)

        # Draw eyes
        pg.draw.circle(self.screen, self.color_black, self.coord_right_eye, self.size_eyes)
        pg.draw.circle(self.screen, self.color_black, self.coord_left_eye, self.size_eyes)

        # Draw buttons
        pg.draw.circle(self.screen, self.color_black, self.coord_button1, self.size_button)
        pg.draw.circle(self.screen, self.color_black, self.coord_button2, self.size_button)
        pg.draw.circle(self.screen, self.color_black, self.coord_button3, self.size_button)
        pg.draw.circle(self.screen, self.color_black, self.coord_button4, self.size_button)

        # Draw nose
        pg.draw.circle(self.screen, self.color_red, self.coord_nose, self.size_nose)

        # Draw mouth
        # pg.draw.circle(self.screen, self.color_green, [250, 250], 40, 20)
        # pygame.draw.circle(screen, BLACK, [250, 250], 40, 10, draw_bottom_right=True

class Moon(Create_Game_Space):

    def __init__(self):

        Create_Game_Space.__init__(self)
        Snowman.__init__(self)

        # Coordinates and dimensions snowman
        self.size_moon1 = [500, 60]
        self.size_moon2 = [475, 60]
        self.diameter_moon = 40

        self.color_gray = (230, 200, 200)   

    def draw(self):
                    
        Snowman.draw(self)

        pg.draw.circle(self.screen, self.color_gray, self.size_moon1, self.diameter_moon)
        pg.draw.circle(self.screen, self.color_black, self.size_moon2, self.diameter_moon)


class Snow(Create_Game_Space):   

    def __init__(self):

        Create_Game_Space.__init__(self)
        Moon.__init__(self)

        self.clock = pg.time.Clock()
        self.snow_list = []   
        self.color_white = (255, 255, 255)

        for self.i in range(80):
            self.x = rd.randrange(0, 600)
            self.y = rd.randrange(0, 500)

            self.snow_list.append([self.x, self.y])
    
       
    def draw(self):          
                 
            self.screen.fill(self.color_black)   

            Moon.draw(self)      
                
            for i in range(len(self.snow_list)):

                pg.draw.circle(self.screen, self.color_white, self.snow_list[i], 2)

                self.snow_list[i][1] += 1

                if  self.snow_list[i][1] > 500:
                    self.y = rd.randrange(-50, -10)
                    self.snow_list[i][1] = self.y
                    self.x = rd.randrange(0, 600)
                    self.snow_list[i][0] = self.x

            self.clock.tick(20)
        
                  
class Manager:

    def __init__(self):

        Snow.__init__(self)       
        
        self.done = False  
        

    def launch(self):    

        while not self.done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.done = True

            Snow.draw(self)
            pg.display.flip()
        
run = Manager()
run.launch()
