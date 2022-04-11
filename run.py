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
