def drawDiceBox(amountGained, currentRound, img, font):
    fill('#1a2236')
    noStroke()
    rect(660, 658, 600, 78, 10)
    fill('#1dc2ce')
    textAlign(CENTER)
    textFont(font, 32)
    image(img, 1130, 675) 
