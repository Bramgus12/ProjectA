from random import randint

# Characters'/enemies' power-ups, names and pictures:
Spiderman = {'name' : 'Spiderman', 'notChosen' : True, 'powerUsed' : False, 'rectangle' : [30, 90, 150, 50,10], 'picture' : 'Spiderman.jpg', 'power' : "Spiderman's power-up is called Webzip. When he uses his power-up, he can move players. The players will be placed 3 steps behind Spiderman. Webzip has a range of 4 spots in front of Spiderman."}
Hulk = {'name' : 'Hulk', 'notChosen' : True, 'powerUsed' : False, 'rectangle' : [30, 160, 150, 50,10], 'picture' : 'Hulk.jpg', 'power' : "Hulk's power-up is called Smash. When he uses his power-up, he blows away all players within a range of 3 steps. Smash blows them 3 steps forward if the players are standing in front of him, and 3 steps backward if the players are standing behind him."}
BlackPanther = {'name' : 'Black Panther', 'notChosen' : True, 'powerUsed' : False, 'rectangle' : [30, 230, 150, 50,10], 'picture' : 'BlackPanther.jpg', 'power' : "Black Panther's power-up is called Kinetic Energy. When he uses his power-up, he blows away all players within a range of 3 steps. Smash blows them 3 steps forward if the players are standing in front of him, and 3 steps backward if the players are standing behind him."}
DrStrange = {'name' : 'Doctor Strange', 'notChosen' : True, 'powerUsed' : False, 'rectangle' : [30, 300, 150, 50,10], 'picture' : 'DoctorStrange.jpg', 'power' : "Doctor Strange's power is called Clone Illusion. When he uses his power-up, he creates a clone of himself. Every player who tries to attack Doctor Strange's clone goes back to his own checkpoint. The power-up stays activated for 3 rounds."}
Thor = {'name' : 'Thor', 'notChosen' : True, 'powerUsed' : False, 'rectangle' : [210, 90, 150, 50,10], 'picture' : 'Thor.jpg', 'power' : "Thor's power-up is called Hammer: Mjolnir. By swinging his hammer, Thor can move 6 steps forward."}
IronMan = {'name' : 'Iron Man', 'notChosen' : True, 'powerUsed' : False, 'rectangle' : [210, 160, 150, 50,10], 'picture' : 'IronMan.jpg', 'power' : "Iron Man's power-up is called Second Suit Roadblock. He can call a second suit to block one upcoming player. After that happens, the suit gets destroyed."}
CptnAmerica = {'name' : 'Captain America', 'notChosen' : True, 'powerUsed' : False, 'rectangle' : [210, 230, 150, 50,10], 'picture' : 'CaptainAmerica.jpg', 'power' : "Captain America's power-up is called Shield. This is a passive power-up: it makes the player immune to every hero's power-up except Webzip and Clone Illusion."}
Venom = {'name' : 'Venom', 'picture' : 'Venom.png', 'power' : 'You are stuck on the B platform and are not allowed to move for 2 rounds.'}
Loki = {'name' : 'Loki', 'picture' : 'Loki.jpg', 'power' : 'For one turn the amount you throw will set you back rather than forward. For example, if you throw 4, you will have to go 4 steps back.'}
Ultron = {'name' : 'Ultron', 'picture' : 'Ultron.jpg', 'power' : 'You will take 1 or 2 steps less on your next throw. This depends on the B platform you land on.'}
Thanos = {'name': 'Thanos', 'picture' : 'Thanos.jpg', 'power' : "Thanos gets spinned when a player enters his area. After the first player enters Thanos' area, Thanos spins every 3 rounds. He will point at three spots. When you land on one of the 3 spots Thanos is pointing at, you must go back to your checkpoint. You cannot get out of Thanos' area. If someone tries to get you out of Thanos' area, the furthest place back where you can go is the checkpoint in Thanos' area."}
Stones = {'name' : 'Infinity Stones', 'power' : 'I.  The Power Stone doubles your steps. It can only be used for one round.\nII.  The Mind Stone makes you indestructible for one round. If a player tries to attack you, nothing happens to the attacking player.\nIII.  The Reality Stone enables you to choose one player who will not be allowed to move for one turn.\nIV.  The Soul Stone enables you to choose one player who will be sent back to his/her last checkpoint.\nV.  The Space Stone allows you to take the place of the player in front of you. The player in front of you goes back to his/her last checkpoint.\nVI.  The Time Stone allows you to send all other players 5 steps back.'}

