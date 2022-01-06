from mainscreen import *
from economy import *
from ui import *

import random

add_library("sound")    

currentScreen = 'MAIN-MENU'
lastScreen = 'MAIN-MENU'
currentRound = 'POINTS'
currentPlayer = 0
activePlayers = []
enteredPlayers = 0
amountGained = 0

## INPUT NAMES AND DICE
shuffled = False
gamer_one = ''
gamer_two = ''
gamer_three = ''
gamer_four = ''
gamer_names = [gamer_one, gamer_two, gamer_three, gamer_four]

currentEntering = 1
current_round = 0

# SHUFFLE
amountOne = 0
amountTwo = 0
thrownDice = False

# SETTINGS
isPlaying = True
notifications = True
soundfx = True

# TROOPS
troopSelected = ''
selectedTroopPoints = 0

diceGained = {
              1: {
                  'name': '',
                  'dice1': 0,
                  'dice2': 0,
                  'total': 0
                  },
              2: {
                  'name': '',
                  'dice1': 0,
                  'dice2': 0,
                  'total': 0
                  },
              3: {
                  'name': '',
                  'dice1': 0,
                  'dice2': 0,
                  'total': 0
                  },
              4: {
                  'name': '',
                  'dice1': 0,
                  'dice2': 0,
                  'total': 0
                  }
              }

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
    #size(1920, 1080)
    size(1920,1080)
    
    ## SOUND
    global sf, sfx
    sf = SoundFile(this,"themesong.mp3")
    sf.play()
    sf.amp(0.6)
    sfx = SoundFile(this,"clickingnoise.wav")
    sfx.amp(0.6) 
    
    ## PLAYERCARDS
    global img_playercard, img_playercard_dead
    img_playercard = loadImage('playercard.png')
    img_playercard_dead = loadImage('playercard_dead.png')
    
    ## TROOPS
    global img_background_troops
    global img_skeleton_white, img_skeleton_blue, img_archer_white, img_archer_blue, img_dwarf_white, img_dwarf_blue
    global img_cannon_white, img_cannon_blue, img_giant_white, img_giant_blue, img_wizard_white, img_wizard_blue
    global img_witch_white, img_witch_blue, img_golem_white, img_golem_blue, img_dragon_white, img_dragon_blue
    
    img_background_troops = loadImage('background_troops.png')
    img_skeleton_white = loadImage('skeleton_white.png')
    img_skeleton_blue = loadImage('skeleton_blue.png')
    img_archer_white = loadImage('archer_white.png')
    img_archer_blue = loadImage('archer_blue.png')
    img_dwarf_white = loadImage('dwarf_white.png')
    img_dwarf_blue = loadImage('dwarf_blue.png')
    img_cannon_white = loadImage('cannon_white.png')
    img_cannon_blue = loadImage('cannon_blue.png')
    img_giant_white = loadImage('giant_white.png')
    img_giant_blue = loadImage('giant_blue.png')
    img_wizard_white = loadImage('wizard_white.png')
    img_wizard_blue = loadImage('wizard_blue.png')
    img_witch_white = loadImage('witch_white.png')
    img_witch_blue = loadImage('witch_blue.png')
    img_golem_white = loadImage('golem_white.png')
    img_golem_blue = loadImage('golem_blue.png')
    img_dragon_white = loadImage('dragon_white.png')
    img_dragon_blue = loadImage('dragon_blue.png')
    
    ## DICE
    global dice_1, dice_2, dice_3, dice_4, dice_5, dice_6
    dice_1 = loadImage('dice_1.png')
    dice_2 = loadImage('dice_2.png')
    dice_3 = loadImage('dice_3.png')
    dice_4 = loadImage('dice_4.png')
    dice_5 = loadImage('dice_5.png')
    dice_6 = loadImage('dice_6.png')
    
    ## CARDS
    global img_all_cards, img_btn_buy, img_btn_buy_small
    img_all_cards = loadImage('all_cards.png')
    img_btn_buy = loadImage('btn_buy.png')
    img_btn_buy_small = loadImage('btn_buy_small.png')
    
    img_card_counter = loadImage('card_counter.png')
    img_card_exchange = loadImage('card_exchange.png')
    img_card_exterminate = loadImage('card_exterminate.png')
    img_card_extramile = loadImage('card_extramile.png')
    img_card_ghost = loadImage('card_ghost.png')
    img_card_heal = loadImage('card_heal.png')
    img_card_kamikaze = loadImage('card_kamikaze.png')
    img_card_multihit = loadImage('card_multihit.png')
    img_card_mutiny = loadImage('card_mutiny.png')
    img_card_reach = loadImage('card_reach.png')
    img_card_refund = loadImage('card_refund.png')
    img_card_reversal = loadImage('card_reversal.png')
    img_card_shield = loadImage('card_shield.png')
    img_card_skip = loadImage('card_skip.png')
    img_card_switcheroo = loadImage('card_switcheroo.png')
    img_card_take = loadImage('card_take.png')
                
    global playingCards
    playingCards = {
             1: {
                 'img': img_card_counter,
                 'name': 'Counter',
                 'taken': False,
                 'drawn': 0,
                 'max': 1
                 },
             2: {
                 'img': img_card_exchange,
                 'name': 'Exchange',
                 'taken': False,
                 'drawn': 0,
                 'max': 3
                 },
             3: {
                 'img': img_card_exterminate,
                 'name': 'Exterminate',
                 'taken': False,
                 'drawn': 0,
                 'max': 1
                 },
             4: {
                 'img': img_card_extramile,
                 'name': 'Extra Mile',
                 'taken': False,
                 'drawn': 0,
                 'max': 2
                 },
             5: {
                 'img': img_card_ghost,
                 'name': 'Ghost',
                 'taken': False,
                 'drawn': 0,
                 'max': 3
                 },
             6: {
                 'img': img_card_heal,
                 'name': 'Heal',
                 'taken': False,
                 'drawn': 0,
                 'max': 1
                 },
             7: {
                 'img': img_card_kamikaze,
                 'name': 'Kamikaze',
                 'taken': False,
                 'drawn': 0,
                 'max': 1
                 },
             8: {
                 'img': img_card_multihit,
                 'name': 'Multi-Hit',
                 'taken': False,
                 'drawn': 0,
                 'max': 1
                 },
             9: {
                 'img': img_card_mutiny,
                 'name': 'Mutiny',
                 'taken': False,
                 'drawn': 0,
                 'max': 1
                 },
             10: {
                  'img': img_card_ghost,
                  'name': 'Reach',
                  'taken': False,
                  'drawn': 0,
                  'max': 2
                  },
             11: {
                  'img': img_card_refund,
                  'name': 'Refund',
                  'taken': False,
                  'drawn': 0,
                  'max': 2
                  },
             12: {
                  'img': img_card_reversal,
                  'name': 'Reversal',
                  'taken': False,
                  'drawn': 0,
                  'max': 2
                  },
             13: {
                  'img': img_card_shield,
                  'name': 'Shield',
                  'taken': False,
                  'drawn': 0,
                  'max': 1
                  },
             14: {
                  'img': img_card_skip,
                  'name': 'Skip',
                  'taken': False,
                  'drawn': 0,
                  'max': 2
                  },
             15: {
                  'img': img_card_switcheroo,
                  'name': 'Switcheroo',
                  'taken': False,
                  'drawn': 0,
                  'max': 1
                  },
             16: {
                  'img': img_card_take,
                  'name': 'Take',
                  'taken': False,
                  'drawn': 0,
                  'max': 1
                  },
             }
    
    ## FONT
    global font_kabel
    font_kabel = loadFont('LeelawadeeUI-Bold-48.vlw')
    
    ## CURSOR
    global img_cursor
    img_cursor = loadImage('cursor.png')
    
    ## BACKGROUND
    global img_bg, img_logo, img_bg2
    img_bg = loadImage('background.png')
    img_logo = loadImage('logo.png')
    img_bg2 = loadImage('background2.png')
    
    
    ## CURRENT ROUND
    global img_round
    img_round = loadImage('round.png')
    
    ## LEFT MENU
    global img_exit, img_settings, img_rules
    img_exit = loadImage('exit.png')
    img_settings = loadImage('settings.png')
    img_rules = loadImage('rules.png')
    
    ## BUTTONS
    global img_btn_back, img_btn_cancel, img_btn_exit, img_btn_cards, img_btn_next, img_btn_shuffle, img_btn_roll
    img_btn_back = loadImage('btn_back.png')
    img_btn_cancel = loadImage('btn_cancel.png')
    img_btn_exit = loadImage('btn_exit.png')
    img_btn_cards = loadImage('btn_cards.png')
    img_btn_next = loadImage('btn_next.png')
    # img_btn_shuffle = loadImage('btn_shuffle.png')
    img_btn_shuffle = loadImage('btn_throw.png')
    img_btn_roll = loadImage('btn_roll_small.png')

    global img_btn_on, img_btn_off, img_btn_low, img_btn_medium, img_btn_high
    img_btn_on = loadImage('btn_on.png')
    img_btn_off = loadImage('btn_off.png')
    img_btn_low = loadImage('btn_low.png')
    img_btn_medium = loadImage('btn_medium.png')
    img_btn_high = loadImage('btn_high.png') 
    
    global img_btn_cardsmall, img_btn_number, img_btn_use
    img_btn_cardsmall = loadImage('btn_cardsmall.png')
    img_btn_number = loadImage('btn_number.png')
    img_btn_use = loadImage('btn_use.png')
    
    ### --- NAME INPUT --- ###
    # input gamer names
    global allowed_characters
    allowed_characters = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", \
                          "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", \
                          "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
    
    global dicePoints
    dicePoints = {
                  1: {
                      'amount': 1,
                      'img': dice_1
                      },
                  2: {
                      'amount': 2,
                      'img': dice_2
                      },
                  3: {
                      'amount': 3,
                      'img': dice_3
                      },
                  4: {
                      'amount': 4,
                      'img': dice_4
                      },
                  5: {
                      'amount': 5,
                      'img': dice_5
                      },
                  6: {
                      'amount': 6,
                      'img': dice_6 
                      }
            }
    

    
