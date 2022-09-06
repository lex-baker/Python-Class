# Lex Baker
# 9/6/22
# Python For Scientists
# 
# A program that simulates a customer/server interaction

# Assign values to variables
guest_name = input("What is your name? ") # Part A
app_cost = float(input("How much does the appetizer cost? ")) # Part C
entree_cost = float(input("How much does the entree cost? ")) # Part A
tip = float(input("What percentage tip do you want to leave? ")) # Part D
tax_rate = .095

# Calculate the tax and total bill
tax_owed = (app_cost + entree_cost) * tax_rate # Part C
total_owed_pre_tax = app_cost + entree_cost + tax_owed # Part C

# Assuming the tip is after tax
tip_owed = total_owed_pre_tax * (tip / 100.0) # Part D
total_owed_post_tax = total_owed_pre_tax + tip_owed # Part D

#Round to the second decimal place
#total_owed = round(total_owed, 2) # Part B
total_owed = round(total_owed_post_tax, 2) # Part D

# Print the simulated conversation
print("Hello,", guest_name)
print("Your appetizer cost $", app_cost, sep="")
print("Your entree cost $", entree_cost, sep="")
print(total_owed_pre_tax)
print("Including tax and tip, your total bill is $", total_owed,sep="")
