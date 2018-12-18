# Characters'/enemies' power-ups, names and pictures:
Spiderman = {'name' : 'Spiderman', 'picture' : 'Spiderman.jpg', 'power' : "Spiderman's power-up is called Webzip. When he uses his power-up, he can move players. The players will be placed 3 steps behind Spiderman. Webzip has a range of 4 spots in front of Spiderman."}
Hulk = {'name' : 'Hulk', 'picture' : 'Hulk.jpg', 'power' : "Hulk's power-up is called Smash. When he uses his power-up, he blows away all players within a range of 3 steps. Smash blows them 3 steps forward if the players are standing in front of him, and 3 steps backward if the players are standing behind him."}
BlackPanther = {'name' : 'Black Panther', 'picture' : 'BlackPanther.jpg', 'power' : "Black Panther's power-up is called Kinetic Energy. When he uses his power-up, he blows away all players within a range of 3 steps. Smash blows them 3 steps forward if the players are standing in front of him, and 3 steps backward if the players are standing behind him."}
DrStrange = {'name' : 'Doctor Strange', 'picture' : 'DoctorStrange.jpg', 'power' : "Doctor Strange's power is called Clone Illusion. When he uses his power-up, he creates a clone of himself. Every player who tries to attack Doctor Strange's clone goes back to his own checkpoint. The power-up stays activated for 3 rounds."}
Thor = {'name' : 'Thor', 'picture' : 'Thor.jpg', 'power' : "Thor's power-up is called Hammer: Mjolnir. By swinging his hammer, Thor can move 6 steps forward."}
IronMan = {'name' : 'Iron Man', 'picture' : 'IronMan.jpg', 'power' : "Iron Man's power-up is called Second Suit Roadblock. He can call a second suit to block one upcoming player. After that happens, the suit gets destroyed."}
CptnAmerica = {'name' : 'Captain America', 'picture' : 'CaptainAmerica.jpg', 'power' : "Captain America's power-up is called Shield. This is a passive power-up: it makes the player immune to every hero's power-up except Webzip and Clone Illusion."}
Venom = {'name' : 'Venom', 'picture' : 'Venom.png', 'power' : 'You are stuck on the B platform and are not allowed to move for 2 rounds.'}
Loki = {'name' : 'Loki', 'picture' : 'Loki.jpg', 'power' : 'For one turn the amount you throw will set you back rather than forward. For example, if you throw 4, you will have to go 4 steps back.'}
Ultron = {'name' : 'Ultron', 'picture' : 'Ultron.jpg', 'power' : 'You will take 1 or 2 steps less on your next throw. This depends on the B platform you land on.'}
Thanos = {'name': 'Thanos', 'picture' : 'Thanos.jpg', 'power' : "Thanos gets spinned when a player enters his area. After the first player enters Thanos' area, Thanos spins every 3 rounds. He will point at three spots. When you land on one of the 3 spots Thanos is pointing at, you must go back to your checkpoint. You cannot get out of Thanos' area. If someone tries to get you out of Thanos' area, the furthest place back where you can go is the checkpoint in Thanos' area."}

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
    global screen1, screen2
    screen1 = True
    screen2 = False
    
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
    global screen1, screen2
    screen1 = False
    screen2 = True
    
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
    
def setup():
    # Screen width, height, font of all the text and powerup screen:
    size(600, 400)
    textFont(loadFont('BentonSans-17.vlw'))
    powerupScreen()
    
def draw():
    mousePressed()
   
def mousePressed():
    if mouseButton == LEFT:
            # This is what happens when you click on a name:
            if screen1:
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
            elif screen2:
                if 500 < mouseX < 550 and 20 < mouseY < 70:
                    powerupScreen()
    
