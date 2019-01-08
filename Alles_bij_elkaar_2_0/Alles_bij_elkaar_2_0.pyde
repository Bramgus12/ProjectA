from random import randint

# Characters'/enemies' power-ups, names and pictures:
Spiderman = {'name' : 'Spiderman', 'rectangle' : [30, 90, 150, 50], 'picture' : 'Spiderman.jpg', 'power' : "Spiderman's power-up is called Webzip. When he uses his power-up, he can move players. The players will be placed 3 steps behind Spiderman. Webzip has a range of 4 spots in front of Spiderman."}
Hulk = {'name' : 'Hulk', 'rectangle' : [30, 160, 150, 50], 'picture' : 'Hulk.jpg', 'power' : "Hulk's power-up is called Smash. When he uses his power-up, he blows away all players within a range of 3 steps. Smash blows them 3 steps forward if the players are standing in front of him, and 3 steps backward if the players are standing behind him."}
BlackPanther = {'name' : 'Black Panther', 'rectangle' : [30, 230, 150, 50], 'picture' : 'BlackPanther.jpg', 'power' : "Black Panther's power-up is called Kinetic Energy. When he uses his power-up, he blows away all players within a range of 3 steps. Smash blows them 3 steps forward if the players are standing in front of him, and 3 steps backward if the players are standing behind him."}
DrStrange = {'name' : 'Doctor Strange', 'rectangle' : [30, 300, 150, 50], 'picture' : 'DoctorStrange.jpg', 'power' : "Doctor Strange's power is called Clone Illusion. When he uses his power-up, he creates a clone of himself. Every player who tries to attack Doctor Strange's clone goes back to his own checkpoint. The power-up stays activated for 3 rounds."}
Thor = {'name' : 'Thor', 'rectangle' : [210, 90, 150, 50], 'picture' : 'Thor.jpg', 'power' : "Thor's power-up is called Hammer: Mjolnir. By swinging his hammer, Thor can move 6 steps forward."}
IronMan = {'name' : 'Iron Man', 'rectangle' : [210, 160, 150, 50], 'picture' : 'IronMan.jpg', 'power' : "Iron Man's power-up is called Second Suit Roadblock. He can call a second suit to block one upcoming player. After that happens, the suit gets destroyed."}
CptnAmerica = {'name' : 'Captain America', 'rectangle' : [210, 230, 150, 50], 'picture' : 'CaptainAmerica.jpg', 'power' : "Captain America's power-up is called Shield. This is a passive power-up: it makes the player immune to every hero's power-up except Webzip and Clone Illusion."}
Venom = {'name' : 'Venom', 'picture' : 'Venom.png', 'power' : 'You are stuck on the B platform and are not allowed to move for 2 rounds.'}
Loki = {'name' : 'Loki', 'picture' : 'Loki.jpg', 'power' : 'For one turn the amount you throw will set you back rather than forward. For example, if you throw 4, you will have to go 4 steps back.'}
Ultron = {'name' : 'Ultron', 'picture' : 'Ultron.jpg', 'power' : 'You will take 1 or 2 steps less on your next throw. This depends on the B platform you land on.'}
Thanos = {'name': 'Thanos', 'picture' : 'Thanos.jpg', 'power' : "Thanos gets spinned when a player enters his area. After the first player enters Thanos' area, Thanos spins every 3 rounds. He will point at three spots. When you land on one of the 3 spots Thanos is pointing at, you must go back to your checkpoint. You cannot get out of Thanos' area. If someone tries to get you out of Thanos' area, the furthest place back where you can go is the checkpoint in Thanos' area."}

def setup():
    size(600, 400)
    startScreen()
    
    noLoop()
    activeScreen = screen3
    
def startScreen():
    global screen1, screen2, screen3, screen4, screen5
    # screen1 = True
    # screen2 = False
    # screen3 = False
    # screen4 = False
    # screen5 = False
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
    
    screen1 = True
    screen2 = False
    screen3 = False
    screen4 = False
    screen5 = False
    
