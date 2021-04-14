def level_one():
    print("These are volatile times...")
    time.sleep()
    print("Large segments of the country are placed under lockdown")
    time.sleep()
    print("Welcome to lockdown 1")
    time.sleep()
    print("Due to new restrictions, members of the public have been urged to only leave their homes for essential items")
    time.sleep()
    print("{} decides to have a walk to the local shop".format(name))
    time.sleep()
    print("There are two seperate routes {} can choose from to get to the shop".format(name))
    time.sleep()
    left_or_right = input("Which should {} choose? [L/R] ".format(name))
    if left_or_right.upper() == "L" or left_or_right.upper() == "LEFT":
        left_path()
    elif left_or_right.upper() == "R" or left_or_right.upper() == "RIGHT":
        right_path()
    else:
        print("Invalid input, try again.")
        level_one()
        #Ask again if not a valid response