import tkinter as tk
from Food import Food
from Snake import Snake

# Initialising Dimensions of Game 
WIDTH = 500
HEIGHT = 500
SPEED = 100
SPACE_SIZE = 20
BODY_SIZE = 2
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FFFFFF"
BACKGROUND_COLOR = "#000000"

# Global Variables
current_score = 0
direction = "down"

def main():
    """Main function to start the game."""
    window = tk.Tk()
    window.title("Snake Game")

    # Create Score Label
    score = tk.Label(window, text=f"Points: {current_score}", font=('consolas', 20))
    score.pack()

    # Create Canvas
    canvas = tk.Canvas(window, bg=BACKGROUND_COLOR, height=HEIGHT, width=WIDTH)
    canvas.pack()

    # Redraw Canvas 
    window.update()

    # Update Direction
    window.bind('<Left>', lambda event: change_direction('left'))
    window.bind('<Right>', lambda event: change_direction('right'))
    window.bind('<Up>', lambda event: change_direction('up'))
    window.bind('<Down>', lambda event: change_direction('down'))

    # Create Snake Object 
    snake = Snake(canvas, BODY_SIZE, SPACE_SIZE, SNAKE_COLOR)

    # Create Food Object
    food = Food(canvas, WIDTH, HEIGHT, SPACE_SIZE, FOOD_COLOR)

    # Call next turn function
    next_turn(window, canvas, snake, food, score)
   
    window.mainloop()

def next_turn(window, canvas, snake, food, score):
    """Function to update the game state in each turn."""
    global direction
    x, y = snake.coordinates[0]

    if direction == "up": 
        y -= SPACE_SIZE 
    elif direction == "down": 
        y += SPACE_SIZE 
    elif direction == "left": 
        x -= SPACE_SIZE 
    elif direction == "right": 
        x += SPACE_SIZE
        
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if abs(x - food.coordinates[0]) <= 20 and abs(y - food.coordinates[1]) <= 20:
        global current_score
        current_score += 1

        # Set Score Label
        score.config(text=f"Points: {current_score}") 
        canvas.delete("food")
        food = Food(canvas, WIDTH, HEIGHT, SPACE_SIZE, FOOD_COLOR)

    else:
        # delete last square
        del(snake.coordinates[-1])
        canvas.delete(snake.squares[-1])
        del(snake.squares[-1])

    # Check Collision
    if collision(snake.coordinates):
        game_over(canvas, window, score)
    else:
        # Update Window
        window.after(SPEED, next_turn, window, canvas, snake, food, score)

def collision(snake_coordinates):
    """Function to check if the snake collides with itself or the boundaries."""
    x, y = snake_coordinates[0] 

    # Check if snake head collides with part of snake
    for part in snake_coordinates[1:]:
        if x == part[0] and y == part[1]:
            return True

    if x > WIDTH or x < 0 or y < 0 or y > HEIGHT:
        return True
    else:
        return False

def game_over(canvas, window, score):
    """Function to handle game over scenario."""
    canvas.delete("all")
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover") 
    
    restart_button = tk.Button(window, text="Restart", font=('consolas', 20), command=lambda: restart_game(canvas, restart_button, score, window))
    restart_button.pack()

def restart_game(canvas, restart_button, score, window):
    """Function to restart the game."""
    canvas.delete("all")
    restart_button.destroy()

    # Reset global variables
    global current_score, direction
    current_score = 0
    direction = "down"
    score.config(text=f"Points: {current_score}")

    # Create new Snake and Food objects
    snake = Snake(canvas, BODY_SIZE, SPACE_SIZE, SNAKE_COLOR)
    food = Food(canvas, WIDTH, HEIGHT, SPACE_SIZE, FOOD_COLOR)

    # Call next_turn function with fresh start
    next_turn(window, canvas, snake, food, score) 

def change_direction(new_direction):
    """Function to change the direction of the snake."""
    global direction

    if new_direction == "left" and direction != "right":
        direction = "left"
    elif new_direction == "right" and direction != "left":
        direction = "right"
    elif new_direction == "up" and direction != "down":
        direction = "up"
    elif new_direction == "down" and direction != "up":
        direction = "down"   
    
if __name__ == "__main__":
    main()
