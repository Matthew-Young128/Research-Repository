#Design Principles and patterns

#Data Separation: The use of separate lists for different story elements demonstrates the separation of concerns, adhering to the principle of modularity.

#Randomization: The random.choice() function is used for random selection, contributing to the unpredictability and variety of generated stories.



#This code aligns with the practice of organizing data into lists, promoting maintainability and ease of modification. The randomization aspect introduces an element of surprise, enhancing the user experience. The design reflects a simple form of the Strategy Pattern, allowing different elements to be chosen independently, promoting flexibility in generating diverse and engaging stories.



#Our task is to generate a random story every time the user runs the program. I will first store the parts of the stories in different lists, then the Random module can be used to select the random parts of the story stored in different lists:


import random

# Lists of possible elements in the story
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
name = ['Ali', 'Miriam', 'Daniel', 'Hoouk', 'Starwalker']
residence = ['Barcelona', 'India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university', 'seminar', 'school', 'laundry']
happened = ['made a lot of friends', 'ate a burger', 'found a secret key', 'solved a mystery', 'wrote a book']

# Generate and print a random story
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) +
      ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))

#source code:
#https://gist.github.com/amankharwal/9a03b08de0a2db521cc342742d92c03d#file-story-py