## --- MAIN SCREEN --- ##
def throwDicePoints():
    global amountGained, currentRound, amountOne, amountTwo, currentPlayer
    amountOne = random.randint(1,6)
    amountTwo = random.randint(1,6)
    amountGained = amountOne + amountTwo
    players[currentPlayer]['points'] += amountGained
    
def throwDiceSteps():
    global amountGained, currentRound, amountOne, amountTwo
    numbers = [1,2,2,3,3,4]
    index = random.randint(0,5)
    amountOne = numbers[index]
    amountGained = amountOne
    
def drawDiceAmount():
    global amountGained, currentRound, amountOne, amountTwo
    if amountGained != 0:
        if currentRound == 'POINTS':
            text(str(amountGained) + ' POINTS', 960, 709)
            image(dicePoints[amountOne]['img'], 677, 672)
            image(dicePoints[amountTwo]['img'], 735, 672)
        if currentRound == 'STEPS':
            text(str(amountGained) + ' STEPS', 960, 709)
            image(dicePoints[amountOne]['img'], 677, 672)
    
## --- SHUFFLE --- ##
def drawDiceShuffleAmount():
    global diceGained, shuffled, name1, gamerList
    
    ## DISPLAYING THROWN DICE
    if shuffled > 0:
        diceGained[1]['name'] = gamerList[0]
        if gamerList[0] == name1[0]:
            player1dice = diceGained[1]['dice1']
            player2dice = diceGained[1]['dice2']
            image(dicePoints[player1dice]['img'], 825, 463)
            image(dicePoints[player2dice]['img'], 885, 463)
        elif gamerList[1] == name1[0]:
            player3dice = diceGained[2]['dice1']
            player4dice = diceGained[2]['dice2']
            image(dicePoints[player3dice]['img'], 825, 463)
            image(dicePoints[player4dice]['img'], 885, 463)
        elif gamerList[2] == name1[0]:
            player5dice = diceGained[3]['dice1']
            player6dice = diceGained[3]['dice2']
            image(dicePoints[player5dice]['img'], 825, 463)
            image(dicePoints[player6dice]['img'], 885, 463)
        elif gamerList[3] == name1[0]:
            player7dice = diceGained[4]['dice1']
            player8dice = diceGained[4]['dice2']
            image(dicePoints[player7dice]['img'], 825, 463)
            image(dicePoints[player8dice]['img'], 885, 463)
        
    if shuffled > 1:
        diceGained[2]['name'] = gamerList[1]
        if gamerList[0] == name1[1]:
            player1dice = diceGained[1]['dice1']
            player2dice = diceGained[1]['dice2']
            image(dicePoints[player1dice]['img'], 825, 563)
            image(dicePoints[player2dice]['img'], 885, 563)
        elif gamerList[1] == name1[1]:
            player3dice = diceGained[2]['dice1']
            player4dice = diceGained[2]['dice2']
            image(dicePoints[player3dice]['img'], 825, 563)
            image(dicePoints[player4dice]['img'], 885, 563)
        elif gamerList[2] == name1[1]:
            player5dice = diceGained[3]['dice1']
            player6dice = diceGained[3]['dice2']
            image(dicePoints[player5dice]['img'], 825, 563)
            image(dicePoints[player6dice]['img'], 885, 563)
        elif gamerList[3] == name1[1]:
            player7dice = diceGained[4]['dice1']
            player8dice = diceGained[4]['dice2']
            image(dicePoints[player7dice]['img'], 825, 563)
            image(dicePoints[player8dice]['img'], 885, 563)
    
    if shuffled > 2:
        diceGained[3]['name'] = gamerList[2]
        if gamerList[0] == name1[2]:
            player1dice = diceGained[1]['dice1']
            player2dice = diceGained[1]['dice2']
            image(dicePoints[player1dice]['img'], 825, 663)
            image(dicePoints[player2dice]['img'], 885, 663)
        elif gamerList[1] == name1[2]:
            player3dice = diceGained[2]['dice1']
            player4dice = diceGained[2]['dice2']
            image(dicePoints[player3dice]['img'], 825, 663)
            image(dicePoints[player4dice]['img'], 885, 663)
        elif gamerList[2] == name1[2]:
            player5dice = diceGained[3]['dice1']
            player6dice = diceGained[3]['dice2']
            image(dicePoints[player5dice]['img'], 825, 663)
            image(dicePoints[player6dice]['img'], 885, 663)
        elif gamerList[3] == name1[2]:
            player7dice = diceGained[4]['dice1']
            player8dice = diceGained[4]['dice2']
            image(dicePoints[player7dice]['img'], 825, 663)
            image(dicePoints[player8dice]['img'], 885, 663)
    
    if shuffled > 3:
        diceGained[4]['name'] = gamerList[3]
        if gamerList[0] == name1[3]:
            player1dice = diceGained[1]['dice1']
            player2dice = diceGained[1]['dice2']
            image(dicePoints[player1dice]['img'], 825, 763)
            image(dicePoints[player2dice]['img'], 885, 763)
        elif gamerList[1] == name1[3]:
            player3dice = diceGained[2]['dice1']
            player4dice = diceGained[2]['dice2']
            image(dicePoints[player3dice]['img'], 825, 763)
            image(dicePoints[player4dice]['img'], 885, 763)
        elif gamerList[2] == name1[3]:
            player5dice = diceGained[3]['dice1']
            player6dice = diceGained[3]['dice2']
            image(dicePoints[player5dice]['img'], 825, 763)
            image(dicePoints[player6dice]['img'], 885, 763)
        elif gamerList[3] == name1[3]:
            player7dice = diceGained[4]['dice1']
            player8dice = diceGained[4]['dice2']
            image(dicePoints[player7dice]['img'], 825, 763)
            image(dicePoints[player8dice]['img'], 885, 763)
        
