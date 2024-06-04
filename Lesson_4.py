# 1. The Range Riddle


# Task 1: Every Other Day Write a program that prints each day of the week, but only if that day is on an even index.

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


for day in range(len(days_of_week)):
    if day % 2 == 0:
        print(days_of_week[day])



# 2. Loop Condition Logic
# Objective: The aim of this assignment is to explore the importance of the loop condition in while loops. You will create loops with different conditions to see how they influence the behavior of the loop.

# Task 1: Loop Condition Exploration Write a while loop with a condition that will never be true (an infinite loop). Ask the user a question until their answer triggers a break statement (hint: use an if statement to evaluate their answer).


while True:
    question = input("Do you want to end this infinite loop?")
    if question == 'yes':
        print("Stopping the infinite loop")
        break
    else:
        print('the infinite loop continues')



# Task 2: Conditional Exit Create a while loop that will terminate after 5 iterations, and each iteration you print which iteration it is on. (use a control variable)

count = 1

while count <= 5:
    print('Running my while loop. This is iteration:', count)
    count += 1




# 4. Python's Random Game Night (EXTRA CREDIT)
# Objective: The aim of this assignment is to explore the random package in Python and understand how it can be used with loops to introduce randomness into your programs.

# Task 1: Random Choice Game Create a game where a player has a list of items. They have to guess which item in the list was selected. Use random.choice() to select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not keep them playing until they guess correctly.

import random

items = ['car', 'train', 'boat', 'plane', 'spaceship']

random_item = random.choice (items)

print("This is a Random Choice Game!")
print("We have selected an item from the following list:")
print(items)
print("Can you guess which item we have selected?")

while True:
    guess = input ("Enter your guess from the list of items:")
    if guess == random_item:
        print ("Congratulations you guessed the correct item!")
        break
    else:
        print("Nope that's wrong. Guess again.")