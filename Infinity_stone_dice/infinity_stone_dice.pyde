from random import randint

def setup():
    size(800,800) #size of the screen
    background(255) #choosing a background color
    f = createFont("Arial",12 , True) # f will represent size 12 Arial, Anti-aliasing is on
    global f#making these variables global
    noLoop()# turning off the draw loop
    
def mouseClicked(): #the button for the dice
    redraw()    

def TextAdd(a,b,c,d,*e): #getting text in the screen. a= the text to put in. b= fintsize
    textFont(f, b)
    fill(*e)
    text(a,c,d)
    
def Rect(a,b,c,d,*e): #rectangle maker a= X coordinate b= Y-coordinate c= Width of the rectangle d= height of the rectangle e= color of the rectangle
    fill(*e)
    rect(a,b,c,d)

def draw():
    global img #etting all the varaibles
    # The button of the dice:
    Rect(60,60,200,80,0) # drawing a rectangle for the button
    TextAdd("CLICK", 48, 70, 120, 255) # Putting text in the button
    
    if ((mouseX < 260) and (mouseX > 60) and (mouseY < 140) and (mouseY > 60) and (mouseButton == LEFT)): # The working of the button
        number = randint(1,6)
        img = loadImage (str(number) + ".jpg")
        image(img,360,320)
    