def characterKiezer():
    global screen1, screen2, screen3, screen4, screen5, choices, playerchoices
    # Spiderman = {'name' : 'Spiderman', 'rectangle' : [30, 90, 150, 50]}
    # Hulk = {'name' : 'Hulk','rectangle' : [30, 160, 150, 50]}
    # BlackPanther = {'name' :'Black Panther','rectangle' : [30, 230, 150, 50]}
    # DrStrange = {'name' : 'Doctor Strange','rectangle' : [30, 300, 150, 50]}
    # Thor = {'name' : 'Thor','rectangle' : [210, 90, 150, 50]}
    # IronMan = {'name' :'Iron Man','rectangle' : [210, 160, 150, 50]}
    # CptnAmerica = {'name' :'Captain America','rectangle' : [210, 230, 150, 50]}
 
    choices =[Spiderman, Hulk, BlackPanther, DrStrange, Thor, IronMan, CptnAmerica]
 
    playerchoices = []
    
    # screen1 = False
    # screen2 = True
    # screen3 = False
    # screen4 = False
    # screen5 = False
    
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


    
    screen1 = False
    screen2 = True
    screen3 = False
    screen4 = False
    screen5 = False
    global choices, playerchoices
    # draw all options
    for i in range(len(choices[0:4])): 
        fill(0)       
        text(choices[i]['name'],30,70*i+120) # write names at x=50, and y dependent on list index
    for i in range(len(choices[4:7])): 
        fill(0)       
        text(choices[i+4]['name'],250,70*i+120) # write names at x=50, and y dependent on list index
    # draw chosen
    for i in range(len(playerchoices)):
        text(playerchoices[i]['name'],410,20*i+100)  # write names at x=400, and y dependent on list index
def Rect(a,b,c,d,*e): #rectangle maker a= X coordinate b= Y-coordinate c= width of the rectangle d= height of the rectangle e= color of the rectangle
    fill(*e)
    rect(a,b,c,d)

def powerupDice():
    global screen1, screen2, screen3, screen4, screen5, PlayerButtonColors, Player1, Player2, Player3, Player4
    screen1 = False
    screen2 = False
    screen3 = True
    screen4 = False
    screen5 = False

    
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
    text(playerchoices[0]['name'], 440, 10, 150, 60)

       
    # The button for player 2
    Rect(440, 80, 150, 60, 255)
    fill(0)
    text(playerchoices[1]['name'], 440, 80, 150, 60)


    # The button for player 3
    if len(playerchoices) >= 3:
        
        Rect(440, 150, 150, 60, 255)
        fill(0)
        text(playerchoices[2]['name'], 440, 150, 150, 60)  

           
    # The button for player 4
    if len(playerchoices) >= 4:
        Rect(440, 220, 150, 60, 255)
        fill(0)
        text(playerchoices[3]['name'], 440, 220, 150, 60)   

def button(x, y, w, h, name):
    # Rectangle and its appearance:
    noStroke()
    fill(255)
    rect(x, y, w, h, 10)
    
    # Text on button and its colour, size and position:
    fill(0)
    textSize(18)
    textAlign(CENTER, CENTER)
    textFont(loadFont('BentonSans-17.vlw'))
    text(name, x, y, w, h)

def powerupScreen():
    global screen1, screen2, screen3, screen4, screen5
    
    screen1 = False
    screen2 = False
    screen3 = False
    screen4 = True
    screen5 = False
    
    # Background colour:
    background(220)
    
    # Top text and its colour and position:
    fill(0)
    textSize(55)
    textFont(loadFont('BentonSans-55.vlw'))
    textAlign(CENTER, CENTER)
    text('Power-ups', 50, 10, 500, 70)
    
    # These are the buttons on the 'first screen'
    button(30, 90, 150, 50, Spiderman['name']) 
    button(30, 160, 150, 50, Hulk['name'])
    button(30, 230, 150, 50, BlackPanther['name'])
    button(30, 300, 150, 50, DrStrange['name'])
    button(210, 90, 150, 50, Thor['name'])    
    button(210, 160, 150, 50, IronMan['name'])
    button(210, 230, 150, 50, CptnAmerica['name']) 
    button(420, 90, 150, 50, Venom['name'])
    button(420, 160, 150, 50, Loki['name'])
    button(420, 230, 150, 50, Ultron['name'])
    button(420, 300, 150, 50, Thanos['name'])
    
