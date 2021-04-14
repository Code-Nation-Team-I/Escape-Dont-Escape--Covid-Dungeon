#! /bin/env python3
from characters import Test, Test2, Test3, Test4, Test5
from enemies import TestA, TestB, TestC
from items import Sword, Helmet
from bosses import Boss1, Boss2, Boss3
import time 
import random
import os
import sys

# Intro here

#############################################################################
############################ CHARACTER SELECTION ############################
#############################################################################

print("The Playable Characters In This Game Are as Follows:")
time.sleep(1)

Character_List = ["Test","Test2","Test3","Test4","Test5"]
print(*Character_List, sep = "\n")
time.sleep(1)

Selection = input("Select Your Character By Entering Character Name ")
time.sleep(1)

if Selection == "Test":
    Character = Test
    print("You Have Selected Test as your character")
    time.sleep(1)
    print(Test.Attack, "Attack")
    time.sleep(1)
    print(Test.Defence, "Defence")
    time.sleep(1)
    print(Test.Health, "Health")
    time.sleep(1)
    print(Test.backstory)
    time.sleep(1)
            
elif Selection == "Test2":
    Character = Test2
    print("You Have Selected Test2 as your character")
    time.sleep(1)
    print(Test2.Attack, "Attack")
    time.sleep(1)
    print(Test2.Defence, "Defence")
    time.sleep(1)
    print(Test2.Health, "Health")
    time.sleep(1)
    print(Test2.backstory)
    time.sleep(1)

elif Selection == "Test3":
    Character = Test3
    print("You Have Selected Test3 as your character")
    time.sleep(1)
    print(Test3.Attack, "Attack")
    time.sleep(1)
    print(Test3.Defence, "Defence")
    time.sleep(1)
    print(Test3.Health, "Health")
    time.sleep(1)
    print(Test3.backstory)
    time.sleep(1)    
            

elif Selection == "Test4":
    Character = Test4
    print("You Have Selected Test4 as your character")
    time.sleep(1)
    print(Test4.Attack, "Attack")
    time.sleep(1)
    print(Test4.Defence, "Defence")
    time.sleep(1)
    print(Test4.Health, "Health")
    time.sleep(1)
    print(Test4.backstory)
    time.sleep(1)        

elif Selection == "Test5":
    Character = Test5
    print("You Have Selected Test5 as your character")
    time.sleep(1)
    print(Test5.Attack, "Attack")
    time.sleep(1)
    print(Test5.Defence, "Defence")
    time.sleep(1)
    print(Test5.Health, "Health")
    time.sleep(1)
    print(Test5.backstory)
    time.sleep(1)

        
else:
    print("Fatal Error.... Please Enter Valid Character Name")
    time.sleep(2)
    os.execv(__file__, sys.argv)
         
   

#############################################################################
################################## LOCKDOWN I ###############################
#############################################################################



#LOCKDOWN I String
time.sleep(1)



##########################
### FIRST ITEM CHOICE ####
##########################

# Items List
Item_List = [Sword, Helmet]

# Item_A imported and picked at random.
Item_A = Item_List[random.randrange(0,2)]

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
Item_B = Item_List[random.randrange(0,2)]

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
Item_C = Item_List[random.randrange(0,2)]

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


Select_First_Path = input("You Stumble Upon Two Forking Paths A And B You Take? ")
time.sleep(1)