def drawDiceShuffle(n):
    global diceGained, playersAdded, gamer_names
    for i in range(1):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        
        diceGained[n]['dice1'] = dice1
        diceGained[n]['dice2'] = dice2
        diceGained[n]['total'] = dice1 + dice2
        diceGained[n]['name'] = gamer_names[shuffled - 1]
    return diceGained[n]['total']
        
def drawPlayerList():
    global diceGained, playersAdded, gamer_names, name1, playerList, gamerList, shuffled
    gamerList = []
    for i in range(len(gamer_names)):
        if gamer_names[i] != '':
            gamerList.append(gamer_names[i])
            
    playerList = {}
    shuffled = 0                         
    for player_name in gamerList:
        shuffled += 1
        playerRoll = drawDiceShuffle(shuffled)
        
        while playerRoll in playerList:
            playerRoll = drawDiceShuffle(shuffled)
        
        playerList[playerRoll] = player_name
        name1 = [playerList[roll] for roll in sorted(playerList.keys(), reverse=True)]
    return [playerList[roll] for roll in sorted(playerList.keys(), reverse=True)]

## --- TROOPS --- ##
def drawTroopsScreen():
    image(img_background_troops, 280, 230)
    textAlign(CENTER)
    textFont(font_kabel, 24)
    fill('#ffffff')
    textAlign(LEFT)
    textFont(font_kabel, 22)
    fill('#1dc1cd')
    text('TO PURCHASE A TROOP, CLICK ON THE TROOP AND\nTHEN THE BUY BUTTON AT THE BOTTOM OF THE\nSCREEN', 50, 980)
    textAlign(CENTER)
    
    if troopSelected == 'SKELETON':
        image(img_skeleton_blue, 1325, 625)
        fill('#1dc1cd')
        text('SKELETON', 1390, 870)
        text('1', 1471, 623)
    else:
        image(img_skeleton_white, 1325, 625)
        fill('#ffffff')
        text('SKELETON', 1390, 870)
        text('1', 1471, 623)
        
    if troopSelected == 'DWARF':
        image(img_dwarf_blue, 1036, 625)
        fill('#1dc1cd')
        text('DWARF', 1104, 870)
        text('2', 1186, 623)
    else:
        image(img_dwarf_white, 1036, 625)
        fill('#ffffff')
        text('DWARF', 1104, 870)
        text('2', 1186, 623)
        
    if troopSelected == 'ARCHER':
        image(img_archer_blue, 749, 625)
        fill('#1dc1cd')
        text('ARCHER', 816, 870)
        text('4', 898, 623)
    else:
        image(img_archer_white, 749, 625)
        fill('#ffffff')
        text('ARCHER', 816, 870)
        text('4', 898, 623)
        
    if troopSelected == 'CANNON':
        image(img_cannon_blue, 461, 625)
        fill('#1dc1cd')
        text('CANNON', 528, 870)
        text('4', 610, 623)
    else:
        image(img_cannon_white, 461, 625)
        fill('#ffffff')
        text('CANNON', 528, 870)
        text('4', 610, 623)
        
    if troopSelected == 'GIANT':
        image(img_giant_blue, 1466, 268)
        fill('#1dc1cd')
        text('GIANT', 1535, 512)
        text('6', 1611, 265)
    else:
        image(img_giant_white, 1466, 268)
        fill('#ffffff')
        text('GIANT', 1535, 512)
        text('6', 1611, 265)
        
    if troopSelected == 'WIZARD':
        image(img_wizard_blue, 1186, 268)
        fill('#1dc1cd')
        text('WIZARD', 1258, 512)
        text('6', 1328, 265)
    else:
        image(img_wizard_white, 1186, 268)
        fill('#ffffff')
        text('WIZARD', 1258, 512)
        text('6', 1328, 265)
        
    if troopSelected == 'WITCH':
        image(img_witch_blue, 898, 268)
        fill('#1dc1cd')
        text('WITCH', 965, 512)
        text('6', 1040, 265)
    else:
        image(img_witch_white, 898, 268)
        fill('#ffffff')
        text('WITCH', 965, 512)
        text('6', 1040, 265)

    if troopSelected == 'GOLEM':
        image(img_golem_blue, 610, 268)
        fill('#1dc1cd')
        text('GOLEM', 678, 512)
        text('8', 753, 265)
    else:
        image(img_golem_white, 610, 268)
        fill('#ffffff')
        text('GOLEM', 678, 512)
        text('8', 753, 265)

    if troopSelected == 'DRAGON':
        image(img_dragon_blue, 322, 268)
        fill('#1dc1cd')
        text('DRAGON', 390, 512)
        textFont(font_kabel, 24)
        text('10', 465, 265)
    else:
        image(img_dragon_white, 322, 268)
        fill('#ffffff')
        text('DRAGON', 390, 512)
        textFont(font_kabel, 24)
        text('10', 465, 265)

## --- CARDS SCREEN --- ##
def drawAllCards():
    image(img_all_cards, 50, 270)
    textAlign(LEFT)
    textFont(font_kabel, 24)
    text('TO PURCHASE A RANDOM CARD, CLICK ON THE\nBUY BUTTON AT THE BOTTOM OF THE SCREEN', 50, 980)

def drawUseButton(x,y):
    image(img_btn_use, x, y, 204, 87)

