#! /bin/env python3
from Assets.characters import Underpaid_NHS_Worker, Karen, Redundant_Robert, Pensioner_Pete, Teenage_Tyrant
from Assets.enemies import Copper, Virus, Maskless_Mark, Coughing_Chris, Nosey_Neighbor, Savage_Dog
from Assets.items import Tissue_Roll, Hand_Sanitizer, Used_Mask, Rubber_Gloves, Bin_Bag, Mop, Vaccine, Bleach, News_Paper, Broken_Brush, Costa_Coffee, Subway_Sandwich, Bottle_Of_Wine, Big_Mac, Chocolate_Bar
from Assets.bosses import Chris_Whitty, Matt_Hancock, Boris_Johnson
import time 
import random
import os
import sys

# Intro

print("You awaken to a new global threat!")
time.sleep(1)
print("The emergence of Covid-19 has catapulted the world into a state of total disarray...")
time.sleep(1)



#############################################################################
############################ CHARACTER SELECTION ############################
#############################################################################



print("The Playable Characters In This Game Are as Follows:")
time.sleep(1)

Character_List = ["Underpaid_NHS_Worker","Karen","Redundant_Robert","Pensioner_Pete","Teenage_Tyrant"]
print(*Character_List, sep = "\n")
time.sleep(1)

Selection = input("Select Your Character By Entering Character Name ")
time.sleep(1)

if Selection == "Underpaid_NHS_Worker":
    Character = Underpaid_NHS_Worker
    print(f"You Have Selected {Underpaid_NHS_Worker.Name} as your character")
    time.sleep(1)
    print(Underpaid_NHS_Worker.Attack, "Attack")
    time.sleep(1)
    print(Underpaid_NHS_Worker.Defence, "Defence")
    time.sleep(1)
    print(Underpaid_NHS_Worker.Health, "Health")
    time.sleep(1)
    print(Underpaid_NHS_Worker.Backstory)
    time.sleep(1)
            
elif Selection == "Karen":
    Character = Karen
    print(f"You Have Selected {Karen.Name} as your character")
    time.sleep(1)
    print(Karen.Attack, "Attack")
    time.sleep(1)
    print(Karen.Defence, "Defence")
    time.sleep(1)
    print(Karen.Health, "Health")
    time.sleep(1)
    print(Karen.Backstory)
    time.sleep(1)

elif Selection == "Redundant_Robert":
    Character = Redundant_Robert
    print(f"You Have Selected {Redundant_Robert.Name} as your character")
    time.sleep(1)
    print(Redundant_Robert.Attack, "Attack")
    time.sleep(1)
    print(Redundant_Robert.Defence, "Defence")
    time.sleep(1)
    print(Redundant_Robert.Health, "Health")
    time.sleep(1)
    print(Redundant_Robert.Backstory)
    time.sleep(1)    
            

elif Selection == "Pensioner_Pete":
    Character = Pensioner_Pete
    print(f"You Have Selected {Pensioner_Pete.Name} as your character")
    time.sleep(1)
    print(Pensioner_Pete.Attack, "Attack")
    time.sleep(1)
    print(Pensioner_Pete.Defence, "Defence")
    time.sleep(1)
    print(Pensioner_Pete.Health, "Health")
    time.sleep(1)
    print(Pensioner_Pete.Backstory)
    time.sleep(1)        

elif Selection == "Teenage_Tyrant":
    Character = Teenage_Tyrant
    print(f"You Have Selected {Teenage_Tyrant.Name} as your character")
    time.sleep(1)
    print(Teenage_Tyrant.Attack, "Attack")
    time.sleep(1)
    print(Teenage_Tyrant.Defence, "Defence")
    time.sleep(1)
    print(Teenage_Tyrant.Health, "Health")
    time.sleep(1)
    print(Teenage_Tyrant.Backstory)
    time.sleep(1)

        
else:
    print("Fatal Error.... Please Enter Valid Character Name")
    time.sleep(2)
    os.execv(__file__, sys.argv)
         
   

#############################################################################
################################## LOCKDOWN I ###############################
#############################################################################



#LOCKDOWN I Intro

print("These are volatile times...")
time.sleep(1)
print("Large segments of the country are placed under lockdown")
time.sleep(1)
print("Welcome to lockdown I")
time.sleep(1)
print("Due to new restrictions, members of the public have been urged to only leave their homes for essential items")


##########################
### FIRST ITEM CHOICE ####
##########################

# Items List
Item_List = [Tissue_Roll, Hand_Sanitizer, Used_Mask, Rubber_Gloves, 
Bin_Bag, Mop, Vaccine, Bleach, News_Paper, Broken_Brush, Costa_Coffee, 
Subway_Sandwich, Bottle_Of_Wine, Big_Mac, Chocolate_Bar]

# Item_A imported and picked at random.
Item_A = Item_List[random.randrange(0,15)]

print("Pick A Starting Item:")
time.sleep(1)

# Item_A Name And Stats Printed
print(f"Item_A is a {Item_A.Name} with the following stats:")
time.sleep(1)

if Item_A.Attack > 0:
    print(Item_A.Attack, "Attack")
    time.sleep(1)


elif Item_A.Defence > 0:
    print(Item_A.Defence, "Defence")
    time.sleep(1)

elif Item_A.Health > 0:
    print(Item_A.Health, "Health") 
    time.sleep(1)


# Item_B imported and picked at random.
Item_B = Item_List[random.randrange(0,15)]

# Item_B Name And Stats Printed
print(f"Item_B is a {Item_B.Name} with the following stats:")
time.sleep(1)

if Item_B.Attack > 0:
    print(Item_B.Attack, "Attack")
    time.sleep(1)

elif Item_B.Defence > 0:
    print(Item_B.Defence, "Defence")
    time.sleep(1)

elif Item_B.Health > 0:
    print(Item_B.Health, "Health") 
    time.sleep(1)


# Item_C imported and picked at random.
Item_C = Item_List[random.randrange(0,15)]

# Item_C Name And Stats Printed
print(f"Item_C is a {Item_C.Name} with the following stats:")
time.sleep(1)

if Item_C.Attack > 0:
    print(Item_C.Attack, "Attack")
    time.sleep(1)

elif Item_C.Defence > 0:
    print(Item_C.Defence, "Defence")
    time.sleep(1)

elif Item_C.Health > 0:
    print(Item_C.Health, "Health") 
    time.sleep(1)



