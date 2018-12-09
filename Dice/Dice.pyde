from random import randint

def setup():
    size(800,800) #size of the screen
    background(255) #choosing a background color
    global f #making these variables global
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

def Rect(a,b,c,d,*e): #rectangle maker a= X coordinate b= Y-coordinate c= width of the rectangle d= height of the rectangle e= color of the rectangle
    fill(*e)
    rect(a,b,c,d)

def draw():
    global f # Getting all the variables
    Rect(60,60,200,80,0) # drawing a rectangle for the button
    TextAdd("Draw!", 48,255) # Putting text in the button
    if ((mouseX < 260) and (mouseX > 60) and (mouseY < 140) and (mouseY > 60) and (mouseButton == LEFT)): # The working of the button
        number = randint(1,6) # generating a random Integer
        dice = loadImage(str(number) + ".png") #loading the image in
        image(dice,270,60,80,80) # drawing the image
