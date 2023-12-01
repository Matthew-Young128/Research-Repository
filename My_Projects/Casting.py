#For this exercise i wanted to learn how casting works

# The Casting.py file provided looked like this:
 
# variable set to integer
my_score = 201
 
print("The type of my_score is ", type(my_score),"\n")
print("my_score is ", my_score,"\n")
 
print("Casting to a string...\n")
# variable cast to string
my_score = str(my_score)
 
print("The type of my_score is now ", type(my_score),"\n")
print("my_score is ", my_score,"\n")


#My ShoeSize.py file looked like this. There were a few questions to answer

# Create and set a float variable
my_size = 8.5

# Output the type and the float value to screen
print("The type of my_size is ", type(my_size), "\n")
print("my_size is ", my_size, "\n")

# Cast my_size to integer and then output the type and value to screen
my_size = int(my_size)
print("Casting to an integer...\n")
print("The type of my_size is now ", type(my_size), "\n")
print("my_size is ", my_size, "\n")


#What happened to the value of my_size?
#Initially, my_size is a float with a value of 8.5.
#After casting it to an integer, the value becomes 8.

#Why did this happen?
#When you cast a float to an integer in Python, the fractional part is truncated, resulting in the whole number part of the float.

#What does this tell you about casting between types?
#Casting between types can lead to loss of information or precision, depending on the types involved. In this case, casting a float to an integer discards the fractional part, and you end up with the whole number part only. 


#In this casting exercise, I learned that converting a float to an integer in Python results in the truncation of the fractional part, leading to the loss of decimal precision. This experience highlighted the importance of being mindful of potential data loss when casting between different types, underscoring the need to carefully consider the implications of such conversions in programming tasks.