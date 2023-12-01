#this was some more practice i did in python dictionaries

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
