# Lex Baker
# Lab 9, For loop and range
# Submitted 10/18/22


# for ii in range(0,10000,5):
#     print(ii)

# for ii in range(5000,-200,-6):
#     print(ii)



# squares = ()
# for ii in range(1,11) :
#    	squares = squares + (ii*ii,)

# print(squares)



# runs = (1, -1, 9, 7)
# total = 0
# for ii in range(0,len(runs)) :
#     total = total + runs[ii]

# average = total/len(runs)
# print(average)



# text = "This is the new texT, not boring in The slighTest."
# special_letter = 'T'
# ocurrences = 0
# for ii in range(len(text)) :
#     print(ii, text[ii])
#     if(text[ii] == special_letter) :
#         ocurrences += 1

# print("The letter '",special_letter,"' ocurrs ",ocurrences," times in the text:", sep="")
# print(text)



# crazy_list = ('hi', 42, True, (1, 3, 5), 1/4, None, "this is crazy", (True or False))
# for element in crazy_list :
#      print(element)   



# text = "CraZy nEw teXt whOoHoO."
# special_letter = 'e'
# ocurrences = 0
# for letter in text :
#     print(letter)
#     if (letter == special_letter) :
#         ocurrences += 1

# print("The letter",special_letter,"ocurrs",ocurrences,"times in the text:")
# print(text)



# MAX = 10
# for ii in range(1, MAX+1):
#      for jj in range(1, ii+1) :
#         print(ii,'\t',end = "")
#      print()



# My modified code from Lab 8, Question 2, Part D
# Mariners_runs = (10, 8, 8, 2, 3, 3, 5, 0, 6, 1)
# Opponents_runs = (3, 5, 2, 3, 1, 6, 3, 2, 4, 3)
# Mariners_record = 0
# for i in range(10):
#     if Mariners_runs[i] > Opponents_runs[i]:
#         Mariners_record += 1
# print(Mariners_record)


# Better demonstration of for loop example
nums = (1,)
new = 1
old = 0
for i in range(1, 100):
    nums += (new + old,)
    old = new
    new = nums[i]
print(len(nums))
print(nums)


# Minimal coding example
nums = (1, 1)
for i in range(1, 99):
    nums += (nums[i] + nums[i-1],)
print(len(nums))
print(nums)