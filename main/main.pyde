from mainscreen import *
import random

currentScreen = 'MAIN-MENU'
lastScreen = 'MAIN-MENU'
currentRound = 'POINTS'
currentPlayer = 0
activePlayers = []
enteredPlayers = 0

## INPUT NAMES AND DICE
shuffled = False
gamer_one = ''
gamer_two = ''
gamer_three = ''
gamer_four = ''
gamer_names = [gamer_one, gamer_two, gamer_three, gamer_four]

currentEntering = 1
current_round = 0

tooltips = {'notEnoughPlayers': False}

players = {
               1: {
                   'name': '',
                   'health': 3,
                   'points': 10,
                   'cards': [],
                   'isDead': True
                   },
                2: {
                   'name': '',
                   'health': 3,
                   'points': 10,
                   'cards': [],
                   'isDead': True
                   },
                3: {
                   'name': '',
                   'health': 3,
                   'points': 10,
                   'cards': [],
                   'isDead': True
                   },
                4: {
                   'name': '',
                   'health': 3,
                   'points': 10,
                   'cards': [],
                   'isDead': True
                   }
               }
   
def setup():
    size(1920, 1080)
    
    ## PLAYERCARDS
    global img_playercard, img_playercard_dead
    img_playercard = loadImage('playercard.png')
    img_playercard_dead = loadImage('playercard_dead.png')
    
    ## FONT
    global font_kabel
    font_kabel = loadFont('LeelawadeeUI-Bold-48.vlw')

    
    
    ## CURSOR
    global img_cursor
    img_cursor = loadImage('cursor.png')
    
    ## BACKGROUND
    global img_bg, img_logo
    img_bg = loadImage('background.png')
    img_logo = loadImage('logo.png')
    
    ## CURRENT ROUND
    global img_round
    img_round = loadImage('round.png')
    
    ## LEFT MENU
    global img_exit, img_settings, img_rules
    img_exit = loadImage('exit.png')
    img_settings = loadImage('settings.png')
    img_rules = loadImage('rules.png')
    
    ## BUTTONS
    global img_btn_back, img_btn_cancel, img_btn_exit, img_btn_cards, img_btn_next, img_btn_shuffle
    img_btn_back = loadImage('btn_back.png')
    img_btn_cancel = loadImage('btn_cancel.png')
    img_btn_exit = loadImage('btn_exit.png')
    img_btn_cards = loadImage('btn_cards.png')
    img_btn_next = loadImage('btn_next.png')
    img_btn_shuffle = loadImage('btn_shuffle.png')

    global img_btn_on, img_btn_off, img_btn_low, img_btn_medium, img_btn_high
    img_btn_on = loadImage('btn_on.png')
    img_btn_off = loadImage('btn_off.png')
    img_btn_low = loadImage('btn_low.png')
    img_btn_medium = loadImage('btn_medium.png')
    img_btn_high = loadImage('btn_high.png') 
    
    global img_btn_cardsmall, img_btn_number
    img_btn_cardsmall = loadImage('btn_cardsmall.png')
    img_btn_number = loadImage('btn_number.png')
    
    ### --- NAME INPUT --- ###
    # input gamer names
    global allowed_characters
    allowed_characters = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", \
                          "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", \
                          "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
    
    # create random number between 2 and 12
    global min_number, max_number, number
    min_number = 2
    max_number = 12
    number = random.randint(min_number, max_number)
    
    # loading dice images
    global img_dice
    img_dice_1 = loadImage('dices/dice_1.png')
    img_dice_2 = loadImage('dices/dice_2.png')
    img_dice_3 = loadImage('dices/dice_3.png')
    img_dice_4 = loadImage('dices/dice_4.png')
    img_dice_5 = loadImage('dices/dice_5.png')
    img_dice_6 = loadImage('dices/dice_6.png')
    img_dice = [img_dice_1, img_dice_2, img_dice_3, img_dice_4, img_dice_5, img_dice_6]
    
def addPlayers():
    global gamer_names, players, activePlayers, enteredPlayers
    adding = 1

    for i in range(0, len(gamer_names)):
        if gamer_names[i] != '':
            players[adding]['name'] = gamer_names[i]
            players[adding]['isDead'] = False
            enteredPlayers+=1
            activePlayers.append(adding)
            adding+=1

def drawTooltip(title, message):
    fill('#131a2a')
    noStroke()
    rect(460, 210, 1000, 200, 10)
    textAlign(CENTER, CENTER)
    textFont(font_kabel, 32)
    fill('#ff2746')
    text(title, 960, 262)
    fill('#ffffff')
    text(message, 960, 335)

