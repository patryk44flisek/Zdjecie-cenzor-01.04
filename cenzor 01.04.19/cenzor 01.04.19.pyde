add_library('pdf')
global zapis
global img
zapis = 0
def setup():
    global img
    img = loadImage("photo.jpg")
    size(284, 365)
    global bot
    global star
    smooth()
    star=loadShape("mous.svg")
def draw():
    shape(star)
    background(102)
    image(img, 0, 0)
    print(mouseX,mouseY)
    rect(56, 158, 170, 40)
    fill(0,0,0)
    if keyPressed:
        if key == 'S' or key == 's':
            beginRecord(PDF, "cenzor.pdf")
            zapis=1
            global img
            global test
            global zapis
if zapis==1:
    endRecord()
    exit()
    


      