Select_Starting_item = input("Select an item by typing A, B or C ")
time.sleep(1)

if Select_Starting_item == "A":
    print(f"You have Taken a {Item_A.Name}")
    time.sleep(1)

    Character.Attack += Item_A.Attack
    Character.Defence += Item_A.Defence
    Character.Health += Item_A.Health
    
    print("Your New Character Stats Are:")
    time.sleep(1)

    print(Character.Attack, "Attack")
    time.sleep(1) 
    print(Character.Defence, "Defence")
    time.sleep(1)
    print(Character.Health, "Health")
    time.sleep(1)


elif Select_Starting_item == "B":
    print(f"You have Taken a {Item_B.Name}")
    time.sleep(1)

    Character.Attack += Item_B.Attack
    Character.Defence += Item_B.Defence
    Character.Health += Item_B.Health
    
    print("Your New Character Stats Are:")
    time.sleep(1)

    print(Character.Attack, "Attack")
    time.sleep(1) 
    print(Character.Defence, "Defence")
    time.sleep(1)
    print(Character.Health, "Health")
    time.sleep(1)


elif Select_Starting_item == "C":
    print(f"You have Taken a {Item_C.Name}")
    time.sleep(1)

    Character.Attack += Item_C.Attack
    Character.Defence += Item_C.Defence
    Character.Health += Item_C.Health

    print("Your New Character Stats Are:")
    time.sleep(1)

    print(Character.Attack, "Attack") 
    time.sleep(1)
    print(Character.Defence, "Defence")
    time.sleep(1)
    print(Character.Health, "Health")
    time.sleep(1)
    


#####################
### PATH CHOICE I ###
#####################

print(f"{Character.Name} decides to have a walk to the local shop")
time.sleep(1)

Select_First_Path = input("There are two separate routes A and B to choose from to get to the shop ")
time.sleep(1)

if Select_First_Path == "A":
    Enemy_List = [Copper, Virus, Maskless_Mark, Coughing_Chris, Nosey_Neighbor, Savage_Dog] 
    Enemy = Enemy_List[random.randrange(0,6)]
    Enemy.Health += 25
    print(f"You Walk to the shop and a {Enemy.Name} jumps out and Attacks You.")
    time.sleep(1)

    while Enemy.Health >= 0:
    
        # Enemy Attacking Character 
        Enemy_Attack = Enemy.Attack - Character.Defence
        print(f"A {Enemy.Name} Has Attacked You For {Enemy_Attack} Damage")
        time.sleep(1)
        Character.Health -= Enemy_Attack
        print(f"You Have {Character.Health} Health Remaining")
        time.sleep(1)

        # Character Attacking Enemy
        Character_Attack = Character.Attack - Enemy.Defence
        print(f"You Attacked a {Enemy.Name} For {Character_Attack} Damage")
        time.sleep(1)
        Enemy.Health -= Character_Attack
        print(f"{Enemy.Name} Has {Enemy.Health} Health Remaining")
        time.sleep(1)


        # Character Defeated
        if Character.Health <= 0:
            print(f"You Were Defeated By a {Enemy.Name} Game Over")
            time.sleep(1)
            exit()


        # Character Defeating Enemy
        elif Enemy.Health <= 0:
            print(f"You have Defeated a {Enemy.Name}")
            time.sleep(1)

            Increased_Attack = random.randint(0, 10)
            Increased_Defence =  random.randint(0, 10)
            Increased_Health =  random.randint(0, 10)

            Character.Attack += Increased_Attack
            Character.Defence += Increased_Defence
            Character.Health += Increased_Health 

            # Level Up/Character Stat Increases
            print("Your Combat Experience Has Increased Yours Character Stats To:")
            time.sleep(1)
            print(f"{Character.Attack}, Attack")
            time.sleep(1)
            print(f"{Character.Defence}, Defence")
            time.sleep(1)
            print(f"{Character.Health}, Health")
            time.sleep(1)




if Select_First_Path == "B":
    Enemy_List = [Copper, Virus, Maskless_Mark, Coughing_Chris, Nosey_Neighbor, Savage_Dog] 
    Enemy = Enemy_List[random.randrange(0,6)] 
    Enemy.Health += 30

    print(f"You Take A Right Down Market Street And You're Confronted By a {Enemy.Name}")
    time.sleep(1)

    while Enemy.Health >= 0:
    
        # Enemy Attacking Character 
        Enemy_Attack = Enemy.Attack - Character.Defence
        print(f" A {Enemy.Name} Has Attacked You For {Enemy_Attack} Damage")
        time.sleep(1)
        Character.Health -= Enemy_Attack
        print(f"You Have {Character.Health} Health Remaining")
        time.sleep(1)

        # Character Attacking Enemy
        Character_Attack = Character.Attack - Enemy.Defence
        print(f"You Attacked a {Enemy.Name} For {Character_Attack} Damage")
        time.sleep(1)
        Enemy.Health -= Character_Attack
        print(f"{Enemy.Name} Has {Enemy.Health} Health Remaining")
        time.sleep(1)

        # Character Defeated
        if Character.Health <= 0:
            print(f"You Were Defeated By a {Enemy.Name} Game Over")
            time.sleep(1)
            exit()

        # Character Defeating Enemy
        elif Enemy.Health <= 0:
            print(f"You have Defeated a {Enemy.Name}")
            time.sleep(1)

            Increased_Attack = random.randint(0, 10)
            Increased_Defence =  random.randint(0, 10)
            Increased_Health =  random.randint(0, 10)

            Character.Attack += Increased_Attack
            Character.Defence += Increased_Defence
            Character.Health += Increased_Health 

            # Level Up/Character Stat Increases
            print("Your Combat Experience Has Increased Yours Character Stats To:")
            time.sleep(1)
            print(f"{Character.Attack}, Attack")
            time.sleep(1)
            print(f"{Character.Defence}, Defence")
            time.sleep(1)
            print(f"{Character.Health}, Health")