def drawInputEnterNames():
    ### 1
    if currentEntering == 1:
        fill('#212b44')
    else:
        fill('#1a2236')
    noStroke()
    rect(460, 450, 300, 75, 10)
    rect(810, 450, 650, 75, 10)
    textAlign(CENTER, CENTER)
    if currentEntering == 1:
        fill('#1dc2ce')
    else:
        fill('#939393')
    textFont(font_kabel, 32)
    text('PLAYER1', 612, 487.5)
    if not len(gamer_names) < 1:
        text(gamer_names[0], 1115, 487.5)
    
    ## 2
    if currentEntering == 2:
        fill('#212b44')
    else:
        fill('#1a2236')
    noStroke()
    rect(460, 550, 300, 75, 10)
    rect(810, 550, 650, 75, 10)
    textAlign(CENTER, CENTER)
    if currentEntering == 2:
        fill('#1dc2ce')
    else:
        fill('#939393')
    textFont(font_kabel, 32)
    text('PLAYER2', 612, 587.5)
    if not len(gamer_names) < 2:
        text(gamer_names[1], 1115, 587.5)
    
    ## 3
    if currentEntering == 3:
        fill('#212b44')
    else:
        fill('#1a2236')
    noStroke()
    rect(460, 650, 300, 75, 10)
    rect(810, 650, 650, 75, 10)
    textAlign(CENTER, CENTER)
    if currentEntering == 3:
        fill('#1dc2ce')
    else:
        fill('#939393')
    textFont(font_kabel, 32)
    text('PLAYER3', 612, 687.5) 
    if not len(gamer_names) < 3:
        text(gamer_names[2], 1115, 687.5)
    
    ## 4
    if currentEntering == 4:
        fill('#212b44')
    else:
        fill('#1a2236')
    noStroke()
    rect(460, 750, 300, 75, 10)
    rect(810, 750, 650, 75, 10)
    textAlign(CENTER, CENTER)
    if currentEntering == 4:
        fill('#1dc2ce')
    else:
        fill('#939393')
    textFont(font_kabel, 32)
    text('PLAYER4', 612, 787.5) 
    if not len(gamer_names) < 4:
        text(gamer_names[3], 1115, 787.5)
    
def drawPlayerList():
    global gamer_names
    text('1. ' + gamer_names[0], width/2, height/2.1)
    text('2. ' + gamer_names[1], width/2, height/1.8)
    text('3. ' + gamer_names[2], width/2, height/1.57)
    text('4. ' + gamer_names[3], width/2, height/1.4)
    
def drawThrowDiceBtn():
    global img_round
    image(img_round, width/2.36, height/1.15, 290, 110)
    fill(255)
    textFont(font_kabel, 25)
    text('THROW DICE', width/2, height/1.08)
    
def changeCursor():
    global img_cursor
    cursor(img_cursor)
    

    
def drawCredits():
    fill(255)
    textSize(50)
    text('THIS GAME AND SUPPLEMENTARY SOFTWARE WERE DEVELOPED BY: ', 960, 340)
    textFont(font_kabel)
    fill(255)
    textSize(60)
    text('LUCAS PRINS\n SVEN GROENEVELD\n ANTON SHI\n SI WAI PANG\n JOOST REINTJES', 960, 530)
    
# displays the dice numbers when user throws the dice
def throwDice():
    global img_dice, number
    if number == 2:
        image(img_dice[0], width/3, height/2.2)
        image(img_dice[0], width/1.9, height/2.2)
    elif number == 3:
        image(img_dice[1], width/3, height/2.2)
        image(img_dice[0], width/1.9, height/2.2)
    elif number == 4:
        image(img_dice[1], width/3, height/2.2)
        image(img_dice[1], width/1.9, height/2.2)
    elif number == 5:
        image(img_dice[2], width/3, height/2.2)
        image(img_dice[1], width/1.9, height/2.2)
    elif number == 6:
        image(img_dice[2], width/3, height/2.2)
        image(img_dice[2], width/1.9, height/2.2)
    elif number == 7:
        image(img_dice[3], width/3, height/2.2)
        image(img_dice[2], width/1.9, height/2.2)
    elif number == 8:
        image(img_dice[3], width/3, height/2.2)
        image(img_dice[3], width/1.9, height/2.2)
    elif number == 9:
        image(img_dice[4], width/3, height/2.2)
        image(img_dice[3], width/1.9, height/2.2)
    elif number == 10:
        image(img_dice[4], width/3, height/2.2)
        image(img_dice[4], width/1.9, height/2.2)
    elif number == 11:
        image(img_dice[5], width/3, height/2.2)
        image(img_dice[4], width/1.9, height/2.2)
    elif number == 12:
        image(img_dice[5], width/3, height/2.2)
        image(img_dice[5], width/1.9, height/2.2)

