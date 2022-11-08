# Author: Lex Baker
# Date: 11/8/22
# Lab 13, Classes

import random

class Person():
    def __init__(self, name, color):
        self.name = name
        self.age = random.randint(1, 99)
        self.favoriteColor = color

    def sayHi(self):
        print("Hi, my name is", self.name)

    def getAge(self):
        return self.age

    def isMinor(self):
        is_minor = False
        if self.age < 21:
            is_minor = True
        return is_minor


def main():
    my_friend_1 = Person("Alice", "red")
    my_friend_2 = Person("Bob", "blue")
    my_friend_3 = Person("Chloe", "yellow")
    my_friend_1.sayHi()
    my_friend_2.sayHi()
    my_friend_3.sayHi()



if __name__ == "__main__":
    main()