# Second Combat Of Path B

    Enemy_List = [Copper, Virus, Maskless_Mark, Coughing_Chris, Nosey_Neighbor, Savage_Dog] 
    Enemy = Enemy_List[random.randrange(0,6)]  
    Enemy.Health += 35

    print(f"You Thought It Was All Over When a {Enemy.Name} Pounces On You")
    
    while Enemy.Health >= 0:
    
        # Enemy Attacking Character 
        Enemy_Attack = Enemy.Attack - Character.Defence
        print(f" A {Enemy.Name} Has Attacked You For {Enemy_Attack} Damage")
        time.sleep(1)
        Character.Health -= Enemy_Attack
        print(f"You Have {Character.Health} Health Remaining")
        time.sleep(1)

        # Character Attacking Enemy
        Character_Attack = Character.Attack - Enemy.Defence
        print(f"You Attacked a {Enemy.Name} For {Character_Attack} Damage")
        time.sleep(1)
        Enemy.Health -= Character_Attack
        print(f"{Enemy.Name} Has {Enemy.Health} Remaining")
        time.sleep(1)

        # Character Defeated
        if Character.Health <= 0:
            print(f"You Were Defeated By a {Enemy.Name} Game Over")
            time.sleep(1)
            exit()

        # Character Defeating Enemy
        elif Enemy.Health <= 0:
            print(f"You have Defeated a {Enemy.Name}")
            time.sleep(1)

            Increased_Attack = random.randint(0, 10)
            Increased_Defence =  random.randint(0, 10)
            Increased_Health =  random.randint(0, 10)

            Character.Attack += Increased_Attack
            Character.Defence += Increased_Defence
            Character.Health += Increased_Health 

            # Level Up/Character Stat Increases
            print("Your Combat Experience Has Increased Yours Character Stats To:")
            time.sleep(1)
            print(f"{Character.Attack}, Attack")
            time.sleep(1)
            print(f"{Character.Defence}, Defence")
            time.sleep(1)
            print(f"{Character.Health}, Health")



##########################
### SECOND ITEM CHOICE ###
##########################



# Items List
Item_List = [Tissue_Roll, Hand_Sanitizer, Used_Mask, Rubber_Gloves, 
Bin_Bag, Mop, Vaccine, Bleach, News_Paper, Broken_Brush, Costa_Coffee, 
Subway_Sandwich, Bottle_Of_Wine, Big_Mac, Chocolate_Bar]

# Item_A imported and picked at random.
Item_A = Item_List[random.randrange(0,15)]

# Item_A Name And Stats Printed
print(f"Item_A is a {Item_A.Name} with the following stats:")
time.sleep(1)

if Item_A.Attack > 0:
    print(Item_A.Attack, "Attack")
    time.sleep(1)

elif Item_A.Defence > 0:
    print(Item_A.Defence, "Defence")
    time.sleep(1)

elif Item_A.Health > 0:
    print(Item_A.Health, "Health") 
    time.sleep(1)


# Item_B imported and picked at random.
Item_B = Item_List[random.randrange(0,15)]

# Item_B Name And Stats Printed
print(f"Item_B is a {Item_B.Name} with the following stats:")
time.sleep(1)

if Item_B.Attack > 0:
    print(Item_B.Attack, "Attack")
    time.sleep(1)

elif Item_B.Defence > 0:
    print(Item_B.Defence, "Defence")
    time.sleep(1)

elif Item_B.Health > 0:
    print(Item_B.Health, "Health") 
    time.sleep(1)


# Item_C imported and picked at random.
Item_C = Item_List[random.randrange(0,15)]

# Item_C Name And Stats Printed
print(f"Item_C is a {Item_C.Name} with the following stats:")
time.sleep(1)

if Item_C.Attack > 0:
    print(Item_C.Attack, "Attack")
    time.sleep(1)

elif Item_C.Defence > 0:
    print(Item_C.Defence, "Defence")
    time.sleep(1)

elif Item_C.Health > 0:
    print(Item_C.Health, "Health") 
    time.sleep(1)



Select_Starting_item = input("Select an item by typing A, B or C ")
time.sleep(1)

if Select_Starting_item == "A":
    print(f"You have Taken a {Item_A.Name}")
    time.sleep(1)

    Character.Attack += Item_A.Attack
    Character.Defence += Item_A.Defence
    Character.Health += Item_A.Health
    
    print("Your New Character Stats Are:")
    time.sleep(1)

    print(Character.Attack, "Attack")
    time.sleep(1) 
    print(Character.Defence, "Defence")
    time.sleep(1)
    print(Character.Health, "Health")
    time.sleep(1)


elif Select_Starting_item == "B":
    print(f"You have Taken a {Item_B.Name}")
    time.sleep(1)

    Character.Attack += Item_B.Attack
    Character.Defence += Item_B.Defence
    Character.Health += Item_B.Health
    
    print("Your New Character Stats Are:")
    time.sleep(1)

    print(Character.Attack, "Attack")
    time.sleep(1) 
    print(Character.Defence, "Defence")
    time.sleep(1)
    print(Character.Health, "Health")
    time.sleep(1)


elif Select_Starting_item == "C":
    print(f"You have Taken a {Item_C.Name}")
    time.sleep(1)

    Character.Attack += Item_C.Attack
    Character.Defence += Item_C.Defence
    Character.Health += Item_C.Health

    print("Your New Character Stats Are:")
    time.sleep(1)

    print(Character.Attack, "Attack") 
    time.sleep(1)
    print(Character.Defence, "Defence")
    time.sleep(1)
    print(Character.Health, "Health")
    time.sleep(1)



#####################
### BOSS BATTLE I ###
##################### 



Boss = Chris_Whitty
print(f"You Are Nearing The End Of The First Lockdown But {Boss.Name} Stands In Your Way Prepare For Battle!")
time.sleep(3)
print(Boss.Backstory)
time.sleep(3)

while Boss.Health >= 0:
    
        # Boss Attacking Character 
        Boss_Attack = Boss.Attack - Character.Defence
        print(f"{Boss.Name} Has Attacked You For {Boss_Attack} Damage")
        time.sleep(1)
        Character.Health -= Boss_Attack
        print(f"You Have {Character.Health} Health Remaining")
        time.sleep(1)

            
        Character_Attack = Character.Attack - Boss.Defence
        print(f"You Attacked {Boss.Name} For {Character_Attack} Damage")
        time.sleep(1)
        Boss.Health -= Character_Attack
        print(f"{Boss.Name} Has {Boss.Health} Health Remaining")
        time.sleep(1)

        # Character Defeated
        if Character.Health <= 0:
            print(f"You Were Defeated By {Boss.Name} Game Over")
            time.sleep(2)
            exit()

        # Boss Defeated
        elif Boss.Health <= 0:
            print(f"You have Defeated {Boss.Name}")
            time.sleep(1)
            Increased_Attack = random.randint(0, 10)
            Increased_Defence =  random.randint(0, 10)
            Increased_Health =  random.randint(0, 10)

            Character.Attack += Increased_Attack
            Character.Defence += Increased_Defence
            Character.Health += Increased_Health 

            # Level Up/Character Stat Increases
            print(f"Your Scrap With {Boss.Name} Has Increased Yours Character Stats To:")
            time.sleep(1)
            print(f"{Character.Attack}, Attack")
            time.sleep(1)
            print(f"{Character.Defence}, Defence")
            time.sleep(1)
            print(f"{Character.Health}, Health")
            time.sleep(1)



