# Write a Python function that: 
# (a) Takes a string as a parameter. 
# (b) Prints out each character followed by their index and the number of times character appears in the string (ignoring capitalization). 
# (c) For example, if you passed in 'HelloOo!!' to the function, the result would be: H (0) - 1 e (1) - 1 l (2) - 2 l (3) - 2 o (4) - 3 O (5) - 3 o (6) - 3 ! (7) - 2 ! (8) - 2

myString = "WhooOoOo!?!!?"

def indexAndCountLetters(myString):
    letter_list = []
    letter_dict = dict()
    myStringLowerCase = myString.lower()
    
    #count letters
    for i in range(len(myString)):
        letter_list.append(myString[i])
        if myStringLowerCase[i] in letter_dict:
            letter_dict[myStringLowerCase[i]] = int(letter_dict.get(myStringLowerCase[i]) + 1)
        else:
            letter_dict[myStringLowerCase[i]] = 1

    #assemble string
    resulting_string = f''
    for i in range(len(letter_list)):
        resulting_string += f"{letter_list[i]} ({i}) - {letter_dict.get(myStringLowerCase[i])} "

    return resulting_string 

result = indexAndCountLetters(myString)

print(result)

