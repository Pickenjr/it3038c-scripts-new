import csv
import sys
import os.path


def main():                                                                                                         # Creating the main function
    with open ("UserInput.txt","r+") as file:                                                                       # Setting the main function to open UserInput.txt as a variable file using read permissions.
        file_reader = csv.reader(file)                                                                              # Creating a variable named file_reader to read the UserInput.txt file with a csv (Comma separated value) reader
        user_find(file_reader)                                                                                      # Running the user_find function to call the main function and read through the text file for the specified user
        file.close()

def check():                                                                                                        # Creating function called check that will check if the necessary file has been created or not, and if it hasn't it will create it.
    if os.path.exists("UserInput.txt"):                                                                             # Checking if the specified file exists.
        print("The file was already created.")                                                                      # Letting the user know the file was already created
    else:                                                                                                           # Creating an else loop if the file wasn't already created
        with open("UserInput.txt", "w+") as file:                                                                   # Creating the file if it wasn't already created
            print("The file 'UserInput.txt' has been created in the present directory")                             # Letting the user know a file named 'UserInput.txt' was created in the current directory
check()                                                                                                             # Calling (running) the check function

def accountCheck():
    print("Do you have an account? Y/N")                                                                            # Asking the user if they have an account already or not
    account = input()                                                                                               # Creating a variable named account and setting it equal to the user's input
    if account == "n" or account == "N" or account == "no" or account == "No" or account == "NO":                   # Creating an if statement, if the account variable is equal to n, N, no, No, or NO, the program will then ask if they want to create an account.       
        print("Would you like to create an account? Y/N")                                                           # Asking the user if they would like to create an account
        Register = input()                                                                                          # Creating a variable named Register and setting it equal to the user's input.
        if Register == "y" or Register == "Y" or Register == "Yes" or Register == "yes" or Register == "YES":       # Creating an if statement, if the Register variable is equal to y, Y, Yes, yes, or YES; the program will then prompt them for a username and password    
            print("What would you like your Username to be?")                                                       # Asking the user what they want their username to be
            username = input()                                                                                      # Asking for the user's input and creating a variable named username from it
            print("What would you like your password to be?")                                                       # Asking the user what they want their password to be
            password = input()                                                                                      # Asking for the user's input and creating a variable named password from it
            with open ("UserInput.txt", "a") as file:                                                               # Opens the file UserInput.txt with writing capabilities
                file.write("%s,%s\n" %(username, password))                                                           # Writes the entered inputs for username and password into the UserInput.txt file
                file.close()                                                                                        # Closes the UserInput.txt file
                print("You have successfully registered.")                                                                                        
        else:
            accountCheck()                                                                                          # This ends the program if the user said they do not have an account and do not wish to create one
        
accountCheck()

def user_find(file):                                                                                                # Creating a function name user_find(file) where we are reading the contents from the file UserInput.txt
        print("Please enter your Username:")                                                                        # Asking the user to input their username.
        user = input()                                                                                              # Setting a variable named user equal to the user's input
        with open("UserInput.txt", "r") as file:                                                                    # Opening the UserInput.txt file
            file_reader = csv.reader(file)                                                                          # Using as csv reader to read the comma separated values in the UserInput.txt file
            for row in file_reader:                                                                                 # Looking at each row in UserInput.txt file
                if row[0] == user:                                                                                  # Comparing if the first value in any of the rows in UserInput.txt file is equal to the variable user, it will then prompt for a password
                    print("Username found. Please enter your password:")                                            # Prompting the user to enter their password if they entered a correct username
                    password = input()                                                                              # Creating a variable named password equal to the user's input.
                    user_found = [row[0],row[1]]                                                                    # Creating a variable named user_found after the user enters a correct username
                    if user_found[1] == password:                                                                   # Comparing if the second value of the variable user_found is equal to the input for the user's password
                        print("Username and password are correct. You are now logged in!")                          # If it matches it lets you know you successfully logged in.
                        sys.exit                                                                                    # Exits the program
                        break                                                                                       # Breaks the loop once the condition has been satisfied.
                    else:                                                                                           # Creating an else statement if the password doesn't match a value in the UserInput.txt file
                        print("Incorrect password. Please try again.")                                              # Telling the user they entered the wrong password and to try again
            else:                                                                                                   # Creating and else statement if the username doesn't match the value in the UserInput.txt file
                print("Username is incorrect please try again.")                                                    # Telling the username they entered a wrong username and to try again
                accountCheck()                                                                                      # Re-runs the accountCheck and the user_find(file) functions.
                user_find(file)                                                                                     # Re-runs the accountCheck and the user_find(file) functions.
main()                                                                                                              # Ends main function
                                                                                                                    # I know this is some spaghetti code but I threw this together in two days.

