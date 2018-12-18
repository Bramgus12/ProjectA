from random import randint


Player1 = "Test1"
Player2 = "Test2"
Player3 = "Test3"
Player4 = "Test4"
PlayerButtonColors = [0,0,0,0]

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
    
def TextAdd(a,b,c,d,*e): #getting text in the screen. a= the text to put in. b= fontsize c= X-coordinate d= Y-coordinate e= text color
    textFont(f, b)
    fill(*e)
    text(a,c,d)

def Rect(a,b,c,d,*e): #rectangle maker a= X coordinate b= Y-coordinate c= width of the rectangle d= height of the rectangle e= color of the rectangle
    fill(*e)
    rect(a,b,c,d)

def draw():
    global f # Getting all the variables
    # The button of the dice:
    Rect(60,60,200,80,0) # drawing a rectangle for the button
    TextAdd("Roll!", 48, 70, 120, 255) # Putting text in the button
  

    # The button for player 1
    Rect(400, 60, 340, 80, PlayerButtonColors[0])
    TextAdd(Player1, 48, 410, 120, 255)

       
    # The button for player 2
    Rect(400, 150, 340, 80, PlayerButtonColors[1])
    TextAdd(Player2, 48, 410, 210, 255)


    # The button for player 3
    Rect(400, 240, 340, 80, PlayerButtonColors[2])
    TextAdd(Player3, 48, 410, 300, 255)  

           
    # The button for player 4
    Rect(400, 330, 340, 80, PlayerButtonColors[3])
    TextAdd(Player4, 48, 410, 390, 255)   

    # Button Player1
    if ((mouseX < 740) and (mouseX > 400) and (mouseY < 140) and (mouseY > 60) and (mouseButton == LEFT)):
        # Rect(400, 60, 340, 80, 100)
        # TextAdd(Player1, 48, 410, 120, 255)
        PlayerButtonColors[0] = 100

    # Button player2
    if ((mouseX < 740) and (mouseX > 400) and (mouseY < 230) and (mouseY > 150) and (mouseButton == LEFT)):
        PlayerButtonColors[1] = 100
        # Rect(400, 150, 340, 80, 100)
        # TextAdd(Player2, 48, 410, 210, 255)

    # Button player3
    if ((mouseX < 740) and (mouseX > 400) and (mouseY < 320) and (mouseY > 240) and (mouseButton == LEFT)):
        # Rect(400, 240, 340, 80, 100)
        # TextAdd(Player3, 48, 410, 300, 255) 
        PlayerButtonColors[2] = 100
      
    # Button player4
    if ((mouseX < 740) and (mouseX > 400) and (mouseY < 410) and (mouseY > 330) and (mouseButton == LEFT)):
        # Rect(400, 330, 340, 80, 100)
        # TextAdd(Player4, 48, 410, 390, 255)
        PlayerButtonColors[3] = 100

    if ((mouseX < 260) and (mouseX > 60) and (mouseY < 140) and (mouseY > 60) and (mouseButton == LEFT)): # The working of the button
        number = randint(1,6) # generating a random Integer
        dice = loadImage(str(number) + ".png") #loading the image in
        image(dice,270,60,80,80) # drawing the image
