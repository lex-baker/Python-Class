##Gets length and width from the user and calculates area
##Uses robust input technique
##Illustrates a funciton with a return value

def getNumber(prompt):
    """ Get a number from the user and return it """
    number = None;
    while number == None:
        try :
            number = int(input(prompt + '\n'));
        except ValueError :
            print("Not a valid input.");
    return number

##Main program
argument_prompt = input("How would you like me to prompt you to add an integer?\n")
x = getNumber(argument_prompt);
y = getNumber(argument_prompt);
print('If the length is', x, 'and the width is',y,\
    'then the area is',x*y);
