from random import randint

def setup():
    size(800,800) #size of the screen
    background(100,100,100) #choosing a background color
    global dice1, dice2, dice3, dice4, dice5, dice6, f #making these variables global
    dice1 = loadImage("1.png") #loading images in the program so that they can be used later
    dice2 = loadImage("2.png")
    dice3 = loadImage("3.png")
    dice4 = loadImage("4.png")
    dice5 = loadImage("5.png")
    dice6 = loadImage("6.png")
    f = createFont("Arial", 16, True) # f will represent size 16 Arial, Anti-aliasing is on
    noLoop() #turning off the draw loop
def mouseClicked(): #the button for the dice
    x = 0
    x += 1
    redraw()
    
def TextAdd(a,b,*c): #getting text in the screen. a= the text to put in. b= fontsize c= text color
    textFont(f, b)
    fill(*c)
    text(a, 70, 130)

def Rect(a,b,c,d,*e): #rectangle maker
    fill(*e)
    rect(a,b,c,d)

def draw():
    global dice1, dice2, dice3, dice4, dice5, dice6, f # Getting all the variables
    Rect(60,60,200,80,0) # drawing a rectangle for the button
    TextAdd("Draw!", 48,150,150,100) # Putting text in the button
    if ((mouseX < 260) and (mouseX > 60) and (mouseY < 140) and (mouseY > 60) and (mouseButton == LEFT)): # The working of the button
        number = randint(1,6)
        if (number == 1):
            image(dice1,300,300,25,25)
        elif (number == 2):
            image(dice2,300,300,25,25)
        elif (number == 3):
            image(dice3,300,300,25,25)
        elif (number == 4):
            image(dice4,300,300,25,25)
        elif (number == 5):
            image(dice5,300,300,25,25)
        elif (number == 6):
            image(dice6,300,300,25,25)