def nextPlayer():
    global img_round
    image(img_round, width/2.36, height/1.15, 290, 110)
    fill(255)
    textAlign(CENTER)
    if current_round < 4:
        text('NEXT PLAYER', width/2, height/1.08)
    else:
        text('START GAME', width/2, height/1.08)
        
# displays the text: 'user throws number'
def playerThrowsNumber():
    global gamer_names, current_round, number
    if current_round == 0:
        text(gamer_names[0] + ' throws ' + str(number), width/2, height/2.5)
    elif current_round == 1:
        text(gamer_names[1] + ' throws ' + str(number), width/2, height/2.5)
    elif current_round == 2:
        text(gamer_names[2] + ' throws ' + str(number), width/2, height/2.5)
    elif current_round == 3:
        text(gamer_names[3] + ' throws ' + str(number), width/2, height/2.5)
    else:
        text('Please start game', width/2, height/2.5)
    
def drawPlayerCards():
    if players[1]['isDead'] == False:
        image(img_playercard, 50, 770)
        if currentPlayer == 1:
            drawCurrentPlayer(62, 1042)
    elif players[1]['isDead'] == True:
        image(img_playercard_dead, 50, 770)
        
    if players[2]['isDead'] == False:
        image(img_playercard, 50 + 430 + 30, 770)
        if currentPlayer == 2:
            drawCurrentPlayer(521, 1042)
    elif players[2]['isDead'] == True:
        image(img_playercard_dead, 50 + 430 + 30, 770)
        
    if players[3]['isDead'] == False:
        image(img_playercard, 50 + 430*2 + 30*2, 770)
        if currentPlayer == 3:
            drawCurrentPlayer(983, 1042)
    elif players[3]['isDead'] == True:
        image(img_playercard_dead, 50 + 430*2 + 30*2, 770)
        
    if players[4]['isDead'] == False:
        image(img_playercard, 50 + 430*3 + 30*3, 770)
        if currentPlayer == 4:
            drawCurrentPlayer(1445, 1042)
    elif players[4]['isDead'] == True:
        image(img_playercard_dead, 50 + 430*3 + 30*3, 770)
        
def changeloghover():
    
    if currentScreen == 'MAIN-MENU':
        if mouseX > 20 and mouseX < 164 and mouseY > 1035 and mouseY < 1065:
            fill(255)
            rect(20, 1064 , 145, 4)
            
    if mouseX > 630 and mouseX < 920 and mouseY > 535 and mouseY < 651:
            textFont(font_kabel)
            fill(255)
            textSize(32)
            textAlign(CENTER)
            text("PLAY", 772, 600)
            
    if mouseX > 1020 and mouseX < 1310 and mouseY > 535 and mouseY < 651:
        textFont(font_kabel)
        fill(255)
        textSize(32)
        textAlign(CENTER)
        text("SETTINGS", 1165, 600)
            
    if mouseX > 630 and mouseX < 920 and mouseY > 710 and mouseY < 826:
        textFont(font_kabel)
        fill(255)
        textSize(32)
        textAlign(CENTER)
        text("CREDITS", 772, 775)
       
            
    if mouseX > 1020 and mouseX < 1310 and mouseY > 710 and mouseY < 826:
        textFont(font_kabel)
        fill(255)
        textSize(32)
        textAlign(CENTER)
        text("CONTACT", 1165, 775)
            
        
    
def drawCurrentPlayer(x,y):
    fill('#1dc2ce')
    noStroke()
    rect(x, y, 409, 10, 10)
    
def drawRound(title):
    image(img_round, 815, 47)
    textFont(font_kabel, 32)
    textAlign(CENTER)
    fill('#1dc2ce')
    text(title, 960, 112)
    
def drawBackground():
    image(img_bg, 0, 0, width, height)
    
def drawCardsButton():
    image(img_btn_cards, 1649, 655, 204, 87)    
    
def drawCardsButtonSmall(x, y):
    image(img_btn_cardsmall, x, y)
    
def drawNextButton():
    image(img_btn_next, 1666, 50, 204, 87)
    
def drawNextButtonBottom():
    image(img_btn_next, 1260, 875, 204, 87)

def drawShuffleButton():
    image(img_btn_shuffle, 460, 875, 204, 87)

def drawBackButton():
    image(img_btn_back, 1666, 50, 204, 87)
    
def drawBackButtonLeft():
    image(img_btn_back, 50, 50, 204, 87)
    
def drawLogo():
    image(img_logo, 542, 150)

def drawExitButton():
    image(img_btn_exit, 725, 550, 204, 87)

def drawCancelButton():
    image(img_btn_cancel, 975, 550, 204, 87)
    
def drawNumberBackground(x, y):
    image(img_btn_number, x, y)

