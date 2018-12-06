from random import randint

def setup():
    size(800,800)
    background(100,100,100)
    global dice1, dice2, dice3, dice4, dice5, dice6, f
    dice1 = loadImage("1.jpg")
    dice2 = loadImage("2.jpg")
    dice3 = loadImage("3.jpg")
    dice4 = loadImage("4.jpg")
    dice5 = loadImage("5.jpg")
    dice6 = loadImage("6.jpg")
    f = createFont("Arial", 16, True)
    noLoop()
def mouseClicked():
    x = 0
    x += 1
    redraw()
    
def Text(a,b,c):
    textFont(f, b)
    fill(c)
    text(a, 70, 130)
def Rect(a,b,c,d,*e):
    fill(*e)
    rect(a,b,c,d)

def draw():
    global dice1, dice2, dice3, dice4, dice5, dice6, f
    Rect(60,60,200,80,0)
    Text("Draw!", 48, 150)
    if ((mouseX < 260) and (mouseX > 60) and (mouseY < 140) and (mouseY > 60) and (mouseButton == LEFT)):
        number = randint(1,6)
        if (number == 1):
            image(dice1,300,300)
        elif (number == 2):
            image(dice2,300,300)
        elif (number == 3):
            image(dice3,300,300)
        elif (number == 4):
            image(dice4,300,300)
        elif (number == 5):
            image(dice5,300,300)
        elif (number == 6):
            image(dice6,300,300)
