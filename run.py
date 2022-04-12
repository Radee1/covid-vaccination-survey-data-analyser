# importing the required libraries
import pandas as pd
# Contants
"""
This is a welcome message
"""
WELCOME_MESSAGE = "\nWelcome to the Covid-19 Vaccination Survey Data Analyser!\n"
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
        if  ask == "0":  # if user refuses to provide name
            print(TIP2)  
            ask = input(TIP1)

        elif ask == "1":  # if answer is yes/ user accepts to provide name
            name = input("\nEnter Your name please!\n")
            print("\nHii "+name+"\n")
            display(WELCOME_MESSAGE)

            # Analysis criteria
            total_vaccinations = input("\nEnter target number of total vaccinations \n")
            total_full_vaccinations = input("\nEnter target number of persons fully vaccinated \n")

            if total_vaccinations != "" and total_full_vaccinations != "":
               limit1 = int(total_vaccinations) #turn str to
               limit2 = int(total_full_vaccinations)
            else:
               print("\nINVALID ANSWERs\n")
               display("Do you want to continue?\n")
               ask = input(TIP1)

            display("\n COUNTRIES THAT HAVE OVER "+total_vaccinations+" TOTAL_VACCINATIONS AND OVER "+total_full_vaccinations+
            " FULLY_VACCINATED PEOPLE\n")
            
            display("\nThese results have also been written into inform.csv in the root folder\n")
            print("Nice working with you "+name) #say bye to the user
            say("Bye")

        elif ask == "2":
            say("Bye")
        else:
            print("\nInvalid answer, please try again \n")
            get_name()
    else:
        print(TIP2)
        ask = input(TIP1)
        get_name()
say("Hi")
get_name()