def drawPlayerStats():
    textAlign(LEFT)
    textFont(font_kabel, 32)
    fill('#1dc2ce')
    
    if bool(players[1]['name']) != False and players[1]['isDead'] == False:
        text(players[1]['name'], 110, 830)
        textSize(24)
        text('Points:', 110, 880)
        drawNumberBackground(325, 850)
        fill('#9d9ebf')
        textAlign(CENTER)
        text(players[1]['points'], 377, 880)
        fill('#1dc2ce')
        drawNumberBackground(325, 900)
        fill('#9d9ebf')
        textAlign(LEFT)
        text(players[1]['health'], 370, 930)
        text('-', 340, 930)
        text('+', 400, 930)
        fill('#1dc2ce')
        text('Health:', 110, 930)
        drawCardsButtonSmall(325, 955)      
        
    if bool(players[2]['name']) != False and players[2]['isDead'] == False:
        textSize(32)
        text(players[2]['name'], 570, 830)
        textSize(24)
        text('Points:', 570, 880)
        drawNumberBackground(785, 850)
        fill('#9d9ebf')
        textAlign(CENTER)
        text(players[2]['points'], 837, 880)
        fill('#1dc2ce')
        drawNumberBackground(785, 900)
        fill('#9d9ebf')
        textAlign(LEFT)
        text(players[2]['health'], 830, 930)
        text('-', 800, 930)
        text('+', 860, 930)
        fill('#1dc2ce')
        text('Health:', 570, 930)
        drawCardsButtonSmall(785, 955) 
        
    if bool(players[3]['name']) != False and players[3]['isDead'] == False:
        textSize(32)
        text(players[3]['name'], 1035, 830)
        textSize(24)
        text('Points:', 1035, 880)
        drawNumberBackground(1245, 850)
        fill('#9d9ebf')
        textAlign(CENTER)
        text(players[3]['points'], 1296, 880)
        fill('#1dc2ce')
        drawNumberBackground(1245, 900)
        fill('#9d9ebf')
        textAlign(LEFT)
        text(players[3]['health'], 1291, 930)
        text('-', 1260, 930)
        text('+', 1320, 930)
        fill('#1dc2ce')
        text('Health:', 1035, 930)
        drawCardsButtonSmall(1245, 955) 
        
    if bool(players[4]['name']) != False and players[4]['isDead'] == False:
        textSize(32)
        text(players[4]['name'], 1495, 830)
        textSize(24)
        text('Points:', 1495, 880)
        drawNumberBackground(1705, 850)
        fill('#9d9ebf')
        textAlign(CENTER)
        text(players[4]['points'], 1754, 880)
        fill('#1dc2ce')
        drawNumberBackground(1705, 900)
        fill('#9d9ebf')
        textAlign(LEFT)
        text(players[4]['health'], 1750, 930)
        text('-', 1720, 930)
        text('+', 1780, 930)
        fill('#1dc2ce')
        text('Health:', 1495, 930)
        drawCardsButtonSmall(1705, 955) 
    
def drawMusic():
    fill('#1a2236')
    noStroke()
    rect(460, 450, 300, 75, 10)
    textAlign(CENTER, CENTER)
    fill('#1dc2ce')
    textFont(font_kabel, 32)
    text('MUSIC', 612, 487.5)
    
def drawVolume():
    fill('#1a2236')
    noStroke()
    rect(460, 550, 300, 75, 10)
    textAlign(CENTER, CENTER)
    fill('#1dc2ce')
    textFont(font_kabel, 32)
    text('VOLUME', 612, 587.5)

def drawNotifications():
    fill('#1a2236')
    noStroke()
    rect(460, 650, 300, 75, 10)
    textAlign(CENTER, CENTER)
    fill('#1dc2ce')
    textFont(font_kabel, 32)
    text('NOTIFICATIONS', 612, 687.5)
    
def drawSoundEffects():
    fill('#1a2236')
    noStroke()
    rect(460, 750, 300, 75, 10)
    textAlign(CENTER, CENTER)
    fill('#1dc2ce')
    textFont(font_kabel, 32)
    text('SOUNDEFFECTS', 612, 787.5)        
            
def drawSoundButtons():     
    image(img_btn_on, 950, 450, 204, 87)
    image(img_btn_off, 1200, 450, 204, 87)
    image(img_btn_low, 950, 550, 204, 87)
    image(img_btn_medium, 1200, 550, 204, 87)
    image(img_btn_high, 1450, 550, 204, 87)    
    image(img_btn_on, 950, 650, 204, 87)
    image(img_btn_off, 1200, 650, 204, 87)    
    image(img_btn_on, 950, 750, 204, 87)
    image(img_btn_off, 1200, 750, 204, 87)
    
