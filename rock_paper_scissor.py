#!/usr/bin/python
import random
import sys

def user_val(user_input):
    options = {"1": "rock", "2": "paper", "3": "scissor"}
    try:
        if (len(user_input) < 1):
            return 0
        user_input_val = user_input.lower()
        for key,value in options.items():
            if value == user_input_val:
                print key
                return key
    except Exception as e:
        return 0


def comp_val():
    options = { 1: "rock", 2: "paper", 3: "scissor"}
    comp_input = random.randint(1,3)
    try:
        for key,value in options.items():
            if key == comp_input:
                print ("computer entered: " + str(value) + "\n")
                print key
                return int(key) 
    except Exception as e:        
        return 0 

def play_the_game(user_input_val,comp_input_val):
    user_input = int(user_input_val)
    comp_input = int(comp_input_val)
    try:
        if (user_input == comp_input):
            print "No one won\n"
        elif user_input == 1 and comp_input == 2:
            print "comp won\n"
        elif user_input == 2 and comp_input == 3:
            print "comp won\n"
        elif user_input == 3 and comp_input == 1:
            print "comp won\n"
        else:               
            print "user won\n" 
        return True
    except Exception as e:
        print e
        return False 

def main():
   # user_input = raw_input("Enter you value. Choose any one of Rock, Paper or Scissors\n")
    play_flag = 1

    while (play_flag == 1):
        user_input = str(raw_input("Enter you value. Choose any one of Rock, Paper or Scissors\n"))
        user_input_key = user_val(user_input) 
        if (user_input_key > 0):
            print "Your value is entered, lets check for computer's value \n" 
        else:
            print "you have entered a wrong value, please enter a value again. \n"
            continue
        try:
            comp_input_key = comp_val()    
            if comp_input_key == 0:
                "There is some error, please play again.\n"
                sys.exit(0)
            else:
                print "Lets see who won....\n"
        except Exception as e:
            print e
        if (play_the_game(user_input_key,comp_input_key) == True):
            play_flag = 0
            print "Thanku for playing \n"
        else:
            print "Something went wrong, lets play again\n"
                
main()
