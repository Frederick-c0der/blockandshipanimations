import pgzrun
import itertools
import random
block=Actor('block', (50,50))
ship=Actor('ship', (400,300))
WIDTH = 800
e = False
HEIGHT = 600
blockmove=[(50,550), (750,550), (750,50), (50,50)]
blockpos=itertools.cycle(blockmove)
def draw():
    screen.blit('spacebg', (0,0))
    block.draw()
    ship.draw()
def animatethatblock():
    animation=animate(block,"bounce_end",pos = next(blockpos), duration = 3)
clock.schedule_interval(animatethatblock, 5)
def animatethatship():
    ship.target = (random.randint(100,700),random.randint(100,500))
    targetangle = ship.angle_to(ship.target)
    animation=animate(ship, angle=targetangle, duration=1,on_finished=movethatship)
def movethatship():
    animation=animate(ship, "accel_decel", pos=ship.target, duration=3, on_finished=animatethatship)
animatethatship()
pgzrun.go()