def drawStartMenu():
    image(img_round, 630, 535)
    image(img_round, 1020, 535)
    image(img_round, 630, 710)
    image(img_round, 1020, 710)
    
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(32)
    textAlign(CENTER)
    text("PLAY", 772, 600)
    
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(32)
    textAlign(CENTER)
    text("SETTINGS", 1165, 600)
    
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(32)
    textAlign(CENTER)
    text("CREDITS", 772, 775)
    
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(32)
    textAlign(CENTER)
    text("CONTACT", 1165, 775)
    
    fill(255)
    textSize(24)
    textAlign(LEFT)
    text('VERSION 0.0', 20, 1060)
    


## BUTTONS
def mousePressed():
    
    ## GLOBALS
    global currentRound, currentScreen, currentPlayer, activePlayers, enteredPlayers, currentEntering
    global player_list, currentScreen, number, current_round, lastScreen, gamer_names, shuffled, tooltips
    
    ## MAIN MENU
    if currentScreen == 'MAIN-MENU':
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 630 and mouseX < 920 and mouseY > 535 and mouseY < 651:
            currentScreen = 'INPUT-NAMES'
            lastScreen = 'MAIN-MENU'
        if mouseX > 1020 and mouseX < 1310 and mouseY > 535 and mouseY < 651:
            currentScreen = 'SETTINGS'
            lastScreen = 'MAIN-MENU'
        if mouseX > 630 and mouseX < 920 and mouseY > 710 and mouseY < 826:
            currentScreen = 'CREDITS'
            lastScreen = 'MAIN-MENU'
        if mouseX > 1020 and mouseX < 1310 and mouseY > 710 and mouseY < 826:
            currentScreen = 'CONTACT'
            lastScreen = 'MAIN-MENU'
        if mouseX > 20 and mouseX < 164 and mouseY > 1035 and mouseY < 1065:
            currentScreen ='Changelog'
            lastScreen = 'MAIN-MENU'
            
    playersAdded = 0
    for i in range(0, len(gamer_names)):
        if gamer_names[i] != '':
            playersAdded+=1
    
    ## INPUT NAMES
    if currentScreen == 'INPUT-NAMES':
        tooltips['notEnoughPlayers'] = False
        if mouseX > 50 and mouseX < 254 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = 'MAIN-MENU'
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137 and playersAdded >= 2: # NEXT BUTTON
            currentScreen = 'SHUFFLE'
            currentEntering = 0
            lastScreen = 'INPUT-NAMES'
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137 and playersAdded < 2:
            tooltips['notEnoughPlayers'] = True
        
        if mouseX > 810 and mouseX < 1460 and mouseY > 450 and mouseY < 525:
            currentEntering = 1 
        if mouseX > 810 and mouseX < 1460 and mouseY > 550 and mouseY < 625:
            currentEntering = 2
        if mouseX > 810 and mouseX < 1460 and mouseY > 650 and mouseY < 725:
            currentEntering = 3
        if mouseX > 810 and mouseX < 1460 and mouseY > 750 and mouseY < 825:
            currentEntering = 4
    
    if currentScreen == 'CONTACT':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = lastScreen
        
    if currentScreen == 'CREDITS':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = lastScreen
            
    ## SHUFFLE
    if currentScreen == 'SHUFFLE':
        if mouseX > 50 and mouseX < 254 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = 'INPUT-NAMES'
            ## SHUFFLE
        if currentScreen == 'SHUFFLE':
            if mouseX > 50 and mouseX < 254 and mouseY > 50 and mouseY < 137 and shuffled == False: # BACK BUTTON
                currentScreen = 'INPUT-NAMES'
            if mouseX > 460 and mouseX < 664 and mouseY > 875 and mouseY < 962: # SHUFFLE BUTTON
                shuffled = True
                gamer_names = list(filter(None, gamer_names))      
                random.shuffle(gamer_names)
            if mouseX > 1260 and mouseX < 1464 and mouseY > 875 and mouseY < 962: # NEXT BUTTON
                addPlayers()
                currentScreen = 'MAIN' 
                lastScreen = 'MAIN'
                currentPlayer = 1
    
    ## MAIN SCREEN
    if currentScreen == 'MAIN':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # NEXT BUTTON
            currentPlayer +=1
            
            if currentPlayer > activePlayers[-1]:
                    if currentRound == 'POINTS':
                        currentRound = 'STEPS'
                        currentPlayer = 1
                        for i in range (0, enteredPlayers):
                            if players[i+1]['isDead'] == False:
                                currentPlayer = i + 1
                                break
                    else:
                        currentRound = 'POINTS'
                        currentPlayer = 1
                        for i in range (0, enteredPlayers):
                            if players[i+1]['isDead'] == False:
                                currentPlayer = i + 1
                                break
                            
            if players[currentPlayer]['isDead'] == True:
                for i in range(0, enteredPlayers):
                    if currentPlayer + i > enteredPlayers:
                        currentPlayer = 0
                    if players[currentPlayer + i]['isDead'] == False and currentPlayer + i <= enteredPlayers:
                        currentPlayer = currentPlayer + i
                        break
                
        if mouseX > 58 and mouseX < 262 and mouseY > 655 and mouseY < 742 and currentRound == 'POINTS': # TROOPS BUTTON
            currentScreen = 'TROOPS'
        if mouseX > 1649 and mouseX < 1853 and mouseY > 655 and mouseY < 742: # CARDS BUTTON
            currentScreen = 'CARDS'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            currentScreen = 'RULES'
        if mouseX > 325 and mouseX < 427 and mouseY > 955 and mouseY < 999: # PLAYER 1 CARDS BUTTON
            currentScreen = 'PLAYER 1 CARDS'
        
        if mouseX > 785 and mouseX < 887 and mouseY > 955 and mouseY < 999: # PLAYER 2 CARDS BUTTON
            currentScreen = 'PLAYER 2 CARDS'
        
        if mouseX > 1245 and mouseX < 1348 and mouseY > 955 and mouseY < 999: # PLAYER 3 CARDS BUTTON
            currentScreen = 'PLAYER 3 CARDS'
        
        if mouseX > 1705 and mouseX < 1807 and mouseY > 955 and mouseY < 999: # PLAYER 4 CARDS BUTTON
            currentScreen = 'PLAYER 4 CARDS'
       
        if mouseX > 336 and mouseX < 351 and mouseY > 915 and mouseY < 930: # PLAYER 1 MINUS BUTTON
            currentHealth = players[1]['health']
            if players[1]['health'] != 0:
                players[1]['health']-= 1
            if currentHealth - 1 == 0:
                players[1]['isDead'] = True
                index = activePlayers.index(1)
                del activePlayers[index]
            
                if currentPlayer + 1 > activePlayers[-1]:
                    if currentRound == 'POINTS':
                        currentRound = 'STEPS'
                        currentPlayer = 1
                        for i in range (0, enteredPlayers):
                            if players[i+1]['isDead'] == False:
                                currentPlayer = i + 1
                                break
                            else:
                                currentRound = 'POINTS'
                                currentPlayer = 1
                                for i in range (0, enteredPlayers):
                                    if players[i+1]['isDead'] == False:
                                        currentPlayer = i + 1
                                        break
                            
                for i in range(0, enteredPlayers):
                    if currentPlayer + i > len(activePlayers):
                        currentPlayer = 0
                    if players[currentPlayer + i]['isDead'] == False and currentPlayer + i <= enteredPlayers:
                        currentPlayer = currentPlayer + i
                        break
        
        if mouseX > 400 and mouseX < 415 and mouseY > 915 and mouseY < 930: # PLAYER 1 PLUS BUTTON
            if players[1]['health'] != 3:
                players[1]['health']+= 1
        
        if mouseX > 796 and mouseX < 811 and mouseY > 915 and mouseY < 930: # PLAYER 2 MINUS BUTTON
            currentHealth = players[2]['health']
            if players[2]['health'] != 0:
                players[2]['health']-= 1
            if currentHealth - 1 == 0:
                players[2]['isDead'] = True
                index = activePlayers.index(2)
                del activePlayers[index]
                if currentPlayer + 1 > activePlayers[-1]:
                    if currentRound == 'POINTS':
                        currentRound = 'STEPS'
                        currentPlayer = 1
                        for i in range (0, enteredPlayers):
                            if players[i+1]['isDead'] == False:
                                currentPlayer = i + 1
                                break
                            else:
                                currentRound = 'POINTS'
                                currentPlayer = 1
                                for i in range (0, enteredPlayers):
                                    if players[i+1]['isDead'] == False:
                                        currentPlayer = i + 1
                                        break
                            
                for i in range(0, enteredPlayers):
                    if currentPlayer + i > enteredPlayers:
                        currentPlayer = 0
                    if players[currentPlayer + i]['isDead'] == False and currentPlayer + i <= enteredPlayers:
                        currentPlayer = currentPlayer + i
                        break
        
        if mouseX > 860 and mouseX < 875 and mouseY > 915 and mouseY < 930: # PLAYER 2 PLUS BUTTON
            if players[2]['health'] != 3:
                players[2]['health']+= 1
        
        if mouseX > 1256 and mouseX < 1271 and mouseY > 915 and mouseY < 930: # PLAYER 3 MINUS BUTTON
            currentHealth = players[3]['health']
            if players[3]['health'] != 0:
                players[3]['health']-= 1
            if currentHealth - 1 == 0:
                players[3]['isDead'] = True
                index = activePlayers.index(3)
                del activePlayers[index]
                if currentPlayer + 1 > activePlayers[-1]:
                    if currentRound == 'POINTS':
                        currentRound = 'STEPS'
                        currentPlayer = 1
                        for i in range (0, enteredPlayers):
                            if players[i+1]['isDead'] == False:
                                currentPlayer = i + 1
                                break
                            else:
                                currentRound = 'POINTS'
                                currentPlayer = 1
                                for i in range (0, enteredPlayers):
                                    if players[i+1]['isDead'] == False:
                                        currentPlayer = i + 1
                                        break
                            
                for i in range(0, enteredPlayers):
                    if currentPlayer + i > enteredPlayers:
                        currentPlayer = 0
                    if players[currentPlayer + i]['isDead'] == False and currentPlayer + i <= enteredPlayers:
                        currentPlayer = currentPlayer + i
                        break
        
        if mouseX > 1320 and mouseX < 1335 and mouseY > 915 and mouseY < 930: # PLAYER 3 PLUS BUTTON
            if players[3]['health'] != 3:
                players[3]['health']+= 1
        
        if mouseX > 1716 and mouseX < 1731 and mouseY > 915 and mouseY < 930: # PLAYER 4 MINUS BUTTON
            currentHealth = players[4]['health']
            if players[4]['health'] != 0:
                players[4]['health']-= 1
            if currentHealth - 1 == 0:
                players[4]['isDead'] = True
                index = activePlayers.index(4)
                del activePlayers[index]
                if currentPlayer + 1 > activePlayers[-1]:
                    if currentRound == 'POINTS':
                        currentRound = 'STEPS'
                        currentPlayer = 1
                        for i in range (0, enteredPlayers):
                            if players[i+1]['isDead'] == False:
                                currentPlayer = i + 1
                                break
                            else:
                                currentRound = 'POINTS'
                                currentPlayer = 1
                                for i in range (0, enteredPlayers):
                                    if players[i+1]['isDead'] == False:
                                        currentPlayer = i + 1
                                        break
                            
                for i in range(0, enteredPlayers):
                    if currentPlayer + i > enteredPlayers:
                        currentPlayer = 0
                    if players[currentPlayer + i]['isDead'] == False and currentPlayer + i <= enteredPlayers:
                        currentPlayer = currentPlayer + i
                        break
        
        if mouseX > 1780 and mouseX < 1795 and mouseY > 915 and mouseY < 930: # PLAYER 4 PLUS BUTTON
            if players[4]['health'] != 3:
                players[4]['health']+= 1
            
    ## TROOP SCREEN
    elif currentScreen == 'TROOPS':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = 'MAIN'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            currentScreen = 'RULES'
            
    ## CARDS SCREEN
    elif currentScreen == 'CARDS':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = 'MAIN'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            currentScreen = 'RULES'
            
    ## EXIT SCREEN
    elif currentScreen == 'EXIT':
        if mouseX > 725 and mouseX < 929 and mouseY > 550 and mouseY < 637: # EXIT BUTTON
            exit() 
        if mouseX > 975 and mouseX < 1179 and mouseY > 550 and mouseY < 637: # CANCEL BUTTON
            currentScreen = lastScreen 
    
    ## SETTINGS SCREEN
    elif currentScreen == 'SETTINGS':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = lastScreen
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            currentScreen = 'RULES'
            
    ## RULES SCREEN
    elif currentScreen == 'RULES':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = 'MAIN'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            currentScreen = 'RULES'
            
    ## PLAYER 1 CARDS SCREEN
    elif currentScreen == 'PLAYER 1 CARDS':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = 'MAIN'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            currentScreen = 'RULES'
                 
    ## PLAYER 2 CARDS SCREEN
    elif currentScreen == 'PLAYER 2 CARDS':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = 'MAIN'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            currentScreen = 'RULES'
    
    ## PLAYER 3 CARDS SCREEN
    elif currentScreen == 'PLAYER 3 CARDS':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = 'MAIN'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            currentScreen = 'RULES'
    
    ## PLAYER 4 CARDS SCREEN
    elif currentScreen == 'PLAYER 4 CARDS':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = 'MAIN'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            currentScreen = 'RULES'
            
