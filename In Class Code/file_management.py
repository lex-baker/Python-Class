def thing1():
    file = open("Practice Code/example.txt", "wt")
    file.write("Hello World\n")
    file.write("Is there a line printed?\n")
    file.write("True")
    #print(file.readlines())
    file.close()

    samefile = open("Practice Code/example.txt", "rt")
    lines = samefile.readlines()
    if(eval(lines[2])):
        print(lines)
    else:
        print("Something went wrong")
    samefile.close()

def main():
    fname = input("Enter filename: ")
    infile = open("Practice Code/" + fname, "r")
    data = infile.read()
    