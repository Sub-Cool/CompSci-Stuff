# Get the string from the user
user_string = input("Enter a string: ")

# Initialize the vowel counter
vowel_count = 0

# Initialize the vowel counters
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

# Loop through the string
for letter in user_string:
    # Check if the letter is a vowel
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        # Increment the vowel counter
        vowel_count += 1

        # Increment the vowel counters
        if letter == "a":
            a_count += 1
        elif letter == "e":
            e_count += 1
        elif letter == "i":
            i_count += 1
        elif letter == "o":
            o_count += 1
        elif letter == "u":
            u_count += 1

# Print the number of vowels in the string
print("There are", vowel_count, "vowels in the string.")

# Print the number of each vowel in the string
print("There are", a_count, "a's in the string.")
print("There are", e_count, "e's in the string.")
print("There are", i_count, "i's in the string.")
print("There are", o_count, "o's in the string.")
print("There are", u_count, "u's in the string.")