if Select_First_Path == "A":
    Enemy_List = [TestA, TestB, TestC] 
    Enemy = Enemy_List[random.randrange(0,3)]
    Enemy.Health += 25
    print(f"You Slowly Creep down An Dark Alleyway And Suddely {Enemy.Name} Jumps out And Attacks You.")
    time.sleep(1)

    while Enemy.Health >= 0:
    
        # Enemy Attacking Character 
        Enemy_Attack = Enemy.Attack - Character.Defence
        print(f"{Enemy.Name} Has Attacked You For {Enemy_Attack} Damage")
        time.sleep(1)
        Character.Health -= Enemy_Attack
        print(f"You Have {Character.Health} Health Remaining")
        time.sleep(1)

        # Character Attacking Enemy
        Character_Attack = Character.Attack - Enemy.Defence
        print(f"You Attacked {Enemy.Name} For {Character_Attack} Damage")
        time.sleep(1)
        Enemy.Health -= Character_Attack
        print(f"{Enemy.Name} Has {Enemy.Health} Health Remaining")
        time.sleep(1)


        # Character Defeated
        if Character.Health <= 0:
            print(f"You Were Defeated By {Enemy.Name} Game Over")
            time.sleep(1)
            exit()


        # Character Defeating Enemy
        elif Enemy.Health <= 0:
            print(f"You have Defeated {Enemy.Name}")
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
    Enemy_List = [TestA, TestB, TestC] 
    Enemy = Enemy_List[random.randrange(0,3)] 
    Enemy.Health += 30

    print(f"You Take A Right Down Market Street And You're Confronted By {Enemy.Name}")
    time.sleep(1)

    while Enemy.Health >= 0:
    
        # Enemy Attacking Character 
        Enemy_Attack = Enemy.Attack - Character.Defence
        print(f"{Enemy.Name} Has Attacked You For {Enemy_Attack} Damage")
        time.sleep(1)
        Character.Health -= Enemy_Attack
        print(f"You Have {Character.Health} Health Remaining")
        time.sleep(1)

        # Character Attacking Enemy
        Character_Attack = Character.Attack - Enemy.Defence
        print(f"You Attacked {Enemy.Name} For {Character_Attack} Damage")
        time.sleep(1)
        Enemy.Health -= Character_Attack
        print(f"{Enemy.Name} Has {Enemy.Health} Health Remaining")
        time.sleep(1)

        # Character Defeated
        if Character.Health <= 0:
            print(f"You Were Defeated By {Enemy.Name} Game Over")
            time.sleep(1)
            exit()

        # Character Defeating Enemy
        elif Enemy.Health <= 0:
            print(f"You have Defeated {Enemy.Name}")
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

    Enemy_List = [TestA, TestB, TestC] 
    Enemy = Enemy_List[random.randrange(0,3)]  
    Enemy.Health += 35

    print(f"You Thought It Was All Over When {Enemy.Name} Pounces On You")
    
    while Enemy.Health >= 0:
    
        # Enemy Attacking Character 
        Enemy_Attack = Enemy.Attack - Character.Defence
        print(f"{Enemy.Name} Has Attacked You For {Enemy_Attack} Damage")
        time.sleep(1)
        Character.Health -= Enemy_Attack
        print(f"You Have {Character.Health} Health Remaining")
        time.sleep(1)

        # Character Attacking Enemy
        Character_Attack = Character.Attack - Enemy.Defence
        print(f"You Attacked {Enemy.Name} For {Character_Attack} Damage")
        time.sleep(1)
        Enemy.Health -= Character_Attack
        print(f"{Enemy.Name} Has {Enemy.Health} Remaining")
        time.sleep(1)

        # Character Defeated
        if Character.Health <= 0:
            print(f"You Were Defeated By {Enemy.Name} Game Over")
            time.sleep(1)
            exit()

        # Character Defeating Enemy
        elif Enemy.Health <= 0:
            print(f"You have Defeated {Enemy.Name}")
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
Item_List = [Sword, Helmet]

# Item_A imported and picked at random.
Item_A = Item_List[random.randrange(0,2)]

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
Item_B = Item_List[random.randrange(0,2)]

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
Item_C = Item_List[random.randrange(0,2)]

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



Boss = Boss1
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



# LOCKDOWN II String
time.sleep(1)



##########################
### THIRD ITEM CHOICE ####
##########################

# Items List
Item_List = [Sword, Helmet]

# Item_A imported and picked at random.
Item_A = Item_List[random.randrange(0,2)]

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
Item_B = Item_List[random.randrange(0,2)]

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
Item_C = Item_List[random.randrange(0,2)]

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


Select_First_Path = input("You Stumble Upon Two Forking Paths A And B You Take? ")
time.sleep(1)

