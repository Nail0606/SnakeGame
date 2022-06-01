import turtle
import random
import time
import tkinter

t = time
w = 700
h = 700
food1 = {'position':(),'size':10}
trap1 = {'position':(),'size':10}
delay = 100
countingTen = t.time()
gameOver = False
maxLife = 5
life = maxLife


def reset():
    global snake, snake_dir, food1, pen, food1,delay,countingTen,startTime,gameOver
    delay = 100
    countingTen = t.time()
    startTime = t.time()
    gameOver = False
    snake = [[0,-20,'up'],[0, 0,'up']]
    snake_dir = "up"
    food1['position'] = get_random_position(food1['size'])
    trap1['position'] = get_random_position(trap1['size'])
    food.goto(food1['position'])
    trap.goto(trap1['position'])
    move_snake()



def move_snake():
    
    global snake_dir, score, delay, countingTen,gameOver, maxLife, life
 
    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_dir][0]
    new_head[1] = snake[-1][1] + offsets[snake_dir][1]
    new_head[2] = snake_dir
 
     
    if headInSnakeCheck(snake, new_head[:2]) or life <= 0:
        #reset()
        print('생존시간:%.2f'%(surviveTime()))
        displayScore.clear()
        displayScore.goto(-w/3,0)
        displayScore.write('''뱀의 길이:%d
생존시간:%.2f초\n
다시하기: ESC
랭킹저장: F1'''%(len(snake),surviveTime()),
                            font=("Arial", 20))
        gameOver = True
        return
    else:
        
        snake.append(new_head)
 
     
        if not food_collision(): #부딪치지 않았다면 
            snake.pop(0)
        
        if trap_collision(): #부딪쳤다면
            pen.color('red')
            life -= 1
            for _ in range(int(len(snake) / 2)):
                snake.pop(0)
            
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
        displayScore.goto(-w/2+10,h/2-40)
        displayScore.write("SCORE:"+str(len(snake))+
                        " \nLIFE:"+str(life)+"/"+str(maxLife))
         
        screen.update()

        #속도 증가
        pen.color('black')
        if t.time() - countingTen > 10 and delay > 40:
            delay -= 5
            countingTen = t.time()
            pen.color('orange')
        
        turtle.ontimer(move_snake, delay)
        
def headInSnakeCheck(snake, head):
    for part in snake:
        if head == part[:2]:
            return True
    return False

def food_collision():
    global food1, trap1
    if get_distance(snake[-1][0:2], food1['position']) < 20:
        food_goto_random()
        trap_goto_random()
        
        #trap food 겹치면 trap 재배치
        for _ in range(100):
            dis = get_distance(trap1['position'],food1['position'])
            if int(dis) < 30: 
                trap_goto_random()
            else:      
                break;
        
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
    

def trap_goto_random():
    global trap1
    trap1['position'] = get_random_position(trap1['size'])
    trap.goto(trap1['position'])

def trap_collision():
    global trap1
    if get_distance(snake[-1][0:2], trap1['position']) < 20:
        trap1['position'] = get_random_position(trap1['size'])
        trap.goto(trap1['position'])
        return True
    return False

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
        
    
    
def onEsc():
    print(gameOver)
    if gameOver:    
        reset()

def onF1():
    if gameOver:
        turtle.bye()
        print('다른모듈 실행')
    
def surviveTime():
    return t.time() - startTime

def start():
    global w, h, food_size, delay, startTime, score, offsets, heading
    

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
    screen.title("Snake HARD")
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
    pen = turtle.Turtle("turtle")
    pen.setheading(0)
    pen.penup() 
     
    
    global food
    food = turtle.Turtle()
    food.shape("square")
    food.color("yellow")
    food.shapesize(food1['size'] / 20)
    food.penup()

    global trap
    trap = turtle.Turtle()
    trap.color('red')
    trap.shape('triangle')
    trap.shapesize(trap1['size'] / 20)
    trap.penup()
    
    screen.listen()
    screen.onkey(go_up, "Up")
    screen.onkey(go_right, "Right")
    screen.onkey(go_down, "Down")
    screen.onkey(go_left, "Left")
    screen.onkey(key="Escape", fun = onEsc)
    screen.onkey(key="F1", fun = onF1)
    
    startTime = t.time()
    
    reset()
    turtle.done()
    

if __name__ == "__main__":
    start()
