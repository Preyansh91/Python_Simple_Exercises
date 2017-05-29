#!/usr/bin/python
import sys


def split_words_and_reverse(arg):
    words_split = []
    words_split = arg.split()
    reversed_list = reverse_list(*words_split)
    return (' ').join(reversed_list)

def reverse_list(*args):
    reversed_list = []
    [reversed_list.insert(0,i) for i in args]
    return reversed_list    

def main():
    user_input = str(raw_input("Enter a string to reverse: \n"))
    if (len(user_input) < 1 or user_input == None):
        print "Enter a proper string\n"
        sys.exit(0)
    else:
        try:
            output = split_words_and_reverse(user_input)
            print output 
        except Exception as e:
            print e        


main()
