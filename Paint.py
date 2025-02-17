import webcolors
import tkinter as tk
from tkinter import colorchooser
import turtle
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
turtle.onscreenclick(turtle.goto)
root = tk.Tk()
root.title('Toolbox')
root.geometry('500x500')
print("""
  _____        _____ _   _ _______ 
 |  __ \ /\   |_   _| \ | |__   __|
 | |__) /  \    | | |  \| |  | |   
 |  ___/ /\ \   | | | . ` |  | |   
 | |  / ____ \ _| |_| |\  |  | |   
 |_| /_/    \_\_____|_| \_|  |_|

----------------------------------

Paint Action Logs:
""")
# Color Functions
def r():
    turtle.color("red")
    print("Color changed to: Red")
    print("----------------------")
def o():
    turtle.color("orange")
    print("Color changed to: Orange")
    print("----------------------")
def y():
    turtle.color("yellow")
    print("Color changed to: Yellow")
    print("----------------------")
def g():
    turtle.color("green")
    print("Color changed to: Green")
    print("----------------------")
def b():
    turtle.color("blue")
    print("Color changed to: Blue")
    print("----------------------")
def p():
    turtle.color("purple")
    print("Color changed to: Purple")
    print("----------------------")
def w():
    turtle.color("white")
    print("Color changed to: White")
    print("----------------------")
def bl():
    turtle.color("black")
    print("Color changed to: Black")
    print("----------------------")
def undo():
    turtle.undo()
    print("Action undone!")
    print("----------------------")
def bgr():
    turtle.bgcolor("red")
    print("Background color changed to: Red")
    print("----------------------")
def bgo():
    turtle.bgcolor("orange")
    print("Background color changed to: Orange")
    print("----------------------")
def bgy():
    turtle.bgcolor("yellow")
    print("Background color changed to: Yellow")
    print("----------------------")
def bgg():
    turtle.bgcolor("green")
    print("Background color changed to: Green")
    print("----------------------")
def bgb():
    turtle.bgcolor("blue")
    print("Background color changed to: Blue")
    print("----------------------")
def bgp():
    turtle.bgcolor("purple")
    print("Background color changed to: Purple")
    print("----------------------")
def bgw():
    turtle.bgcolor("white")
    print("Background color changed to: White")
    print("----------------------")
def bgbl():
    turtle.bgcolor("black")
    print("Background color changed to: Black")
    print("----------------------")
def clear():
    turtle.clear()
    print("Cleared!")
    print("----------------------")
def credit():
    mb.showinfo("Credits", "Created By: Alex")
def pensize():
    size = sd.askinteger("Pen Size", "Set Size", parent=root)
    turtle.pensize(size)
    print("Pensize changed to: " + str(size))
    print("----------------------")
def pensizereset():
    turtle.pensize(1)
    print("Pensize reset.")
    print("----------------------")
def penup():
    turtle.penup()
    print("Stop drawing.")
    print("----------------------")
def pendown():
    turtle.pendown()
    print("Started drawing.")
    print("----------------------")
def bfill():
    turtle.begin_fill()
    print("Started filling.")
    print("----------------------")
def efill():
    turtle.end_fill()
    print("Stopped filling.")
    print("----------------------")
def randomize():
    color = random.choice(colors)
def turtlereset():
    turtle.goto(0,0)
    turtle.bgcolor("White")
    turtle.pensize(1)
    turtle.color("Black")
    turtle.clear()
    print("Screen has been reset.")
    print("----------------------")
def ccolor():
    picked_color = colorchooser.askcolor(title='Select Color')[0]
    turtle.color(webcolors.rgb_to_hex(picked_color))
    while True:
        if picked_color != None:
            actual_name, closest_name = get_color_name(picked_color)
            if actual_name == None:
                print("No actual color found", "RGB Value: ", picked_color)
                print("Closest Color found: ", closest_name)
                print('----------------------------------')
            else:
                print("Color has been changed to: ", actual_name, " or ", picked_color)
                print('----------------------------------')
            break
        else:
            break
def bccolor():
    picked_color = colorchooser.askcolor(title='Select Color')[0]
    turtle.bgcolor(webcolors.rgb_to_hex(picked_color))
    while True:
        if picked_color != None:
            actual_name, closest_name = get_color_name(picked_color)
            if actual_name == None:
                print("No actual color found", "RGB Value: ", picked_color)
                print("Closest Color found: ", closest_name)
                print('----------------------------------')
            else:
                print("Color has been changed to: ", actual_name, " or ", picked_color)
                print('----------------------------------')
            break
        else:
            break
# Functions
def closest_color(requested_color):
    min_colours = {}
    for name in webcolors.names("css3"):
        r_c, g_c, b_c = webcolors.name_to_rgb(name)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_color_name(requested_color):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_color)
    except ValueError:
        closest_name = closest_color(requested_color)
        actual_name = None
    return actual_name, closest_name
# GUI

tk.Label(root, text="Colors").grid(row=1,column=1)
tk.Label(root, text="Background Color").grid(row=1,column=2)
tk.Label(root, text="Pen Options").grid(row=1,column=3)
tk.Label(root, text="Other/Misc").grid(row=1,column=4)

tk.Button(root,text = 'Red', command=r).grid(row=2,column=1)
tk.Button(root,text = 'Orange', command=o).grid(row=3,column=1)
tk.Button(root,text = 'Yellow', command=y).grid(row=4,column=1)
tk.Button(root,text = 'Green', command=g).grid(row=5,column=1)
tk.Button(root,text = 'Blue', command=b).grid(row=6,column=1)
tk.Button(root,text = 'Purple', command=p).grid(row=7,column=1)
tk.Button(root,text = 'White', command=w).grid(row=8,column=1)
tk.Button(root,text = 'Black', command=bl).grid(row=9,column=1)
tk.Button(root, text='Custom Color',command=ccolor).grid(row=10,column=1)

tk.Button(root,text = 'Red', command=bgr).grid(row=2,column=2)
tk.Button(root,text = 'Orange', command=bgo).grid(row=3,column=2)
tk.Button(root,text = 'Yellow', command=bgy).grid(row=4,column=2)
tk.Button(root,text = 'Green', command=bgg).grid(row=5,column=2)
tk.Button(root,text = 'Blue', command=bgb).grid(row=6,column=2)
tk.Button(root,text = 'Purple', command=bgp).grid(row=7,column=2)
tk.Button(root,text = 'White', command=bgw).grid(row=8,column=2)
tk.Button(root,text = 'Black', command=bgbl).grid(row=9,column=2)
tk.Button(root, text='Custom Color',command=bccolor).grid(row=10,column=2)

tk.Button(root,text = 'Pen Size', command=pensize).grid(row=2,column=3)
tk.Button(root,text = 'Pen Size Reset', command=pensizereset).grid(row=3,column=3)
tk.Button(root,text = 'Pen Up',command=penup).grid(row=4,column=3)
tk.Button(root,text = 'Pen Down',command=pendown).grid(row=5,column=3)

tk.Button(root,text = 'Clear',command=clear).grid(row=2,column=4)
tk.Button(root,text = 'Undo', command=undo).grid(row=3,column=4)
tk.Button(root,text = 'Reset',command=turtlereset).grid(row=4,column=4)
tk.Button(root,text = 'Begin Fill',command=bfill).grid(row=5,column=4)
tk.Button(root,text = 'Finish Fill',command=efill).grid(row=6,column=4)
tk.Button(root,text = 'Randomize',command=randomize).grid(row=7,column=4)
tk.Button(root,text = 'Credits', command=credit).grid(row=8,column=4)
