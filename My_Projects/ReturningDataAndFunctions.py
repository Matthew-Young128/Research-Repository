#for this exercise i was working on creating functions that the user can interact with. 

#Through these function exercises, I've learned to design modular and reusable Python code, enhancing organization and readability. With parameters and return statements, I can handle inputs, perform operations, and obtain valuable results. Encapsulation principles promote code manageability, and user interaction within functions is crucial for user-friendly programs. These skills will be key in building efficient, readable code and tackling diverse programming scenarios in the future.

#Challenge 1

def run_quiz():
    # Initialize the score
    score = 0

    # Question 1
    print("Question 1: What is the capital of France?")
    answer1 = input("a) Paris\nb) London\nc) Berlin\nYour answer: ").lower()
    score += evaluate_answer(answer1, 'a')

    # Question 2
    print("\nQuestion 2: What is the largest mammal on Earth?")
    answer2 = input("a) Elephant\nb) Blue Whale\nc) Giraffe\nYour answer: ").lower()
    score += evaluate_answer(answer2, 'b')

    # Display the final score
    print(f"\nYour final score is: {score}/2")


def evaluate_answer(user_answer, correct_answer):
    # Evaluate user's answer and return 1 if correct, 0 otherwise
    if user_answer == correct_answer:
        print("Correct!\n")
        return 1
    else:
        print("Incorrect.\n")
        return 0

# Run the quiz
run_quiz()



#Challenge 2

def add_numbers(num1, num2):
    # Function to add two numbers
    return num1 + num2

def run_calculator():
    # Get user input for the numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculate the sum using the function
    result = add_numbers(num1, num2)

    # Display the result
    print(f"The sum of {num1} and {num2} is: {result}")

# Run the calculator
run_calculator()


#Challenge 3

def calculate_parking_cost(hours):
    # Function to calculate parking cost
    base_cost = 4
    additional_hours_cost = max(0, hours - 2) * 3
    total_cost = base_cost + additional_hours_cost
    return total_cost

def run_parking_meter():
    # Display welcome message and instructions
    print("Welcome to the Parking Meter Program!")
    print("The first 2 hours cost $4, and each additional hour costs $3.")

    # Get user input for the number of hours
    hours = float(input("Enter the number of hours you need to park: "))

    # Calculate and display the parking cost using the function
    cost = calculate_parking_cost(hours)
    print(f"The total cost of parking for {hours} hours is: ${cost}")

# Run the parking meter program
run_parking_meter()


#Challenge 4

list_a = ["brown", "grey", "amber"]
list_b = ["red", "green"]
list_c = ["purple"]

list_d = [list_a, list_b, list_c]

def fill_list(lst):
    # Function to fill a list with user input if it has less than 3 elements
    while len(lst) < 3:
        user_input = input(f"Enter an element for the list ({len(lst) + 1}/3): ")
        lst.append(user_input)

def check_and_fill_lists():
    # Check and fill lists in list_d
    for i, sublist in enumerate(list_d, 1):
        print(f"\nChecking List {i}: {sublist}")
        if len(sublist) < 3:
            fill_list(sublist)
            print(f"List {i} updated: {sublist}")

# Run the program
check_and_fill_lists()
