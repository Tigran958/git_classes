# name = input("enter something")

# if name.isdigit():
# 	print("digits")

# name = input("enter something")	

# if name.isalpha():
# 	print("Letters")	

# 	if name.islower():
# 		print("Lower")

# 	elif name.isupper():
# 		print("Upper")


name = input("enter something and I'll tell you if it is a letter or digit: ")

if name.isalpha():
	if name.isupper():
		print(name + " is a Capital letter")
	else:
		print(name + " is a lowercase letter")
else:
	print(name + " is a digit")

print("thanks for paticipating")
