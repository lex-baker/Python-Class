##Program to explore scope

def what_is_accessible(parameter_in_function) :
    global message_in_main;
    """ Helper function to explore variable scope """
    print("First print in function: ", parameter_in_function);
    parameter_in_function += "More important information.";
    print("Second print in function: ",parameter_in_function);
    message_created_in_function = "...and don't foget this information.";
    print("Third print in function: ", message_created_in_function);
    message_in_main += " Modified from function"
    print("Fourth print in function:", message_in_main);

    return message_created_in_function;

# def my_test(a, b):
#     a = 5
#     b += 5
#     return

# def my_array_test(a, b):
#     a = [5]
#     b += [5]
#     return 

# #Main program - my additions
# first = 1
# second = 2
# my_test(first, second)
# print(first, second) # 1 2
# arr = [1, 2, 3, 4]
# arr2 = [1, 2, 3, 4]
# my_array_test(arr, arr2)
# print(arr, arr2) # [1, 2, 3, 4] [1, 2, 3, 4, 5]

# def more_testing():
#     if is_global:
#         print("Globally accessible variable")
#     print(is_global)

# is_global = True
# more_testing()

# def param_exists(check_var):
#     check_var += 10
#     global a_new_var
#     a_new_var = 17
#     return

# example = 5
# param_exists(example)
# # print(check_var)
# print(a_new_var)

# def param_mod(param):
#     print(param) # Returns 32
#     param += 10
#     print(param) # Returns 42
#     return

# param_mod(32)


#"Main program" to explore scope of variables with functions
message_in_main = "Important information.";
print("First print in main:", message_in_main);
value_returned_from_function = what_is_accessible(message_in_main);
print("Second print in main:", value_returned_from_function);
print("Third print in main:", message_in_main);
try:
    print(parameter_in_function);
except NameError:
    print("The parameter name is not valid back in the main program.")
