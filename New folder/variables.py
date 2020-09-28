class MyClass:
	
	def __init__(self, name, age):
		self.name = name
		age = age
		self.age = age + 24
		self.greating = None
	def new_function(self):
		
		self.greating = f"{self.age} name: {self.name}"
		return self.greating

print("sad")
print(MyClass)

a = MyClass(5, 9)
print(a.name)
# print(a.age)
# a.name = 5
# a.age = 6
print(a.name)
print(a.age)
# print(MyClass.age)
# print(a.greating)
print(a.new_function())
print(MyClass.new_function)
# print(MyClass.greating)