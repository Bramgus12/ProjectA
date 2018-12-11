def setup():
    # Grootte van de venster en achtergrondkleur
    size(1600,900)
    background(255)
    
    # Avengers foto:
    Avengers = loadImage('Avengers.png')
    image(Avengers, 350, 100, 900, 350)
    
    # Uiterlijk van de tekst:
    fill(0)
    smooth(2)

def draw():
    # Font van tekst, grootte van tekst en tekst zelf:
    textFont(loadFont('Marvel.vlw'))
    textSize(90)
    text('Click anywhere to start', 425, 600)

        