def keyPressed():
    global gamer_names, allowed_characters, currentScreen, currentEntering
    # input names
    if currentScreen == 'INPUT-NAMES':
        if key == TAB:
            if currentEntering == 4:
                currentEntering = 1
            else:
                currentEntering+=1
                
        if key == ENTER:
            if currentEntering == 4:
                currentEntering = 1
            else:
                currentEntering+=1
        
        if len(gamer_names[currentEntering-1]) < 15:
            if key in allowed_characters:
                gamer_names[currentEntering-1] += key
            if key == ' ':
                gamer_names[currentEntering-1] += ' '
        if key == BACKSPACE:
            gamer_names[currentEntering-1] = gamer_names[currentEntering-1][:-1]
        if key == DELETE:
            gamer_names[currentEntering-1] = ''           
      
## DRAW SCREENS
def draw():
    
    global img_cursor
    
    ## GLOBALS
    global currentRound, currentScreen, currentPlayer, activePlayers, shuffled, tooltips
    
    if currentScreen == 'MAIN-MENU':
        lastScreen = 'MAIN-MENU'
        drawBackground()
        drawLogo()
        drawStartMenu()
        drawExit()
        changeloghover()
   
    
    ## INPUT NAMES
    if currentScreen == 'INPUT-NAMES':
        drawBackground()
        drawRound('NAMES')
        drawNextButton()
        drawBackButtonLeft()
        drawInputEnterNames()
        
        fill('#1a2236')
        noStroke()
        rect(460, 300, 1000, 100, 10)
        textAlign(CENTER, CENTER)
        fill('#1dc2ce')
        textFont(font_kabel, 32)
        text('PLEASE ENTER YOUR NAMES', 960, 350)
        
        if tooltips['notEnoughPlayers'] == True:
            drawTooltip('NOT ENOUGH PLAYERS', 'YOU NEED ATLEAST 2 PLAYERS TO START THE GAME\nPLEASE ENTER MORE NAMES')
            
        
    if currentScreen == 'SHUFFLE':
        drawBackground()
        drawRound('SHUFFLE')
        if shuffled == False:
            drawBackButtonLeft()
        
        drawInputEnterNames()
        drawNextButtonBottom()
        drawShuffleButton()
        
        fill('#1a2236')
        noStroke()
        rect(460, 300, 1000, 100, 10)
        textAlign(CENTER, CENTER)
        fill('#1dc2ce')
        textFont(font_kabel, 32)
        text('DO YOU WANT TO SHUFFLE THE ORDER?', 960, 350)
    
    ## MAIN SCREEN
    if currentScreen == 'MAIN':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawPlayerCards()
        drawPlayerStats()
        drawNextButton()
        drawCardsButton()
        drawRound(currentRound)
        if currentRound == 'POINTS':
            drawTroopsButton()
            
            
     # Changelog       
    if currentScreen == 'Changelog':
        drawBackground()
        
    ## TROOPS SCREEN
    elif currentScreen == 'TROOPS':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawRound(currentRound)
        drawBackButton()
    
    ## CARDS SCREEN
    elif currentScreen == 'CARDS':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawRound(currentRound)
        drawBackButton()
    
    ## EXIT SCREEN
    elif currentScreen == 'EXIT':
        drawBackground()
        fill('#1a2236')
        noStroke()
        rect(460, 390, 1000, 300, 10)
        textAlign(CENTER, CENTER)
        fill('#1dc2ce')
        textFont(font_kabel, 32)
        text('DO YOU WANT TO EXIT?', 960, 480)
        drawExitButton()
        drawCancelButton()
    
    ## SETTINGS SCREEN
    elif currentScreen == 'SETTINGS':
        drawBackground()
        drawExit()
        drawBackButton()
        drawNotifications()
        drawVolume()
        drawMusic()
        drawSoundButtons()
        drawSoundEffects()
        drawRound('SETTINGS')
        
    elif currentScreen == 'CONTACT':
        drawBackground()
        drawRound('CONTACT')
        drawExit()
        drawBackButton()
        
    elif currentScreen == 'CREDITS':
        drawBackground()
        drawRound('CREDITS')
        drawExit()
        drawBackButton()
        drawCredits()
        
    ## RULES SCREEN
    elif currentScreen == 'RULES':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawBackButton()
        drawRound('RULES')
    
    ## PLAYER 1 CARDS SCREEN 
    elif currentScreen == 'PLAYER 1 CARDS':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawBackButton()
        drawRound(currentRound)
        
    ## PLAYER 1 CARDS SCREEN 
    elif currentScreen == 'PLAYER 2 CARDS':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawBackButton()
        drawRound(currentRound)
    
    ## PLAYER 1 CARDS SCREEN 
    elif currentScreen == 'PLAYER 3 CARDS':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawBackButton()
        drawRound(currentRound)
    
    ## PLAYER 1 CARDS SCREEN 
    elif currentScreen == 'PLAYER 4 CARDS':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawBackButton()
        drawRound(currentRound)
