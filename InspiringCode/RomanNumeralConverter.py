#Dictionary (tallies): Maps each Roman numeral to its corresponding decimal value.
#Function (RomanNumeralToDecimal): Takes a Roman numeral string as input and converts it to its decimal equivalent using the specified rules. The function iterates through the characters of the Roman numeral and calculates the decimal value based on the comparison of consecutive characters.


# Dictionary to map Roman numerals to their decimal values
tallies = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    # specify more numerals if you wish
}

# Function to convert Roman numerals to decimal
def RomanNumeralToDecimal(romanNumeral):
    sum = 0
    for i in range(len(romanNumeral) - 1):
        left = romanNumeral[i]
        right = romanNumeral[i + 1]
        # Subtract the left numeral if it's smaller than the right numeral
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else:
            # Add the left numeral if it's greater than or equal to the right numeral
            sum += tallies[left]
    # Add the value of the last numeral in the Roman numeral string
    sum += tallies[romanNumeral[-1]]
    return sum

#source code:
#https://gist.github.com/amankharwal/4ea5fc3efbe8b522dc340de8f72dbbd9#file-roman-to-decimal-py