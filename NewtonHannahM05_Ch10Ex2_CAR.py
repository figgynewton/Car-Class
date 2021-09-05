Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Car:
	def __init__(self, make, year_model):
		self.__make = make
		self.__year_model = year_model
		self.__speed = 0
	def accelerate(self):
		self.__speed += 5
	def brake(self):
		self.__speed -= 5
	def get_speed(self):
		return self.__speed

>>>


	