def drawDiceBoxBottom():
    global currentPlayer
    fill('#1a2236')
    noStroke()
    rect(660, 950, 600, 78, 10)
    fill('#1dc2ce')
    textAlign(CENTER)
    textFont(font_kabel, 32)
    text(str(players[currentPlayer]['points']) + ' POINTS', 960, 1000)

def drawCardScreenBottom(player):
    global currentPlayer
    fill('#1a2236')
    noStroke()
    rect(660, 950, 600, 78, 10)
    fill('#1dc2ce')
    textAlign(CENTER)
    textFont(font_kabel, 32)
    text(str(players[player]['points']) + ' POINTS', 960, 1000)   

def drawCardsBuyButton():
    image(img_btn_buy_small, 1135, 966)
    
## --- PLAYING CARDS --- ##
def buyCard():
    bought = False
    while bought == False:
        num = random.randint(1, 16)
        if playingCards[num]['taken'] == False:
            cardName = playingCards[num]['name']
            players[currentPlayer]['cards'].append(cardName)
            bought = True
            playingCards[num]['drawn'] += 1
            if playingCards[num]['max'] == playingCards[num]['drawn']:
                playingCards[num]['taken'] = True
        
def drawCardPlayer(player):
    totalCards = len(players[player]['cards'])
    
    if totalCards > 0:
        card1 = players[player]['cards'][0]
        for i in range(1, 17):
            if playingCards[i]['name'] == card1:
                img1 = playingCards[i]['img']
    if totalCards > 1:
        card2 = players[player]['cards'][1]
        for i in range(1, 17):
            if playingCards[i]['name'] == card2:
                img2 = playingCards[i]['img']
    if totalCards > 2:
        card3 = players[player]['cards'][2]
        for i in range(1, 17):
            if playingCards[i]['name'] == card3:
                img3 = playingCards[i]['img']
           
    if totalCards > 2:
        image(img1, 465, 315)
        image(img2, 812, 315)
        image(img3, 1157, 315)
        drawUseButton(512, 760)
        drawUseButton(858, 760)
        drawUseButton(1205, 760)
    elif totalCards > 1:
        image(img1, 640, 315)
        image(img2, 985, 315)
        drawUseButton(685, 760)
        drawUseButton(1030, 760)
    elif totalCards > 0:
        image(img1, 812, 315)
        drawUseButton(858, 760)
        
        
## --- CARD FUNCTIONALITIES --- ##  
def checkCard(player, index):
    global amountGained, currentPlayer, currentRound, enteredPlayers, activePlayers
    specialCards = ['Heal', 'Extra Mile', 'Take', 'Exchange', 'Skip']
    
    if players[player]['cards'][index] == 'Heal' and players[player]['health'] != 3:
        healCard(player)
        del players[player]['cards'][index]
    elif players[player]['cards'][index] == 'Extra Mile' and currentRound == 'STEPS':
        amountGained+=1
        del players[player]['cards'][index]
    elif players[player]['cards'][index] == 'Take':
        logCards = len(players[player]['cards'])
        takeCard(player)
        del players[player]['cards'][index]
        if len(players[player]['cards']) < logCards:
            players[player]['cards'].append('Take')
    elif players[player]['cards'][index] == 'Skip':
        del players[player]['cards'][index]
        if players[currentPlayer+1]['isDead'] == True:
            currentPlayer+=3
        else:
            currentPlayer +=2
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
            
    elif players[player]['cards'][index] not in specialCards:
        del players[player]['cards'][index]
            
def takeCard(player):
    totalCards = len(players[player]['cards'])
    found = 0
    
    
    if totalCards < 3:
        for i in range(0, len(activePlayers)):
            if activePlayers[i] != player:
                found = activePlayers[i]
                break
             
        if found != 0:
            stealable = len(players[found]['cards'])
            if stealable != 0:
                card = random.randint(1, stealable)    
                players[player]['cards'].append(players[found]['cards'][card-1])
                del players[found]['cards'][card-1]
        
def healCard(player):
    players[player]['health']+=1

## --- INPUT SCREEN --- ##
def addPlayers():
    global gamer_names, players, activePlayers, enteredPlayers, diceGained
    adding = 1
    
    for i in range(0, len(gamer_names)):
        if gamer_names[i] != '':
            players[adding]['name'] = gamer_names[i]
            players[adding]['isDead'] = False
            enteredPlayers+=1
            activePlayers.append(adding)
            adding+=1

def drawTooltip(title, message):
    
    global notifications
    if notifications == True: 
     fill('#131a2a')
     noStroke()
     rect(460, 210, 1000, 200, 10)
     textAlign(CENTER, CENTER)
     textFont(font_kabel, 32)
     fill('#ff363b')
     text(title, 960, 260)
     fill('#ffffff')
     text(message, 960, 335)

def drawInputEnterNames():
    global playerList, currentScreen
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
        
## --- CREDITS --- ##
def drawCredits():
    fill(255)
    textSize(32)
    fill('#1dc2ce')
    text('THIS GAME AND SUPPLEMENTARY SOFTWARE\nWERE DEVELOPED BY: ', 960, 340)
    textFont(font_kabel)
    fill(255)
    textSize(32)
    text('LUCAS PRINS\n\nSVEN GROENEVELD\n\nANTON SHI\n\nSI WAI PANG\n\nJOOST REINTJES', 960, 530)    


def drawContact():
    fill('#1dc2ce')
    textSize(35)
    text('IN CASE YOU HAVE NO OTHER WAY OF REACHING US\n WE CAN BE CONTACTED HERE:', 960, 330)
    textSize(50)
    fill(255)
    text('towerdefenseboardgame@gmail.com', 960, 650)
    textSize(35)
    text('(may take up to 3-4 business years)', 960, 720)
    
def changeCursor():
    global img_cursor
    cursor(img_cursor)
    
def changeloghover():
    if currentScreen == 'MAIN-MENU':
        if mouseX > 20 and mouseX < 164 and mouseY > 1035 and mouseY < 1065:
            fill(255)
            rect(20, 1064 , 166, 4)
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
        
def ruleshover():
    if currentScreen == 'RULES':
    
     if mouseX > 645 and mouseX < 875 and mouseY > 317 and mouseY < 377:
            textFont(font_kabel)
            fill(255)
            textSize(35)
            text('WINNING', 765, 368)
     if mouseX > 645 and mouseX < 875 and mouseY > 477 and mouseY < 547:
            textFont(font_kabel)
            fill(255)
            textSize(34)
            text('GAMEPLAY', 765, 528)
     if mouseX > 645 and mouseX < 875 and mouseY > 637 and mouseY < 707 :
        textFont(font_kabel)
        fill(255)
        textSize(37)
        text('ZONES', 765, 688)
     if mouseX > 645 and mouseX < 875 and mouseY > 797 and mouseY < 867 :
       textFont(font_kabel)
       fill(255)
       textSize(35)
       text('BUYING', 765, 848)
     if mouseX > 1035 and mouseX < 1265  and mouseY > 317 and mouseY < 377:
        textFont(font_kabel)
        fill(255)
        textSize(37)
        text('MOVING ', 1160, 368)
     if mouseX > 1035 and mouseX < 1265 and mouseY > 477 and mouseY < 547:
         textFont(font_kabel)
         fill(255)
         textSize(34)
         text('ATTACKING', 1155, 528)
     if mouseX > 1035 and mouseX < 1265 and mouseY > 637 and mouseY < 707 :
            textFont(font_kabel)
            fill(255)
            textSize(37)
            text('CARDS', 1155, 688)
     if mouseX > 1035 and mouseX < 1265 and mouseY > 797 and mouseY < 867 :
            textFont(font_kabel)
            fill(255)
            textSize(37)
            text('TROOPS', 1155, 848)
           
     if mouseX > 850 and mouseX < 1080 and mouseY > 950 and mouseY < 1020 :
            textFont(font_kabel)
            fill(255)
            textSize(43)
            text('FAQ', 965, 1000)
            
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
    
