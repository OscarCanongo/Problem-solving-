# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_count(input_str):
    num_vowels = 0
    # your code here
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for x in vowels:
        num_vowels = num_vowels + list(input_str).count(x)
            
    return num_vowels