import turtle
import random
from tqdm import tqdm
from tkinter import * 
from PIL import Image
import os


def eps_to_png(infile, outfile):
    TARGET_BOUNDS = (1024, 1024)
    wd = os.getcwd()
    # Load the EPS at 10 times whatever size Pillow thinks it should be
    # (Experimentaton suggests that scale=1 means 72 DPI but that would
    #  make 600 DPI scale=8⅓ and Pillow requires an integer)
    pic = Image.open(wd + '/' + infile + '.eps')
    pic.load(scale=10)

    # Ensure scaling can anti-alias by converting 1-bit or paletted images
    if pic.mode in ('P', '1'):
        pic = pic.convert("RGB")

    # Calculate the new size, preserving the aspect ratio
    ratio = min(TARGET_BOUNDS[0] / pic.size[0],
                TARGET_BOUNDS[1] / pic.size[1])
    new_size = (int(pic.size[0] * ratio), int(pic.size[1] * ratio))

    # Resize to fit the target size
    pic = pic.resize(new_size, Image.ANTIALIAS)

    # Save to PNG
    pic.save(wd + '/' + outfile + ".png")


def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else chr for chr in axiom])


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom


# turtle.pencolor('white')
# turtle.goto(-WIDTH // 2 + 60, HEIGHT // 2 - 100)
# turtle.clear()
# turtle.write(f'generation: {gens}', font=("Arial", 60, "normal"))

def generate(gens, axiom, thickness, step, angle):
    axiom = get_result(gens, axiom)
    leo.left(90)
    leo.pensize(thickness)
    for chr in tqdm(axiom):
        leo.color(color)
        if chr == 'F' or chr == 'X':
            leo.forward(step)
        elif chr == '@':
            step -= 6
            color[1] += 0.04
            thickness -= 2
            thickness = max(1, thickness)
            leo.pensize(thickness)
        elif chr == '+':
            leo.right(angle)
        elif chr == '-':
            leo.left(angle)
        elif chr == '[':
            angle_, pos_ = leo.heading(), leo.pos()
            stack.append((angle_, pos_, thickness, step, color[1]))
        elif chr == ']':
            angle_, pos_, thickness, step, color[1] = stack.pop()
            leo.pensize(thickness)
            leo.setheading(angle_)
            leo.penup()
            leo.goto(pos_)
            leo.pendown()


if __name__ == "__main__":
    arbre = int(input("Type d'arbre (0, 1 ou 2) : "))
    gens = int(input("Nombre de ramifications : "))
    # screen settings
    WIDTH, HEIGHT = 1.0, 1.0
    screen = turtle.Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    #screen.screensize(WIDTH, HEIGHT)
    screen.delay(0)
    # turtle settings
    leo = turtle.Turtle()
    leo.hideturtle()
    leo.pensize(3)
    leo.speed(0)
    leo.penup()
    leo.setpos(0, -350)
    leo.pendown()
    leo.color('green')
    # l-system settings
    axiom = 'XY'
    rules = ['F[@[-X]+X]', 'F-[@[X]+X]+F@[+FX]-X', 'F[@[+X]F[-@X]+X]']
    
    # 'F@[[+X]-FX]-F@[-FX]+X'
    
    size_thicknes_angle_dic = {
        0 : (85, 20, random.randint(15, 41)),
        1 : (65, 10, random.randint(15, 26)), 
        2 : (75, 10, random.randint(15, 21))
    }
    
    choice = arbre
    chr_1, rule_1 = 'X', rules[choice]
    step = size_thicknes_angle_dic[choice][0]
    #angle = random.randint(0, 40)
    angle = size_thicknes_angle_dic[choice][2]
    stack = []
    color = [0.35, 0.2, 0.0]
    thickness = size_thicknes_angle_dic[choice][1]

    generate(gens, axiom, thickness, step, angle)

    #ts = leo.getscreen()
    #file_img = f"tree{gens}"
    #ts.getcanvas().postscript(file=file_img + ".eps")
    #eps_to_png(file_img, file_img)
    screen.exitonclick()