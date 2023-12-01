#this was some more practice i did in python dictionaries

#In Challenge 1, I added a new occupation to an individual's information in a stored dictionary. Challenge 2 involved merging two dictionaries, combining their key-value pairs. Challenge 4 calculated the sum of integer values in a stored dictionary using the sum() function. Lastly, Challenge 6 removed entries with keys of length 2 from a stored dictionary, resulting in a filtered dictionary. These exercises deepened my understanding of dictionary manipulation, merging, and summation, enhancing my skills for future Python projects.


# Challenge 1: Add a dictionary item to a stored dictionary

# Stored dictionary
stored_dict = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

# New dictionary item to add
new_item = {"occupation": "Engineer"}

# Add the new item to the stored dictionary
stored_dict.update(new_item)

# Display the updated dictionary
print("Updated Dictionary (Challenge 1):", stored_dict)



# Challenge 2: Join (merge) two stored dictionaries

# Stored dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Join (merge) the dictionaries
joined_dict = {**dict1, **dict2}

# Display the joined dictionary
print("Joined Dictionary (Challenge 2):", joined_dict)



# Challenge 4: Sum all values of a stored dictionary

# Stored dictionary with integer values
stored_dict = {
    "value1": 10,
    "value2": 20,
    "value3": 30,
    "value4": 15
}

# Sum all values in the dictionary
total_sum = sum(stored_dict.values())

# Display the total sum
print("Total Sum of Values (Challenge 4):", total_sum)


# Challenge 6: Remove entries with keys of length 2 from a stored dictionary

# Stored dictionary
stored_dict = {
    "name": "John",
    "age": 25,
    "city": "New York",
    "ab": 42,
    "xy": 18,
    "country": "USA"
}

# Remove entries with keys of length 2
filtered_dict = {key: value for key, value in stored_dict.items() if len(key) != 2}

# Display the filtered dictionary
print("Filtered Dictionary (Challenge 6):", filtered_dict)
