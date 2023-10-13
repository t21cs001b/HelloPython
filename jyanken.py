'''
Created on 2023/10/13

@author: t21cs001
'''
import random

def jyanken():
    awin = 0
    bwin = 0
    
    while awin < 3 and bwin < 3:
        a = random.randint(0, 2)
        b = random.randint(0, 2)

        hands = ["グー", "チョキ", "パー"]

        print("Aの手:", hands[a])
        print("Bの手:", hands[b])

        if a == b:
            print("引き分け")
        elif (a - b == 1) or (a - b == -2):
            print("Aの勝ち")
            awin += 1
        else:
            print("Bの勝ち")
            bwin += 1
    
    if awin > bwin:
        print("Aの勝ち")
    else:
        print("Bの勝ち")
jyanken()
