from selenium import webdriver
from selenium import *
import numpy as np
import time
import re

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome("c:\\chromedriver.exe", options=options)

driver.get("https://colonist.io/")

lenOfLis = 0

blueCards = np.array([0,0,0,0,0,-1])
redCards = np.array([0,0,0,0,0,-1])
greenCards = np.array([0,0,0,0,0,-1])
orangeCards = np.array([0,0,0,0,0,-1])
blackCards = np.array([0,0,0,0,0,-1])

order=["","","",""]

blue="B"
green="G"
red="R"
orange="O"
black="K"

count=0

namebox = driver.find_element_by_class_name("tooltip_container")
you = namebox.text
print(you)
def modify_cards(name, array):
    if name == blue:
        global blueCards
        blueCards = blueCards + array
    elif name == green:
        global greenCards
        greenCards = greenCards + array
    elif name == red:
        global redCards
        redCards = redCards + array
    elif name == orange:
        global orangeCards
        orangeCards = orangeCards + array
    elif name == black:
        global blackCards
        blackCards = blackCards + array
def print_cards(name):
    if name == blue:
        print("BLUE: " + str(blueCards))
    elif name == green:
        print("GREN: " + str(greenCards))
    elif name == red:
        print("RED : " + str(redCards))
    elif name == orange:
        print("ORNG: " + str(orangeCards))
    elif name == black:
        print("BLCK: " + str(blackCards))
