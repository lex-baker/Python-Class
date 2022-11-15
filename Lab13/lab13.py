# Author: Lex Baker
# Date: 11/15/22
# Lab 13 or 14 or something



###
### Problem 1
###
print("\nProblem 1\n")

class Account(object):
    interest = 0.02
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Yes!")

a = Account("Billy")
# print(a.account_holder)

print(a.holder)

# print(Account.holder)

print(Account.interest)

print(a.interest)

Account.interest = 0.03
print(a.interest)

print(a.deposit(1000))

print(a.balance)

a.interest = 9001
print(Account.interest)


###
### Problem 2
###
print("\nProblem 2\n")


class Person(object):
    """Person class. Docstring tests follow:
    steven = Person("Steven")
    steven.repeat() # starts at whatever value you'd like
    # 'I squirreled it away before it could catch on fire.'
    steven.say("Hello")
    # 'Hello'
    steven.repeat()
    # 'Hello'
    steven.greet()
    # 'Hello, my name is Steven'
    steven.repeat()
    # 'Hello, my name is Steven'
    steven.ask("preserve abstraction barriers")
    # 'Would you please preserve abstraction barriers'
    steven.repeat()
    # 'Would you please preserve abstraction barriers'
    """
    # Class definitons begin here:
    def __init__(self, name):
        self.name = name
        self.last_spoke = "I squirreled it away before it could catch on fire."
    def say(self, stuff):
        self.last_spoke = stuff
        return stuff
    def ask(self, stuff):
        return self.say("Would you please " + stuff)
    def greet(self):
        return self.say("Hello, my name is " + self.name)
    def repeat(self):
        "*** YOUR CODE HERE ***"
        return self.say(self.last_spoke)

steven = Person("Steven")
print(steven.repeat()) # starts at whatever value you'd like
# 'I squirreled it away before it could catch on fire.'
print(steven.say("Hello"))
# 'Hello'
print(steven.repeat())
# 'Hello'
print(steven.greet())
# 'Hello, my name is Steven'
print(steven.repeat())
# 'Hello, my name is Steven'
print(steven.ask("preserve abstraction barriers"))
# 'Would you please preserve abstraction barriers'
print(steven.repeat())
# 'Would you please preserve abstraction barriers'



###
### Problem 3
###
print("\nProblem 3\n")


class Account(object):
    interest = 0.02
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Yes!")

class CheckingAccount(Account):
    def __init__(self, account_holder):
        Account.__init__(self, account_holder)
    def deposit(self, amount):
        Account.deposit(self, amount)
        print("Have a nice day!")

a = Account("Billy")
print(a.balance)

c = CheckingAccount("Eric")
print(c.balance)

a.deposit(30)

c.deposit(30)

print(c.interest)


###
### Problem 4
###
print("\nProblem 4\n")



"""
steven = DoubleTalker("Steven")
print(steven.say("hello"))
# "hello hello"
print(steven.say("the sky is falling"))
# "the sky is falling the sky is falling"
"""

# class DoubleTalker(Person):
#     def __init__(self, name):
#         Person.__init__(self, name)
#     def say(self, stuff):
#         return Person.say(self, stuff) + " " + self.repeat()

# steven = DoubleTalker("Steven")
# print(steven.say("hello"))
# # "hello hello"
# print(steven.say("the sky is falling"))
# # "the sky is falling the sky is falling"

class DoubleTalker(Person):
    def __init__(self, name):
        Person.__init__(self, name)
    def say(self, stuff):
        return stuff + " " + stuff

steven = DoubleTalker("Steven")
print(steven.say("hello"))
# "hello hello"
print(steven.say("the sky is falling"))
# "the sky is falling the sky is falling"

class DoubleTalker(Person):
    def __init__(self, name):
        Person.__init__(self, name)
    def say(self, stuff):
        return Person.say(self, stuff + " " + stuff)

steven = DoubleTalker("Steven")
print(steven.say("hello"))
# "hello hello"
print(steven.say("the sky is falling"))
# "the sky is falling the sky is falling"




###
### Problem 5
###
print("\nProblem 5\n")




class Account(object):
    """A bank account that allows deposits and withdrawals.
    eric_account = Account('Eric')
    print(eric_account.deposit(10000)) # depositing my paycheck for the
    week
    # 10000
    print(eric_account.transactions)
    # [('deposit', 10000)]
    print(eric_account.withdraw(100)) # buying dinner
    # 999900
    print(eric_account.transactions)
    # [('deposit', 10000), ('withdraw', 100)]
    print(eric_account.report())

    # Transaction Report for Eric
    # Type Amount
    # =================================
    # deposit 10000
    # withdraw 100
    # ---------------------------------
    # Balance 9900
    """
    interest = 0.02
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []
    def deposit(self, amount):
        """Increase the account balance by amount and return the
        new balance.
        """
        self.balance = self.balance + amount
        self.transactions.append("deposit " + str(amount))
        return self.balance
    def withdraw(self, amount):
        """Decrease the account balance by amount and return the
        new balance.
        """
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        self.transactions.append("withdraw " + str(amount))
        return self.balance
    def report(self):
        output = "Transaction Report for " + str(self.holder) \
            + "\nType Amount\n" + ("=" * 33) + "\n"
        for t in self.transactions:
            output += t + "\n"
        output += "-" * 33
        output += "\nBalance " + str(self.balance) +"\n"
        return output


eric_account = Account('Eric')
print(eric_account.deposit(10000)) # depositing my paycheck for the week
# 10000
print(eric_account.transactions)
# [('deposit', 10000)]
print(eric_account.withdraw(100)) # buying dinner
# 999900
print(eric_account.transactions)
# [('deposit', 10000), ('withdraw', 100)]
print(eric_account.report())

# Transaction Report for Eric
# Type Amount
# =================================
# deposit 10000
# withdraw 100
# ---------------------------------
# Balance 9900