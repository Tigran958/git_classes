class Fruit:
	def __init__(self, name, color, price):
		self.name = name
		self.color = color
		self.price_kg = price

	def presentation(self):
		text = f"The fruit is {self.name} it's color is {self.color}"\
				f" and the price for kg is {self.price_kg}"
		return text

	def change_name(self, name):
		self.name = name

orange = Fruit("Orange", 'orange', 700)
print(orange.presentation())
orange.change_name("Limon")
print(orange.presentation())

print("we will win!")




