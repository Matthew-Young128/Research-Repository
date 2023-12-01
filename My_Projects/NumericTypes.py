#for this exercise i was working on numeric types in python

#Calculate area of circle with radius 6. You should store radius in variable 'r' and 'area' in variable area. Display area of circle and data type of both variables 'r' and 'area'. 
# Calculate area of a circle with radius 6
import math

# Store the radius in a variable 'r'
r = 6

# Calculate the area using the formula: area = π * r^2
area = math.pi * (r ** 2)

# Display the area of the circle
print(f"The area of the circle with radius {r} is: {area}")

# Display the data type of variable 'r' and 'area'
print(f"The data type of 'r' is: {type(r)}")
print(f"The data type of 'area' is: {type(area)}")



#Create three variables x = 4, y = 7, and y = 34.7. Add values of these variable and store them in 'add' variable. Display value of add variable and data type of all variables. 
# Create three variables
x = 4
y = 7
z = 34.7

# Add values of x, y, and z and store in 'add' variable
add = x + y + z

# Display the value of 'add' variable
print(f"The sum of x, y, and z is: {add}")

# Display the data types of all variables
print(f"The data type of 'x' is: {type(x)}")
print(f"The data type of 'y' is: {type(y)}")
print(f"The data type of 'z' is: {type(z)}")
print(f"The data type of 'add' is: {type(add)}")

#Display real and imaginary part of following numbers. 
#3 + 7j
#9j 

# Complex numbers
complex_number1 = 3 + 7j
complex_number2 = 9j

# Display real and imaginary parts
print(f"For the complex number {complex_number1}:")
print(f"Real part: {complex_number1.real}")
print(f"Imaginary part: {complex_number1.imag}\n")

print(f"For the complex number {complex_number2}:")
print(f"Real part: {complex_number2.real}")
print(f"Imaginary part: {complex_number2.imag}")
