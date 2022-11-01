##Prints a silly song
##Illustrates how to define and call a custom function

def funnyFruit() :
    """ Create and print a silly message """
    # message = letter + "pples and b" + letter + "n" \
    #     + letter + "n" + letter + "s"
    # print(message)
    for l in range(26):
        message = chr(97 + l) + "pples and b" + chr(97 + l) + "n" \
            + chr(97 + l) + "n" + chr(97 + l) + "s"
        print(message)

##Main program
print("I like to eat, eat, eat...")

funnyFruit()

# funnyFruit('a')
# funnyFruit('e')
# funnyFruit('i')
# funnyFruit('o')
# funnyFruit('u')

# accented_a = chr(int('e1',16))
# funnyFruit(accented_a)
# funnyFruit(chr(int('fc',16)))

