import time

start_time = time.time()
print('What is your name?')
myname= input()

while myname != 'Jake':
    if myname == 'your name':
        print("Bad joke. What's your real name?")
        myname = input()
    else:
        print("That's not your name, please tell me your real name.")
        myname = input()

print('Hello, ' +myname + '. That is a good name. How old are you?')
myage = int(input())

if myage < 13:
    print("You're just a kid.")
elif myage == 13:
    print("You're a teenage now. that's neat I guess.")
elif myage >13 and myage < 30:
    print("You're young and dumb.")
elif myage >= 30 and myage < 65:
    print("You're adulting.")
else:
    print("You're old.")
programage = int(time.time() - start_time)

print("%s? That's funny, I'm only %s seconds old." % (myage, programage))
#print("I wish I was " + str(int(myage) * 2) + " years old")
print("I wish I was %s years old" % (myage * 2))

time.sleep(3)
print("I'm tired, bye.")