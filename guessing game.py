import random
print "lets play the guessing game"
y = int(input("guess a number between 1 and 10: "))
x = random.randint(1,10)
if x == y:
    print "you win!"
else:
    print("you lose! the correct number was: " + str(x))
