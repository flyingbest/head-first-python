# Class
class Student:
	name = 'ansxodbs'
	def info(self):
		print("My name is " + self.name + ". ")

inst = Student()

print(type(inst))
print(inst.name)
inst.info()

class Book:
	# Constructor
	def __init__(self, BookName):
		self.name = BookName
		print("object is constructed. The book name is " + self.name + ". ")
	# Destructor
	def __del__(self):
		print("object " + self.name + " is destructed.")

objectBook = Book('Python3 programming')
del objectBook


# Inheritance
class Person:
	def __init__(self, name, age, gender):
		self.Name = name
		self.Age = age
		self.Gender = gender
	def printInfo(self):
		print("My name is " + self.Name + ". I am " + str(self.Age) + " years old.")

class Employee(Person):
	def __init__(self, name, age, gender, salary, hiredate):
		Person.__init__(self, name, age, gender)
		self.Salary = salary
		self.Hiredate = hiredate
	def doWork(self):
		print("I'm working hard!")
	def printInfo(self):
		Person.printInfo(self)
		print("My salary is " + str(self.Salary) + " dollars. And My hiredate is " + self.Hiredate + ".")

objectEmployee = Employee("ansxodbs", 20, "man", 50000000, "04-05-2017")
objectEmployee.doWork()
objectEmployee.printInfo()


# Multiple Inheritance
class ParentOne:
	def func(self):
		print("call func of ParentOne!")

class ParentTwo:
	def func(self):
		print("call func of ParentTwo!")

class Child(ParentOne, ParentTwo):
	def childFunc(self):
		ParentOne.func(self)
		ParentTwo.func(self)
		print("call func of child!")

objectChild = Child()
objectChild.childFunc()
print()
objectChild.func()
print()

class A:
	def __init__(self):
		print("call constructor of A class")

class B(A):
	def __init__(self):
		#A.__init__(self)
		super().__init__()
		print("call constructor of B class")

class C(A):
	def __init__(self):
		#A.__init__(self)
		super().__init__()
		print("call constructor of C class")

class D(B, C):
	def __init__(self):
		#B.__init__(self)
		#C.__init__(self)
		super().__init__()
		print("call constructor of D class")

objectD = D()


# Operator Overloading
class Numbox:
	def __init__(self, num):
		self.Num = num
	def __add__(self, num):
		self.Num += num
	def __radd__(self, num):
		self.Num += num
	def __sub__(self, num):
		self.Num -= num

n = Numbox(50)
n + 100
print(n.Num)
100 + n
print(n.Num)
n - 110
print(n.Num)
print()

