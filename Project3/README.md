# Rudimentary Username and Password checker using Python.

## Prerequisites
Please run this script on Windows. 
To successfully run this script you must have Python.
Check if you have installed Python by opening Powershell (not ISE) or Command Prompt and running the command Python --version.
If it is installed you will have an output similar to 

```
PS C:\it3038c-scripts> python --version
Python 3.8.1
```

### Installing
If you don't have python installed navigate to https://www.python.org/downloads/windows/ and download the latest version of Python.

## Running the script. 
Once Python is installed and running and you have downloaded Project3.py (NO OTHER FILE IS NECESSARY TO RUN THIS), navigate to the directory the script is stored in, using Powershell (not ISE) or command prompt.
Once in the correct directory, run the script by running the following command: python Projec3.py

### Outputs
Once you have started the script you will be taken through a series of prompts to check if you have an account already stored in the UserInput.txt file.
The start of the script looks like so

```
C:\it3038c-scripts\Project3>python Project3.py
The file was already created.
Do you have an account? Y/N
```

OR 

```
C:\it3038c-scripts\Project3>python Project3.py
The file 'UserInput.txt' has been created in the present directory.
Do you have an account? Y/N
```

From here you can either enter "n", "N, "no", "No", or "NO" to proceed to creating an account.

```
Do you have an account? Y/N
n
Would you like to create an account? Y/N
```

If you enter "y", "Y", "yes", "Yes", or "YES" you will be prompted to enter a username and password that will then be save to the UserInput.txt file in a new line.
Any other input will take you back to asking if you have an account.

```
Do you have an account? Y/N
n
Would you like to create an account? Y/N
y
What would you like your Username to be?
Pickenjr
What would you like your password to be?
test
You have successfully registered.
Please enter your Username:

```


Any other input and the program will proceed to asking for a Username

```
Do you have an account? Y/N
y
Please enter your Username:
Pickenjr
```

After entering your username, it will check if the username is in the UserInput.txt file.
If it is, it will proceed to asking for your password.

```
Please enter your Username:
Pickenjr
Username found. Please enter your password:

```

If you enter the correct password you will see a result like so:

```
Please enter your username:
Pickenjr
Please enter your password:
test
Username and password are correct. You are now logged in!

C:\it3038c-scripts\Project3>
```

If you enter an incorrect password after entering a correct Username you will see:

```
Please enter your Username:
Pickenjr
Please enter your password:
haha
Incorrect password please try again.

C:\it3038c-scripts\Project3>
```

### That is my very rudimentary username and password checker.