##############################################################################
################################## LOCKDOWN II ###############################
##############################################################################



# LOCKDOWN II Intro

print("These are volatile times...")
time.sleep(1)
print("Large segments of the country are placed under another lockdown")
time.sleep(1)
print("Welcome to lockdown II")
time.sleep(1)
print("Due to new restrictions, members of the public have been urged to only leave their homes for essential items")
time.sleep(1)



##########################
### THIRD ITEM CHOICE ####
##########################

# Items List
Item_List = [Tissue_Roll, Hand_Sanitizer, Used_Mask, Rubber_Gloves, 
Bin_Bag, Mop, Vaccine, Bleach, News_Paper, Broken_Brush, Costa_Coffee, 
Subway_Sandwich, Bottle_Of_Wine, Big_Mac, Chocolate_Bar]

# Item_A imported and picked at random.
Item_A = Item_List[random.randrange(0,15)]

print("Pick An Item:")
time.sleep(1)

# Item_A Name And Stats Printed
print(f"Item_A is a {Item_A.Name} with the following stats:")
time.sleep(1)

if Item_A.Attack > 0:
    print(Item_A.Attack, "Attack")
    time.sleep(1)

elif Item_A.Defence > 0:
    print(Item_A.Defence, "Defence")
    time.sleep(1)

elif Item_A.Health > 0:
    print(Item_A.Health, "Health") 
    time.sleep(1)


# Item_B imported and picked at random.
Item_B = Item_List[random.randrange(0,15)]

# Item_B Name And Stats Printed
print(f"Item_B is a {Item_B.Name} with the following stats:")
time.sleep(1)

if Item_B.Attack > 0:
    print(Item_B.Attack, "Attack")
    time.sleep(1)

elif Item_B.Defence > 0:
    print(Item_B.Defence, "Defence")
    time.sleep(1)

elif Item_B.Health > 0:
    print(Item_B.Health, "Health") 
    time.sleep(1)


# Item_C imported and picked at random.
Item_C = Item_List[random.randrange(0,15)]

# Item_C Name And Stats Printed
print(f"Item_C is a {Item_C.Name} with the following stats:")
time.sleep(1)

if Item_C.Attack > 0:
    print(Item_C.Attack, "Attack")
    time.sleep(1)

elif Item_C.Defence > 0:
    print(Item_C.Defence, "Defence")
    time.sleep(1)

elif Item_C.Health > 0:
    print(Item_C.Health, "Health") 
    time.sleep(1)



Select_Starting_item = input("Select an item by typing A, B or C ")
time.sleep(1)

if Select_Starting_item == "A":
    print(f"You have Taken a {Item_A.Name}")
    time.sleep(1)

    Character.Attack += Item_A.Attack
    Character.Defence += Item_A.Defence
    Character.Health += Item_A.Health
    
    print("Your New Character Stats Are:")
    time.sleep(1)

    print(Character.Attack, "Attack")
    time.sleep(1) 
    print(Character.Defence, "Defence")
    time.sleep(1)
    print(Character.Health, "Health")
    time.sleep(1)


elif Select_Starting_item == "B":
    print(f"You have Taken a {Item_B.Name}")
    time.sleep(1)

    Character.Attack += Item_B.Attack
    Character.Defence += Item_B.Defence
    Character.Health += Item_B.Health
    
    print("Your New Character Stats Are:")
    time.sleep(1)

    print(Character.Attack, "Attack")
    time.sleep(1) 
    print(Character.Defence, "Defence")
    time.sleep(1)
    print(Character.Health, "Health")
    time.sleep(1)


elif Select_Starting_item == "C":
    print(f"You have Taken a {Item_C.Name}")
    time.sleep(1)

    Character.Attack += Item_C.Attack
    Character.Defence += Item_C.Defence
    Character.Health += Item_C.Health

    print("Your New Character Stats Are:")
    time.sleep(1)

    print(Character.Attack, "Attack") 
    time.sleep(1)
    print(Character.Defence, "Defence")
    time.sleep(1)
    print(Character.Health, "Health")
    time.sleep(1)
    


######################
### PATH CHOICE II ###
######################

print("You are out and about walking, taking your daily (one!!) hour exercise ")
time.sleep(1)
Select_First_Path = input("Which route will you take A or B? ")
time.sleep(1)

if Select_First_Path == "A":
    Enemy_List = [Copper, Virus, Maskless_Mark, Coughing_Chris, Nosey_Neighbor, Savage_Dog] 
    Enemy = Enemy_List[random.randrange(0,6)] 
    Enemy.Health += 40


    print(f"You are walking down an alleyway and a {Enemy.Name} appears and you are forced to defend yourself...")
    time.sleep(1)

    while Enemy.Health >= 0:
    
        # Enemy Attacking Character 
        Enemy_Attack = Enemy.Attack - Character.Defence
        print(f" A {Enemy.Name} Has Attacked You For {Enemy_Attack} Damage")
        time.sleep(1)
        Character.Health -= Enemy_Attack
        print(f"You Have {Character.Health} Health Remaining")
        time.sleep(1)

        # Character Attacking Enemy
        Character_Attack = Character.Attack - Enemy.Defence
        print(f"You Attacked a {Enemy.Name} For {Character_Attack} Damage")
        time.sleep(1)
        Enemy.Health -= Character_Attack
        print(f"{Enemy.Name} Has {Enemy.Health} Remaining")
        time.sleep(1)

        # Character Defeated
        if Character.Health <= 0:
            print(f"You Were Defeated By a {Enemy.Name} Game Over")
            time.sleep(1)
            exit()

        # Character Defeating Enemy
        elif Enemy.Health <= 0:
            print(f"You have Defeated a {Enemy.Name}")
            time.sleep(1)

            Increased_Attack = random.randint(0, 10)
            Increased_Defence =  random.randint(0, 10)
            Increased_Health =  random.randint(0, 10)

            Character.Attack += Increased_Attack
            Character.Defence += Increased_Defence
            Character.Health += Increased_Health 

            # Level Up/Character Stat Increases
            print("Your Combat Experience Has Increased Yours Character Stats To:")
            time.sleep(1)
            print(f"{Character.Attack}, Attack")
            time.sleep(1)
            print(f"{Character.Defence}, Defence")
            time.sleep(1)
            print(f"{Character.Health}, Health")




