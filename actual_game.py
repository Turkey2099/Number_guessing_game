#the fundamentals and rule for the game
print("Number Guessing Game".center(100)) #heading
print("RULES FOR THE GAME".center(40))
print("""   1. You have to guess the secret number\n   2. The number is between 1 - 100\n   3. Your number of attempts will be decided by the level of difficulty you select\n i. Kid\n ii. Easy\n iii. Medium\n iv. Hard\n v.Extreme\n   4. Best of luck""" )
#random number and all
import random
secret_word = random.randint(0 , 100)#random number
attempts = 0 
#difficulty
print("please select difficulty")
print("select 1 for Kid difficulty(20 attempts)\nselect 2 for easy difficulty(15 attempts)\nselect 3 for medium difficulty(10 attempts)(\nselect 4 for hard difficulty(5 attempts)\nselect 5 for 'extreme' difficulty(3 attempts)")
difficulty = int(input("enter difficulty"))
if difficulty == 1:
    attempts = 20
    print("you have selected kid difficulty")
if difficulty == 2:
    attempts = 15
    print("you have selected easy difficulty")
if difficulty == 3:
    attempts = 10
    print("you have selected medium difficulty")
if difficulty == 4:
    attempts = 5
    print("you have selected hard difficulty")
if difficulty == 5:
    attempts = 3
    print("you have selected 'extreme' difficulty")
if difficulty > 5:
    print("please select valid difficulty level")
#taking guess
while attempts > 0 :
    print("attempts left:",attempts)
    guess = int(input("take a guess"))
    if int(guess) > int(secret_word):
        print("too high")
    if int(guess) < int(secret_word):
        print("too low")
#attempt minusing
    if int(guess) != int(secret_word):
        attempts -= 1
    if int(guess) == int(secret_word):
        print("congrats you have guessed the word",secret_word)
    if attempts == 0 :
        print("you are out of attempts :()")
        print("Game Over")
