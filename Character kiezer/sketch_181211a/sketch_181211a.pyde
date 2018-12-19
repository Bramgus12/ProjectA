
Spiderman = {'name' : 'Spiderman', 'rectangle' : [30, 90, 150, 50]}                     
Hulk = {'name' : 'Hulk','rectangle' : [30, 160, 150, 50]}
BlackPanther = {'name' :'Black Panther','rectangle' : [30, 230, 150, 50]}
DrStrange = {'name' : 'Doctor Strange','rectangle' : [30, 300, 150, 50]}
Thor = {'name' : 'Thor','rectangle' : [210, 90, 150, 50]}
IronMan = {'name' :'Iron Man','rectangle' : [210, 160, 150, 50]}
CptnAmerica = {'name' :'Captain America','rectangle' : [210, 230, 150, 50]}
 
choices =[Spiderman, Hulk, BlackPanther, DrStrange, Thor, IronMan, CptnAmerica]
 
playerchoices = []
 
def choice():
 
   
    # background colour:
    background(220)
   
    fill(0)
    textSize(25)
    text('Choose your charachter', 150, 60)
   
    # rectangles' colour:
    fill(255)
    rect(30, 90, 150, 50)
    rect(30, 160, 150, 50)
    rect(30, 230, 150, 50)
    rect(30, 300, 150, 50)
   
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
 
   
        
 
 
def setup():
    # screen width, height:
    size(900, 800)
   
    # noStroke()
    choice()
 
 
# def playerOne(rect):
#         fill(235)
#         rect(420,90,150,50)
 
def draw():
    pass
#     global choices,playerchoices
#     if mousePressed and mouseButton == LEFT:
#         for charachter in choices:
#             if mouseX >= charachter['rectangle'][0] and mouseX <= charachter['rectangle'][2] + charachter['rectangle'][0]  and mouseY >= charachter['rectangle'][1] and mouseY <= charachter['rectangle'][3] + charachter['rectangle'][1] :
#                 (playerchoices.append(charachter))
#             fill(187)  
#         for i in range(len(playerchoices)):
#             rect(420,90+(50 * i),150,50)
 
def mousePressed():
    global choices,playerchoices
    print(choices)
    if mouseButton == LEFT:
        if len(playerchoices) < 4:
            for charachter in choices:
                if mouseX >= charachter['rectangle'][0] and mouseX <= charachter['rectangle'][2] + charachter['rectangle'][0]  and mouseY >= charachter['rectangle'][1] and mouseY <= charachter['rectangle'][3] + charachter['rectangle'][1] :
                    (playerchoices.append(charachter))
            for i in range(len(playerchoices)):
                fill(135)
                rect(420,90+(50 * i),150,50)
                fill(190)
                text(playerchoices[i]['name'] ,420,90+(50 * i),150,50)
                     
