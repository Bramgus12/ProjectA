from random import randint

def setup():
    size(600, 400)
    startScreen()
    noLoop()

def Rect(a,b,c,d,*e): #rectangle maker a= X coordinate b= Y-coordinate c= width of the rectangle d= height of the rectangle e= color of the rectangle
    fill(*e)
    rect(a,b,c,d)

def guideLines():
    

def powerupDice():
    global screen1, screen2, screen3, screen4, screen5, PlayerButtonColors, Player1, Player2, Player3, Player4
    screen1 = False
    screen2 = False
    screen3 = True
    screen4 = False
    screen5 = False
    
    Player1 = "Test1"
    Player2 = "Test2"
    Player3 = "Test3"
    Player4 = "Test4"
    
    background(255)
    textAlign(CENTER,CENTER)
    textSize(35)
    # The button of the dice:
    Rect(10,10,150,60,255) # drawing a rectangle for the button
    fill(0)
    text("Roll dice!", 10, 10, 150,60) # Putting text in the button
    
    Rect(10,80,150,60,255) # drawing a rectangle for the button
    fill(0)
    text("Roll stone!", 10,80,150,60) # Putting text in the button
    
    Rect(10,150,150,60,255) # drawing a rectangle for the button
    fill(0)
    text("Guidelines", 10,150,150,60) # Putting text in the button  

    # The button for player 1
    Rect(440, 10, 150, 60, 255)
    fill(0)
    text(Player1, 440, 10, 150, 60)

       
    # The button for player 2
    Rect(440, 80, 150, 60, 255)
    fill(0)
    text(Player2, 440, 80, 150, 60)


    # The button for player 3
    Rect(440, 150, 150, 60, 255)
    fill(0)
    text(Player3, 440, 150, 150, 60)  

           
    # The button for player 4
    Rect(440, 220, 150, 60, 255)
    fill(0)
    text(Player4, 440, 220, 150, 60)   

def characterKiezer():
    global screen1, screen2, screen3, screen4, screen5, choices, playerchoices
    Spiderman = {'name' : 'Spiderman', 'rectangle' : [30, 90, 150, 50]}
    Hulk = {'name' : 'Hulk','rectangle' : [30, 160, 150, 50]}
    BlackPanther = {'name' :'Black Panther','rectangle' : [30, 230, 150, 50]}
    DrStrange = {'name' : 'Doctor Strange','rectangle' : [30, 300, 150, 50]}
    Thor = {'name' : 'Thor','rectangle' : [210, 90, 150, 50]}
    IronMan = {'name' :'Iron Man','rectangle' : [210, 160, 150, 50]}
    CptnAmerica = {'name' :'Captain America','rectangle' : [210, 230, 150, 50]}
 
    choices =[Spiderman, Hulk, BlackPanther, DrStrange, Thor, IronMan, CptnAmerica]
 
    playerchoices = []
    
    screen1 = False
    screen2 = True
    screen3 = False
    screen4 = False
    screen5 = False
    
    # background colour:
    background(255)
   
    fill(0)
    textSize(25)
    text('Choose your charachter', 150, 60)
   
    # rectangles' colour:
    fill(255)
    rect(30, 90, 150, 50)
    rect(30, 160, 150, 50)
    rect(30, 230, 150, 50)
    rect(30, 300, 150, 50)
    rect(210, 300, 150, 50)
    rect(210, 90, 150, 50)
    rect(210, 160, 150, 50)
    rect(210, 230, 150, 50)
    rect(420,90,150,250)

    fill(0)
    textSize(18)
    textAlign(CENTER, CENTER)
    text(Spiderman['name'], Spiderman ['rectangle'][0], Spiderman ['rectangle'][1], Spiderman ['rectangle'][2], Spiderman ['rectangle'][3],)
    text(Hulk['name'], Hulk ['rectangle'][0], Hulk ['rectangle'][1], Hulk ['rectangle'][2], Hulk ['rectangle'][3],)
    text(BlackPanther['name'], BlackPanther ['rectangle'][0], BlackPanther ['rectangle'][1], BlackPanther ['rectangle'][2], BlackPanther ['rectangle'][3],)
    text(DrStrange['name'], DrStrange ['rectangle'][0], DrStrange ['rectangle'][1], DrStrange ['rectangle'][2], DrStrange ['rectangle'][3],)
    text(Thor['name'], Thor ['rectangle'][0], Thor ['rectangle'][1], Thor ['rectangle'][2], Thor ['rectangle'][3],)
    text(IronMan['name'], IronMan ['rectangle'][0], IronMan ['rectangle'][1], IronMan ['rectangle'][2], IronMan ['rectangle'][3],)
    text(CptnAmerica['name'], CptnAmerica ['rectangle'][0], CptnAmerica ['rectangle'][1], CptnAmerica ['rectangle'][2], CptnAmerica ['rectangle'][3],)    
    text("Next", 210, 300, 150, 50)
    