if Select_First_Path == "B":
    Enemy_List = [Copper, Virus, Maskless_Mark, Coughing_Chris, Nosey_Neighbor, Savage_Dog] 
    Enemy = Enemy_List[random.randrange(0,6)] 
    Enemy.Health += 45

    print(f"You Take A Right Down Market Street And You're Confronted By a {Enemy.Name} you suddenly feel you are under attack and, therefore, must engage in battle...")
    
    time.sleep(1)

    while Enemy.Health >= 0:
    
        # Enemy Attacking Character 
        Enemy_Attack = Enemy.Attack - Character.Defence
        print(f" A {Enemy.Name} Has Attacked You For {Enemy_Attack} Damage")
        time.sleep(1)
        Character.Health -= Enemy_Attack
        print(f"You Have {Character.Health} Health Remaining")
        time.sleep(1)

        # Character Attacking Enemy
        Character_Attack = Character.Attack - Enemy.Defence
        print(f"You Attacked a {Enemy.Name} For {Character_Attack} Damage")
        time.sleep(1)
        Enemy.Health -= Character_Attack
        print(f"{Enemy.Name} Has {Enemy.Health} Remaining")
        time.sleep(1)

        # Character Defeated
        if Character.Health <= 0:
            print(f"You Were Defeated By a {Enemy.Name} Game Over")
            time.sleep(1)
            exit()

        # Character Defeating Enemy
        elif Enemy.Health <= 0:
            print(f"You have Defeated a {Enemy.Name}")
            time.sleep(1)

            Increased_Attack = random.randint(0, 10)
            Increased_Defence =  random.randint(0, 10)
            Increased_Health =  random.randint(0, 10)

            Character.Attack += Increased_Attack
            Character.Defence += Increased_Defence
            Character.Health += Increased_Health 

            # Level Up/Character Stat Increases
            print("Your Combat Experience Has Increased Yours Character Stats To:")
            time.sleep(1)
            print(f"{Character.Attack}, Attack")
            time.sleep(1)
            print(f"{Character.Defence}, Defence")
            time.sleep(1)
            print(f"{Character.Health}, Health")



# Second Combat Of Path B

    Enemy_List = [Copper, Virus, Maskless_Mark, Coughing_Chris, Nosey_Neighbor, Savage_Dog] 
    Enemy = Enemy_List[random.randrange(0,6)]  
    Enemy.Health += 50
    print(f"You Thought It Was All Over When {Enemy.Name} Squares up to You")
    
    while Enemy.Health >= 0:
    
        # Enemy Attacking Character 
        Enemy_Attack = Enemy.Attack - Character.Defence
        print(f" A {Enemy.Name} Has Attacked You For {Enemy_Attack} Damage")
        time.sleep(1)
        Character.Health -= Enemy_Attack
        print(f"You Have {Character.Health} Health Remaining")
        time.sleep(1)

        # Character Attacking Enemy
        Character_Attack = Character.Attack - Enemy.Defence
        print(f"You Attacked a {Enemy.Name} For {Character_Attack} Damage")
        time.sleep(1)
        Enemy.Health -= Character_Attack
        print(f"{Enemy.Name} Has {Enemy.Health} Remaining")
        time.sleep(1)

        # Character Defeated
        if Character.Health <= 0:
            print(f"You Were Defeated By a {Enemy.Name} Game Over")
            time.sleep(1)
            exit()

        # Character Defeating Enemy
        elif Enemy.Health <= 0:
            print(f"You have Defeated a {Enemy.Name}")
            time.sleep(1)

            Increased_Attack = random.randint(0, 10)
            Increased_Defence =  random.randint(0, 10)
            Increased_Health =  random.randint(0, 10)

            Character.Attack += Increased_Attack
            Character.Defence += Increased_Defence
            Character.Health += Increased_Health 

            # Level Up/Character Stat Increases
            print("Your Combat Experience Has Increased Yours Character Stats To:")
            time.sleep(1)
            print(f"{Character.Attack}, Attack")
            time.sleep(1)
            print(f"{Character.Defence}, Defence")
            time.sleep(1)
            print(f"{Character.Health}, Health")



############################
#### FOURTH ITEM CHOICE ####
############################



# Items List
Item_List = [Tissue_Roll, Hand_Sanitizer, Used_Mask, Rubber_Gloves, 
Bin_Bag, Mop, Vaccine, Bleach, News_Paper, Broken_Brush, Costa_Coffee, 
Subway_Sandwich, Bottle_Of_Wine, Big_Mac, Chocolate_Bar]

# Item_A imported and picked at random.
Item_A = Item_List[random.randrange(0,15)]

# Item_A Name And Stats Printed
print(f"Item_A is a {Item_A.Name} with the following stats:")
time.sleep(1)

if Item_A.Attack > 0:
    print(Item_A.Attack, "Attack")
    time.sleep(1)

elif Item_A.Defence > 0:
    print(Item_A.Defence, "Defence")
    time.sleep(1)

elif Item_A.Health > 0:
    print(Item_A.Health, "Health") 
    time.sleep(1)


# Item_B imported and picked at random.
Item_B = Item_List[random.randrange(0,15)]

# Item_B Name And Stats Printed
print(f"Item_B is a {Item_B.Name} with the following stats:")
time.sleep(1)

if Item_B.Attack > 0:
    print(Item_B.Attack, "Attack")
    time.sleep(1)

elif Item_B.Defence > 0:
    print(Item_B.Defence, "Defence")
    time.sleep(1)

elif Item_B.Health > 0:
    print(Item_B.Health, "Health") 
    time.sleep(1)


# Item_C imported and picked at random.
Item_C = Item_List[random.randrange(0,15)]

# Item_C Name And Stats Printed
print(f"Item_C is a {Item_C.Name} with the following stats:")
time.sleep(1)

