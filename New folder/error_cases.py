a = input("give me a positive number ")

try:
	if not a.isdigit():
		raise ValueError("Wrong Value it is not a digit")
	a = int(a)
	if a < 5:
		raise Exception("the number could not be lower than 5")
except ValueError as error:
	print(error)
	a = input("give me a positive NUMBER ")
except Exception as e:
	print(e)
	a = input("give me a POSITIVE > 5 number ")




















########______________________ Password validator_________________#############
a = input("give me a password ")
check = True
while check:
	try:
		a = input("password ")
		if len(a) < 8:
			raise ValueError("wrong password less than 8")

		my_list = []
		for i in a:
			if i.isdigit():
				my_list.append(True)
				break

		if len(my_list) == 0:
			raise TypeError("wrong type should contain number")

		if not a[0].isupper():
			raise Exception("should be upper")

		check = False
	except ValueError as v:
		print(v)

	except TypeError as t:
		print(t)
	except Exception as e:
		print(e)