def drawBackground2():
    image(img_bg2, 0, 0, width, height)
    
    
    
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
    rect(460, 330, 300, 75, 10)
    textAlign(CENTER, CENTER)
    fill('#1dc2ce')
    textFont(font_kabel, 32)
    text('MUSIC', 612, 367.5)
    
def drawVolume():
    fill('#1a2236')
    noStroke()
    rect(460, 430, 300, 75, 10)
    textAlign(CENTER, CENTER)
    fill('#1dc2ce')
    textFont(font_kabel, 32)
    text('VOLUME', 612, 467.5)

def drawNotifications():
    fill('#1a2236')
    noStroke()
    rect(460, 530, 300, 75, 10)
    textAlign(CENTER, CENTER)
    fill('#1dc2ce')
    textFont(font_kabel, 32)
    text('NOTIFICATIONS', 612, 567.5)
    
def drawSoundEffects():
    fill('#1a2236')
    noStroke()
    rect(460, 630,300, 75, 10)
    textAlign(CENTER, CENTER)
    fill('#1dc2ce')
    textFont(font_kabel, 32)
    text('SOUNDEFFECTS', 612, 667.5)        
            
def drawSoundButtons():     
    image(img_btn_on, 950, 330, 204, 87)
    image(img_btn_off, 1200, 330, 204, 87)
    image(img_btn_low, 950, 430, 204, 87)
    image(img_btn_medium, 1200, 430, 204, 87)
    image(img_btn_high, 1450, 430, 204, 87)    
    image(img_btn_on, 950, 530, 204, 87)
    image(img_btn_off, 1200, 530, 204, 87)    
    image(img_btn_on, 950, 630, 204, 87)
    image(img_btn_off, 1200, 630, 204, 87)
    
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
    text('VERSION 0.4.0', 20, 1060)
    
## boxes on the rules page
def  drawRulesboxes():
      image(img_round, 620, 300)
      image(img_round, 620, 460)
      image(img_round, 620, 620)
      image(img_round, 620, 780)
      image(img_round, 1010, 300)
      image(img_round, 1010, 460)
      image(img_round, 1010, 620)
      image(img_round, 1010, 780)
      image(img_round, 825, 930)
      
## text on the rules page
def drawRulestext():
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(35)
    textAlign(CENTER)
    text('WINNING', 765, 368)
    textSize(34)
    text('GAMEPLAY', 765, 528)
    textSize(37)
    text('ZONES', 765, 688)
    textSize(35)
    text('BUYING', 765, 848)
    textSize(37)
    text('MOVING ', 1160, 368)
    textSize(34)
    text('ATTACKING', 1155, 528)
    textSize(37)
    text('CARDS', 1155, 688)
    text('TROOPS', 1155, 848)
    textSize(43)
    text('FAQ', 965, 1000)
    

