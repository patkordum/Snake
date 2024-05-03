''' This class designs a snake Object'''

class Snake:
    def __init__(self,canvas,body_size,space_size,snake_color):
        self.canvas=canvas
        self.body_size=body_size
        self.space_size=space_size
        self.snake_color=snake_color
        self.coordinates=[]
        self.squares=[]

        for _ in range(0,body_size):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            square=canvas.create_rectangle(x,y,x+self.space_size,y+self.space_size,fill=self.snake_color)
            self.squares.append(square)
            
        

