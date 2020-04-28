import csv
import sys
import os.path

def main():                                                                                                     # Creating the main function
    with open ("UserInput.txt","r+") as file:                                                                   # Setting the main function to open UserInput.txt as a variable file using read permissions.
        file_reader = csv.reader(file)                                                                          # 
        user_find(file_reader)

def check():                                                                                                    # Creating function called check that will check if the necessary file has been created or not, and if it hasn't it will create it.
    if os.path.exists("UserInput.txt"):                                                                         # Checking if the specified file exists.
        print("The file was already created.")                                                                  # Letting the user know the file was already created
    else:                                                                                                       # Creating an else loop if the file wasn't already created
        with open("UserInput.txt", "w+") as file:                                                               # Creating the file if it wasn't already created
            print("The file 'UserInput.txt' has been created in the present directory")                         # Letting the user know a file named 'UserInput.txt' was created in the current directory
check()                                                                                                         # Calling (running) the check function
def accountCheck():
    
    def accountCreate(account):    
        if account == "y" or account == "Y" or account == "yes" or account == "Yes" or account == "YES":
            user_find(file)
        else:    
            print("Would you like to create an account? Y/N")
            Register = input()

            def accountRegister(Register):
                print("What would you like your Username to be?")                                                       # Asking the user what they want their username to be
                username = input()                                                                                      # Asking for the user's input and creating a variable named username from it
                print("What would you like your password to be?")                                                       # Asking the user what they want their password to be
                password = input()                                                                                      # Asking for the user's input and creating a variable named password from it
                with open ("UserInput.txt", "w+") as file:                                                              # Opens the file UserInput.txt with writing capabilities
                    file.write("%s,%s" %(username, password))                                                           # Writes the entered inputs for username and password into the UserInput.txt file
                    file.close()

    def user_find(file):
        print("Please enter your Username:")
        user = input()
        if user in file:
            print("Please enter your password")
            password = input()
            if password == file[user]:
                print("You are now logged in")
            else: 
                print("Password is incorrect")
        else: 
            print("Username is incorrect. Please try again. (Enter 'Register' if you would like to create an account.")
            user = input()
print("Do you have an account? Y/N")                                                                            # Asking the user if they have an account already or not
account = input()                                                                                               # Creating a variable named account and setting it equal to the user's input 