deg = 0   
speed = 0
is_slowing = False
rotation_speed = 0
rotation = 0



def setup():
    global pointer, wheel
    size(600, 400, P3D)
    startScreen()
    noLoop()
    pointer = loadImage("pointer.png")
    wheel = loadImage("wheel.png")
    startScreen()

      
def startScreen():
    global screen1, screen2, screen3, screen4, screen5, screen6
    screen1 = True
    screen2 = False
    screen3 = False
    screen4 = False
    screen5 = False
    
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
    
    
def characterKiezer():
    global screen1, screen2, screen3, screen4, screen5, screen6, choices, playerchoices
    screen1 = False
    screen2 = True
    screen3 = False
    screen4 = False
    screen5 = False
    
    choices =[Spiderman, Hulk, BlackPanther, DrStrange, Thor, IronMan, CptnAmerica]
    playerchoices = []
    
    # background colour:
    background(220)
   
    fill(0)
    textFont(loadFont('BentonSans-55.vlw'))
    textSize(45)
    textAlign(CENTER, CENTER)
    text('Choose your charachter', 300, 40)
   
    # rectangles:
    noStroke()
    fill(255)
    rect(30, 90, 150, 50, 10)
    rect(30, 160, 150, 50, 10)
    rect(30, 230, 150, 50, 10)
    rect(30, 300, 150, 50, 10)
    rect(210, 300, 150, 50, 10)
    rect(210, 90, 150, 50, 10)
    rect(210, 160, 150, 50, 10)
    rect(210, 230, 150, 50, 10)
    rect(420, 90, 150, 200)

    textSize(18)
    textFont(loadFont('BentonSans-17.vlw'))
    
    global choices, playerchoices
    # draw all options
    for i in range(len(choices[0:4])): 
        fill(0)       
        text(choices[i]['name'],105,70*i+115) # write names at x=50, and y dependent on list index
        # rect(30, 70,20 * i+120,10)
    for i in range(len(choices[4:7])): 
        fill(0)       
        text(choices[i+4]['name'],285,70*i+115) # write names at x=50, and y dependent on list index
    # draw chosen
    for i in range(len(playerchoices)):
        text(playerchoices[i]['name'],410,20*i+100)  # write names at x=400, and y dependent on list index
    text('Next', 210, 300, 150, 50)
    
def Rect(a,b,c,d,*e): #rectangle maker a= X coordinate b= Y-coordinate c= width of the rectangle d= height of the rectangle e= color of the rectangle
    fill(*e)
    rect(a,b,c,d,10)

def powerupDice():
    global screen1, screen2, screen3, screen4, screen5, screen6, PlayerButtonColors, Player1, Player2, Player3, Player4
    screen1 = False
    screen2 = False
    screen3 = True
    screen4 = False
    screen5 = False
    
    background(220)
    textAlign(CENTER,CENTER)
    textSize(18)
    textFont(loadFont('BentonSans-17.vlw'))
    # Buttons:
    Rect(10,10,150,60,255) # drawing a rectangle for the button
    fill(0)
    text("Roll dice!", 10, 10, 150,60) # Putting text in the button
    
    Rect(10,80,150,60,255) # drawing a rectangle for the button
    fill(0)
    text("Roll stone!", 10,80,150,60) # Putting text in the button
    
    Rect(10,150,150,60,255) # drawing a rectangle for the button
    fill(0)
    text("Guidelines", 10,150,150,60) # Putting text in the button  
    
    Rect(10,220,150,60,255) # drawing a rectangle for the button
    fill(0)
    text("Thanos Arm", 10,220,150,60) # Putting text in the button  
    
    # The button for player 1
    if playerchoices[0]['powerUsed']:
        fill(110)
    else:
        fill(255)    
    rect(440, 10, 150, 60, 10)
    fill(0)
    text(playerchoices[0]['name'], 440, 10, 150, 60)
       
    # The button for player 2
    if playerchoices[1]['powerUsed']:
        fill(110)
    else:
        fill(255)
    rect(440, 80, 150, 60, 10)
    fill(0)
    text(playerchoices[1]['name'], 440, 80, 150, 60)

    # The button for player 3
    if len(playerchoices) >= 3:
        if playerchoices[2]['powerUsed']:
            fill(110)
        else:
            fill(255)
        rect(440, 150, 150, 60, 10)
        fill(0)
        text(playerchoices[2]['name'], 440, 150, 150, 60)  

    # The button for player 4
    if len(playerchoices) >= 4:
        if playerchoices[3]['powerUsed']:
            fill(110)
        else:
            fill(255)      
        rect(440, 220, 150, 60, 10)
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
    # textAlign(CENTER, CENTER)
    textFont(loadFont('BentonSans-17.vlw'))
    text(name, x, y, w, h)

