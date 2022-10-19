# Write a function named readposint that uses the input dialog to prompt the user for a 
# positive integer and then checks the input to confirm that it meets the requirements. 
# It should be able to handle inputs that cannot be converted to int, as well as negative int, 
# and edge cases (e.g. when the user closes the dialog, or does not enter anything at all.)

def readposint():
    try:
        num = int(input("Enter: "))
        if num <= 0:
            print("Not a positive integer!")
            exit()
        elif not num > 0:
            print("I don't know what you did but it wasn't right!")
            exit()
        print(num, "is a positive integer!!")
    except Exception as e:
        print("Something else went wrong:")
        print(e)
readposint()