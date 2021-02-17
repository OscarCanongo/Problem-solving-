# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

def pig_it(text):
    x = text.split(" ")
    word = ""
    for y in x:
        if(y[0] == "!" or y[0] == "?"):
            word += y[0]
        else:    
            word += y[1:len(y)]+ y[0] + "ay "
    print(word)
    return word.strip()