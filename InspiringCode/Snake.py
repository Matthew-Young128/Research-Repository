#The Snake game follows several design principles and patterns to create a modular and structured program. The Single Responsibility Principle (SRP) is evident as each function handles a specific aspect of the game logic, such as changing direction, checking boundaries, and updating the game state. The use of functions like change, inside, and move demonstrates modularity, enabling easier maintenance and readability. Additionally, the code leverages the Observer pattern through event-driven programming, where key presses are observed, and corresponding actions are triggered. The Model-View-Controller (MVC) pattern is implicit, separating the game's data (snake, food) and logic (move, inside) from the presentation (Turtle graphics). This separation enhances maintainability and scalability, supporting potential future extensions or modifications. Overall, the Snake game exemplifies sound design principles, fostering readability, maintainability, and extensibility in its codebase.



from turtle import *
from random import randrange
from freegames import square, vector

# Initial positions for food, snake, and movement direction
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    # Check if the snake is out of bounds or collided with itself
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    # Check if the snake has eaten the food
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    # Draw the snake
    for body in snake:
        square(body.x, body.y, 9, 'black')

    # Draw the food
    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

# Setup Turtle window and key bindings
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# Start the game loop
move()
done()

#source code:
#https://github.com/ganeshkavhar/snake-game-in-python-by-ganesh-kavhar/blob/master/snake.py