## BUTTONS
def mousePressed():
    
    ## GLOBALS
    global troopSelected, selectedTroopPoints
    global currentRound, currentScreen, currentPlayer, activePlayers, enteredPlayers, currentEntering
    global player_list, currentScreen, number, current_round, lastScreen, gamer_names, shuffled, tooltips, thrownDice, amountGained, sf, isPlaying, playersAdded
    global sfx, notifications, soundfx
    ## MAIN MENU
    if currentScreen == 'MAIN-MENU':
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'EXIT'
        if mouseX > 630 and mouseX < 920 and mouseY > 535 and mouseY < 651:
            if soundfx == True: 
                sfx.play()
            currentScreen = 'INPUT-NAMES'
            lastScreen = 'MAIN-MENU'
        if mouseX > 1020 and mouseX < 1310 and mouseY > 535 and mouseY < 651:
            if soundfx == True: 
                sfx.play()
            currentScreen = 'SETTINGS'
            lastScreen = 'MAIN-MENU'
        if mouseX > 630 and mouseX < 920 and mouseY > 710 and mouseY < 826:
            if soundfx == True: 
                sfx.play()
            currentScreen = 'CREDITS'
            lastScreen = 'MAIN-MENU'
        if mouseX > 1020 and mouseX < 1310 and mouseY > 710 and mouseY < 826:
            if soundfx == True: 
                sfx.play()
            currentScreen = 'CONTACT'
            lastScreen = 'MAIN-MENU'
        if mouseX > 20 and mouseX < 164 and mouseY > 1035 and mouseY < 1065:
            if soundfx == True: 
                sfx.play()
            currentScreen ='CHANGELOG'
            lastScreen = 'MAIN-MENU'
    
    playersAdded = 0
    for i in range(0, len(gamer_names)):
        if gamer_names[i] != '':
            playersAdded+=1
    
    ## INPUT NAMES
    if currentScreen == 'INPUT-NAMES':
        if mouseX > 0 and mouseX < 1920 and mouseY > 0 and mouseY < 1080:
            if soundfx == True: 
                sfx.play()
            tooltips['notEnoughPlayers'] = False
        if mouseX > 50 and mouseX < 254 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'MAIN-MENU'
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137 and playersAdded >= 2: # NEXT BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'SHUFFLE'
            currentEntering = 0
            lastScreen = 'INPUT-NAMES'
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137 and playersAdded < 2:
            if soundfx == True: 
                sfx.play()
            tooltips['notEnoughPlayers'] = True
        
        if mouseX > 810 and mouseX < 1460 and mouseY > 450 and mouseY < 525:
            if soundfx == True: 
                sfx.play()
            currentEntering = 1 
        if mouseX > 810 and mouseX < 1460 and mouseY > 550 and mouseY < 625:
            if soundfx == True: 
                sfx.play()
            currentEntering = 2
        if mouseX > 810 and mouseX < 1460 and mouseY > 650 and mouseY < 725:
            if soundfx == True: 
                sfx.play()
            currentEntering = 3
        if mouseX > 810 and mouseX < 1460 and mouseY > 750 and mouseY < 825:
            if soundfx == True: 
                sfx.play()
            currentEntering = 4
    
    if currentScreen == 'CONTACT':
        lastScreen = 'MAIN-MENU'
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = lastScreen
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'EXIT'
            lastScreen = 'CONTACT'
            
    if currentScreen == 'CHANGELOG':
        lastScreen = 'MAIN-MENU'
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = lastScreen
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'EXIT'
            lastScreen = 'CHANGELOG'
        
    if currentScreen == 'CREDITS':
        lastScreen = 'MAIN-MENU'
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = lastScreen
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'EXIT'
            lastScreen = 'CREDITS'
            
    ## SHUFFLE
    if currentScreen == 'SHUFFLE':
        if mouseX > 50 and mouseX < 254 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'INPUT-NAMES'
            ## SHUFFLE
        if currentScreen == 'SHUFFLE':
            if mouseX > 50 and mouseX < 254 and mouseY > 50 and mouseY < 137 and shuffled == False: # BACK BUTTON
                if soundfx == True: 
                    sfx.play()
                currentScreen = 'INPUT-NAMES'
            if mouseX > 460 and mouseX < 664 and mouseY > 875 and mouseY < 962: # SHUFFLE BUTTON
                if soundfx == True: 
                    sfx.play()
                shuffled = True
                gamer_names = drawPlayerList()
                # drawDiceShuffle()
            if mouseX > 1260 and mouseX < 1464 and mouseY > 875 and mouseY < 962: # NEXT BUTTON
                if soundfx == True: 
                    sfx.play()
                addPlayers()
                currentScreen = 'MAIN' 
                lastScreen = 'MAIN'
                currentPlayer = 1
    
    ## MAIN SCREEN
    if currentScreen == 'MAIN':
        if mouseX > 1130 and mouseX < 1232 and mouseY > 675 and mouseY < 719:
            if soundfx == True: 
                sfx.play()
            if currentRound == 'POINTS' and thrownDice == False:
                throwDicePoints()
                thrownDice = True
            if currentRound == 'STEPS' and thrownDice == False:
                throwDiceSteps()
                thrownDice = True
        
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137 and thrownDice == True: # NEXT BUTTON
            if soundfx == True: 
                sfx.play()
            if players[currentPlayer]['points'] > 10:
                players[currentPlayer]['points'] = 10
            
            thrownDice = False
            amountGained = 0
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
            if soundfx == True: 
                sfx.play()
            currentScreen = 'TROOPS'
        if mouseX > 1649 and mouseX < 1853 and mouseY > 655 and mouseY < 742: # CARDS BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'CARDS'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
             if soundfx == True: 
                sfx.play()
             currentScreen = 'SETTINGS2'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'RULES'
        if mouseX > 325 and mouseX < 427 and mouseY > 955 and mouseY < 999: # PLAYER 1 CARDS BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'PLAYER 1 CARDS'
        
        if mouseX > 785 and mouseX < 887 and mouseY > 955 and mouseY < 999: # PLAYER 2 CARDS BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'PLAYER 2 CARDS'
        
        if mouseX > 1245 and mouseX < 1348 and mouseY > 955 and mouseY < 999: # PLAYER 3 CARDS BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'PLAYER 3 CARDS'
        
        if mouseX > 1705 and mouseX < 1807 and mouseY > 955 and mouseY < 999: # PLAYER 4 CARDS BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'PLAYER 4 CARDS'
       
        if mouseX > 336 and mouseX < 351 and mouseY > 915 and mouseY < 930: # PLAYER 1 MINUS BUTTON
            if soundfx == True: 
                sfx.play()
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
            if soundfx == True: 
                sfx.play()
            if players[1]['health'] != 3:
                players[1]['health']+= 1
        
        if mouseX > 796 and mouseX < 811 and mouseY > 915 and mouseY < 930: # PLAYER 2 MINUS BUTTON
            if soundfx == True: 
                sfx.play()
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
            if soundfx == True: 
                sfx.play()
            if players[2]['health'] != 3:
                players[2]['health']+= 1
        
        if mouseX > 1256 and mouseX < 1271 and mouseY > 915 and mouseY < 930: # PLAYER 3 MINUS BUTTON
            if soundfx == True: 
                sfx.play()
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
            if soundfx == True: 
                sfx.play()
            if players[3]['health'] != 3:
                players[3]['health']+= 1
        
        if mouseX > 1716 and mouseX < 1731 and mouseY > 915 and mouseY < 930: # PLAYER 4 MINUS BUTTON
            if soundfx == True: 
                sfx.play()
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
            if soundfx == True: 
                sfx.play()
            if players[4]['health'] != 3:
                players[4]['health']+= 1
            
    ## TROOP SCREEN
    elif currentScreen == 'TROOPS':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'MAIN'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'RULES'
        if mouseX > 281 and mouseX < 497 and mouseY > 227 and mouseY < 443: # BUY DRAGON BUTTON
            if soundfx == True: 
                sfx.play()
            troopSelected = 'DRAGON'
            selectedTroopPoints = 10
        if mouseX > 570 and mouseX < 786 and mouseY > 227 and mouseY < 443: # BUY GOLEM BUTTON
            if soundfx == True: 
                sfx.play()
            troopSelected = 'GOLEM'
            selectedTroopPoints = 8
        if mouseX > 858 and mouseX < 1074 and mouseY > 227 and mouseY < 443: # BUY WITCH BUTTON
            if soundfx == True: 
                sfx.play()
            troopSelected = 'WITCH'
            selectedTroopPoints = 6
        if mouseX > 1146 and mouseX < 1362 and mouseY > 227 and mouseY < 443: # BUY WIZARD BUTTON
            if soundfx == True: 
                sfx.play()
            troopSelected = 'WIZARD'
            selectedTroopPoints = 6
        if mouseX > 1425 and mouseX < 1641 and mouseY > 227 and mouseY < 443: # BUY GIANT BUTTON
            if soundfx == True: 
                sfx.play()
            troopSelected = 'GIANT'
            selectedTroopPoints = 6
        if mouseX > 420 and mouseX < 626 and mouseY > 584 and mouseY < 800: # BUY CANNON BUTTON
            if soundfx == True: 
                sfx.play()
            troopSelected = 'CANNON'
            selectedTroopPoints = 4
        if mouseX > 709 and mouseX < 925 and mouseY > 584 and mouseY < 800: # BUY ARCHER BUTTON
            if soundfx == True: 
                sfx.play()
            troopSelected = 'ARCHER'
            selectedTroopPoints = 4
        if mouseX > 997 and mouseX < 1213 and mouseY > 584 and mouseY < 800: # BUY DWARF BUTTON
            if soundfx == True: 
                sfx.play()
            troopSelected = 'DWARF'
            selectedTroopPoints = 2
        if mouseX > 1285 and mouseX < 1501 and mouseY > 584 and mouseY < 800: # BUY SKELETON BUTTON
            if soundfx == True: 
                sfx.play()
            troopSelected = 'SKELETON'
            selectedTroopPoints = 1
        if mouseX > 1135 and mouseX < 1237 and mouseY > 966 and mouseY < 1010: # BUY BUTTON
            if soundfx == True: 
                sfx.play()
            if troopSelected != '' and players[currentPlayer]['points'] >= selectedTroopPoints:
                players[currentPlayer]['points'] -= selectedTroopPoints
                

            
    ## CARDS SCREEN
    elif currentScreen == 'CARDS':
        if mouseX > 1135 and mouseX < 1237 and mouseY > 966 and mouseY < 1010: # BUY BUTTON
            if soundfx == True: 
                sfx.play()
            if players[currentPlayer]['points'] >= 10 and len(players[currentPlayer]['cards']) < 3:
                players[currentPlayer]['points'] -= 10
                buyCard()
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'MAIN'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'RULES'
            
    ## EXIT SCREEN
    elif currentScreen == 'EXIT':
        if mouseX > 725 and mouseX < 929 and mouseY > 550 and mouseY < 637: # EXIT BUTTON
            if soundfx == True: 
                sfx.play()
            exit() 
        if mouseX > 975 and mouseX < 1179 and mouseY > 550 and mouseY < 637: # CANCEL BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = lastScreen 
    
    ## SETTINGS SCREEN
    elif currentScreen == 'SETTINGS':
        lastScreen = 'MAIN-MENU'
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = lastScreen
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'EXIT'
            lastScreen = 'SETTINGS'
            
        if mouseX >  950 and mouseX < 1154 and mouseY > 330 and mouseY < 417: #MUSIC ON
            if soundfx == True: 
                sfx.play()
            if isPlaying == False:
                sf.play()
                isPlaying = True
        if mouseX > 1200 and mouseX < 1404 and mouseY > 330 and mouseY < 417: #MUSIC OFF
            if soundfx == True: 
                sfx.play()
            if isPlaying == True:
                sf.stop()
                isPlaying = False
        if mouseX > 950 and mouseX < 1154 and mouseY > 430 and mouseY < 517: #VOLUME LOW
            if soundfx == True: 
                sfx.play()
            sf.amp(0.3)
        if mouseX > 1200 and mouseX < 1404 and mouseY > 430 and mouseY < 517: #VOLUME MEDIUM
            if soundfx == True: 
                sfx.play()
            sf.amp(0.5)
        if mouseX > 1450 and mouseX < 1654 and mouseY > 430 and mouseY < 517: #VOLUME HIGH
            if soundfx == True: 
                sfx.play()
            sf.amp(1)
        if mouseX > 950 and mouseX < 1154 and mouseY > 530 and mouseY < 617: #NOTIFICATIONS ON
            if soundfx == True:
                sfx.play()
            if notifications == False:
                notifications = True
        
        if mouseX > 1200 and mouseX < 1404 and mouseY > 530 and mouseY < 617: #NOTIFICATIONS OFF    
            if soundfx == True:
                sfx.play()
            if notifications == True:
                notifications = False
                
        if mouseX > 950 and mouseX < 1154 and mouseY > 630 and mouseY < 717: #SOUNDEFFECTS ON
            if soundfx == True:
                sfx.play()
            if soundfx == False:
                sfx.play()
                soundfx = True
        if mouseX > 1200 and mouseX < 1404 and mouseY > 630 and mouseY < 717: #SOUNDEFFECTS OFF
            if soundfx == True:
                sfx.play()
            if soundfx == True:
                sfx.stop()
                soundfx = False
     
      
    elif currentScreen == 'SETTINGS2':
        lastScreen = 'MAIN'
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = lastScreen
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'EXIT'
            lastScreen = 'SETTINGS2'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'SETTINGS2'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'RULES'
        if mouseX >  950 and mouseX < 1154 and mouseY > 330 and mouseY < 417: #MUSIC ON
            if soundfx == True: 
                sfx.play()
            if isPlaying == False:
                sf.play()
                isPlaying = True
        if mouseX > 1200 and mouseX < 1404 and mouseY > 330 and mouseY < 417: #MUSIC OFF
            if soundfx == True: 
                sfx.play()
            if isPlaying == True:
                sf.stop()
                isPlaying = False
        if mouseX > 950 and mouseX < 1154 and mouseY > 430 and mouseY < 517: #VOLUME LOW
            if soundfx == True: 
                sfx.play()
            sf.amp(0.3)
        if mouseX > 1200 and mouseX < 1404 and mouseY > 430 and mouseY < 517: #VOLUME MEDIUM
            if soundfx == True: 
                sfx.play()
            sf.amp(0.5)
        if mouseX > 1450 and mouseX < 1654 and mouseY > 430 and mouseY < 517: #VOLUME HIGH
            if soundfx == True: 
                sfx.play()
            sf.amp(1) 
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'RULES'
        if mouseX > 950 and mouseX < 1154 and mouseY > 530 and mouseY < 617: #NOTIFICATIONS ON
            if soundfx == True:
                sfx.play()
            if notifications == False:
                notifications = True
        
        if mouseX > 1200 and mouseX < 1404 and mouseY > 530 and mouseY < 617: #NOTIFICATIONS OFF
            if soundfx == True:
                sfx.play()
            if notifications == True:
                notifications = False
                
        if mouseX > 950 and mouseX < 1154 and mouseY > 630 and mouseY < 717: #SOUNDEFFECTS ON
            if soundfx == True:
                sfx.play()
            if soundfx == False:
                sfx.play()
                soundfx = True
        if mouseX > 1200 and mouseX < 1404 and mouseY > 630 and mouseY < 717: #SOUNDEFFECTS OFF
            if soundfx == True:
                sfx.play()
            if soundfx == True:
                sfx.stop()
                soundfx = False
        
    ## RULES SCREEN
    elif currentScreen == 'RULES':
        lastScreen = 'MAIN'
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = lastScreen
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'EXIT'
            lastScreen = 'RULES'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'SETTINGS2'
            lastScreen = 'RULES'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'RULES'
        if mouseX > 645 and mouseX < 875 and mouseY > 317 and mouseY < 377:
            if soundfx == True: 
                sfx.play()
            currentScreen = 'WINNING'
            lastScreen = 'RULES'
        if mouseX > 645 and mouseX < 875 and mouseY > 477 and mouseY < 547:
            if soundfx == True: 
                sfx.play()
            currentScreen = 'GAMEPLAY'
            lastScreen = 'RULES'
        if mouseX > 645 and mouseX < 875 and mouseY > 637 and mouseY < 707 :
            if soundfx == True: 
                sfx.play()
            currentScreen = 'ZONES'
            lastScreen = 'RULES'
        if mouseX > 645 and mouseX < 875 and mouseY > 797 and mouseY < 867 :
            if soundfx == True: 
                sfx.play()
            currentScreen = 'BUYING'
            lastScreen = 'RULES'
        if mouseX > 1035 and mouseX < 1265  and mouseY > 317 and mouseY < 377:
            if soundfx == True: 
                sfx.play()
            currentScreen = 'MOVING'
            lastScreen = 'RULES'
        if mouseX > 1035 and mouseX < 1265 and mouseY > 477 and mouseY < 547:
            if soundfx == True: 
                sfx.play()
            currentScreen = 'ATTACKING'
            lastScreen = 'RULES'
        if mouseX > 1035 and mouseX < 1265 and mouseY > 637 and mouseY < 707 :
            if soundfx == True: 
                sfx.play()
            currentScreen = 'CARDS-R'
            lastScreen = 'RULES'
        if mouseX > 1035 and mouseX < 1265 and mouseY > 797 and mouseY < 867 :
            if soundfx == True: 
                sfx.play()
            currentScreen = 'TROOPS-R'
            lastScreen = 'RULES'
        if mouseX > 850 and mouseX < 1080 and mouseY > 950 and mouseY < 1020 :
            if soundfx == True: 
                sfx.play()
            currentScreen = 'FAQ'
            lastScreen = 'RULES'
        
            
    ## PLAYER 1 CARDS SCREEN
    elif currentScreen == 'PLAYER 1 CARDS':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'MAIN'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'RULES'
        
        totalCards1 = len(players[1]['cards'])    
        if totalCards1 > 2:
            if mouseX > 512 and mouseX < 716 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(1,0)
            if mouseX > 858 and mouseX < 1062 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(1,1)
            if mouseX > 1205 and mouseX < 1409 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(1,2)
        
        elif totalCards1 > 1:
            if mouseX > 685 and mouseX < 889 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(1,0)
            if mouseX > 1030 and mouseX < 1234 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(1,1)
        
        elif totalCards1 > 0:
            if mouseX > 858 and mouseX < 1062 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(1,0)
    ## PLAYER 2 CARDS SCREEN
    elif currentScreen == 'PLAYER 2 CARDS':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'MAIN'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'RULES'
            
        totalCards2 = len(players[2]['cards'])    
        if totalCards2 > 2:
            if mouseX > 512 and mouseX < 716 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(2,0)
            if mouseX > 858 and mouseX < 1062 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(2,1)
            if mouseX > 1205 and mouseX < 1409 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(2,2)
        
        elif totalCards2 > 1:
            if mouseX > 685 and mouseX < 889 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(2,0)
            if mouseX > 1030 and mouseX < 1234 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(2,1)
        
        elif totalCards2 > 0:
            if mouseX > 858 and mouseX < 1062 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(2,0)
    
    ## PLAYER 3 CARDS SCREEN
    elif currentScreen == 'PLAYER 3 CARDS':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'MAIN'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'RULES'
            
        totalCards3 = len(players[3]['cards'])    
        if totalCards3 > 2:
            if mouseX > 512 and mouseX < 716 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(3,0)
            if mouseX > 858 and mouseX < 1062 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(3,1)
            if mouseX > 1205 and mouseX < 1409 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(3,2)
        
        elif totalCards3 > 1:
            if mouseX > 685 and mouseX < 889 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(3,0)
            if mouseX > 1030 and mouseX < 1234 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(3,1)
        
        elif totalCards3 > 0:
            if mouseX > 858 and mouseX < 1062 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(3,0)
    
    ## PLAYER 4 CARDS SCREEN
    elif currentScreen == 'PLAYER 4 CARDS':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'MAIN'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            if soundfx == True: 
                sfx.play()
            currentScreen = 'RULES'
            
        totalCards4 = len(players[4]['cards'])    
        if totalCards4 > 2:
            if mouseX > 512 and mouseX < 716 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(4,0)
            if mouseX > 858 and mouseX < 1062 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(4,1)
            if mouseX > 1205 and mouseX < 1409 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(4,2)
        
        elif totalCards4 > 1:
            if mouseX > 685 and mouseX < 889 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(4,0)
            if mouseX > 1030 and mouseX < 1234 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(4,1)
        
        elif totalCards4 > 0:
            if mouseX > 858 and mouseX < 1062 and mouseY > 760 and mouseY < 847:
                if soundfx == True: 
                    sfx.play()
                checkCard(4,0)
            
    
                 
   
            
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
    global img_cursor, img_btn_roll
    
    ## GLOBALS
    global currentRound, currentScreen, currentPlayer, activePlayers, shuffled, tooltips, font_kabel, shuffled, diceGained
    
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
            drawShuffleButton()
        else:
            drawNextButtonBottom()
        drawInputEnterNames()
        drawDiceShuffleAmount()
        
        fill('#1a2236')
        noStroke()
        rect(460, 300, 1000, 100, 10)
        textAlign(CENTER, CENTER)
        fill('#1dc2ce')
        textFont(font_kabel, 32)
        text('THROW DICE TO DECIDE WHO GOES FIRST', 960, 350)
    
    ## MAIN SCREEN
    if currentScreen == 'MAIN':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawPlayerCards()
        drawPlayerStats()
        drawNextButton()
        drawCardsButton()
        drawRound(currentRound)
        drawDiceBox(amountGained, currentRound, img_btn_roll, font_kabel)
        drawDiceAmount()
        if currentRound == 'POINTS':
            drawTroopsButton()
            
    ## TROOPS SCREEN
    elif currentScreen == 'TROOPS':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawRound(currentRound)
        drawBackButton()
        drawDiceBoxBottom()
        drawCardsBuyButton()
        drawTroopsScreen()
    
    ## CARDS SCREEN
    elif currentScreen == 'CARDS':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawRound(currentRound)
        drawBackButton()
        drawDiceBoxBottom()
        drawAllCards()
        drawCardsBuyButton()
    
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
        
    elif currentScreen == 'SETTINGS2':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
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
        drawContact()
        
    elif currentScreen == 'CREDITS':
        drawBackground()
        drawRound('CREDITS')
        drawExit()
        drawBackButton()
        drawCredits()
        
    elif currentScreen == 'CHANGELOG':
        drawBackground2()
        drawRound('CHANGELOG')
        drawExit()
        drawBackButton()
  
        
    ## RULES SCREEN
    elif currentScreen == 'RULES':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawBackButton()
        drawRound('RULES')
        drawRulesboxes()
        drawRulestext()
        ruleshover()

    
    ## PLAYER 1 CARDS SCREEN 
    elif currentScreen == 'PLAYER 1 CARDS':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawBackButton()
        drawRound(currentRound)
        drawCardPlayer(1)
        drawCardScreenBottom(1)
        
    ## PLAYER 1 CARDS SCREEN 
    elif currentScreen == 'PLAYER 2 CARDS':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawBackButton()
        drawRound(currentRound)
        drawCardPlayer(2)
        drawCardScreenBottom(2)
    
    ## PLAYER 1 CARDS SCREEN 
    elif currentScreen == 'PLAYER 3 CARDS':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawBackButton()
        drawRound(currentRound)
        drawCardPlayer(3)
        drawCardScreenBottom(3)
    
    ## PLAYER 1 CARDS SCREEN 
    elif currentScreen == 'PLAYER 4 CARDS':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawBackButton()
        drawRound(currentRound)
        drawCardPlayer(4)
        drawCardScreenBottom(4)
        
    elif currentScreen == 'WINNING':
        drawBackground()
        
    elif currentScreen == 'GAMEPLAY':
        drawBackground()
        
    elif currentScreen == 'ZONES':
        drawBackground()
        
    elif currentScreen == 'BUYING':
        drawBackground()
        
    elif currentScreen == 'MOVING':
        drawBackground()
        
    elif currentScreen == 'ATTACKING':
        drawBackground()
        
    elif currentScreen == 'CARDS-R':
        drawBackground()
        
    elif currentScreen == 'TROOPS-R':
        drawBackground()
        
    elif currentScreen == 'FAQ':
        drawBackground()
