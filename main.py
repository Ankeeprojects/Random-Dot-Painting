import random
import turtle as t
import random as r
import colorgram

def picka_cor():
    return (r.randint(0,255), r.randint(0,255), r.randint(0,255))

tim = t.Turtle()
tim.shape("turtle")
tim.color("green")
tim.pencolor("black")

angulo = 5
dist = 5
tim.pensize(9)
t.colormode(255)
tim.speed(20)

def formas():
    for x in range(3,13):
        cor = picka_cor()
        tim.pencolor(cor)

        angulo = 360 / x
        for _ in range(x):
            tim.forward(100)
            tim.left(angulo)


def linhas_random():
    tim.speed(20)

    for x in range(300):
        tim.pencolor(picka_cor())
        graus = 90 * r.randint(0,3)
        tim.left(graus)
        tim.forward(50)

def spirograph(tamanho):
    quantos = int(360 / tamanho)

    for _ in range(quantos):
        tim.pencolor(picka_cor())
        tim.circle(200)
        tim.left(tamanho)

def get_cores(ficheiro):
    cores_foto = colorgram.extract(ficheiro, 10)
    cores = []

    for i in range(10):
        r = cores_foto[i].rgb[0]
        g = cores_foto[i].rgb[1]
        b = cores_foto[i].rgb[2]
        cores.append((r, g, b))

    return cores

def quadro(linhas, colunas):
    cores = get_cores("painting.jpg")
    tim.penup()
    tim.setx(tim.xcor() - 50 * (colunas / 2))
    tim.sety(tim.ycor() - 50 * (colunas / 2))

    for y in range(linhas):
        for x in range(colunas):
            cor = random.choice(cores)
            tim.color(cor)
            tim.dot(20)
            tim.setx(tim.xcor() + 50)
        tim.sety(tim.ycor() + 50)
        tim.setx(tim.xcor() - 50*colunas)


quadro(10, 10)

screen = t.Screen()
screen.exitonclick()

