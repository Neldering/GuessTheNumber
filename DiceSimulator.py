import random

min = float(input("enter min num: " ))
max = float(input("enter max num: "))

Roll_again = raw_input("Would you like to Roll? ")

while Roll_again == "Yes" or Roll_again == "yes" or Roll_again == "y" or Roll_again == "Y":
	print(random.randint(min,max))
	Roll_again = raw_input("Would you like to roll again?: ")
	
while Roll_again == "No" or Roll_again == "no" or Roll_again == "n" or Roll_again == "N":
	print("Have a good one")
	break