def powerup(power, picture, name):
    global screen1, screen2, screen3, screen4, screen5
    
    screen1 = False
    screen2 = False
    screen3 = False
    screen4 = False
    screen5 = True
    
    # Background colour:
    background(220)
    
    # Back button:
    # fill(255)
    # rect(500, 20, 50, 50)
    image(loadImage('back.png'), 500, 20, 51, 51)
   
    # Top text, character's/enemy's name:
    fill(0)
    textSize(55)
    textAlign(CENTER, CENTER)
    textFont(loadFont('BentonSans-55.vlw'))
    text(name, 35, 10, 485, 70)
    
    # Powerup text:
    textSize(18)
    textAlign(LEFT)
    textFont(loadFont('BentonSans-17.vlw'))
    text(power, 20, 100, 350, 300)
    
     # Picture of character/enemy:
    image(loadImage(picture), 420, 90, 150, 230)

def mouseClicked():
    redraw()  
    
def draw():
    global activeScreen, screen1, screen2, screen3, screen4, screen5
#     mousePressed()
   
# def mousePressed():
    if mouseButton == LEFT:
        if screen1:
            if 0 < mouseX < 800 and 0 < mouseY < 800:
                # characterKiezer()
                characterKiezer()
        
        elif screen2:
            print(choices)
            if ((mouseX < 360) and (mouseX > 210) and (mouseY < 350) and (mouseY > 300)):
                powerupDice()
            elif len(playerchoices) < 4:
                for charachter in choices:
                    if mouseX >= charachter['rectangle'][0] and mouseX <= charachter['rectangle'][2] + charachter['rectangle'][0]  and mouseY >= charachter['rectangle'][1] and mouseY <= charachter['rectangle'][3] + charachter['rectangle'][1] :
                        (playerchoices.append(charachter)) # add character to selectedlist
                        fill(100)  
                        rect(charachter['rectangle'][0], charachter['rectangle'][1], charachter['rectangle'][2], charachter['rectangle'][3])

                for i in range(len(playerchoices)):
                    fill(135)
                    rect(420,90+(50 * i),150,50)
                    fill(190)
                    text(playerchoices[i]['name'] ,420,90+(50 * i),150,50)
                    if len(playerchoices) == 4: # if 4 characters chosen, move to next gamestate / screen
                        powerupDice()
            

            
        # if ((mouseX < 590) and (mouseX > 440) and (mouseY < 70) and (mouseY > 10)) and activeScreen == screen3:
        elif screen3:
            if ((mouseX < 590) and (mouseX > 440) and (mouseY < 70) and (mouseY > 10)):
                Rect(440, 10, 150, 60, 100)
                fill(0)
                text(playerchoices[0]['name'], 440, 10, 150, 60)
            # Button player2
            elif ((mouseX < 590) and (mouseX > 440) and (mouseY < 140) and (mouseY > 80)):
                Rect(440, 80, 150, 60, 100)
                fill(0)
                text(playerchoices[1]['name'], 440, 80, 150, 60)

            # Button player3
            elif ((mouseX < 590) and (mouseX > 440) and (mouseY < 210) and (mouseY > 150)):
                if len(playerchoices) >= 3:
                    Rect(440, 150, 150, 60, 100)
                    fill(0)
                    text(playerchoices[2]['name'], 440, 150, 150, 60)  

      
            # Button player4
            elif ((mouseX < 590) and (mouseX > 440) and (mouseY < 280) and (mouseY > 220)):
                if len(playerchoices) >= 4:
                    Rect(440, 220, 150, 60, 100)
                    fill(0)
                    text(playerchoices[3]['name'], 440, 220, 150, 60)  


            elif ((mouseX < 160) and (mouseX > 10) and (mouseY < 70) and (mouseY > 10)):
                number = randint(1,6) # generating a random Integer
                dice = loadImage(str(number) + "d.png") #loading the image in
                image(dice,170,10,60,60) # drawing the image   
                
            elif ((mouseX < 160) and (mouseX > 10) and (mouseY < 140) and (mouseY > 80)):
                number2 = randint(1,6) # generating a random Integer
                diceInf = loadImage(str(number2) + ".jpg") #loading the image in
                image(diceInf,170,80,36,60) # drawing the image 
                
           
            elif ((mouseX < 160) and (mouseX > 10) and (mouseY < 210) and (mouseY > 150)):
                powerupScreen() 
                
        elif screen4:
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
        
        # This is what happens when you click on the back button:
        elif screen5:
            if 500 < mouseX < 550 and 20 < mouseY < 70:
                powerupScreen()