if Item_C.Attack > 0:
    print(Item_C.Attack, "Attack")
    time.sleep(1)

elif Item_C.Defence > 0:
    print(Item_C.Defence, "Defence")
    time.sleep(1)

elif Item_C.Health > 0:
    print(Item_C.Health, "Health") 
    time.sleep(1)



Select_Starting_item = input("Select an item by typing A, B or C ")
time.sleep(1)

if Select_Starting_item == "A":
    print(f"You have Taken a {Item_A.Name}")
    time.sleep(1)

    Character.Attack += Item_A.Attack
    Character.Defence += Item_A.Defence
    Character.Health += Item_A.Health
    
    print("Your New Character Stats Are:")
    time.sleep(1)

    print(Character.Attack, "Attack")
    time.sleep(1) 
    print(Character.Defence, "Defence")
    time.sleep(1)
    print(Character.Health, "Health")
    time.sleep(1)


elif Select_Starting_item == "B":
    print(f"You have Taken a {Item_B.Name}")
    time.sleep(1)

    Character.Attack += Item_B.Attack
    Character.Defence += Item_B.Defence
    Character.Health += Item_B.Health
    
    print("Your New Character Stats Are:")
    time.sleep(1)

    print(Character.Attack, "Attack")
    time.sleep(1) 
    print(Character.Defence, "Defence")
    time.sleep(1)
    print(Character.Health, "Health")
    time.sleep(1)


elif Select_Starting_item == "C":
    print(f"You have Taken a {Item_C.Name}")
    time.sleep(1)

    Character.Attack += Item_C.Attack
    Character.Defence += Item_C.Defence
    Character.Health += Item_C.Health

    print("Your New Character Stats Are:")
    time.sleep(1)

    print(Character.Attack, "Attack") 
    time.sleep(1)
    print(Character.Defence, "Defence")
    time.sleep(1)
    print(Character.Health, "Health")
    time.sleep(1)



######################
### BOSS BATTLE II ###
######################



Boss = Matt_Hancock
print(f"You Are Nearing The End Of The Second Lockdown But {Boss.Name} stands in you way, time to sort him out")
time.sleep(3)
print(Boss.Backstory)
time.sleep(3)

while Boss.Health >= 0:

        # Boss Attacking Character
        Boss_Attack = Boss.Attack - Character.Defence
        print(f"{Boss.Name} Has Attacked You For {Boss_Attack} Damage")
        time.sleep(1)
        Character.Health -= Boss_Attack
        print(f"You Have {Character.Health} Health Remaining")
        time.sleep(1)

        # Character Attacking Boss
        Character_Attack = Character.Attack - Boss.Defence
        print(f"You Attacked {Boss.Name} For {Character_Attack} Damage")
        time.sleep(1)
        Boss.Health -= Character_Attack
        print(f"{Boss.Name} Has {Boss.Health} Health Remaining")
        time.sleep(1)


        # Character Defeated
        if Character.Health <= 0:
            print(f"You Were Defeated By {Boss.Name} Game Over")
            time.sleep(2)
            exit()

        # Boss Defeated
        elif Boss.Health <= 0:
            print(f"You have slain {Boss.Name}")
            time.sleep(1)
            Increased_Attack = random.randint(0, 10)
            Increased_Defence =  random.randint(0, 10)
            Increased_Health =  random.randint(0, 10)

            Character.Attack += Increased_Attack
            Character.Defence += Increased_Defence
            Character.Health += Increased_Health 

            # Level Up/Character Stat Increases
            print(f"Your Scrap With {Boss.Name} Has Increased Yours Character Stats To:")
            time.sleep(1)
            print(f"{Character.Attack}, Attack")
            time.sleep(1)
            print(f"{Character.Defence}, Defence")
            time.sleep(1)
            print(f"{Character.Health}, Health")
            time.sleep(1)



###############################################################################
################################## LOCKDOWN III ###############################
###############################################################################



# LOCKDOWN III Intro

print("These are volatile times...")
time.sleep(1)
print("Large segments of the country are placed under another (another) lockdown")
time.sleep(1)
print("Welcome to lockdown III")
time.sleep(1)
print("Due to new restrictions, members of the public have been urged to only leave their homes for essential items")
time.sleep(1)



##########################
### FIFTH ITEM CHOICE ####
##########################



# Items List
Item_List = [Tissue_Roll, Hand_Sanitizer, Used_Mask, Rubber_Gloves, 
Bin_Bag, Mop, Vaccine, Bleach, News_Paper, Broken_Brush, Costa_Coffee, 
Subway_Sandwich, Bottle_Of_Wine, Big_Mac, Chocolate_Bar]

# Item_A imported and picked at random.
Item_A = Item_List[random.randrange(0,15)]

print("Pick An Item:")
time.sleep(1)

# Item_A Name And Stats Printed
print(f"Item_A is a {Item_A.Name} with the following stats:")
time.sleep(1)

if Item_A.Attack > 0:
    print(Item_A.Attack, "Attack")
    time.sleep(1)

elif Item_A.Defence > 0:
    print(Item_A.Defence, "Defence")
    time.sleep(1)

elif Item_A.Health > 0:
    print(Item_A.Health, "Health") 
    time.sleep(1)


# Item_B imported and picked at random.
Item_B = Item_List[random.randrange(0,15)]

# Item_B Name And Stats Printed
print(f"Item_B is a {Item_B.Name} with the following stats:")
time.sleep(1)

if Item_B.Attack > 0:
    print(Item_B.Attack, "Attack")
    time.sleep(1)

elif Item_B.Defence > 0:
    print(Item_B.Defence, "Defence")
    time.sleep(1)

elif Item_B.Health > 0:
    print(Item_B.Health, "Health") 
    time.sleep(1)


# Item_C imported and picked at random.
Item_C = Item_List[random.randrange(0,15)]

# Item_C Name And Stats Printed
print(f"Item_C is a {Item_C.Name} with the following stats:")
time.sleep(1)

if Item_C.Attack > 0:
    print(Item_C.Attack, "Attack")
    time.sleep(1)

elif Item_C.Defence > 0:
    print(Item_C.Defence, "Defence")
    time.sleep(1)

elif Item_C.Health > 0:
    print(Item_C.Health, "Health") 
    time.sleep(1)



Select_Starting_item = input("Select an item by typing A, B or C ")
time.sleep(1)

