
# Create a function that randomly generates and returns a tuple of two positive one-digit integers.
import random

def question():
   #get two numbers
    num1 = random.randrange(10)
    num2 = random.randrange(10)

    return(f'How much is {num1} * {num2} ?', num1 * num2, num1, num2)

question, answer, num1, num2 = question() 
print(question)

guess = int(input('Enter your guess: '))

while guess != answer:
    guess = int(input(f"{num1} times {num2} is not {guess},please try again: " ))
   
if guess == answer:
    print("done")
    