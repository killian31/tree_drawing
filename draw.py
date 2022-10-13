from turtle import *
import random
import numpy as np
from tqdm import tqdm


def initialize_color(level):
    if level > 1:
        pencolor(random.randint(0, 256)//level, random.randint(0, 256)//level, random.randint(0, 256)//level)

def y(level, angle, pbar, sz=150):
    pbar.update(1)
    if level > 0:
        colormode(255)
        
        # splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level
        pencolor(0, 255//level, 0)
        initialize_color(level)
        # drawing the base
        fd(sz)

        rt(angle)

        # recursive call for
        # the right subtree
        y(level = level - 1, angle = angle, pbar=pbar, sz = 0.8 * sz)
        
        pencolor(0, 255//level, 0)
        initialize_color(level)
        lt( 2 * angle )

        # recursive call for
        # the left subtree
        y(level = level - 1, angle = angle, pbar=pbar, sz = 0.8 * sz)
        
        pencolor(0, 255//level, 0)
        
        rt(angle)
        fd(-sz)

def nb_of_lines(level):
    return 2**(level+1) - 1

def time_to_complete(level):
    """
    :return the time to complete a tree in seconds:
    """
    lines = nb_of_lines(level)
    return lines/4

def get_diff_times():
    times = [time_to_complete(lvl) for lvl in range(11, 15)]
    print("Choose a time between these :")
    for time in times:
        print(f"{int(time/60)} min")

def time_to_level(tps):
    """
    :tps: time in minutes 
    """
    lines = 4*tps*60
    level = int(np.log(lines + 1)/np.log(2) - 1)
    return level

def main():
    get_diff_times()
    user_time = int(input("Desired size : "))
    lvl = time_to_level(user_time)
    lines = nb_of_lines(lvl)
    print(f"\nDrawing with {lvl} levels of depth.\n")
    pbar = tqdm(range(1, lines+1))
    hideturtle()
    pensize(width=3)
    colormode(255)
    pencolor(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
    screen = Screen()
    screen.setup(width = 1.0, height = 1.0)
    speed(0.8)
    # turning the turtle to face upwards
    rt(90)
    penup()
    fd(300)
    pendown()
    rt(-180)
    # the acute angle between the base and branch of the Y
    angle = random.randint(15, 65)
    y(level = lvl, angle = angle, pbar = pbar)
    
    done()

if __name__ == '__main__':
    main()
    
