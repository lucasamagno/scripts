# Write a Python function that: 
# (a) Takes a string as a parameter. 
# (b) Prints out each character followed by their index and the number of times character appears in the string (ignoring capitalization). 
# (c) For example, if you passed in 'HelloOo!!' to the function, the result would be: H (0) - 1 e (1) - 1 l (2) - 2 l (3) - 2 o (4) - 3 O (5) - 3 o (6) - 3 ! (7) - 2 ! (8) - 2

my_string = "WhooOoOo!?!!?"

def indexAndCountLetters(my_string):
    letter_list = []
    letter_dict = dict()
    my_string_lower_case = my_string.lower()
    
    #count letters
    for i in range(len(my_string)):
        letter_list.append(my_string[i])
        if my_string_lower_case[i] in letter_dict:
            letter_dict[my_string_lower_case[i]] = int(letter_dict.get(my_string_lower_case[i]) + 1)
        else:
            letter_dict[my_string_lower_case[i]] = 1

    #assemble string
    resulting_string = f''
    for i in range(len(letter_list)):
        resulting_string += f"{letter_list[i]} ({i}) - {letter_dict.get(my_string_lower_case[i])} "

    return resulting_string 

result = indexAndCountLetters(my_string)

print(result)

