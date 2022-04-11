# importing the required libraries

# Contants
"""
This is a welcome message
"""
WELCOME_MESSAGE = "\nWelcome to the Covid-19 Vaccination Survey Data Analyser Command Line Interface! \n"
TIP1 = "Press 0 if no, 1 if yes and 2 to quit !\n"
TIP2 = "\nYour name has to be filled in, for you to continue"


def say(word):
    """
    This function is for greeting the user
    """
    if word == "Hi" :
        print("\nHii User \n")
    else:
        print("\nGood Bye my friend!\n")


def display(message):
    """
    This function displays an input string
    """
    print(message)


def get_name():
    """
    This function captures the user's initial inputs
    validates the intial input
    Captures the users name
    Captures criteria for analysis
    validates the criteria for analysis
    """
    display("May I know your name?\n")
    ask = input(TIP1)  # This captures the initial input of the user

    if ask != "":  # checks if the user input is not empty
        if  ask == "0":  # is user refuses to provide name
            print(TIP2)  
            ask = input(TIP1)
        elif ask == "1":  # if answer is yes/ user accepts to provide name
            name = input("\nEnter Your name please!\n")
            print("\nHii "+name+"\n")
            display(WELCOME_MESSAGE)