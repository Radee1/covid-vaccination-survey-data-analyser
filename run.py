# importing the required libraries
import pandas as pd
import pygsheets 

# Contants
"""
This is a welcome message
"""
w1 = "\nWelcome to the Covid-19 Vaccination "
w2 = "Survey Data Analyser! \n"
WELCOME_MESSAGE = w1+w2
TIP1 = "Press 0 if no, 1 if yes and 2 to quit !\n"
TIP2 = "\nYour name has to be filled in, for you to continue\n"
TIP3 = "\nThese results have also been written into the shared google sheet\n"

# Functions


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


# Validate


def validate():
    """
    Captures user name
    Validates the user input
    compares the criteria
    loading and writing the data for analysis from the dataset
    processing and saving analyzed data
    
    """
    name = input("\nEnter Your name please!\n")

    if len(name) > 4:
        print("\nHii "+name+"\n")
        display(WELCOME_MESSAGE)

        data = pd.read_csv('data.csv')

        # Analysis criteria

        i1 = input("\nEnter target number of total vaccinations \n")
        i2 = input("\nEnter target number of persons fully vaccinations\n")
        total_vaccinations = i1
        total_full_vaccinations = i2

        if total_vaccinations != "" and total_full_vaccinations != "":
            limit1 = int(total_vaccinations)  # turn str to integer
            limit2 = int(total_full_vaccinations)
        else:
            print("\nINVALID ANSWERs\n")
            display("Do you want to continue?\n")
            ask = input(TIP1)
        
        # Filter the data accordingly.

        data = data[data['TOTAL_VACCINATIONS'] > limit1]
        data = data[data['PERSONS_FULLY_VACCINATED'] > limit2]

        data.to_csv('filtered-data.csv', index=False)  # create filtered csv
        d1 = pd.read_csv('filtered-data.csv')  # read filtered data
        filtered_data = d1
        filtered_data = filtered_data[['COUNTRY', 'TOTAL_VACCINATIONS', 'PERSONS_FULLY_VACCINATED',
        'VACCINES_USED']].sort_values(by="TOTAL_VACCINATIONS", ascending=False)
        filtered_data.to_csv('inform.csv', index=False)  # write informative csv
        data1 = pd.read_csv('inform.csv')  # read informed csv
        display("\n COUNTRIES THAT HAVE OVER " + total_vaccinations + " TOTAL_VACCINATIONS AND OVER " + total_full_vaccinations +
        " FULLY_VACCINATED PEOPLE\n")
        print(data1)

        # google authorization

        google_credentials = pygsheets.authorize(service_file='creds.json')

        # Create empty dataframe

        df = pd.DataFrame()

        # save analyzed data

        df= data1 # write informative csv

        # open the google spreadsheet (where 'Covid-data.csv' is the name of my sheet)
        sh = google_credentials.open('Covid-data.csv')

        # select the first sheet
        wks = sh[0]

        # write analyzed data to google sheet.
        wks.set_dataframe(df,(1,1))

        display(TIP3)
        print("Nice working with you "+name)  # say bye to the user
        say("Bye")

    else:
        print("\nAtleast 5 characters needed, please try again \n")
        validate()

def get_name():
    """
    This function captures the user's initial inputs
    
    """
    display("May I know your name?\n")
    ask = input(TIP1)

    if ask != "":
        if str(ask) == "0":
            print(TIP2)
            get_name()
        elif ask == "1":
            validate()
        elif ask == "2":
            say("Bye ")
        else:
            print("\nInvalid entry, please try again \n")
            get_name()
    else:
        print(TIP2)
        ask = input(TIP1)
        get_name()


say("Hi")
get_name()