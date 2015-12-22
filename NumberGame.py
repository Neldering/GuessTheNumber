import random
count = 0
print("Let's play a game!")
print("Rules are simple, pick a min and max number")
print("and I'll think of a number between them and you'll guess it!...")
print("you have 10 attempts")
min = float(input("enter min num: " ))
max = float(input("enter max num: "))
x = random.randint(min,max)
y = float(input("enter a number between your min and max :"))


while y != x and count < 11:
	if y < x:
		print("Larger")
	elif y > x:
		print("Smaller")
	count += 1
	y = float(input("Enter another attempt: "))

print("Game Over",y,x)
