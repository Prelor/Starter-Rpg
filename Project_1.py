import time
import os

os.system("cls")

def tab(): #User Experience
    print("-----------")
    print("Current Position: " + area)
    print(" ")
    print("Description: " + desc)
    print("------------")
    
    def descriptor():
        os.system("cls")
        print(descrip)
        enter()

    def redirect():
        if area == "The Path Cont." and p_action == "1":
            crossroads1()
        if area == "First Item" and p_action == "1":
            path_cont1()
            descriptor()
        if area == "The Path" and p_action == "1":                  # This chunk is the actions that advance you
            first_item()
            descriptor()
        if area == "The Beginning" and p_action == "1":
            the_path()
            descriptor()
       
           
        if area == "The Beginning" and p_action == "2":
            os.system("cls")
            print("The sign reads, \"The start of your journey is behind this door\"")
            enter()
            os.system("cls")
        if area == "The Beginning" and p_action == "3":
            print("You do nothing.")
            enter()
        if area == "The Path" and p_action == "2":
            print("The ground trembles in fear.")
            enter()
        if area == "The Path" and p_action == "3":
            beginning()
        if area == "First Item" and p_action == "2":
            os.system("cls")
            print("You look closer at the object and find it's a FLASHLIGHT.")
            global item1
            item1 = "FLASHLIGHT"
            print("You stash the FLASHLIGHT away in your inventory.")
            re_redirect()
            enter()
        if area == "First Item" and p_action == "3":
            os.system("cls")
            print("You try to turn back but are faced with a massive brick wall.")
            enter()
        if area == "The Path Cont." and p_action == "2":
            print("You land...on your face.")
            enter()
        if area == "The Path Cont." and p_action == "3":
            print("A cloud of thick fog prevents you from turning back.")

    def crossroads1():
        global area
        area == "Outside The House"
        global desc
        desc = "There is a small wooden house on the side of The Path."
        global descrip
        descrip = "You keep walking on The Path"
        global action1
        action1 = "Keep walking"
        global action2
        action2 = "Open front door"
        global action3
        action3 = "Go back"
        
        
    def first_item():
        global area
        area = "First Item"
        global desc
        desc = "You spot a shiny object on the side of the path."
        global descrip
        descrip = "You start walking, hopeful of what will come."
        global action1
        action1 = "Ignore it and keep walking"
        global action2
        action2 = "Inspect the object"
        global action3
        action3 = "Go back"

    def enter():
        input("Press Enter To Continue")
        os.system("cls")
    
    def beginning():
        global area
        area = "The Beginning"
        global desc
        desc = "You seem to be inside a small run-down room with a door and a sign just above it."
        global action1
        action1 = "Open Door"
        global action2
        action2 = "Read Sign"
        global action3
        action3 = "Do Nothing"
        global action4
        action4 = "Use Item"

    def the_path():
        global area
        area = "The Path"
        global desc
        desc = "You are at the start of a dirt path that seems to go on forever."
        global action1
        action1 = "Start walking on The Path"
        global action2
        action2 = "Yell at the ground"
        global action3
        action3 = "Go Back"
        
    def path_cont1():
        global area
        area = "The Path Cont."
        global desc
        desc = "You keep moving on this never-ending path."
        global action1
        action1 = "Continue on The Path"
        global action2
        action2 = "Do a backflip"
        global action3
        action3 = "Go back"
        global descrip
        descrip = "You shake your head and start to regain focus on the path."
        
       
    def re_redirect():
        if area == "First Item" and p_action == "2":
            global action1
            action1 = "Keep walking on the path"
            global action2
            action2 = "[Action Used]"
            global desc 
            desc = "There is a hole on the side of the path where an object may have once laid."

    def inventory():
        os.system("cls")
        print("Item Slot 1: " + item1)
        print("Item Slot 2: " + item2)
        print("Item Slot 3: " + item3)
        print("")
        if item1 == "Empty":
            has_item1 = False
        else:
            has_item1 = True        # Messy Messy
        if item2 == "Empty":
            has_item2 = False
        else:                           # All of this is Messy Messy
            has_item2 = True
        if item3 == "Empty":
            has_item3 = False
        else:                                 #Can't even understand sick fuck
            has_item3 = True
        if use_item == False:
            enter()
        if use_item == True:
            if item1 == "Empty" and item2 == "Empty" and item3 == "Empty":
                print("You don't have any items!")
                enter()
            else:
                item_use = input("Item Number: ")                                                                                            
                if item_use == "1":
                    if has_item1 == True:
                        gonna_use1 = input("Use " + item1 + "?(y/n): ")
                    if has_item1 == False:
                        print("There is nothing there!")
                        enter()
                if item_use == "2":                                               # These variables are so understandable right?
                    if has_item2 == True:
                        gonna_use2 = input("Use " + item2 + "?(y/n): ")
                    if has_item2 == False:
                        print("There is nothing there!")
                        enter()
                if item_use == "3":
                    if has_item3 == True:
                        gonna_use3 = input("Use " + item3 + "?(y/n): ")
                    if has_item3 == False:
                        print("There is nothing there!")
                        enter()
    def actions():
        print("Action 1: " + action1)
        print("Action 2: " + action2)
        print("Action 3: " + action3)
        print("Action 4: " + action4)
        print("Action 5: Inventory")
        global p_action
        p_action = input("Enter Action Number: ")
        if p_action == "1" or p_action == "2" or p_action == "3":
            os.system("cls")
            redirect() 
        if p_action == "4":
            global use_item
            use_item = True
            inventory()
        if p_action == "Inventory" or p_action == "5":
            use_item = False
            inventory()
        if p_action == "q" or p_action == "quit":
            global quit
            quit = True
        if p_action == "":
            os.system("cls")
        if p_action == "6" or p_action == "7":
            os.system("cls")
            print("Not a valid action!")
    actions()
    

    

print("Welcome To Your Adventure!")

input("Press Enter To Continue")

os.system("cls")

area = "The Beginning"
 
desc = "You seem to be inside a small run-down room with a door and a sign just above it."

action1 = "Open Door"

action2 = "Read Sign"

action3 = "Do Nothing"

action4 = "Use Item"

item1 = "Empty"

item2 = "Empty"

item3 = "Empty"

descrip = "You open the door and walk outside."

use_item = False

quit = False

while quit == False:
    tab()



