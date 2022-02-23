from tkinter import *
from phue import Bridge
from time import time
from random import random
from tkinter.colorchooser import askcolor

b = Bridge('172.30.1.39')
selected = "lightstrip"

window=Tk()
window.title("Jay's Bedroom Lighting System Controller")
window.geometry("320x320")
window.resizable(width=False, height=False)

bri = 0

def LightStripOn():
    if (selected == "lightstrip"):
        b.set_light('Lightstrip', 'on', True)
    elif (selected == "bedroom"):
        b.set_light('Bedroom', 'on', True)

def LightStripOff():
    if (selected == "lightstrip"):
        b.set_light('Lightstrip', 'on', False)
    elif (selected == "bedroom"):
        b.set_light('Bedroom', 'on', False)

def slider_changed(event):  
    global bri 
    bri = Slider.get()
    if (selected == "lightstrip"):
        if (bri == 0):
            b.set_light('Lightstrip', 'on', False)
        else:
            b.set_light('Lightstrip', 'on', True)
            b.set_light('Lightstrip', 'bri', bri)
    elif (selected == "bedroom"):
        if (bri == 0):
            b.set_light('Bedroom', 'on', False)
        else:
            b.set_light('Bedroom', 'on', True)
            b.set_light('Bedroom', 'bri', bri)

def change_color():
    colors = askcolor(title="PHUE ColorChooser")
    ColorCode = colors[1]
    FinalColor = ColorCode.lstrip("#")
    if (selected == "lightstrip"):
        b.set_light('Lightstrip','xy',convertColor(FinalColor))
    elif (selected == "bedroom"):
        b.set_light('Bedroom','xy',convertColor(FinalColor))

def convertColor(hexCode):
    R = int(hexCode[:2],16)
    G = int(hexCode[2:4],16)
    B = int(hexCode[4:6],16)

    total = R + G + B

    if R == 0:
        firstPos = 0
    else:
        firstPos = R / total
    
    if G == 0:
        secondPos = 0
    else:
        secondPos = G / total

    return [firstPos, secondPos]

def selectBedroom():
    global selected
    selected = "bedroom"

def selectLightStrip():
    global selected
    selected = "lightstrip"


Bedroom = Button(window, overrelief="solid", width=20, command=selectBedroom, text="Lamp")
Bedroom.pack()

Lightstrip = Button(window, overrelief="solid", width=20, command=selectLightStrip, text="Lightstrip")
Lightstrip.pack()

button1 = Button(window, overrelief="solid", width=15, command=LightStripOn, repeatdelay=1000, repeatinterval=100, text="켜기")
button1.pack()

button2 = Button(window, overrelief="solid", width=15, command=LightStripOff, repeatdelay=1000, repeatinterval=100, text="끄기")
button2.pack()

Slider = Scale(window, from_=0, to=254, orient=HORIZONTAL, command=slider_changed)
Slider.pack()

ColorChoose = Button(window, text='Select a Color', command=change_color).pack(expand=True)
Slider.pack()


mainloop()