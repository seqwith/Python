#
# Michael Winder
# SEC 290 Summer B2
# Programming Assignment 7
# Grade Book App
# August 22, 2020
#

# Define a class, and include methods to figure out grades, and grade averages for different assignments and quizzes, including final exam

# Define our class here
class GradeBook:
    #Need some lists to hold the grades and set final exam to default 0
    quizzes = []
    assignments = []
    final_exam = 0

    #Define the functions that will append to the lists
    def quizScore(self, score):
        self.quizzes.append(score)

    def assignmentScore(self, score):
        self.assignments.append(score)

    # Define method to edit final exam score
    def finalExamScore(self, score):
        GradeBook.final_exam = score

    # Here is where we will figure out the current Average of grades
    def currentAverage(self):
        if len(GradeBook.assignments) > 0:
            assignments_average = sum(GradeBook.assignments) // len(GradeBook.assignments)
        else:
            assignments_average = 0

        if len(GradeBook.quizzes) > 0:
            quiz_average = sum(GradeBook.quizzes) // len(GradeBook.quizzes)
        else:
            quiz_average = 0

        currentGrade = (0.4 * GradeBook.final_exam) + (0.3 * quiz_average) + (0.3 * assignments_average)
        
        return currentGrade


#User Menu
menu = ('''
Grade Book

0: Exit
1: Enter assignment grade
2: Enter quiz grade
3: Enter fianl exam grade
4: Display current grade
''')
#print(menu) was orignially here, but I didn't like how it would not print out after entering a grade, so moved it inside while loop at top.


#Main part of program goes here
while True:
    # Moved print(menu) to here to see menu each time after grade is entered.
    print(menu)
    #Create instance of class
    my_grades = GradeBook()
    #Lets make sure we are getting proper input if not catch exceptions
    try: 
        choice = int(input('\nPlease enter a choice: '))

        # Option 0
        if choice == 0:
            break
        # Option 1
        elif choice == 1:
            while True:
                try:
                    assignment_grade = float(input('\nPlease enter a grade for the assignment: '))
                    my_grades.assignmentScore(assignment_grade)
                    break
                except:
                    print('\nPlease check you input and try again.')
                    continue
        #Option 2
        elif choice == 2:
            while True:
                try:
                    quiz_grade = float(input('\nPlease enter a grade for the quiz: '))
                    my_grades.quizScore(quiz_grade)
                    break
                except:
                    print('\nPlease check your input and try again.')
                    continue
        #Option 3
        elif choice == 3:
            while True:
                try:
                    final_grade = float(input('\nPlease enter a grade for the final exam: '))
                    my_grades.finalExamScore(final_grade)
                    break
                except:
                    print('\nPlease check your input and try again.')
                    continue
        #Option 4
        elif choice == 4:
            average = my_grades.currentAverage()
            print('\nYour current grade Average is: {}' .format(average))
        else:
            print('\nPlease check your input and try again.')
            continue

    except:
        print('\nPlease check your input and try again.')
        print(menu)
        continue
