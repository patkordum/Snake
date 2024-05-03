import tkinter as tk
import Food
import Snake
import time

# Initialising Dimensions of Game 
WIDTH = 500
HEIGHT = 500
SPEED = 10
SPACE_SIZE = 10
BODY_SIZE = 2
SNAKE = "#00FF00"
FOOD = "#FFFFFF"
BACKGROUND = "#000000"

# Global Variables
current_score = 0
direction = "down"

def main():
    # Create Game Window and Canvas
    window = tk.Tk() 
    window.title("Snake Game ")

    # Create Score Label
    score = tk.Label(window,  
              text=f"Points:{current_score}",  
              font=('consolas', 20)) 
    
    score.pack()

    # Create Canvas
    canvas = tk.Canvas(window,bg=BACKGROUND, height=HEIGHT, width=WIDTH)
    canvas.pack()

    # Redraw Canvas 
    window.update() 

    # Update Direction
    window.bind('<Left>',  
            lambda event: change_direction('left')) 
    window.bind('<Right>',  
            lambda event: change_direction('right')) 
    window.bind('<Up>',  
            lambda event: change_direction('up')) 
    window.bind('<Down>',  
            lambda event: change_direction('down')) 

    # Create Snake Object 
    snake=Snake.Snake(canvas,BODY_SIZE,SPACE_SIZE,SNAKE)
   

    # Create Food Object
    food=Food.Food(canvas, WIDTH, HEIGHT,SPACE_SIZE, FOOD)

    # Call next turn function
    next_turn(window,canvas, snake,food)
   
    window.mainloop()

def next_turn(window,canvas,snake,food):
    x,y=snake.coordinates[0]
    if direction == "up": 
        y -= SPACE_SIZE 
    elif direction == "down": 
        y += SPACE_SIZE 
    elif direction == "left": 
        x -= SPACE_SIZE 
    elif direction == "right": 
        x += SPACE_SIZE
    
    snake.coordinates.insert(0,(x,y))
    square=canvas.create_rectangle(x,y,x+ SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE)
    snake.squares.insert(0,square)
    print((food.coordinates[0]//10)*10,x,y)
    if x==(food.coordinates[0]//10)*10 and y == (food.coordinates[0]//10)*10:
        global current_score
        current_score+=1
        
        # delete food  https://www.geeksforgeeks.org/snake-game-using-tkinter-python/
 


    # else delete last square
    del(snake.coordinates[-1])
    canvas.delete(snake.squares[-1])
    del(snake.squares[-1])

    # Wait 0.2 seconds before the update
    time.sleep(0.2)
    window.after(SPEED, next_turn,window,canvas,snake,food)
    
def change_direction(new_direction):
    global direction
    if new_direction=="left" and direction != "right":
        direction="left"
    elif new_direction=="right" and direction != "left":
        direction="right"
    elif new_direction=="up" and direction != "down":
        direction="up"
    elif new_direction=="down" and direction != "up":
        direction="down"   
    
if __name__ == "__main__":
    main()