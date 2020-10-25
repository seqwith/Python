#
# Michael Winder
# SEC 290 Summer B2
# August 8, 2020
# hmwk5.py
#

# FAQ Dictionary
# this is to create a starting dictionary
# could also use faqs = {} to create an empty dictionary

faqs = {'Question 1': 'Answer: 1', 'Question 2': 'Answer 2',
        'Question 3': 'Answer 3', 'Question 4': 'Answer: 4'
        }

#Global title, so we can use multiple times
title = "Frequently Asked Questions"

#Main Menu

def MainMenu():
    print("{}" .format('=' * len(title)))
    print("{}" .format(title))
    print("{}" .format('=' * len(title)))
    print("\n")
    print("0: Exit")
    print("1: List FAQ's")
    print("2: Add FAQ's")
    print("3: Delete FAQ's")
    print("\n")
    selection = int(input("Please enter a choice: "))
    if selection == 0:
        print("Goodbye")
        exit
    elif selection == 1:
        ListFaq()
    elif selection == 2:
        AddFaq()
    elif selection == 3:
        DeleteFaq()
    else:
        print("That is an invalid choice. Enter 0-3\n")
        MainMenu()
# Function to List the FAQ's nice and neat
def ListFaq():
    print("\n")
    print(title)
    print("{}\n" .format('=' * len(title)))
    print("\n".join("Question: {}\nAnswer: {}\n" .format(k,v) for k,v in faqs.items()))
    anykey = input("Hit any key to return to the main menu")
    MainMenu()

#This function will Add to the FAQ dictionary
def AddFaq():
    print("What question would you like to add")
    question = input("Question: ")
    
    #Check to see if the question already exists, if it doesn't add it
    if question not in faqs.keys():
        answer = input("Question not found, what is the answer to {}: " .format(question))
        faqs.update({question : answer})
        print("Question Added")
    #Question is already in the FAQ, do nothing
    elif question in faqs.keys():
        print("That questions is already in the FAQ")
        
    anykey = input("Hit any key to return to the main menu")
    MainMenu()

#This function should delete a listing from the FAQ
def DeleteFaq():
    print("What question would you like to delete")
    question = input("Question: ")

    #Check to see if the key exists and delete it
    if question in faqs.keys():
        answer = input("Are you sure you want to delete (Y or N): ")
        if answer.lower() == 'y':
            del faqs[question]
            print("Question deleted")
        #They decided no to delete
        elif answer.lower() == 'n':
            print("Did not delete")
    #Question does not exist
    elif question not in faqs.keys():
        print("Questions is not in FAQ's, no Changes made")
        
    anykey = input("\nHit any key to return to the main menu")
    MainMenu()
    

#main routine
MainMenu()
