import turtle
import time
import random

# Configuración de la pantalla
window = turtle.Screen()
window.title("Juego de la Serpiente")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)  

# Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()

# Comida de la serpiente
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

# Funciones de movimiento
def arriba():
    if cabeza.direction != "down":
        cabeza.direction = "up"

def abajo():
    if cabeza.direction != "up":
        cabeza.direction = "down"

def izquierda():
    if cabeza.direction != "right":
        cabeza.direction = "left"

def derecha():
    if cabeza.direction != "left":
        cabeza.direction = "right"

def mover():
    if cabeza.direction == "up":
        y = cabeza.ycor() + 20
        cabeza.sety(y)
    if cabeza.direction == "down":
        y = cabeza.ycor() - 20
        cabeza.sety(y)
    if cabeza.direction == "left":
        x = cabeza.xcor() - 20
        cabeza.setx(x)
    if cabeza.direction == "right":
        x = cabeza.xcor() + 20
        cabeza.setx(x)

# Teclado
window.listen()
window.onkeypress(arriba, "w")
window.onkeypress(abajo, "s")
window.onkeypress(izquierda, "a")
window.onkeypress(derecha, "d")


# Bucle principal del juego
while True:
    window.update()

    # Movimiento de la serpiente
    mover()

    # Verificar colisiones con los bordes
    if (
        cabeza.xcor() > 290
        or cabeza.xcor() < -290
        or cabeza.ycor() > 290
        or cabeza.ycor() < -290
    ):
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"

    # Verificar colisión con la comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        comida.goto(x, y)

    time.sleep(0.1)

window.mainloop()
