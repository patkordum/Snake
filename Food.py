import random

''' This class implements the "food" for the snake - yellow rectangles at random positions'''

class Food:
    def __init__(self, canvas, screen_width, screen_height, space_size,food_color):
        self.canvas=canvas
        self.space_size=space_size
        self.food_color=food_color
        self.screen_width=screen_width
        self.screen_height=screen_height

        x=random.randint(20,screen_width-20)
        y=random.randint(20,screen_height-20)

        self.coordinates=[x,y]

        canvas.create_oval(x,y,x+space_size,y+space_size,fill=food_color)