if Select_First_Path == "A":
    Enemy_List = [TestA, TestB, TestC] 
    Enemy = Enemy_List[random.randrange(0,3)]
    Enemy.Health += 40
    
    print(f"You Slowly Creep down An Dark Alleyway And Suddely {Enemy.Name} Jumps out And Attacks You.")
    time.sleep(1)

    while Enemy.Health >= 0:
    
        # Enemy Attacking Character 
        Enemy_Attack = Enemy.Attack - Character.Defence
        print(f"{Enemy.Name} Has Attacked You For {Enemy_Attack} Damage")
        time.sleep(1)
        Character.Health -= Enemy_Attack
        print(f"You Have {Character.Health} Health Remaining")
        time.sleep(1)

        # Character Attacking Enemy
        Character_Attack = Character.Attack - Enemy.Defence
        print(f"You Attacked {Enemy.Name} For {Character_Attack} Damage")
        time.sleep(1)
        Enemy.Health -= Character_Attack
        print(f"{Enemy.Name} Has {Enemy.Health} Remaining")
        time.sleep(1)

        # Character Defeated
        if Character.Health <= 0:
            print(f"You Were Defeated By {Enemy.Name} Game Over")
            time.sleep(1)
            exit()

        # Character Defeating Enemy
        elif Enemy.Health <= 0:
            print(f"You have Defeated {Enemy.Name}")
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
    Enemy_List = [TestA, TestB, TestC] 
    Enemy = Enemy_List[random.randrange(0,3)] 
    Enemy.Health += 45

    print(f"You Take A Right Down Market Street And You're Confronted By {Enemy.Name}")
    time.sleep(1)

    while Enemy.Health >= 0:
    
        # Enemy Attacking Character 
        Enemy_Attack = Enemy.Attack - Character.Defence
        print(f"{Enemy.Name} Has Attacked You For {Enemy_Attack} Damage")
        time.sleep(1)
        Character.Health -= Enemy_Attack
        print(f"You Have {Character.Health} Health Remaining")
        time.sleep(1)

        # Character Attacking Enemy
        Character_Attack = Character.Attack - Enemy.Defence
        print(f"You Attacked {Enemy.Name} For {Character_Attack} Damage")
        time.sleep(1)
        Enemy.Health -= Character_Attack
        print(f"{Enemy.Name} Has {Enemy.Health} Remaining")
        time.sleep(1)

        # Character Defeated
        if Character.Health <= 0:
            print(f"You Were Defeated By {Enemy.Name} Game Over")
            time.sleep(1)
            exit()

        # Character Defeating Enemy
        elif Enemy.Health <= 0:
            print(f"You have Defeated {Enemy.Name}")
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

    Enemy_List = [TestA, TestB, TestC] 
    Enemy = Enemy_List[random.randrange(0,3)]  
    Enemy.Health += 50
    print(f"You Thought It Was All Over When {Enemy.Name} Pounces On You")
    
    while Enemy.Health >= 0:
    
        # Enemy Attacking Character 
        Enemy_Attack = Enemy.Attack - Character.Defence
        print(f"{Enemy.Name} Has Attacked You For {Enemy_Attack} Damage")
        time.sleep(1)
        Character.Health -= Enemy_Attack
        print(f"You Have {Character.Health} Health Remaining")
        time.sleep(1)

        # Character Attacking Enemy
        Character_Attack = Character.Attack - Enemy.Defence
        print(f"You Attacked {Enemy.Name} For {Character_Attack} Damage")
        time.sleep(1)
        Enemy.Health -= Character_Attack
        print(f"{Enemy.Name} Has {Enemy.Health} Remaining")
        time.sleep(1)

        # Character Defeated
        if Character.Health <= 0:
            print(f"You Were Defeated By {Enemy.Name} Game Over")
            time.sleep(1)
            exit()

        # Character Defeating Enemy
        elif Enemy.Health <= 0:
            print(f"You have Defeated {Enemy.Name}")
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
Item_List = [Sword, Helmet]

# Item_A imported and picked at random.
Item_A = Item_List[random.randrange(0,2)]

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
Item_B = Item_List[random.randrange(0,2)]

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
Item_C = Item_List[random.randrange(0,2)]

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



Boss = Boss2
print(f"You Are Nearing The End Of The Second Lockdown But {Boss.Name} Stands In Your Way Prepare For Battle!")
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



# LOCKDOWN III String
time.sleep(1)



##########################
### FIFTH ITEM CHOICE ####
##########################



# Items List
Item_List = [Sword, Helmet]

# Item_A imported and picked at random.
Item_A = Item_List[random.randrange(0,2)]

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
Item_B = Item_List[random.randrange(0,2)]

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
Item_C = Item_List[random.randrange(0,2)]

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


Select_First_Path = input("You Stumble Upon Two Forking Paths A And B You Take? ")
time.sleep(1)

