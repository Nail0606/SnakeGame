import turtle
import random
import time
import tkinter
#
t = time
w = 700
h = 700
food1 = {'position':(),'size':10}
#trap1 = {'position':(),'size':10}
delay = 100
countingTen = t.time()
gameOver = False

def reset():
    global snake,snake2, snake_dir, snake2_dir, food1, pen,pen2, food1,delay,countingTen,startTime,gameOver
    delay = 100
    countingTen = t.time()
    startTime = t.time()
    gameOver = False
    snake = [[0,-20,'up'],[0, 0,'up']]
    snake2 = [[-40,-20,'up'],[-40, 0,'up'], [-40, 20,'up']]

    snake2_dir = "up"
    snake_dir = "up"
    
    food1['position'] = get_random_position(food1['size'])
    #trap1['position'] = get_random_position(trap1['size'])
    food.goto(food1['position'])
    #trap.goto(trap1['position'])
    move_snake()
    move_snake2()

#RED
def move_snake():
    
    global snake_dir, snake2_dir, score, delay, countingTen,gameOver

    if gameOver:
        return
    
    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_dir][0]
    new_head[1] = snake[-1][1] + offsets[snake_dir][1]
    new_head[2] = snake_dir
    
    if headInSnakeCheck(snake2, new_head[0:2]):
            gameOverfunc('BLUE')
            return
    if headInSnakeCheck(snake, new_head[0:2]):
            print('생존시간:%.2f'%(surviveTime()))
            gameOverfunc('BLUE')
            return
    else:
        snake.append(new_head)

     
        if not food_collision(snake): #부딪치지 않았다면 
            snake.pop(0)
        
        #if trap_collision(): #부딪쳤다면
        #    pen.color('red')
        #    for _ in range(int(len(snake) / 2)):
        #       snake.pop(0)
            
        if snake[-1][0] > w / 2:
            snake[-1][0] -= w
        elif snake[-1][0] < - w / 2:
            snake[-1][0] += w
        elif snake[-1][1] > h / 2:
            snake[-1][1] -= h
        elif snake[-1][1] < -h / 2:
            snake[-1][1] += h
 
 
        pen.clearstamps()
        
         
        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.setheading(heading[segment[2]])
            pen.stamp()
        
        displayScore.clear()
        displayScore.goto(-w/2+10,h/2-20)
        displayScore.write("SCORE:"+str(len(snake)))
         
        screen.update()

        #속도 증가
        #pen.color('black')
        #if t.time() - countingTen > 10 and delay > 40:
        #    delay -= 5
        #    countingTen = t.time()
        #    pen.color('orange')
        
        turtle.ontimer(move_snake, delay)

#blue
def move_snake2():
    
    global snake2_dir, score, delay, countingTen,gameOver

    if gameOver:
        return

    new_head2 = snake[-1].copy()
    new_head2[0] = snake2[-1][0] + offsets[snake2_dir][0]
    new_head2[1] = snake2[-1][1] + offsets[snake2_dir][1]
    new_head2[2] = snake2_dir
    
    if headInSnakeCheck(snake2, new_head2[0:2]):
        gameOverfunc('RED')
        return
    if headInSnakeCheck(snake, new_head2[0:2]):
        print('생존시간:%.2f'%(surviveTime()))
        gameOverfunc('RED')
        return
    else:
        snake2.append(new_head2)

 
     
        if not food_collision(snake2): #부딪치지 않았다면 
            snake2.pop(0)
        
        #if trap_collision(): #부딪쳤다면
        #    pen.color('red')
        #    for _ in range(int(len(snake) / 2)):
        #       snake.pop(0)
            
        if snake2[-1][0] > w / 2:
            snake2[-1][0] -= w
        elif snake2[-1][0] < - w / 2:
            snake2[-1][0] += w
        elif snake2[-1][1] > h / 2:
            snake2[-1][1] -= h
        elif snake2[-1][1] < -h / 2:
            snake2[-1][1] += h
 
         
        pen2.clearstamps()
        
         
        for segment in snake2:
            pen2.goto(segment[0], segment[1])
            pen2.setheading(heading[segment[2]])
            pen2.stamp()
         
        screen.update()

        #속도 증가
        #pen.color('black')
        #if t.time() - countingTen > 10 and delay > 40:
        #    delay -= 5
        #    countingTen = t.time()
        #    pen.color('orange')
        
        turtle.ontimer(move_snake2, delay)

def headInSnakeCheck(snake, head):
    for part in snake:
        if head == part[:2]:
            return True
    return False

