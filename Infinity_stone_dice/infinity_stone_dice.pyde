
def setup():
    size(800,800) #size of the screen
    background(255) #choosing a background color
    global f#making these variables global
    noLoop()# turning off the draw loop
    
def mouseClicked(): #the button for the dice
    x = 0
    x += 1
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
    TextAdd("BITCH", 48, 70, 120, 255) # Putting text in the button
    
    background(220, 220, 220)
    fill (225, 0, 0)
    img = loadImage ("Infinity Stone Mind.jpg")
    image(img,0,0)
    