if Select_Starting_item == "A":
    print(f"You have Taken a {Item_A.Name}")
    time.sleep(1)

    Character.Attack += Item_A.Attack
    Character.Defence += Item_A.Defence
    Character.Health += Item_A.Health
    
    print("Your New Character Stats Are:")
    time.sleep(1)

    print(Character.Attack, "Attack")
    time.sleep(1) 
    print(Character.Defence, "Defence")
    time.sleep(1)
    print(Character.Health, "Health")
    time.sleep(1)


elif Select_Starting_item == "B":
    print(f"You have Taken a {Item_B.Name}")
    time.sleep(1)

    Character.Attack += Item_B.Attack
    Character.Defence += Item_B.Defence
    Character.Health += Item_B.Health
    
    print("Your New Character Stats Are:")
    time.sleep(1)

    print(Character.Attack, "Attack")
    time.sleep(1) 
    print(Character.Defence, "Defence")
    time.sleep(1)
    print(Character.Health, "Health")
    time.sleep(1)


elif Select_Starting_item == "C":
    print(f"You have Taken a {Item_C.Name}")
    time.sleep(1)

    Character.Attack += Item_C.Attack
    Character.Defence += Item_C.Defence
    Character.Health += Item_C.Health

    print("Your New Character Stats Are:")
    time.sleep(1)

    print(Character.Attack, "Attack") 
    time.sleep(1)
    print(Character.Defence, "Defence")
    time.sleep(1)
    print(Character.Health, "Health")
    time.sleep(1)
    


#######################
### PATH CHOICE III ###
#######################


Select_First_Path = input("You are on your way into an illegal rave which entrance will you take A or B? ")
time.sleep(1)

if Select_First_Path == "A":
    Enemy_List = [Copper, Virus, Maskless_Mark, Coughing_Chris, Nosey_Neighbor, Savage_Dog] 
    Enemy = Enemy_List[random.randrange(0,6)]
    Enemy.Health += 55
    
    print(f"You enter through the backdoor when a {Enemy.Name} asks you for a light.")
    time.sleep(1)

    while Enemy.Health >= 0:
    
        # Enemy Attacking Character 
        Enemy_Attack = Enemy.Attack - Character.Defence
        print(f" A {Enemy.Name} Has Attacked You For {Enemy_Attack} Damage")
        time.sleep(1)
        Character.Health -= Enemy_Attack
        print(f"You Have {Character.Health} Health Remaining")
        time.sleep(1)

        # Character Attacking Enemy
        Character_Attack = Character.Attack - Enemy.Defence
        print(f"You Attacked a {Enemy.Name} For {Character_Attack} Damage")
        time.sleep(1)
        Enemy.Health -= Character_Attack
        print(f"{Enemy.Name} Has {Enemy.Health} Remaining")
        time.sleep(1)

        # Character Defeated
        if Character.Health <= 0:
            print(f"You Were Defeated By a {Enemy.Name} Game Over")
            time.sleep(1)
            exit()

        # Character Defeating Enemy
        elif Enemy.Health <= 0:
            print(f"You have Defeated a {Enemy.Name}")
            time.sleep(1)

            Increased_Attack = random.randint(0, 10)
            Increased_Defence =  random.randint(0, 10)
            Increased_Health =  random.randint(0, 10)

            Character.Attack += Increased_Attack
            Character.Defence += Increased_Defence
            Character.Health += Increased_Health 

            # Level Up/Character Stat Increases
            print("Your Combat Experience Has Increased Yours Character Stats To:")
            time.sleep(1)
            print(f"{Character.Attack}, Attack")
            print(f"{Character.Defence}, Defence")
            print(f"{Character.Health}, Health")




if Select_First_Path == "B":
    Enemy_List = [Copper, Virus, Maskless_Mark, Coughing_Chris, Nosey_Neighbor, Savage_Dog] 
    Enemy = Enemy_List[random.randrange(0,6)] 
    Enemy.Health += 60

    print(f"You kick open the fire escape when a {Enemy.Name} is within your 2 metre personal space")
    time.sleep(1)

    while Enemy.Health >= 0:
    
        # Enemy Attacking Character 
        Enemy_Attack = Enemy.Attack - Character.Defence
        print(f"A {Enemy.Name} Has Attacked You For {Enemy_Attack} Damage")
        time.sleep(1)
        Character.Health -= Enemy_Attack
        print(f"You Have {Character.Health} Health Remaining")
        time.sleep(1)

        # Character Attacking Enemy
        Character_Attack = Character.Attack - Enemy.Defence
        print(f"You Attacked a {Enemy.Name} For {Character_Attack} Damage")
        time.sleep(1)
        Enemy.Health -= Character_Attack
        print(f"{Enemy.Name} Has {Enemy.Health} Remaining")
        time.sleep(1)

        # Character Defeated
        if Character.Health <= 0:
            print(f"You Were Defeated By a {Enemy.Name} Game Over")
            time.sleep(1)
            exit()

        # Character Defeating Enemy
        elif Enemy.Health <= 0:
            print(f"You have Defeated a {Enemy.Name}")
            time.sleep(1)

            Increased_Attack = random.randint(0, 10)
            Increased_Defence =  random.randint(0, 10)
            Increased_Health =  random.randint(0, 10)

            Character.Attack += Increased_Attack
            Character.Defence += Increased_Defence
            Character.Health += Increased_Health 

            # Level Up/Character Stat Increases
            print("Your Combat Experience Has Increased Yours Character Stats To:")
            time.sleep(1)
            print(f"{Character.Attack}, Attack")
            time.sleep(1)
            print(f"{Character.Defence}, Defence")
            time.sleep(1)
            print(f"{Character.Health}, Health")



