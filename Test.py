# Import a libraries of functions called 'pygame' and 'random'
import pygame as pg
import random as rd

# Initialize the game engine
pg.init()


# Create  ground space
class Ground:

    def __init__(self):
        
        # Create work space
        # Definind the colors work space we will use in RGB format
        self.color_black = (0, 0, 0)

        # Size visible window
        self.width_window = 600
        self.height_window = 500
        self.size_screen = (self.width_window, self.height_window)

        # Create a visible space
        self.screen = pg.display.set_mode(self.size_screen)
        pg.display.set_caption("--- My Snowman ---")
        self.screen.fill(self.color_black)
      
        # Definind the colors ground we will use in RGB format
        self.color_white = (255, 255, 255)

        # Coordinates of the origin of the ground
        self.x = 0
        self.y = 360

        # Dimensions the ground
        self.width = 600
        self.height = 140
        self.ground = (self.x, self.y, self.width, self.height)

    # Draw ground
    def draw_ground(self):

        pg.draw.rect(self.screen, self.color_white, self.ground)
       
# Create Snowman
class Snowman(Ground):

    def __init__(self):

        Ground.__init__(self)
        
        # Definind the colors we will use in RGB format
        self.color_gray = (230, 200, 200)
        self.color_red = (209, 25, 25)
        # self.color_green = (0, 255, 0)

        # Dimensions body snowman
        self.size_lower_ball = 80 # starting value
        self.size_middle_ball = self.size_lower_ball - 20
        self.size_ball_head = self.size_lower_ball - 40

        # Coordinates body snowman
        self.x = 300
        self.y = 400
        self.coord_lower_ball = [self.x, self.y]
        self.coord_middle_ball = [self.x, self.y - 130]
        self.coord_ball_head = [self.x, self.y - 220]

        # Coordinates eyes snowman
        self.coord_right_eye = [self.x - 15, self.y - 230]
        self.coord_left_eye = [self.x + 15, self.y - 230]

        # Dimensions eyes snowman
        self.size_eyes = self.size_lower_ball - 74

        # Coordinates buttons
        self.coord_button1 = [self.x, self.y - 20]
        self.coord_button2 = [self.x, self.y - 60]
        self.coord_button3 = [self.x, self.y - 100]
        self.coord_button4 = [self.x, self.y - 140]

        # Dimensions buttons
        self.size_button = self.size_lower_ball - 76

        # Coordinates nose
        self.coord_nose = [self.x, self.y - 215]

        # Dimensions nose
        self.size_nose = self.size_lower_ball - 76
      
        # Coordinates and dimensions mouth

    # Draw body snowman
    def draw_body(self):
        
        Ground.draw_ground(self) 
        
        pg.draw.circle(self.screen, self.color_gray, self.coord_lower_ball, self.size_lower_ball)
        pg.draw.circle(self.screen, self.color_gray, self.coord_middle_ball, self.size_middle_ball)
        pg.draw.circle(self.screen, self.color_gray, self.coord_ball_head, self.size_ball_head)

    # Draw eyes
    def draw_eyes(self):
        pg.draw.circle(self.screen, self.color_black, self.coord_right_eye, self.size_eyes)
        pg.draw.circle(self.screen, self.color_black, self.coord_left_eye, self.size_eyes)

    # Draw buttons
    def draw_buttons(self):
        pg.draw.circle(self.screen, self.color_black, self.coord_button1, self.size_button)
        pg.draw.circle(self.screen, self.color_black, self.coord_button2, self.size_button)
        pg.draw.circle(self.screen, self.color_black, self.coord_button3, self.size_button)
        pg.draw.circle(self.screen, self.color_black, self.coord_button4, self.size_button)

    # Draw nose
    def draw_nose(self):

        pg.draw.circle(self.screen, self.color_red, self.coord_nose, self.size_nose)

        # Draw mouth
        # pg.draw.circle(self.screen, self.color_green, [250, 250], 40, 20)
        # pygame.draw.circle(screen, BLACK, [250, 250], 40, 10, draw_bottom_right=True

class Moon(Ground):

    def __init__(self):

        Ground.__init__(self)
        Snowman.__init__(self)

        self.color_gray = (230, 200, 200)   

        # Coordinates and dimensions snowman
        self.size_moon1 = [500, 60]
        self.size_moon2 = [475, 60]
        self.diameter_moon = 40
      

    def draw(self):
                    
        Snowman.draw_body(self)
        Snowman.draw_nose(self)
        Snowman.draw_buttons(self)
        Snowman.draw_eyes(self)
        
        pg.draw.circle(self.screen, self.color_gray, self.size_moon1, self.diameter_moon)
        pg.draw.circle(self.screen, self.color_black, self.size_moon2, self.diameter_moon)

class Snow(Ground):   

    def __init__(self):

        Ground.__init__(self)
        Moon.__init__(self)

        self.color_white = (255, 255, 255)

        self.clock = pg.time.Clock()
        self.snow_list = []   
        
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

# Launches all processes
class Manager:

    def __init__(self):
 
        Snow.__init__(self)       
        self.done = False  

    def launch(self):
        # The loop runs until the close button is pressed.
        while not self.done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.done = True

            Snow.draw(self)
            pg.display.flip()
        
run = Manager()
run.launch()

        
                  


