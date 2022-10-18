# Lex Baker
# Lab 9, For loop and range
# Submitted 10/18/22

# index = range(10)
# print(index[0])
# print(index[1])
# print(index[9])
# #print(index[10])
# print(index)
# print(tuple(index))

# even_nums = range(0,10,2)
# print(even_nums[0])
# print(even_nums[1])
# print(even_nums[2])
# print(len(even_nums))
# print(tuple(even_nums))

# my_range = range(3, 15, 4)  # 15 exclusive
# print(tuple(my_range))
# my_range = range(3, 16, 4) # 15 inclusive
# print(tuple(my_range))

# my_range = range(5, -1, -1)
# print(len(my_range))
# print(tuple(my_range))

# my_range = range(0, 5, .5)
# print(tuple(my_range))

range1 = range(0, 5)
range2 = range(5, 10)
# throws an error, can't concatenate ranges
big_range = range1 + range2