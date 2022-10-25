# Lex Baker
# Lab 10, Lists and Dictionaries
# Submitted 10/25/22

import random

# torisGrades= [80, 95, 88, 73, 92]
# print(torisGrades)
# torisGrades.append(89)
# print(torisGrades)
# torisGrades = torisGrades + [79, 73]
# print(torisGrades)

# johnsGrades = []
# for i in torisGrades:
#     johnsGrades.append(random.randint(50, 100))

# print("Tori's grades:", torisGrades)
# print("John's grades:", johnsGrades)

# print(torisGrades)
# torisGrades[1] = 93
# print(torisGrades)

# del torisGrades[4]
# print(torisGrades)


# print(len(torisGrades)) # Returns the length of the list
# print(max(torisGrades)) # Returns the highest value in the list
# print(min(torisGrades)) # Returns the lowest value in the list
# print(sum(torisGrades)) # Returns the sum of all values in the list
# print(88 in torisGrades) # Returns True if 88 is in the list, False if not
# print(70 in torisGrades) # Returns True if 70 is in the list, False if not

# print(sorted(torisGrades))
# median_grade = sorted(torisGrades)[len(torisGrades) // 2]
# print("Her median grade is:", median_grade)

suits = ['S', 'C', 'H', 'D']
ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
deck = []

for s in suits:
    for r in ranks:
        deck.append(r + s)
# print(len(deck))
# print(deck)

def shuffle():
    shuffled_deck = []
    for c in range(52):
        shuffled_deck.append(deck[random.randrange(52 - len(shuffled_deck))])
    # My Original Implementation
    # Swap two random cards 52 times, 5 times over
    # for i in range(5):
    #     for s in range(52):
    #         index1 = random.randrange(52)
    #         index2 = random.randrange(52)
    #         temp = d[index1]
    #         d[index1] = d[index2]
    #         d[index2] = temp
    # Returning the shuffled deck
    return shuffled_deck

# new_deck = shuffle()
# print(new_deck)


# Experimentally testing probability

# Theoretical prob. for this is 1/13
def ace_first(iters):
    # iters is the total number of trials run
    # Probability of drawing an ace off the top of a randomly shuffled deck
    total_aces = 0
    for i in range(iters):
        new_deck = shuffle()
        if new_deck[0][0] == "A":
            total_aces += 1

    print(f"Total aces drawn first over {iters} trials: {total_aces}")
    exp_prob = (total_aces / iters) * 100
    print(f"Experimental probability of drawing ace first: {exp_prob:0.2f}%")

# ace_first(100)
# ace_first(1000)
# ace_first(10000)

# print("\n\n")

# Theoretical prob. for this is 1/17
def pair_first(iters):
    # iters is the total number of trials run
    # Probability of drawing two cards off the top of a randomly shuffled deck and them being pairs
    total_pairs = 0
    for i in range(iters):
        new_deck = shuffle()
        if new_deck[0][0] == new_deck[1][0]:
            total_pairs += 1
    
    print(f"Total pairs drawn first over {iters} trials: {total_pairs}")
    exp_prob = (total_pairs / iters) * 100
    print(f"Experimental probability of drawing a pair first: {exp_prob:0.2f}%")


# pair_first(100)
# pair_first(1000)
# pair_first(10000)


# scores = {"Ben": 4.1, "Angie": 3.7, "Liz": 2.5, "Heather": 3.3}

# print(scores.keys())
# print(scores.values())
# print(scores["Ben"])
# print(scores.get("Angie"))
# print(scores.get("Angie", "Key does not exist in dictionary."))
# print(scores.get("Mike", "Key does not exist in dictionary."))
# print("Heather" in scores)
# # print("Heather" in geek)
# del scores["Liz"]
# scores["Gen"] = 3.9
# print(scores.items())


squares = [x*x for x in range(10)]
print(squares)
evenSquares = [x*x for x in range(10) if x%2==0]
print(evenSquares)

given_list = [x for x in range(10)]
mult_by_7 = [x*7 for x in given_list if x%3==0]
print(mult_by_7)

words= ['python','onomatopaeia','pernicious','orangutang','ephemeral']
first_letters = [x[0] for x in words]
print(first_letters)