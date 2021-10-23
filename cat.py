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

p1Cards = np.array([0,0,0,0,0,0,-1])
p2Cards = np.array([0,0,0,0,0,0,-1])
p3Cards = np.array([0,0,0,0,0,0,-1])
p4Cards = np.array([0,0,0,0,0,0,-1])

order=["","","",""]

count=0

namebox = driver.find_element_by_class_name("tooltip_container")
you = namebox.text

break_strings = ["card_devcardback","monopoly","icon_longest_road","robber","Year of Plenty","Knight","Road Building","rolled:","wants"]

def modify_cards(name, array):
    if name == order[0]:
        global p1Cards
        p1Cards = p1Cards + array
    elif name == order[1]:
        global p2Cards
        p2Cards = p2Cards + array
    elif name == order[2]:
        global p3Cards
        p3Cards = p3Cards + array
    elif name == order[3]:
        global p4Cards
        p4Cards = p4Cards + array

def print_cards(name):
    if name == order[0]:
        print(order[0][0:4] + ": " + str(p1Cards))
    elif name == order[1]:
        print(order[1][0:4] + ": " + str(p2Cards))
    elif name == order[2]:
        print(order[2][0:4] + ": " + str(p3Cards))
    elif name == order[3]:
        print(order[3][0:4] + ": " + str(p4Cards))
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
                    parsback = parsed
                    parsed = parsed.split()

                    if "settlement" in parsback:
                        parsed[3] = "settlement"
                        parsed = parsed[0:4]
                    elif "road" in parsback:
                        parsed[3] = "road"
                        parsed = parsed[0:4]
                    elif "city" in parsback:
                        parsed[3] = "city"
                        parsed = parsed[0:4]

                    if any(x in parsback for x in break_strings):
                        parsed[0] = "Bot"
                    
                    if parsed[0] != "Bot":
                        print(*parsed)
                        if len(messages)<30:
                            if parsed[2] == ("left" or "disconnected." or "reconnected." or "reconnected!" or "reconnected,"):
                                break
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

                        if parsed[1] == "built":
                            if parsed[3] == "settlement":
                                modify_cards(parsed[0], [-1,-1,-1,-1,0,0,0])
                            elif parsed[3] == "road":
                                modify_cards(parsed[0], [-1,-1,0,0,0,0,0])
                            elif parsed[3] == "city":
                                modify_cards(parsed[0], [0,0,0,-2,-3,0,0])
                        elif parsed[1] == "received":
                            for i in range(len(parsed)-4):
                                if parsed[4+i] == "grain":
                                    modify_cards(parsed[0], [0,0,0,1,0,0,0])
                                elif parsed[4+i] == "wool":
                                    modify_cards(parsed[0], [0,0,1,0,0,0,0])
                                elif parsed[4+i] == "ore":
                                    modify_cards(parsed[0], [0,0,0,0,1,0,0]) 
                                elif parsed[4+i] == "brick":
                                    modify_cards(parsed[0], [0,1,0,0,0,0,0])
                                elif parsed[4+i] == "lumber":
                                    modify_cards(parsed[0], [1,0,0,0,0,0,0])
                        elif parsed[1] == "got:":
                            for i in range(len(parsed)-2):
                                if parsed[2+i] == "grain":
                                    modify_cards(parsed[0], [0,0,0,1,0,0,0])
                                elif parsed[2+i] == "wool":
                                    modify_cards(parsed[0], [0,0,1,0,0,0,0])
                                elif parsed[2+i] == "ore":
                                    modify_cards(parsed[0], [0,0,0,0,1,0,0]) 
                                elif parsed[2+i] == "brick":
                                    modify_cards(parsed[0], [0,1,0,0,0,0,0])
                                elif parsed[2+i] == "lumber":
                                    modify_cards(parsed[0], [1,0,0,0,0,0,0])
                        elif parsed[1] == "traded:":
                            for i in range(parsed.index('for:')-2):
                                if parsed[2+i] == "grain":
                                    modify_cards(parsed[0], [0,0,0,-1,0,0,0])
                                    modify_cards(parsed[-1], [0,0,0,1,0,0,0])
                                elif parsed[2+i] == "wool":
                                    modify_cards(parsed[0], [0,0,-1,0,0,0,0])
                                    modify_cards(parsed[-1], [0,0,1,0,0,0,0])
                                elif parsed[2+i] == "ore":
                                    modify_cards(parsed[0], [0,0,0,0,-1,0,0])
                                    modify_cards(parsed[-1], [0,0,0,0,1,0,0]) 
                                elif parsed[2+i] == "brick":
                                    modify_cards(parsed[0], [0,-1,0,0,0,0,0])
                                    modify_cards(parsed[-1], [0,1,0,0,0,0,0])
                                elif parsed[2+i] == "lumber":
                                    modify_cards(parsed[0], [-1,0,0,0,0,0,0])
                                    modify_cards(parsed[-1], [1,0,0,0,0,0,0])
                            for i in range(parsed.index('with:')-parsed.index('for:')-1):
                                if parsed[parsed.index('for:')+1+i] == "grain":
                                    modify_cards(parsed[0], [0,0,0,1,0,0,0])
                                    modify_cards(parsed[-1], [0,0,0,-1,0,0,0])
                                elif parsed[parsed.index('for:')+1+i] == "wool":
                                    modify_cards(parsed[0], [0,0,1,0,0,0,0])
                                    modify_cards(parsed[-1], [0,0,-1,0,0,0,0])
                                elif parsed[parsed.index('for:')+1+i] == "ore":
                                    modify_cards(parsed[0], [0,0,0,0,1,0,0])
                                    modify_cards(parsed[-1], [0,0,0,0,-1,0,0]) 
                                elif parsed[parsed.index('for:')+1+i] == "brick":
                                    modify_cards(parsed[0], [0,1,0,0,0,0,0])
                                    modify_cards(parsed[-1], [0,-1,0,0,0,0,0])
                                elif parsed[parsed.index('for:')+1+i] == "lumber":
                                    modify_cards(parsed[0], [1,0,0,0,0,0,0])
                                    modify_cards(parsed[-1], [-1,0,0,0,0,0,0])
                        elif parsed[1] == "gave":
                            for i in range(parsed.index('and')-2):
                                if parsed[3+i] == "grain":
                                    modify_cards(parsed[0], [0,0,0,-1,0,0,0])
                                elif parsed[3+i] == "wool":
                                    modify_cards(parsed[0], [0,0,-1,0,0,0,0])
                                elif parsed[3+i] == "ore":
                                    modify_cards(parsed[0], [0,0,0,0,-1,0,0])
                                elif parsed[3+i] == "brick":
                                    modify_cards(parsed[0], [0,-1,0,0,0,0,0])
                                elif parsed[3+i] == "lumber":
                                    modify_cards(parsed[0], [-1,0,0,0,0,0,0])
                            for i in range(len(parsed)-parsed.index('took')-1):
                                if parsed[parsed.index('took')+1+i] == "grain":
                                    modify_cards(parsed[0], [0,0,0,1,0,0,0])
                                elif parsed[parsed.index('took')+1+i] == "wool":
                                    modify_cards(parsed[0], [0,0,1,0,0,0,0])
                                elif parsed[parsed.index('took')+1+i] == "ore":
                                    modify_cards(parsed[0], [0,0,0,0,1,0,0])
                                elif parsed[parsed.index('took')+1+i] == "brick":
                                    modify_cards(parsed[0], [0,1,0,0,0,0,0])
                                elif parsed[parsed.index('took')+1+i] == "lumber":
                                    modify_cards(parsed[0], [1,0,0,0,0,0,0])   
                        elif parsed[1] == "stole:":
                            if parsed[-1] == "you":
                                if "grain" in parsback:
                                    modify_cards(parsed[0], [0,0,0,1,0,0,0])
                                    modify_cards(you, [0,0,0,-1,0,0,0])
                                elif "ore" in parsback:
                                    modify_cards(parsed[0], [0,0,0,0,1,0,0]) 
                                    modify_cards(you, [0,0,0,0,-1,0,0]) 
                                elif "wool" in parsback:
                                    modify_cards(parsed[0], [0,0,1,0,0,0,0])
                                    modify_cards(you, [0,0,-1,0,0,0,0])
                                elif "brick" in parsback:
                                    modify_cards(parsed[0], [0,1,0,0,0,0,0])
                                    modify_cards(you, [0,-1,0,0,0,0,0])
                                elif "lumber" in parsback:
                                    modify_cards(parsed[0], [1,0,0,0,0,0,0])
                                    modify_cards(you, [-1,0,0,0,0,0,0])
                            else: 
                                if "grain" in parsback:
                                    modify_cards(you, [0,0,0,1,0,0,0])
                                    modify_cards(parsed[-1], [0,0,0,-1,0,0,0])
                                elif "ore" in parsback:
                                    modify_cards(you, [0,0,0,0,1,0,0]) 
                                    modify_cards(parsed[-1], [0,0,0,0,-1,0,0]) 
                                elif "wool" in parsback:
                                    modify_cards(you, [0,0,1,0,0,0,0])
                                    modify_cards(parsed[-1], [0,0,-1,0,0,0,0])
                                elif "brick" in parsback:
                                    modify_cards(you, [0,1,0,0,0,0,0])
                                    modify_cards(parsed[-1], [0,-1,0,0,0,0,0])
                                elif "lumber" in parsback:
                                    modify_cards(you, [1,0,0,0,0,0,0])
                                    modify_cards(parsed[-1], [-1,0,0,0,0,0,0])
                        elif parsed[1] == "stole":
                            if parsed[-1] == "lumber":
                                modify_cards(parsed[0], [int(parsed[2][0]),0,0,0,0,0,0])
                                if parsed[0]!=order[0]:
                                    p1Cards[0]=0
                                if parsed[0]!=order[1]:
                                    p2Cards[0]=0
                                if parsed[0]!=order[2]:
                                    p3Cards[0]=0
                                if parsed[0]!=order[3]:    
                                    p4Cards[0]=0
                            elif parsed[-1] == "brick":
                                modify_cards(parsed[0], [0,int(parsed[2][0]),0,0,0,0,0])
                                if parsed[0]!=order[0]:
                                    p1Cards[1]=0
                                if parsed[0]!=order[1]:
                                    p2Cards[1]=0
                                if parsed[0]!=order[2]:
                                    p3Cards[1]=0
                                if parsed[0]!=order[3]:  
                                    p4Cards[1]=0
                            elif parsed[-1] == "sheep":
                                modify_cards(parsed[0], [0,0,int(parsed[2][0]),0,0,0,0])
                                if parsed[0]!=order[0]:
                                    p1Cards[2]=0
                                if parsed[0]!=order[1]:
                                    p2Cards[2]=0
                                if parsed[0]!=order[2]:
                                    p3Cards[2]=0
                                if parsed[0]!=order[3]:  
                                    p4Cards[2]=0    
                            elif parsed[-1] == "wheat":
                                modify_cards(parsed[0], [0,0,0,int(parsed[2][0]),0,0,0])
                                if parsed[0]!=order[0]:
                                    p1Cards[3]=0
                                if parsed[0]!=order[1]:
                                    p2Cards[3]=0
                                if parsed[0]!=order[2]:
                                    p3Cards[3]=0
                                if parsed[0]!=order[3]:  
                                    p4Cards[3]=0
                            elif parsed[-1] == "ore":
                                modify_cards(parsed[0], [0,0,0,0,int(parsed[2][0]),0,0])
                                if parsed[0]!=order[0]:
                                    p1Cards[4]=0
                                if parsed[0]!=order[1]:
                                    p2Cards[4]=0
                                if parsed[0]!=order[2]:
                                    p3Cards[4]=0
                                if parsed[0]!=order[3]:  
                                    p4Cards[4]=0
                            else:
                                modify_cards(parsed[0], [0,0,0,0,0,1])
                                modify_cards(parsed[-1], [0,0,0,0,0,-1])
                        elif parsed[1] == "discarded:":
                            for i in range(len(parsed)-2):
                                if parsed[2+i] == "grain":
                                    modify_cards(parsed[0], [0,0,0,-1,0,0,0])
                                elif parsed[2+i] == "ore":
                                    modify_cards(parsed[0], [0,0,0,0,-1,0,0]) 
                                elif parsed[2+i] == "wool":
                                    modify_cards(parsed[0], [0,0,-1,0,0,0,0])
                                elif parsed[2+i] == "brick":
                                    modify_cards(parsed[0], [0,-1,0,0,0,0,0])
                                elif parsed[2+i] == "lumber":
                                    modify_cards(parsed[0], [-1,0,0,0,0,0,0])
                        elif parsed[1] == "bought":
                            modify_cards(parsed[0], [0,0,-1,-1,-1,0,0])
                        elif parsed[1] == "took":
                            for i in range(len(parsed)-4):
                                if parsed[4+i] == "grain":
                                    modify_cards(parsed[0], [0,0,0,1,0,0,0])
                                elif parsed[4+i] == "ore":
                                    modify_cards(parsed[0], [0,0,0,0,1,0,0]) 
                                elif parsed[4+i] == "wool":
                                    modify_cards(parsed[0], [0,0,1,0,0,0,0])
                                elif parsed[4+i] == "brick":
                                    modify_cards(parsed[0], [0,1,0,0,0,0,0])
                                elif parsed[4+i] == "lumber":
                                    modify_cards(parsed[0], [1,0,0,0,0,0,0])
            lenOfLis = len(messages)

            print("    : [ L  B  S  W  O  T  X]")
            print_cards(order[0])
            print_cards(order[1])
            print_cards(order[2])
            print_cards(order[3])
            print("")
            print("TOTL: " + str(p1Cards+p2Cards+p3Cards+p4Cards))
            print("")
    except:
        print("waiting")