# Second Combat Of Path B

    Enemy_List = [Copper, Virus, Maskless_Mark, Coughing_Chris, Nosey_Neighbor, Savage_Dog] 
    Enemy = Enemy_List[random.randrange(0,6)]  
    Enemy.Health += 60

    print(f"You thought it was all over when a {Enemy.Name} starts clapping for the NHS, so you are forced to defend yourself...")
    
    while Enemy.Health >= 0:
    
        # Enemy Attacking Character 
        Enemy_Attack = Enemy.Attack - Character.Defence
        print(f"A {Enemy.Name} Has Attacked You For {Enemy_Attack} Damage")
        time.sleep(1)
        Character.Health -= Enemy_Attack
        print(f"You Have {Character.Health} Health Remaining")
        time.sleep(1)

        # Character Attacking Enemy
        Character_Attack = Character.Attack - Enemy.Defence
        print(f"You Attacked a {Enemy.Name} For {Character_Attack} Damage")
        time.sleep(1)
        Enemy.Health -= Character_Attack
        print(f"{Enemy.Name} Has {Enemy.Health} Remaining")
        time.sleep(1)

        # Character Defeated
        if Character.Health <= 0:
            print(f"You Were Defeated By a {Enemy.Name} Game Over")
            time.sleep(1)
            exit()

        # Character Defeating Enemy
        elif Enemy.Health <= 0:
            print(f"You have Defeated a {Enemy.Name}")
            time.sleep(1)

            Increased_Attack = random.randint(0, 10)
            Increased_Defence =  random.randint(0, 10)
            Increased_Health =  random.randint(0, 10)

            Character.Attack += Increased_Attack
            Character.Defence += Increased_Defence
            Character.Health += Increased_Health 

            # Level Up/Character Stat Increases
            print("Your Combat Experience Has Increased Yours Character Stats To:")
            time.sleep(1)
            print(f"{Character.Attack}, Attack")
            time.sleep(1)
            print(f"{Character.Defence}, Defence")
            time.sleep(1)
            print(f"{Character.Health}, Health")
            time.sleep(1)



###########################
#### SIXTH ITEM CHOICE ####
###########################



# Items List
Item_List = [Tissue_Roll, Hand_Sanitizer, Used_Mask, Rubber_Gloves, 
Bin_Bag, Mop, Vaccine, Bleach, News_Paper, Broken_Brush, Costa_Coffee, 
Subway_Sandwich, Bottle_Of_Wine, Big_Mac, Chocolate_Bar]

# Item_A imported and picked at random.
Item_A = Item_List[random.randrange(0,15)]

# Item_A Name And Stats Printed
print(f"Item_A is a {Item_A.Name} with the following stats:")
time.sleep(1)

if Item_A.Attack > 0:
    print(Item_A.Attack, "Attack")
    time.sleep(1)

elif Item_A.Defence > 0:
    print(Item_A.Defence, "Defence")
    time.sleep(1)

elif Item_A.Health > 0:
    print(Item_A.Health, "Health") 
    time.sleep(1)


# Item_B imported and picked at random.
Item_B = Item_List[random.randrange(0,15)]

# Item_B Name And Stats Printed
print(f"Item_B is a {Item_B.Name} with the following stats:")
time.sleep(1)

if Item_B.Attack > 0:
    print(Item_B.Attack, "Attack")
    time.sleep(1)

elif Item_B.Defence > 0:
    print(Item_B.Defence, "Defence")
    time.sleep(1)

elif Item_B.Health > 0:
    print(Item_B.Health, "Health") 
    time.sleep(1)


# Item_C imported and picked at random.
Item_C = Item_List[random.randrange(0,15)]

# Item_C Name And Stats Printed
print(f"Item_C is a {Item_C.Name} with the following stats:")
time.sleep(1)

if Item_C.Attack > 0:
    print(Item_C.Attack, "Attack")
    time.sleep(1)

elif Item_C.Defence > 0:
    print(Item_C.Defence, "Defence")
    time.sleep(1)

elif Item_C.Health > 0:
    print(Item_C.Health, "Health") 
    time.sleep(1)



Select_Starting_item = input("Select an item by typing A, B or C ")
time.sleep(1)

if Select_Starting_item == "A":
    print(f"You have Taken a {Item_A.Name}")
    time.sleep(1)

    Character.Attack += Item_A.Attack
    Character.Defence += Item_A.Defence
    Character.Health += Item_A.Health
    
    print("Your New Character Stats Are:")
    time.sleep(1)

    print(Character.Attack, "Attack")
    time.sleep(1) 
    print(Character.Defence, "Defence")
    time.sleep(1)
    print(Character.Health, "Health")
    time.sleep(1)


elif Select_Starting_item == "B":
    print(f"You have Taken a {Item_B.Name}")
    time.sleep(1)

    Character.Attack += Item_B.Attack
    Character.Defence += Item_B.Defence
    Character.Health += Item_B.Health
    
    print("Your New Character Stats Are:")
    time.sleep(1)

    print(Character.Attack, "Attack")
    time.sleep(1) 
    print(Character.Defence, "Defence")
    time.sleep(1)
    print(Character.Health, "Health")
    time.sleep(1)


elif Select_Starting_item == "C":
    print(f"You have Taken a {Item_C.Name}")
    time.sleep(1)

    Character.Attack += Item_C.Attack
    Character.Defence += Item_C.Defence
    Character.Health += Item_C.Health

    print("Your New Character Stats Are:")
    time.sleep(1)

    print(Character.Attack, "Attack") 
    time.sleep(1)
    print(Character.Defence, "Defence")
    time.sleep(1)
    print(Character.Health, "Health")
    time.sleep(1)



#######################
### BOSS BATTLE III ###
#######################



Boss = Boris_Johnson
print(f"You Are Nearing The End Of The Third And Last Lockdown But {Boss.Name} has adviced to stay indoors but go outside")
time.sleep(3)
print(Boss.Backstory)
time.sleep(3)

while Boss.Health >= 0:

        # Boss Attacking Character
        Boss_Attack = Boss.Attack - Character.Defence
        print(f"{Boss.Name} Has Attacked You For {Boss_Attack} Damage")
        time.sleep(1)
        Character.Health -= Boss_Attack
        print(f"You Have {Character.Health} Health Remaining")
        time.sleep(1)

        # Character Attacking Boss
        Character_Attack = Character.Attack - Boss.Defence
        print(f"You Attacked {Boss.Name} For {Character_Attack} Damage")
        time.sleep(1)
        Boss.Health -= Character_Attack
        print(f"{Boss.Name} Has {Boss.Health} Health Remaining")
        time.sleep(1)

        # Character Defeated
        if Character.Health <= 0:
            print(f"You Were Defeated By {Boss.Name} Game Over")
            time.sleep(2)
            exit()

        # Boss Defeated
        elif Boss.Health <= 0:
            print(f"You have Smited {Boss.Name}")
            time.sleep(1)
            
            print(f"Congratulations You have Defeated {Boss.Name} And Escaped Lockdown!!! welcome to tax rises")