def powerupScreen():
    global screen1, screen2, screen3, screen4, screen5, screen6
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
    button(210, 300, 150, 50, Stones['name'])
    button(420, 90, 150, 50, Venom['name'])
    button(420, 160, 150, 50, Loki['name'])
    button(420, 230, 150, 50, Ultron['name'])
    button(420, 300, 150, 50, Thanos['name'])
    image(loadImage('back.png'), 500, 20, 51, 51)
    
def powerup(power, picture, name):
    global screen1, screen2, screen3, screen4, screen5, screen6
    screen1 = False
    screen2 = False
    screen3 = False
    screen4 = False
    screen5 = True
    
    # Background colour:
    background(220)
    
    # Back button:
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

def stonePower(power, name):
    global screen1, screen2, screen3, screen4, screen5
    screen1 = False
    screen2 = False
    screen3 = False
    screen4 = False
    screen5 = True
    
    # Background colour:
    background(220)
    
    # Back button:
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
    text(power, 20, 100, 550, 300)
    
    


def ThanosArm ():
    global screen1, screen2, screen3, screen4, screen5, screen6, pointer, wheel, rotation_speed, rotate_counter, is_slowing, rotation, deg
    screen1 = False
    screen2 = False
    screen3 = False
    screen4 = False
    screen5 = False
    screen6 = True

    background(255)
    noStroke()


    while rotation_speed > 0:
        if is_slowing:
            rotation_speed -= 0.1
        else:
            rotation_speed += deg

        if rotation_speed >= 25:
            is_slowing = True

    
        

        rotation += rotation_speed
        # Push, pop keep transforms seperated from the rest of the draw function
        pushMatrix()
        # Draw the wheel and the pointer
        image(pointer, width/2 - pointer.width/2, height/2 - pointer.height/2)
        translate(width/2, height/2)
        rotateZ(radians(rotation))
        image(wheel, -wheel.width/2, -wheel.height/2)
        popMatrix()
        
    # Draw the button
    pushMatrix()
    rect(342.5, 0, 150, 24)
    textAlign(CENTER, CENTER)
    fill(255)
    textSize(20)
    text('Test your luck!', 342.5, 0, 150, 24)
    popMatrix()

    

def mouseClicked():
    redraw()  
    