def gameOverfunc(player):
    global gameOver
    
    displayScore.clear()
    displayScore.goto(-w/3,0)
    displayScore.write(player+"WIN",font=("Arial", 20))
    gameOver = True

def food_collision(snake):
    global food1, trap1
    if get_distance(snake[-1][0:2], food1['position']) < 20:
        food_goto_random()
        #trap_goto_random()

        #food 몸통위에 스폰시 재 배치
        for _ in range(100):
            iscollision = False
            for snakePart in snake[:-1]:
                if get_distance(snakePart[0:2], food1['position']) < 20:
                    print('ON')
                    food_goto_random()
                    iscollision = True
            if not iscollision:
                break
             
        return True
    return False

def food_goto_random():
    global food1
    food1['position'] = get_random_position(food1['size'])
    food.goto(food1['position'])
    

#def trap_goto_random():
#    global trap1
#    trap1['position'] = get_random_position(trap1['size'])
#    trap.goto(trap1['position'])
#
#def trap_collision():
#    global trap1
#    if get_distance(snake[-1], trap1['position']) < 20:
#        trap1['position'] = get_random_position(trap1['size'])
#        trap.goto(trap1['position'])
#        return True
#    return False

def get_random_position(size):
    x = random.randint(- w / 2 + size, w / 2 - size)
    y = random.randint(- h / 2 + size, h / 2 - size)
    return (x, y)

 
def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def go_up():
    global snake_dir
    if snake_dir != "down":
        snake_dir = "up"
 
def go_right():
    global snake_dir
    if snake_dir != "left":
        snake_dir = "right"
 
def go_down():
    global snake_dir
    if snake_dir!= "up":
        snake_dir = "down"
 
def go_left():
    global snake_dir
    if snake_dir != "right":
        snake_dir = "left"
        
def go_up_2p():
    global snake2_dir
    if snake2_dir != "down":
        snake2_dir = "up"
 
def go_right_2p():
    global snake2_dir
    if snake2_dir != "left":
        snake2_dir = "right"
 
def go_down_2p():
    global snake2_dir
    if snake2_dir!= "up":
        snake2_dir = "down"
 
def go_left_2p():
    global snake2_dir
    if snake2_dir != "right":
        snake2_dir = "left"

def onEsc():
    print(gameOver)
    if gameOver:    
        reset()

def onF1():
    turtle.bye()
    print('다른모듈 실행')
    
def surviveTime():
    return t.time() - startTime

def start():
    global w, h, food_size, delay, startTime, score, offsets,heading
    

    offsets = {
        "up": (0, 20),
        "down": (0, -20),
        "left": (-20, 0),
        "right": (20, 0)
    }
    heading = {
        "up": 90,
        "down": 270,
        "left": 180,
        "right": 0
    }
    global screen
    screen = turtle.Screen()
    screen.setup(w, h)
    screen.title("Snake EASY")
    screen.bgcolor("green")
    screen.setup(w, h)
    screen.tracer(0)

    global displayScore
    displayScore = turtle.Turtle()
    displayScore.color('white')
    displayScore.hideturtle()
    displayScore.penup()
    displayScore.goto(-w/2+10,h/2-20)
    
    global pen
    pen = turtle.Turtle("triangle")
    pen.color('red')
    pen.penup() 

    global pen2
    pen2 = turtle.Turtle("turtle")
    pen2.color('blue')
    pen2.penup() 
    
    global food
    food = turtle.Turtle()
    food.shape("square")
    food.color("yellow")
    food.shapesize(food1['size'] / 20)
    food.penup()

    #global trap
    #trap = turtle.Turtle()
    #trap.color('red')
    #trap.shape('triangle')
    #trap.shapesize(trap1['size'] / 20)
    #trap.penup()
    
    screen.listen()
    screen.onkey(go_up, "Up")
    screen.onkey(go_right, "Right")
    screen.onkey(go_down, "Down")
    screen.onkey(go_left, "Left")
    screen.onkey(key="Escape", fun = onEsc)
    screen.onkey(key="F1", fun = onF1)
    #2p
    screen.onkey(go_up_2p, "w")
    screen.onkey(go_right_2p, "d")
    screen.onkey(go_down_2p, "s")
    screen.onkey(go_left_2p, "a")
    screen.onkey(go_up_2p, "W")
    screen.onkey(go_right_2p, "D")
    screen.onkey(go_down_2p, "S")
    screen.onkey(go_left_2p, "A")
    
    startTime = t.time()
    
    reset()
    turtle.done()
    

if __name__ == "__main__":
    start()
