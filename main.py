import turtle
import os
import math
import random
import keyboard


#ОКНО
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.tracer(0)


#Границы квадрата
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#счёт
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))

#персонаж
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.settiltangle(90)


#КОЛИЧЕСВТО ПРОТИВНИКОВ
numbers_of_enemis = 5
enemies = []
#создание
for i in range(numbers_of_enemis):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape('circle')
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)
enemyspeed = 0.1  # СКОРОСТЬ ПРОТИВНИКОВ

#пуля
bullet=turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

#скорость пресонажа и пули
bulletspeed=0.5
bulletstate = "ready"
player_speed = 15

#СКОРОСТЬ ВЛЕВО
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -285:
        x = -285
    player.setx(x)

#СКОРОСТЬ ВПРАВО
def move_right():
    x = player.xcor()
    x += player_speed
    if x > 285:
        x = 285
    player.setx(x)

#ФУНКЦИИ ПУЛИ
def fire():
    global  bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #ПЕРЕМЕЩЕНИЕ ПУЛИ ОТ КООРДИНАТ ИГРОКА
        x=player.xcor()
        y=player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

#СТОЛКНОВЕНИЕ ПУЛИ И ВРАГОВ
def DTP(t1,t2):
    distanse = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distanse<15:
        return  True
    else:
        return False


#УПРАВЛЕНИЕ
#keyboard.read_key()
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire,"space")
turtle.onkey(move_left, "a")
turtle.onkey(move_right, "d")
turtle.onkey(fire,"w")

#turtle.onkey(close_window, "Escape")




#основной цикл
while True:
    t=0
    wn.update()
    for enemy in enemies:
        #ДВИЖЕНИЕ
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)
        #ОГРАНИЧЕНИЕ ВРАГОВ И ПЕРЕМЕЩЕНИЕ ВПЕРЁД
        if enemy.xcor() >280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
        if enemy.xcor() <-280:
            for e in enemies:
                y = e.ycor()
                y-= 40
                e.sety(y)
            enemyspeed *= -1

        if DTP(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # ВОЗРАТ ПРОТИВНИКА
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)

        if DTP(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Игра окончена")
            break

        def close_window(): #Закрытие программы
            turtle.bye()
        screen = turtle.Screen()
        screen.onkey(close_window, "Escape")


    #ДВИЖЕНИЕ ПУЛИ
    if bulletstate == "fire":
        y=bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)

    #ГРАНИЦА ИСЧЕЗНОВЕНИЯ ПУЛИ
    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletstate="ready"




#turtle.Screen().mainloop() оставить на крайний случай