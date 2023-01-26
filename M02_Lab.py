#Jimmy Correa
#M02 Lab
#This application takes a users name and GPA and then tests
#to see if they have made either the Dean's list or the honor roll.

#while statement to restart the program
while True:
    
    #Getting requested last name
    lastName = input("What is your last name?\n")

    #Testing for null last name "ZZZ"
    #If entered, program terminates
    if lastName == "ZZZ":
        print("Program Terminated")
        exit()
    
    #Getting requested first name    
    firstName = input("What is your first name?\n")

    #Getting float and then halting at 2 decimal points for GPA
    gPA = float(input("What's your GPA?\n"))
    newGPA = float("{0:.2f}".format(gPA))

    #Series of if else statements that determines student placing
    if newGPA >= 3.5:
        print("This student has made the Dean's list")

    elif newGPA >= 3.25:
        print("This student has made the honor roll")
        
    else:
        print("You are still awesome in my eyes")
    
    restart = input("Would you like to see another student? Y or N.\n")
    
    #If user wishes to continue, we continue
    if restart == "Y" or "y":
        continue
    
    #Program terminated if response is no
    elif restart == "N" or "n":
        break 
    
