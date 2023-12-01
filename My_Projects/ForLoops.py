#for this exercise i was practicing for loops
#the questions are provided from https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

#Through the FizzBuzz exercise, I learned to apply conditional statements in Python to address specific criteria for printing messages. This exercise enhanced my understanding of modulus operations to identify multiples of numbers. It demonstrated the importance of logical conditions in programming to create dynamic and rule-based output. Overall, FizzBuzz provided a practical application of control flow in Python, contributing to my problem-solving skills.


import random
#1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

# Find numbers divisible by 7 and multiples of 5 between 1500 and 2700
result_numbers = [num for num in range(1500, 2701) if num % 7 == 0 and num % 5 == 0]

# Display the result
print("Numbers divisible by 7 and multiples of 5 between 1500 and 2700:")
print(result_numbers)


#3. Write a Python program to guess a number between 1 and 9. Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.



# Generate a random number between 1 and 9
secret_number = random.randint(1, 9)

while True:
    # Prompt the user to enter a guess
    user_guess = int(input("Guess a number between 1 and 9: "))

    # Check if the guess is correct
    if user_guess == secret_number:
        print("Well guessed!")
        break
    else:
        print("Try again. Incorrect guess.")


#8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.Note : Use 'continue' statement. Expected Output : 0 1 2 4 5

# Print numbers from 0 to 6 except 3 and 6
for num in range(7):
    if num == 3 or num == 6:
        continue  # Skip printing 3 and 6
    print(num, end=' ')

# FizzBuzz program
for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