def startScreen():
    global screen1, screen2, screen3, screen4, screen5
    screen1 = True
    screen2 = False
    screen3 = False
    screen4 = False
    screen5 = False
    # Grootte van de venster en achtergrondkleur
    background(255)
    
    # Avengers foto:
    Avengers = loadImage('Avengers.png')
    image(Avengers, 48, 75, 504, 200)
    
    # Uiterlijk van de tekst:
    fill(0)
    smooth(2)
    
    textFont(loadFont('Marvel.vlw'))
    textSize(60)
    text('Click anywhere to start', 75, 350)

def mouseClicked():
    redraw()    

def draw():
    if mouseButton == LEFT:
        if screen1:
            if 0 < mouseX < 800 and 0 < mouseY < 800:
                # characterKiezer()
                characterKiezer()
        
        if screen2:
            print(choices)
            if ((mouseX < 360) and (mouseX > 210) and (mouseY < 350) and (mouseY > 300)):
                powerupDice()
            elif len(playerchoices) < 4:
                for charachter in choices:
                    if mouseX >= charachter['rectangle'][0] and mouseX <= charachter['rectangle'][2] + charachter['rectangle'][0]  and mouseY >= charachter['rectangle'][1] and mouseY <= charachter['rectangle'][3] + charachter['rectangle'][1] :
                        (playerchoices.append(charachter))
                for i in range(len(playerchoices)):
                    fill(135)
                    rect(420,90+(50 * i),150,50)
                    fill(190)
                    text(playerchoices[i]['name'] ,420,90+(50 * i),150,50)
            

        if screen3:
            if ((mouseX < 590) and (mouseX > 440) and (mouseY < 70) and (mouseY > 10)):
                Rect(440, 10, 150, 60, 100)
                fill(0)
                text(Player1, 440, 10, 150, 60)
            # Button player2
            elif ((mouseX < 590) and (mouseX > 440) and (mouseY < 140) and (mouseY > 80)):
                Rect(440, 80, 150, 60, 100)
                fill(0)
                text(Player2, 440, 80, 150, 60)

            # Button player3
            elif ((mouseX < 590) and (mouseX > 440) and (mouseY < 210) and (mouseY > 150)):
                Rect(440, 150, 150, 60, 100)
                fill(0)
                text(Player3, 440, 150, 150, 60)  

      
            # Button player4
            elif ((mouseX < 590) and (mouseX > 440) and (mouseY < 280) and (mouseY > 220)):
                Rect(440, 220, 150, 60, 100)
                fill(0)
                text(Player4, 440, 220, 150, 60)  


            elif ((mouseX < 160) and (mouseX > 10) and (mouseY < 70) and (mouseY > 10)):
                number = randint(1,6) # generating a random Integer
                dice = loadImage(str(number) + "d.png") #loading the image in
                image(dice,170,10,60,60) # drawing the image   
                
            elif ((mouseX < 160) and (mouseX > 10) and (mouseY < 140) and (mouseY > 80)):
                number2 = randint(1,6) # generating a random Integer
                diceInf = loadImage(str(number2) + ".jpg") #loading the image in
                image(diceInf,170,80,36,60) # drawing the image 
           
            elif ((mouseX < 160) and (mouseX > 10) and (mouseY < 210) and (mouseY > 150)):
                guideLines() 
        if screen4:
            if 30 < mouseX < 180 and 90 < mouseY < 140:
                powerup(Spiderman['power'], Spiderman['picture'], Spiderman['name'])
            elif 30 < mouseX < 180 and 160 < mouseY < 210:
                powerup(Hulk['power'], Hulk['picture'], Hulk['name'])
            elif 30 < mouseX < 180 and 230 < mouseY < 280:
                powerup(BlackPanther['power'], BlackPanther['picture'], BlackPanther['name'])
            elif 30 < mouseX < 180 and 300 < mouseY < 350:
                powerup(DrStrange['power'], DrStrange['picture'], DrStrange['name'])
            elif 210 < mouseX < 360 and 90 < mouseY < 140:
                powerup(Thor['power'], Thor['picture'], Thor['name'])
            elif 210 < mouseX < 360 and 160 < mouseY < 210:
                powerup(IronMan['power'], IronMan['picture'], IronMan['name'])
            elif 210 < mouseX < 360 and 230 < mouseY < 280:
                powerup(CptnAmerica['power'], CptnAmerica['picture'], CptnAmerica['name'])
            elif 420 < mouseX < 570 and 90 < mouseY < 140:
                powerup(Venom['power'], Venom['picture'], Venom['name'])
            elif 420 < mouseX < 570 and 160 < mouseY < 210:
                powerup(Loki['power'], Loki['picture'], Loki['name'])
            elif 420 < mouseX < 570 and 230 < mouseY < 280:
                powerup(Ultron['power'], Ultron['picture'], Ultron['name'])
            elif 420 < mouseX < 570 and 300 < mouseY < 350:
                powerup(Thanos['power'], Thanos['picture'], Thanos['name'])
