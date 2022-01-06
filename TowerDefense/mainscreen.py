def drawLeftMenu(img1, img2, img3):
    image(img1, 50, 50, 92, 101)
    image(img2, 167, 50, 92, 101)
    image(img3, 284, 50, 92, 101)
    
def drawExit():
    global img_exit
    img_exit = loadImage('exit.png')
    image(img_exit, 50, 50, 92, 101)
    
def drawTroopsButton():
    global img_btn_troops
    img_btn_troops = loadImage('btn_troops.png')
    image(img_btn_troops, 58, 655, 204, 87)
