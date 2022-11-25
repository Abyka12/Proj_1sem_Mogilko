import pgzrun
from pgzero.actor import Actor
from pgzero.game import screen


def draw():
    screen.blit("background.png", (0, 0))
    paddle.draw()
    ball.draw()


def update():
    pass


TITLE = "Arkanoid clone"
WIDTH = 800
HEIGHT = 500

paddle = Actor("paddle.png")
paddle.x = 120
paddle.y = 420

ball = Actor("ball.png")
ball.x = 30
ball.y = 300

pgzrun.go()
