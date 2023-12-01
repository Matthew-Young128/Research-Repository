#This project is a calculator that calulates how many hours you've spent sleeping in your life

# SleepCalculator.py

print("Welcome to the Sleep Calculator\n")

# Prompt the user to enter their year of birth
user_yob = int(input("Please enter your year of birth: "))

# Calculate the number of hours the user has slept assuming an average of 7 hours per day
hours_slept = (2023 - user_yob) * 365 * 7

# Display the result
print(f"Thank you for your input!\n")
print(f"If you sleep an average of 7 hours per day, you have slept approximately {hours_slept} hours in total.")


#in this project i learned how to create a simple python progrom for user interaction. I practiced user input, variable assignment, Basic calculation, output display and data types.