def draw():
    global deg, is_slowing, rotation, rotation_speed
    if mouseButton == LEFT:
        if screen1:
            characterKiezer()
        
        elif screen2:
            print(choices)
            if 210 < mouseX < 360 and 300 < mouseY < 350:
                if len(playerchoices) < 2:
                    characterKiezer()
                    for character in choices:
                        character['notChosen'] = True

                else:
                    powerupDice()
                
                
            elif len(playerchoices) < 4:
                for charachter in choices:
                    if charachter['notChosen'] and mouseX >= charachter['rectangle'][0] and mouseX <= charachter['rectangle'][2] + charachter['rectangle'][0]  and mouseY >= charachter['rectangle'][1] and mouseY <= charachter['rectangle'][3] + charachter['rectangle'][1] :
                        (playerchoices.append(charachter)) # add character to selectedlist
                        fill(100)  
                        rect(charachter['rectangle'][0], charachter['rectangle'][1], charachter['rectangle'][2], charachter['rectangle'][3],charachter['rectangle'][4])
                        charachter['notChosen'] = False


                for i in range(len(playerchoices)):
                    fill(135)
                    rect(420,90+(50 * i),150,50)
                    fill(0)
                    text(playerchoices[i]['name'] ,420,90+(50 * i),150,50)
                    # if len(playerchoices) == 4: # if 4 characters chosen, move to next gamestate / screen
                    #     powerupDice()    

        elif screen3:
            # Button player1
            if playerchoices[0]['powerUsed'] or 440 < mouseX < 590 and 10 < mouseY < 70:
                Rect(440, 10, 150, 60, 100)
                fill(0)
                text(playerchoices[0]['name'], 440, 10, 150, 60)
                playerchoices[0]['powerUsed'] = True
                
            # Button player2
            if 440 < mouseX < 590 and 80 < mouseY < 140:
                Rect(440, 80, 150, 60, 100)
                fill(0)
                text(playerchoices[1]['name'], 440, 80, 150, 60)
                playerchoices[1]['powerUsed'] = True

            # Button player3
            if 440 < mouseX < 590 and 150 < mouseY < 210:
                if len(playerchoices) >= 3:
                    Rect(440, 150, 150, 60, 100)
                    fill(0)
                    text(playerchoices[2]['name'], 440, 150, 150, 60)  
                    playerchoices[2]['powerUsed'] = True
      
            # Button player4
            if 440 < mouseX < 590 and 220 < mouseY < 280:
                if len(playerchoices) >= 4:
                    Rect(440, 220, 150, 60, 100)
                    fill(0)
                    text(playerchoices[3]['name'], 440, 220, 150, 60) 
                    playerchoices[3]['powerUsed'] = True 

            if 10 < mouseX < 160 and 10 < mouseY < 70:
                number = randint(1,6) # generating a random Integer
                dice = loadImage(str(number) + "d.png") #loading the image in
                image(dice,170,10,60,60) # drawing the image   
                
            if 10 < mouseX < 160 and 80 < mouseY < 140:
                number2 = randint(1,6) # generating a random Integer
                diceInf = loadImage(str(number2) + ".jpg") #loading the image in
                image(diceInf,170,80,36,60) # drawing the image
           
            if 10 < mouseX < 160 and 150 < mouseY < 210:
                powerupScreen() 
            if 10 < mouseX < 160 and 220 < mouseY < 260:
                ThanosArm() 

                
        elif screen4:
            # buttons van de powerup screen:
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
            elif 210 < mouseX < 360 and 300 < mouseY < 350:
                stonePower(Stones['power'], Stones['name'])
            elif 420 < mouseX < 570 and 90 < mouseY < 140:
                powerup(Venom['power'], Venom['picture'], Venom['name'])
            elif 420 < mouseX < 570 and 160 < mouseY < 210:
                powerup(Loki['power'], Loki['picture'], Loki['name'])
            elif 420 < mouseX < 570 and 230 < mouseY < 280:
                powerup(Ultron['power'], Ultron['picture'], Ultron['name'])
            elif 420 < mouseX < 570 and 300 < mouseY < 350:
                powerup(Thanos['power'], Thanos['picture'], Thanos['name'])
            
            elif 500 < mouseX < 550 and 20 < mouseY < 70:
                powerupDice()
 
        elif screen5:
            # back button:
            if 500 < mouseX < 550 and 20 < mouseY < 70:
                powerupScreen()
        
        elif screen6:
            if mouseX > 342.5 and mouseX < 492.5 and mouseY > 0 and mouseY < 24:
                is_slowing = False
                rotation = 0
                rand = int(random(1, 4))
                rand2 = int(random(1, 90))
                rand_usage = rand * 90 + rand2
                # Set the degree at which the W should point, and devide it through 1000
                deg = (rand_usage / 420.0)#blaze it
                rotation_speed = 0.1
                ThanosArm()
 
 
 
 
