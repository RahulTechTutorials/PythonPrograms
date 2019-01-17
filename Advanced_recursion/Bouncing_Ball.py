from visual import *
ground = box(size = (10,0.1,10), color = color.white, material = material.wood)
ball = sphere(pos = (0,4,0), radius = 1 , color = color.yellow)
scene.center = vector(0,5,5)
velocity = 10
e = 0.9
dt = 0.01
while True:
    rate(300)
    prevPos = ball.y
    ball.y += velocity * dt
    if ball.y < ball.radius:
        velocity = -velocity * e
        ball.y = ball.radius
    if (prevPos - ball.y) == 0:
        break
    velocity = velocity - 9.81 * dt
