#
# Programming Assignment 4
# Michael Winder
# SEC 290 Summer B2
# July 31, 2020
#

gradesList = [85.2, 85.3, 21.99]

#Need to convert the list to a float list, only method I can think of
listOfGrades = []
for i in gradesList:
    listOfGrades.append(float(i))
    
#Let's define some functions to complete the work
#remember, need to use listOfGrades list for everything from here on out
def displayScoresHightoLow():
    listOfGrades.sort()
    return listOfGrades

def addToList():
    try:
        number = float(input("What is the number you would like to add: "))
    except ValueError:
        print("That is not a valid entry, please enter a proper Number!")
    else:
        if number < float(0.0):
            print("That number is to low, please enter number between 0.0 and 100.0")
        elif number > float(100.0):
            print("That number is to High, please enter a number between 0.0 and 100.0")
        else:
            listOfGrades.append(number)
            print(listOfGrades)
            return

def displayHighAndLow():
    listOfGrades.sort()
    lowest = listOfGrades[0]
    highest = listOfGrades[len(listOfGrades) - 1]
    print(" Highest value is {:.2f} and Lowest value is {:.2f}" .format(highest, lowest))
    return

# Start of our while loop for menu
exit = True
while exit:
    choice = input("""
1. Choose to exit 
2. Choose to display the scores from highest to lowest values.
3. Choose to add a score to the list. Note that scores must be floating point numbers.
4. Choose to display the highest and lowest scores.
Please Make a Choice (1-4): """)
    if choice == "1":
        print("GoodBye")
        exit = False
    elif choice =="2":
        displayScoresHightoLow()
        print(listOfGrades)
    elif choice == "3":
        addToList()
    elif choice == "4":
        displayHighAndLow()
    else:
        print("Not a valid choice, Please enter a number 1-4.")
    
#Menu functionality below here
