# Write a Python function that: 
# (a) Takes a string as a parameter. 
# (b) Prints out each character followed by their index and the number of times character appears in the string (ignoring capitalization). 
# (c) For example, if you passed in 'HelloOo!!' to the function, the result would be: 
# H (0) - 1 
# e (1) - 1 
# l (2) - 2 
# l (3) - 2 
# o (4) - 3 
# O (5) - 3 
# o (6) - 3 
# ! (7) - 2 
# ! (8) - 2

myString = "HelloOo!!"

def compute(myString):
    passed_in_string = myString.lower()
    letter_list = []
    resulting_string = f''
    letter_dictionary = dict()
    #count values
    for i in range(len(passed_in_string)):
        letter_list.append(myString[i])
        if passed_in_string[i].lower() in letter_dictionary:
            letter_dictionary[passed_in_string[i]] = int(letter_dictionary.get(passed_in_string[i]) + 1)
        else:
            letter_dictionary[passed_in_string[i]] = 1

    #assemble string
    for i in range(len(letter_list)):
        resulting_string = resulting_string + f"{letter_list[i]} ({i}) - {letter_dictionary.get(passed_in_string[i])} "

    return resulting_string 

result = compute(myString)

print(result)

