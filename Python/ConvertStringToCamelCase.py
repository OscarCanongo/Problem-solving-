# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
#The first word within the output should be capitalized only if the original word was capitalized 
#(known as Upper Camel Case, also often referred to as Pascal case).

def to_camel_case(text):
    print(text)
    flag = False
    res = ''
    for x in text:
        if(x == '-' or x == '_'):
            x = ''
            flag = True
        elif(flag):
            res = res + x.upper()
            flag = False
        else:
            res = res + x
    print(res)
    return res;