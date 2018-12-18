from random import randint

def setup():
    global f
    size(800,800) #size of the screen
    background(255) #choosing a background color
    f = createFont("Arial",12 , True) # f will represent size 12 Arial, Anti-aliasing is on
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
    # The button of the dice:
    Rect(60,60,200,80,0) # drawing a rectangle for the button
    TextAdd("CLICK", 48, 70, 120, 255) # Putting text in the button
    
    if 60 < mouseX < 260 and 60 < mouseY < 140 and mouseButton == LEFT: # The working of the button
        image(loadImage(str(randint(1,6)) + ".jpg"),360,320)
    