while 1 == 1:
    time.sleep(3)
    try:
        chat = driver.find_element_by_class_name("game_chat_text_div")
        messages = chat.find_elements_by_class_name("message_post")
        if (len(messages)>lenOfLis):
            for i in reversed(range(len(messages)-lenOfLis)):
                message = messages[-1-i]
                if (message.get_attribute('style') != "color: rgb(102, 102, 102);"):
                    result = message.get_attribute('innerHTML')
                    parsed = result[(result.find('>')+1):]
                    parsed = parsed.replace('<img src="../dist/images/card_lumber.svg?v116" alt="lumber" height="20" width="14.25" class="lobby-chat-text-icon">', "lumber ")
                    parsed = parsed.replace('<img src="../dist/images/card_grain.svg?v116" alt="grain" height="20" width="14.25" class="lobby-chat-text-icon">', "grain ")
                    parsed = parsed.replace('<img src="../dist/images/card_ore.svg?v116" alt="ore" height="20" width="14.25" class="lobby-chat-text-icon">', "ore ")
                    parsed = parsed.replace('<img src="../dist/images/card_brick.svg?v116" alt=" brick" height="20" width="14.25" class="lobby-chat-text-icon">', "brick ")
                    parsed = parsed.replace('<img src="../dist/images/card_wool.svg?v116" alt="wool" height="20" width="14.25" class="lobby-chat-text-icon">', "wool ")
                    parsed = parsed.replace('<img src="../dist/images/road_red.svg?v116" alt="road" height="20" width="20" class="lobby-chat-text-icon">', "road ")
                    parsed = parsed.replace('<img src="../dist/images/road_blue.svg?v116" alt="road" height="20" width="20" class="lobby-chat-text-icon">', "road ")
                    parsed = parsed.replace('<img src="../dist/images/road_orange.svg?v116" alt="road" height="20" width="20" class="lobby-chat-text-icon">', "road ")
                    parsed = parsed.replace('<img src="../dist/images/road_green.svg?v116" alt="road" height="20" width="20" class="lobby-chat-text-icon">', "road ")
                    parsed = parsed.replace('<img src="../dist/images/settlement_green.svg?v116" alt="settlement" height="20" width="20" class="lobby-chat-text-icon">', "settlement ")
                    parsed = parsed.replace('<img src="../dist/images/settlement_blue.svg?v116" alt="settlement" height="20" width="20" class="lobby-chat-text-icon">', "settlement ")
                    parsed = parsed.replace('<img src="../dist/images/settlement_red.svg?v116" alt="settlement" height="20" width="20" class="lobby-chat-text-icon">', "settlement ")
                    parsed = parsed.replace('<img src="../dist/images/card_rescardback.svg?v116" alt="card" height="20" width="14.25" class="lobby-chat-text-icon">', "card ")
                    parsed = parsed.replace('<img src="../dist/images/settlement_orange.svg?v116" alt="settlement" height="20" width="20" class="lobby-chat-text-icon">', "settlement ")
                    parsed = parsed.replace('<img src="../dist/images/card_roadbuilding.svg?v116" alt="road building" height="20" width="14.25" class="lobby-chat-text-icon">', "roadbuilding ")
                    parsed = parsed.replace('<img src="../dist/images/city_orange.svg?v116" alt="city" height="20" width="20" class="lobby-chat-text-icon">', "city ")
                    parsed = parsed.replace('<img src="../dist/images/city_red.svg?v116" alt="city" height="20" width="20" class="lobby-chat-text-icon">', "city ")
                    parsed = parsed.replace('<img src="../dist/images/city_blue.svg?v116" alt="city" height="20" width="20" class="lobby-chat-text-icon">', "city ")
                    parsed = parsed.replace('<img src="../dist/images/city_green.svg?v116" alt="city" height="20" width="20" class="lobby-chat-text-icon">', "city ")
                    parsed = parsed.replace('<img src="../dist/images/icon_robber.svg?v116" alt="robber" height="20" width="20" class="lobby-chat-text-icon">: <img src="../dist/images/prob_8.svg?v116" alt="prob_8" height="20" width="20" class="lobby-chat-text-icon">', "robber")
                    parsed = parsed.replace('<img src="../dist/images/card_monopoly.svg?v116" alt="monopoly" height="20" width="14.25" class="lobby-chat-text-icon">', "monopoly ")
                    parsback = parsed
                    parsed = parsed.split()

                    if parsed[1] != "rolled:" and parsed[1] != "wants":
                        print(parsback)
                    
                    if parsed[0] != "Bot":
                        if len(messages)<30:
                            if (message.get_attribute('style') == "color: rgb(226, 113, 116);"):
                                red = parsed[0]
                            elif (message.get_attribute('style') == "color: rgb(98, 185, 93);"):
                                green = parsed[0]
                            elif (message.get_attribute('style') == "color: rgb(34, 54, 151);"):
                                blue = parsed[0]
                            elif (message.get_attribute('style') == "color: rgb(224, 151, 66);"):
                                orange = parsed[0]
                            elif (message.get_attribute('style') == "color: rgb(62, 62, 62);"):
                                black = parsed[0]
                            if count<8:
                                count += 1
                                if count==1:
                                    order[0]=parsed[0]
                                elif count==3:
                                    order[1]=parsed[0]
                                elif count==5:
                                    order[2]=parsed[0]
                                elif count==7:
                                    order[3]=parsed[0]
                                    print(order[0])
                                    print(order[1])
                                    print(order[2])
                                    print(order[3])
                                    print(red)
                                    print(blue)
                                    print(green)
                                    print(orange)
                                    print(black)
                                    if red == "R":
                                        red = parsed[0]
                                        print("R")
                                    elif blue == "B":
                                        blue = parsed[0]
                                        print("B")
                                    elif green == "G":
                                        green = parsed[0]
                                        print("G")
                                    elif orange == "O":
                                        orange = parsed[0]
                                        print("O")
                                    elif black == "K":
                                        black = parsed[0]
                                        print("K")
                        if parsed[1] == "built":
                            if parsed[3] == "settlement":
                                modify_cards(parsed[0], [-1,-1,-1,-1,0,0])
                            elif parsed[3] == "road":
                                modify_cards(parsed[0], [-1,-1,0,0,0,0])
                            elif parsed[3] == "city":
                                modify_cards(parsed[0], [0,0,0,-2,-3,0])
                        elif parsed[1] == "received":
                            for i in range(len(parsed)-4):
                                if parsed[4+i] == "grain":
                                    modify_cards(parsed[0], [0,0,0,1,0,0])
                                elif parsed[4+i] == "wool":
                                    modify_cards(parsed[0], [0,0,1,0,0,0])
                                elif parsed[4+i] == "ore":
                                    modify_cards(parsed[0], [0,0,0,0,1,0]) 
                                elif parsed[4+i] == "brick":
                                    modify_cards(parsed[0], [0,1,0,0,0,0])
                                elif parsed[4+i] == "lumber":
                                    modify_cards(parsed[0], [1,0,0,0,0,0])
                        elif parsed[1] == "got:":
                            for i in range(len(parsed)-2):
                                if parsed[2+i] == "grain":
                                    modify_cards(parsed[0], [0,0,0,1,0,0])
                                elif parsed[2+i] == "wool":
                                    modify_cards(parsed[0], [0,0,1,0,0,0])
                                elif parsed[2+i] == "ore":
                                    modify_cards(parsed[0], [0,0,0,0,1,0]) 
                                elif parsed[2+i] == "brick":
                                    modify_cards(parsed[0], [0,1,0,0,0,0])
                                elif parsed[2+i] == "lumber":
                                    modify_cards(parsed[0], [1,0,0,0,0,0])
                        elif parsed[1] == "traded:":
                            for i in range(parsed.index('for:')-2):
                                if parsed[2+i] == "grain":
                                    modify_cards(parsed[0], [0,0,0,-1,0,0])
                                    modify_cards(parsed[-1], [0,0,0,1,0,0])
                                elif parsed[2+i] == "wool":
                                    modify_cards(parsed[0], [0,0,-1,0,0,0])
                                    modify_cards(parsed[-1], [0,0,1,0,0,0])
                                elif parsed[2+i] == "ore":
                                    modify_cards(parsed[0], [0,0,0,0,-1,0])
                                    modify_cards(parsed[-1], [0,0,0,0,1,0]) 
                                elif parsed[2+i] == "brick":
                                    modify_cards(parsed[0], [0,-1,0,0,0,0])
                                    modify_cards(parsed[-1], [0,1,0,0,0,0])
                                elif parsed[2+i] == "lumber":
                                    modify_cards(parsed[0], [-1,0,0,0,0,0])
                                    modify_cards(parsed[-1], [1,0,0,0,0,0])
                            for i in range(parsed.index('with:')-parsed.index('for:')-1):
                                if parsed[parsed.index('for:')+1+i] == "grain":
                                    modify_cards(parsed[0], [0,0,0,1,0,0])
                                    modify_cards(parsed[-1], [0,0,0,-1,0,0])
                                elif parsed[parsed.index('for:')+1+i] == "wool":
                                    modify_cards(parsed[0], [0,0,1,0,0,0])
                                    modify_cards(parsed[-1], [0,0,-1,0,0,0])
                                elif parsed[parsed.index('for:')+1+i] == "ore":
                                    modify_cards(parsed[0], [0,0,0,0,1,0])
                                    modify_cards(parsed[-1], [0,0,0,0,-1,0]) 
                                elif parsed[parsed.index('for:')+1+i] == "brick":
                                    modify_cards(parsed[0], [0,1,0,0,0,0])
                                    modify_cards(parsed[-1], [0,-1,0,0,0,0])
                                elif parsed[parsed.index('for:')+1+i] == "lumber":
                                    modify_cards(parsed[0], [1,0,0,0,0,0])
                                    modify_cards(parsed[-1], [-1,0,0,0,0,0])
                        elif parsed[1] == "gave":
                            for i in range(parsed.index('and')-2):
                                if parsed[3+i] == "grain":
                                    modify_cards(parsed[0], [0,0,0,-1,0,0])
                                elif parsed[3+i] == "wool":
                                    modify_cards(parsed[0], [0,0,-1,0,0,0])
                                elif parsed[3+i] == "ore":
                                    modify_cards(parsed[0], [0,0,0,0,-1,0])
                                elif parsed[3+i] == "brick":
                                    modify_cards(parsed[0], [0,-1,0,0,0,0])
                                elif parsed[3+i] == "lumber":
                                    modify_cards(parsed[0], [-1,0,0,0,0,0])
                            for i in range(len(parsed)-parsed.index('took')-1):
                                if parsed[parsed.index('took')+1+i] == "grain":
                                    modify_cards(parsed[0], [0,0,0,1,0,0])
                                elif parsed[parsed.index('took')+1+i] == "wool":
                                    modify_cards(parsed[0], [0,0,1,0,0,0])
                                elif parsed[parsed.index('took')+1+i] == "ore":
                                    modify_cards(parsed[0], [0,0,0,0,1,0])
                                elif parsed[parsed.index('took')+1+i] == "brick":
                                    modify_cards(parsed[0], [0,1,0,0,0,0])
                                elif parsed[parsed.index('took')+1+i] == "lumber":
                                    modify_cards(parsed[0], [1,0,0,0,0,0])   
                        elif parsed[1] == "stole:":
                            if parsed[-1] == "you":
                                if parsed[2] == "grain":
                                    modify_cards(parsed[0], [0,0,0,1,0,0])
                                    modify_cards(you, [0,0,0,-1,0,0])
                                elif parsed[2] == "ore":
                                    modify_cards(parsed[0], [0,0,0,0,1,0]) 
                                    modify_cards(you, [0,0,0,0,-1,0]) 
                                elif parsed[2] == "wool":
                                    modify_cards(parsed[0], [0,0,1,0,0,0])
                                    modify_cards(you, [0,0,-1,0,0,0])
                                elif parsed[2] == "brick":
                                    modify_cards(parsed[0], [0,1,0,0,0,0])
                                    modify_cards(you, [0,-1,0,0,0,0])
                                elif parsed[2] == "lumber":
                                    modify_cards(parsed[0], [1,0,0,0,0,0])
                                    modify_cards(you, [-1,0,0,0,0,0])
                            else: 
                                if parsed[2] == "grain":
                                    modify_cards(you, [0,0,0,1,0,0])
                                    modify_cards(parsed[-1], [0,0,0,-1,0,0])
                                elif parsed[2] == "ore":
                                    modify_cards(you, [0,0,0,0,1,0]) 
                                    modify_cards(parsed[-1], [0,0,0,0,-1,0]) 
                                elif parsed[2] == "wool":
                                    modify_cards(you, [0,0,1,0,0,0])
                                    modify_cards(parsed[-1], [0,0,-1,0,0,0])
                                elif parsed[2] == "brick":
                                    modify_cards(you, [0,1,0,0,0,0])
                                    modify_cards(parsed[-1], [0,-1,0,0,0,0])
                                elif parsed[2] == "lumber":
                                    modify_cards(you, [1,0,0,0,0,0])
                                    modify_cards(parsed[-1], [-1,0,0,0,0,0])
                        elif parsed[1] == "discarded:":
                            for i in range(len(parsed)-2):
                                if parsed[2+i] == "grain":
                                    modify_cards(parsed[0], [0,0,0,-1,0,0])
                                elif parsed[2+i] == "ore":
                                    modify_cards(parsed[0], [0,0,0,0,-1,0]) 
                                elif parsed[2+i] == "wool":
                                    modify_cards(parsed[0], [0,0,-1,0,0,0])
                                elif parsed[2+i] == "brick":
                                    modify_cards(parsed[0], [0,-1,0,0,0,0])
                                elif parsed[2+i] == "lumber":
                                    modify_cards(parsed[0], [-1,0,0,0,0,0])
                        elif parsed[1] == "bought":
                            modify_cards(parsed[0], [0,0,-1,-1,-1,0])
                        elif parsed[1] == "used":
                            if parsed[2] == "monopoly":
                                if parsed[-1] == "lumber":
                                    modify_cards(parsed[0], [redCards[0],0,0,0,0,0])
                                    if parsed[0]!=red:
                                        redCards[0]=0
                                    modify_cards(parsed[0], [greenCards[0],0,0,0,0,0])
                                    if parsed[0]!=green:
                                        greenCards[0]=0
                                    modify_cards(parsed[0], [blueCards[0],0,0,0,0,0])
                                    if parsed[0]!=blue:
                                        blueCards[0]=0
                                    modify_cards(parsed[0], [orangeCards[0],0,0,0,0,0])
                                    if parsed[0]!=orange:    
                                        orangeCards[0]=0
                                    modify_cards(parsed[0], [blackCards[0],0,0,0,0,0])
                                    if parsed[0]!=black:    
                                        blackCards[0]=0
                                elif parsed[-1] == "brick":
                                    modify_cards(parsed[0], [0,redCards[0],0,0,0,0])
                                    if parsed[0]!=red:
                                        redCards[1]=0
                                    modify_cards(parsed[0], [0,greenCards[0],0,0,0,0])
                                    if parsed[0]!=green:
                                        greenCards[1]=0
                                    modify_cards(parsed[0], [0,blueCards[0],0,0,0,0])
                                    if parsed[0]!=blue:
                                        blueCards[1]=0
                                    modify_cards(parsed[0], [0,orangeCards[0],0,0,0,0])
                                    if parsed[0]!=orange:  
                                        orangeCards[1]=0
                                    modify_cards(parsed[0], [0,blackCards[0],0,0,0,0])
                                    if parsed[0]!=black:    
                                        blackCards[1]=0
                                elif parsed[-1] == "sheep":
                                    modify_cards(parsed[0], [0,0,redCards[0],0,0,0])
                                    if parsed[0]!=red:
                                        redCards[2]=0
                                    modify_cards(parsed[0], [0,0,greenCards[0],0,0,0])
                                    if parsed[0]!=green:
                                        greenCards[2]=0
                                    modify_cards(parsed[0], [0,0,blueCards[0],0,0,0])
                                    if parsed[0]!=blue:
                                        blueCards[2]=0
                                    modify_cards(parsed[0], [0,0,orangeCards[0],0,0,0])
                                    if parsed[0]!=orange:  
                                        orangeCards[2]=0    
                                    modify_cards(parsed[0], [0,0,blackCards[0],0,0,0])    
                                    if parsed[0]!=black:    
                                        blackCards[2]=0
                                elif parsed[-1] == "wheat":
                                    modify_cards(parsed[0], [0,0,0,redCards[0],0,0])
                                    if parsed[0]!=red:
                                        redCards[3]=0
                                    modify_cards(parsed[0], [0,0,0,greenCards[0],0,0])
                                    if parsed[0]!=green:
                                        greenCards[3]=0
                                    modify_cards(parsed[0], [0,0,0,blueCards[0],0,0])
                                    if parsed[0]!=blue:
                                        blueCards[3]=0
                                    modify_cards(parsed[0], [0,0,0,orangeCards[0],0,0])
                                    if parsed[0]!=orange:  
                                        orangeCards[3]=0
                                    modify_cards(parsed[0], [0,0,0,blackCards[0],0,0])    
                                    if parsed[0]!=black:    
                                        blackCards[3]=0
                                elif parsed[-1] == "ore":
                                    modify_cards(parsed[0], [0,0,0,0,redCards[0],0])
                                    if parsed[0]!=red:
                                        redCards[4]=0
                                    modify_cards(parsed[0], [0,0,0,0,greenCards[0],0])
                                    if parsed[0]!=green:
                                        greenCards[4]=0
                                    modify_cards(parsed[0], [0,0,0,0,blueCards[0],0])
                                    if parsed[0]!=blue:
                                        blueCards[4]=0
                                    modify_cards(parsed[0], [0,0,0,0,orangeCards[0],0])
                                    if parsed[0]!=orange:  
                                        orangeCards[4]=0
                                    modify_cards(parsed[0], [0,0,0,0,blackCards[0],0])
                                    if parsed[0]!=black:    
                                        blackCards[4]=0
                        elif parsed[1] == "took":
                            for i in range(len(parsed)-4):
                                if parsed[4+i] == "grain":
                                    modify_cards(parsed[0], [0,0,0,1,0,0])
                                elif parsed[4+i] == "ore":
                                    modify_cards(parsed[0], [0,0,0,0,1,0]) 
                                elif parsed[4+i] == "wool":
                                    modify_cards(parsed[0], [0,0,1,0,0,0])
                                elif parsed[4+i] == "brick":
                                    modify_cards(parsed[0], [0,1,0,0,0,0])
                                elif parsed[4+i] == "lumber":
                                    modify_cards(parsed[0], [1,0,0,0,0,0])
            lenOfLis = len(messages)

            print("    : [ L  B  S  W  O  T]")
            print_cards(order[0])
            print_cards(order[1])
            print_cards(order[2])
            print_cards(order[3])
    except:
        print("couldn't find the element")