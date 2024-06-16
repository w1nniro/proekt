import turtle
import math
import platform


#ОКНО
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.tracer(0)
wn.bgpic("SI.gif")

turtle.register_shape("protiv.gif")
turtle.register_shape("gamer2.gif")


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
scorestring = "Счёт: {}".format(score)
score_pen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))
score_pen.hideturtle()


#персонаж
player = turtle.Turtle()
player.color("blue")
player.shape("gamer2.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.settiltangle(90)


#КОЛИЧЕСВТО ПРОТИВНИКОВ
numbers_of_enemis = 30
enemies = []
#создание
for i in range(numbers_of_enemis):
    enemies.append(turtle.Turtle())


start_y = 250
nomer = 0


for enemy in enemies:
    enemy.color("red")
    enemy.shape("protiv.gif")
    enemy.penup()
    enemy.speed(0)
    x = -225 + (50*nomer)
    y = start_y
    enemy.setposition(x, y)
    nomer += 1
    if nomer == 10:
        start_y -= 50
        nomer = 0

enemyspeed = 0.25 # СКОРОСТЬ ПРОТИВНИКОВ

#пуля
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

#скорость пресонажа и пули
bulletspeed = 3
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
    global bulletstate
    if bulletstate == "ready":
        play_sound("strel.wav")
        bulletstate = "fire"
        #ПЕРЕМЕЩЕНИЕ ПУЛИ ОТ КООРДИНАТ ИГРОКА
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

#СТОЛКНОВЕНИЕ ПУЛИ И ВРАГОВ
def DTP(t1,t2):
    distanse = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distanse < 15:
        return True
    else:
        return False

def play_sound(file_path):
    if platform.system() == 'Windows':
        import winsound
        winsound.PlaySound(file_path, winsound.SND_ASYNC)



#УПРАВЛЕНИЕ
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire,"space")
wn.onkeypress(move_left, "a")
wn.onkeypress(move_right, "d")
wn.onkeypress(fire,"w")



#основной цикл
while True:
    wn.update()
    for enemy in enemies:
        #ДВИЖЕНИЕ
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)
        #ОГРАНИЧЕНИЕ ВРАГОВ И ПЕРЕМЕЩЕНИЕ ВПЕРЁД
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1


        if DTP(bullet, enemy):
            play_sound("vsriv.wav")
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # ВОЗРАТ ПРОТИВНИКА
            enemy.setposition(0,1000)
            #обновление счёта
            score += 10
            scorestring = "Счёт: {}".format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))

        for enemy in enemies:
            if enemy.ycor() < -270:
                player.hideturtle()
                enemy.hideturtle()
                op = turtle.Turtle()
                op.speed(0)
                op.color('white')
                op.penup()
                op.setposition(-70, 50)
                opte = "Вы проиграли!".format(op)
                op.write(opte, False, align='left', font=('Arial', 18, 'normal'))
                op.hideturtle()
                ty = "Вы проиграли!"

        for enemy in enemies:
            if DTP(player, enemy):
                player.hideturtle()
                enemy.hideturtle()
                op = turtle.Turtle()
                op.speed(0)
                op.color('white')
                op.penup()
                op.setposition(-70, 50)
                opte = "Вы проиграли!".format(op)
                op.write(opte, False, align='left', font=('Arial', 18, 'normal'))
                op.hideturtle()
                ty = "Вы проиграли!"


        if score == 300:
            op = turtle.Turtle()
            op.speed(0)
            op.color('white')
            op.penup()
            op.setposition(-70, 50)
            opte = "Вы победили!".format(op)
            op.write(opte, False, align='left', font=('Arial', 18, 'normal'))
            op.hideturtle()
            ty = "Вы победили!"


        def close_window():
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
        bulletstate = "ready"