if Select_First_Path == "A":
    Enemy_List = [TestA, TestB, TestC] 
    Enemy = Enemy_List[random.randrange(0,3)]
    Enemy.Health += 55

    print(f"You Slowly Creep down An Dark Alleyway And Suddely {Enemy.Name} Jumps out And Attacks You.")
    time.sleep(1)

    while Enemy.Health >= 0:
    
        # Enemy Attacking Character 
        Enemy_Attack = Enemy.Attack - Character.Defence
        print(f"{Enemy.Name} Has Attacked You For {Enemy_Attack} Damage")
        time.sleep(1)
        Character.Health -= Enemy_Attack
        print(f"You Have {Character.Health} Health Remaining")
        time.sleep(1)

        # Character Attacking Enemy
        Character_Attack = Character.Attack - Enemy.Defence
        print(f"You Attacked {Enemy.Name} For {Character_Attack} Damage")
        time.sleep(1)
        Enemy.Health -= Character_Attack
        print(f"{Enemy.Name} Has {Enemy.Health} Remaining")
        time.sleep(1)

        # Character Defeated
        if Character.Health <= 0:
            print(f"You Were Defeated By {Enemy.Name} Game Over")
            time.sleep(1)
            exit()

        # Character Defeating Enemy
        elif Enemy.Health <= 0:
            print(f"You have Defeated {Enemy.Name}")
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
    Enemy_List = [TestA, TestB, TestC] 
    Enemy = Enemy_List[random.randrange(0,3)] 
    Enemy.Health += 60

    print(f"You Take A Right Down Market Street And You're Confronted By {Enemy.Name}")
    time.sleep(1)

    while Enemy.Health >= 0:
    
        # Enemy Attacking Character 
        Enemy_Attack = Enemy.Attack - Character.Defence
        print(f"{Enemy.Name} Has Attacked You For {Enemy_Attack} Damage")
        time.sleep(1)
        Character.Health -= Enemy_Attack
        print(f"You Have {Character.Health} Health Remaining")
        time.sleep(1)

        # Character Attacking Enemy
        Character_Attack = Character.Attack - Enemy.Defence
        print(f"You Attacked {Enemy.Name} For {Character_Attack} Damage")
        time.sleep(1)
        Enemy.Health -= Character_Attack
        print(f"{Enemy.Name} Has {Enemy.Health} Remaining")
        time.sleep(1)

        # Character Defeated
        if Character.Health <= 0:
            print(f"You Were Defeated By {Enemy.Name} Game Over")
            time.sleep(1)
            exit()

        # Character Defeating Enemy
        elif Enemy.Health <= 0:
            print(f"You have Defeated {Enemy.Name}")
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

    Enemy_List = [TestA, TestB, TestC] 
    Enemy = Enemy_List[random.randrange(0,3)]  
    Enemy.Health += 60

    print(f"You Thought It Was All Over When {Enemy.Name} Pounces On You")
    
    while Enemy.Health >= 0:
    
        # Enemy Attacking Character 
        Enemy_Attack = Enemy.Attack - Character.Defence
        print(f"{Enemy.Name} Has Attacked You For {Enemy_Attack} Damage")
        time.sleep(1)
        Character.Health -= Enemy_Attack
        print(f"You Have {Character.Health} Health Remaining")
        time.sleep(1)

        # Character Attacking Enemy
        Character_Attack = Character.Attack - Enemy.Defence
        print(f"You Attacked {Enemy.Name} For {Character_Attack} Damage")
        time.sleep(1)
        Enemy.Health -= Character_Attack
        print(f"{Enemy.Name} Has {Enemy.Health} Remaining")
        time.sleep(1)

        # Character Defeated
        if Character.Health <= 0:
            print(f"You Were Defeated By {Enemy.Name} Game Over")
            time.sleep(1)
            exit()

        # Character Defeating Enemy
        elif Enemy.Health <= 0:
            print(f"You have Defeated {Enemy.Name}")
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
Item_List = [Sword, Helmet]

# Item_A imported and picked at random.
Item_A = Item_List[random.randrange(0,2)]

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
Item_B = Item_List[random.randrange(0,2)]

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
Item_C = Item_List[random.randrange(0,2)]

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



Boss = Boss3
print(f"You Are Nearing The End Of The Third And Last Lockdown But {Boss.Name} Stands In Your Way Prepare For Battle!")
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
            
            print(f"Congratulations You have Defeated {Boss.Name} And Escaped Lockdown!!!")