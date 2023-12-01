#for this activity I was practicing manipulating strings



import random

#Challenge 1: Write a program that produces the following output:

#Please enter your class size:
#3

# Please enter student 1 name:
#Beyonce

# Please enter student 2 name:
# Michelle

#Please enter student 3 name:
#Kelly

#Thank you, the names of your students in swapped case are: bEYONCE, kELLY, mICHELLE
# Challenge 1: Program for swapping case of student names

# Prompt the user to enter the class size
class_size = int(input("Please enter your class size: "))

# Initialize an empty list to store student names
student_names = []

# Prompt the user to enter each student's name
for i in range(1, class_size + 1):
    student_name = input(f"Please enter student {i} name: ")
    student_names.append(student_name)

# Swap case for each student name
swapped_case_names = [name.swapcase() for name in student_names]

# Display the result
print("Thank you, the names of your students in swapped case are:", ", ".join(swapped_case_names))


#Challenge 2: Write a program that accepts a user input sentence and then replaces all the spaces with dashes before displaying the output to screen.

# Challenge 2: Replace spaces with dashes in a user input sentence

# Prompt the user to enter a sentence
user_sentence = input("Please enter a sentence: ")

# Replace spaces with dashes
modified_sentence = user_sentence.replace(" ", "-")

# Display the modified sentence
print("Modified Sentence:", modified_sentence)


#Challenge 4: Write a program that randomly picks a character from a stored string and then places that character between every character in the string.


# Challenge 4: Randomly insert a character between every character in a stored string

# Stored string
stored_string = "Hello"

# Randomly pick a character
random_char = random.choice(stored_string)

# Insert the random character between every character in the string
modified_string = random_char.join(stored_string)

# Display the result
print("Stored String:", stored_string)
print(f"Randomly inserted '{random_char}' between every character:", modified_string)


#Challenge 3: Write a program that reverses the letters in a stored string.

# Challenge 3: Reverse the letters in a stored string

# Stored string
stored_string = "Hello"

# Reverse the letters in the string
reversed_string = stored_string[::-1]

# Display the result
print("Stored String:", stored_string)
print("Reversed String:", reversed_string)
