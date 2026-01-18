def pin_extractor(poems):
    secret_codes = []  # Initialize an empty list to store PINs for all poems
    
    # Loop over each poem in the list of poems
    for poem in poems:
        secret_code = ''  # Initialize an empty string to store the PIN for the current poem
        lines = poem.split('\n')  # Split the poem into lines using the newline character
        
        # Loop over each line in the poem with its index
        for line_index, line in enumerate(lines):
            words = line.split()  # Split the line into words
            
            # If the line has enough words, take the length of the nth word
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))  # Convert length to string and append to PIN
            else:
                secret_code += '0'  # If the word doesn't exist, append '0' to the PIN
        
        secret_codes.append(secret_code)  # Add the completed PIN for this poem to the list
    
    return secret_codes  # Return the list of all PINs


# Define poems
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

# Call the function with a list of poems and print the resulting PINs
print(pin_extractor([poem, poem2, poem3]))

